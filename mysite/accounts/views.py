from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm
    return render(request, 'authentication/sign_up.html', {'form': form})
