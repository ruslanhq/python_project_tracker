from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.forms import UserCreationForm, UserUpdateForm, PasswordChangeForm, SignUpForm


# def login_view(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             context['has_error'] = True
#     return render(request, 'accounts/login.html', context=context)


# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('index')
from accounts.models import Profile


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'register.html', {'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_profile', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserChangeView):
    template_name = 'user_change_pass.html'
    form_class = PasswordChangeForm

    def get_success_url(self):
        return reverse('accounts:login')


class UserListView(ListView):
    context_object_name = 'users'
    template_name = 'users_list.html'
    model = User


