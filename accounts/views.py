from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# def signup_view(request):
#     form = UserCreationForm()
#     return render(request, 'accounts/signup.html', { 'form':form })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request,user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form})
