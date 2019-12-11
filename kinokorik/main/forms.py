from django import forms
from .models import AdvUser, SuperCategory, SubCategory
from django.contrib.auth.forms import UserCreationForm
from .models import Bb, AdditionalImage
from django.forms import inlineformset_factory
from captcha.fields import CaptchaField
from .models import Comment

class ChangeUserInfoForm(forms.ModelForm):
	email = forms.EmailField(required=True, label='Email address')

	class Meta:
		model = AdvUser
		fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')

class ChangeMovieData(forms.ModelForm):
	pass
	
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = AdvUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_messages']

class SubCategoryForm(forms.ModelForm):
	super_category = forms.ModelChoiceField(queryset=SuperCategory.objects.all(), empty_label=None, label='Category', required=True)

	class Meta:
		model = SubCategory
		fields = '__all__'

class SearchForm(forms.Form):
	keyword = forms.CharField(required=False, max_length=20, label='')

class BbForm(forms.ModelForm):
	class Meta:
		model = Bb
		fields = '__all__'
		widgets = {'author': forms.HiddenInput}

AiFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__')

class UserCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ('is_active',)
		widgets = {'bb': forms.HiddenInput}

class GuestCommentForm(forms.ModelForm):
	captcha = CaptchaField(label='Enter text from image', error_messages={'invalid': 'Incorrect text'})