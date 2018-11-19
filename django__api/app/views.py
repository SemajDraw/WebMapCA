from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfilePicForm


# Render landing page
def landing(request):
    return render(request, 'app/landing.html')


@login_required
# Render landing page
def profile(request):
    return render(request, 'app/profile.html')


@login_required
def update_profile_pic(request):
    if request.method == 'POST':
        profile_pic_form = ProfilePicForm(request.FILES, instance=request.user.profile)
        if profile_pic_form.is_valid():
            profile_pic_form.save()
            return render(request, 'app/profile.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfilePicForm()
    return render(request, 'app/update_profile_pic.html', {
        'profile_pic_form': form
    })


