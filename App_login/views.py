from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from App_login.forms import RegistrationForm, LoginForm, EditProfile
from django.urls import reverse, reverse_lazy
from App_login.models import UserProfile, Follow
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from App_post.forms import PostForms


# Create your views here.

def RegistrationView(request):
    form = RegistrationForm()
    registered = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_login:login'))

    return render(request, 'App_login/registration.html', context={'title': 'Sign Up . Instagram', 'form': form})

def LoginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_post:home'))
    
    return render(request, 'App_login/login.html', context={'title':'login . Social','form': form})

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/profile.html', context={'form':form})


@login_required
def Logout(request):
    logout = (request)
    return HttpResponseRedirect(reverse('App_login:login')) 

@login_required
def ProfileDetails(request):
    form = PostForms()
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_login/profile_edit.html', context={'title': 'user','form': form})

@login_required
def UserInfo(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following =user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/user_info.html', context={'user_other': user_other, 'already_followed':already_followed})

@login_required
def FollowView(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following =following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following =following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_login:user_info', kwargs={"username":username}))

@login_required
def UnFollowView(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following =following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_login:user_info', kwargs={"username":username}))

