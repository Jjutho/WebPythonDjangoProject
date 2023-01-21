from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('home')
    else:
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)
