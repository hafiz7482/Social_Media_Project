from django.urls import reverse
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App_login.models import UserProfile
from django.contrib.auth.models import User
from App_login.models import UserProfile, Follow
from App_post.models import Post, Likes

# Create your views here.

@login_required
def Home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Likes.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_post/home.html', context={'title':'Home', 'search':search, 'result':result, 'posts':posts,'liked_post_list':liked_post_list})

@login_required
def LikeView(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Likes.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Likes(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def UnLikeView(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Likes.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))

