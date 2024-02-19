from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Dart
from .forms import DartForm, SignUpForm, ProfilePictureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = DartForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                dart = form.save(commit=False)
                dart.user = request.user
                dart.save()
                messages.success(request, f'Dart created successfully')
                return redirect('home')
            else:
                messages.success(request, f'Error: Dart not created')
                return redirect('home')
        darts = Dart.objects.all().order_by('-date_created')
        return render(request, 'home.html', {"darts": darts, "form": form})
    else:
        darts = Dart.objects.all().order_by('-date_created')
        return render(request, 'home.html', {"darts": darts})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
    else:
        messages.success(request, f'Please login to view profiles')
        return redirect('home')

    return render(request, 'profile_list.html', {"profiles": profiles})

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        darts = Dart.objects.filter(user_id=pk).order_by('-date_created')

        # POST form logic
        if request.method == 'POST':
            current_user = request.user.profile
            action = request.POST['follow']
            if action == 'follow':
                current_user.follow.add(profile)
                current_user.save()
                messages.success(request, f'You are now following {profile.user.username}')
                return render(request, 'profile.html', {"profile": profile, "darts": darts})
            elif action == 'unfollow':
                current_user.follow.remove(profile)
                current_user.save()
                messages.success(request, f'You are no longer following {profile.user.username}')
                return render(request, 'profile.html', {"profile": profile, "darts": darts})
            else:
                messages.success(request, f'Error: Something went wrong')
                return render(request, 'profile.html', {"profile": profile, "darts": darts})
            

        return render(request, 'profile.html', {"profile": profile, "darts": darts})
    else:
        messages.success(request, f'You need to be logged in to view your profile')
        return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}')
            return redirect('home')
        else:
            messages.success(request, f'Error: Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, f'Welcome {username}')
            return redirect('home')
        
    return render(request, 'register.html', {"form": form})

def edit_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user__id=request.user.id)

        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=user)
        profile_form = ProfilePictureForm(request.POST or None, request.FILES or None, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, user)
            messages.success(request, f'Profile updated successfully')
            return redirect('profile', pk=request.user.id)
        
        return render(request, 'edit_profile.html', {"profile": profile, "user_form": user_form, "profile_form": profile_form})
    else:
        messages.success(request, f'You need to be logged in to edit your profile')
        return redirect('home')

def dart_like(request, pk):
    if request.user.is_authenticated:
        dart = get_object_or_404(Dart, id=pk)\
        
        if dart.dislikes.filter(id=request.user.id).exists():
            dart.dislikes.remove(request.user)

        liked = not dart.likes.filter(id=request.user.id).exists()
        if liked:
            dart.likes.add(request.user)
        else:
            dart.likes.remove(request.user)

        responce = {
            'likes_count': dart.likes.count(),
            'dislikes_count': dart.dislikes.count(),
            'liked': liked
        }
        return JsonResponse(responce)

def dart_dislike(request, pk):
    if request.user.is_authenticated:
        dart = get_object_or_404(Dart, id=pk)

        if dart.likes.filter(id=request.user.id).exists():
            dart.likes.remove(request.user)

        disliked = not dart.dislikes.filter(id=request.user.id).exists()
        if disliked:
            dart.dislikes.add(request.user)
        else:
            dart.dislikes.remove(request.user)

        responce = {
            'likes_count': dart.likes.count(),
            'dislikes_count': dart.dislikes.count(),
            'disliked': disliked
        }
        return JsonResponse(responce)
    else:
        messages.success(request, f'You need to be logged in to like or dislike a dart')
        return redirect(request.META.get("HTTP_REFERER"))
    
def delete_dart(request, pk):
    if request.user.is_authenticated:
        if request.user.username == dart.user.username:
            dart = get_object_or_404(Dart, id=pk)
            dart.delete()
            messages.success(request, f'Dart deleted successfully')
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, f'You need to be logged in to delete a dart')
        return redirect('home')
    
def delete_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user.delete()
        messages.success(request, f'Account deleted successfully')
        return redirect('home')
    else:
        messages.success(request, f'You need to be logged in to delete your account')
        return redirect('home')
    
def edit_dart(request, pk):
    if request.user.is_authenticated:
        dart = get_object_or_404(Dart, id=pk)
        form = DartForm(request.POST or None, instance=dart)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dart updated successfully')
            return redirect('profile', pk=request.user.id)    
        return render(request, 'edit_dart.html', {"form": form})
    else:
        messages.success(request, f'You need to be logged in to edit a dart')
        return redirect('home')