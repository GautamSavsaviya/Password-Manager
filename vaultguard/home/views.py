from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegitrationForm, LoginForm, UpdatePasswordsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db.models import Q
from .models import UserPassword
from .utils import encrypt, decrypt


# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def register_user(request):
    if request.method == "POST":
        form = RegitrationForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. Please login to your account')

    else:
        form = RegitrationForm()
    return render(request, 'home/signup.html', {'form': form})


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'home/login.html'

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        messages.success(self.request, f'Welcome {form.get_user()}')
        return super().form_valid(form)


def login_user(request):
    if request.user.is_authenticated:
        redirect('home:index')
    return UserLoginView.as_view()(request)


@login_required(login_url='home:login')
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url='home:login')
def add_password(request):
    if request.method == "POST":
        username = request.POST['username']
        password = encrypt(request.POST['password'])
        application_type = request.POST['application_type']

        if application_type == "Website":
            website_name = request.POST['website_name']
            website_url = request.POST['website_url']
            UserPassword.objects.create(user=request.user, username=username, password=password,
                                        application_type=application_type, website_name=website_name, website_url=website_url)
            messages.success(request, 'New password added...!')

        elif application_type == "Desktop Application":
            application_name = request.POST['application_name']
            UserPassword.objects.create(user=request.user, username=username, password=password,
                                        application_type=application_type, application_name=application_name)
            messages.success(request, 'New password added...!')

        elif application_type == "Game":
            game_name = request.POST['game_name']
            UserPassword.objects.create(user=request.user, username=username,
                                        password=password, application_type=application_type, game_name=game_name)
            messages.success(request, 'New password added...!')
        return render(request, 'home/add-password.html')

    return render(request, 'home/add-password.html')


@login_required(login_url='home:login')
def manage_password(request):
    user = request.user
    password_list = UserPassword.objects.filter(
        user=user).order_by('-created_at')

    if request.method == "POST":
        print(request.POST)
        if 'clear_filter' in request.POST:
            password_list = UserPassword.objects.filter(
                user=user).order_by('-created_at')
            return render(request, 'home/manage-password.html', {'password_list': password_list})

        search_key = request.POST.get('search')

        if password_list.filter(Q(username__icontains=search_key) | Q(application_type__icontains=search_key) | Q(website_name__icontains=search_key) | Q(application_name__icontains=search_key) | Q(game_name__icontains=search_key)):

            password_list = password_list.filter(Q(username__icontains=search_key) | Q(application_type__icontains=search_key) | Q(website_name__icontains=search_key) | Q(application_name__icontains=search_key) | Q(game_name__icontains=search_key))
        else:
            messages.error(request, "Search Password does not Exist...!")

    context = {
        'password_list': password_list,
    }
    return render(request, 'home/manage-password.html', context)


@login_required(login_url='home:login')
def edit_password(request, id):
    user_password = UserPassword.objects.get(id=id)
    user_password.password = decrypt(user_password.password)
    form = UpdatePasswordsForm(instance=user_password)

    if request.method == "POST":
        form = UpdatePasswordsForm(request.POST, instance=user_password)
        if form.is_valid():
            try:
                user_password.password = encrypt(user_password.password)
                form.save()
                messages.success(request, 'Password updated.')
                user_password.password = decrypt(user_password.password)
            except ValidationError as e:
                form.add_error(e)

    context = {
        'form': form,
    }
    return render(request, 'home/edit-password.html', context)


@login_required(login_url='home:login')
def delete_password(request, id):
    password_obj = UserPassword.objects.get(id=id)
    password_obj.delete()
    return redirect('home:manage_password')
