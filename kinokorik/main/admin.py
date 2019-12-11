from django.contrib import admin
from .models import (
		AdvUser,
		SuperCategory,
		SubCategory,
		Bb,
		AdditionalImage,
	)
from .forms import SubCategoryForm
# Register your models here.

admin.site.register(AdvUser)

class SubCategoryInline(admin.TabularInline):
	model = SubCategory

class SuperCategoryAdmin(admin.ModelAdmin):
	exclude = ('super_category',)
	inlines = (SubCategoryInline,)

admin.site.register(SuperCategory, SuperCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
	form = SubCategoryForm

admin.site.register(SubCategory, SubCategoryAdmin)

class AdditionalImageInline(admin.TabularInline):
	model = AdditionalImage

class BbAdmin(admin.ModelAdmin):
	list_display = ('category', 'title', 'content', 'author', 'created_at')
	fields = (('category', 'author'), 'title', 'content', 'contacts', 'image', 'is_active')
	inlines = (AdditionalImageInline,)

admin.site.register(Bb, BbAdmin)