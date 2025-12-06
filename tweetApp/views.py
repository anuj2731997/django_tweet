from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required


from .models import Tweet
from .forms import TweetForm, RegistrationForm, LoginForm, LogoutForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def logout_view(request):
    if request.method == "POST":
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)

    return redirect("/login/")


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


def register(request):
    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = RegistrationForm()
    return render(request, "registration/signup.html", {"form": form})


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")

    return render(request, "tweet/tweet_list.html", {"tweets": tweets})


@login_required
def tweets(request):
    user_tweets = Tweet.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "tweet/user_tweets.html", {"tweets": user_tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("/")
    else:
        form = TweetForm()

    return render(request, "tweet/tweet_create.html", {"form": form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("/")
    else:
        form = TweetForm(instance=tweet)

    return render(request, "tweet/tweet_create.html", {"form": form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("/")

    return render(request, "tweet/tweet_delete.html", {"tweet": tweet})
