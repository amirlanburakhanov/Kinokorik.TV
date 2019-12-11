from django.db import models
from .utilities import get_timestamp_path

# Create your models here.

from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
	send_messages = models.BooleanField(default=True, verbose_name='Notify me of new comments?')

	def delete(self, *args, **kwargs):
		for bb in self.bb_set.all():
			bb.delete()
		super().delete(*args, **kwargs)

	class Meta:
		pass

class Category(models.Model):
	name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Title')
	order = models.SmallIntegerField(default=0, db_index=True,verbose_name='order')
	super_category = models.ForeignKey('SuperCategory', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Category')


class SuperCategoryManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(super_category__isnull=True)

class SuperCategory(Category):
	objects = SuperCategoryManager()

	def __str__(self):
		return self.name

	class Meta:
		proxy = True
		ordering = ('order', 'name')
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class SubCategoryManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(super_category__isnull=False)

class SubCategory(Category):
	objects = SubCategoryManager()

	def __str__(self):
		return '%s - %s' % (self.super_category.name, self.name)

	class Meta:
		proxy = True
		ordering = ('super_category__order', 'super_category__name', 'order', 'name')
		verbose_name = 'SubCategory'
		verbose_name_plural = 'SubCategories'


class Bb(models.Model):
	category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Category')
	title = models.CharField(max_length=50, verbose_name = 'Movie')
	content = models.TextField(verbose_name='Content')
	contacts = models.TextField(verbose_name='Contacts')
	image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Image')
	author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Author of movie')
	is_active = models.BooleanField(default=True, db_index=True, verbose_name='Add to list?')
	created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

	def delete(self, *args, **kwargs):
		for ai in self.additionalimage_set.all():
			ai.delete()
		super().delete(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Movie'
		verbose_name = 'Movie'
		ordering = ['-created_at']

class AdditionalImage(models.Model):
	bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Movie')
	image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Image')

	class Meta:
		verbose_name_plural = 'additional illustrations'
		verbose_name = 'additional illustration'

class Comment(models.Model):
	bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Movie')
	author = models.CharField(max_length=30, verbose_name='Author')
	content = models.TextField(verbose_name='Content')
	is_active = models.BooleanField(default=True, db_index=True, verbose_name='Display on screen?')
	created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')

	class Meta:
		verbose_name_plural = 'Comments'
		verbose_name = 'Comment'
		ordering = ['created_at']