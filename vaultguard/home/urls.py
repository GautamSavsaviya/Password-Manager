from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.register_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home:login')), name='logout'),
    path('home/', views.home, name='home'),
    path('add-password/', views.add_password, name='add_password'),
    path('manage-password/', views.manage_password, name='manage_password'),
    path('edit-password/<id>', views.edit_password, name='edit_password'),
    path('delete-password/<id>', views.delete_password, name='delete_password'),
]
