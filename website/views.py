from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from website.forms import TweetForm
from website.models import Tweet
from django.contrib.auth.models import User


def timeline(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            t = Tweet()
            t.user = request.user
            t.message = form.cleaned_data['message']
            t.save()
            return HttpResponseRedirect("/")
    else:
        form = TweetForm()

    tweets = Tweet.objects.all().order_by('-timestamp')
    return render(request, 'website/index.html', {'tweets': tweets, 'form': form})


def tweet_page(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, 'website/tweet_page.html', {'tweet': tweet})

def user_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'website/user_page.html', {'page_user':user})

def users_list(request):
    users= User.objects.all()
    return render(request, 'website/users_list.html', {'users': users})

def mentions_page(request):
    tweets = Tweet.objects.filter(message__icontains=request.user.username).order_by('-timestamp')
    return render(request, 'website/mentions_page.html', {'tweets': tweets})  

def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    tweet.delete()
    return HttpResponseRedirect("/") 

def retweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    t = Tweet()
    t.user = request.user
    t.message = "RT " + tweet.message
    t.save()
    return HttpResponseRedirect("/")