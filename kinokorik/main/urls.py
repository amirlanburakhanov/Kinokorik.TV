from django.urls import path
from django.contrib.auth import views as auth_view

from .views import(
    index, 
    other_page,
	ChangeUserInfoView,
	BBPasswordChangeView,
	profile,
	register,
	RegisterDoneView,
	DeleteUserView,
	by_category,
	detail,
	profile_bb_add,
	profile_bb_delete,
	profile_bb_detail,
	)

app_name = 'main'
urlpatterns = [
	path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
	path('accounts/register/', register, name='register'),
	path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
	path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
	path('accounts/logout/', auth_view.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
	path('accounts/login/', auth_view.LoginView.as_view(template_name='main/login.html'), name='login'),
	path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
	path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
	path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
	path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
	path('accounts/profile/', profile, name='profile'),
	path('<int:category_pk>/<int:pk>/', detail, name='detail'),
	path('<int:pk>/', by_category, name='by_category'),
	path('<str:page>/', other_page, name='other'),
	path('', index, name='index'),
]