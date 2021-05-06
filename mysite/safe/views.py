from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import SafeForm, PasswordCheck
from .models import Safe


def index(request):
    safe_count = Safe.objects.count()
    user_count = User.objects.count()
    return render(request, 'index.html', {
        'safe_count': safe_count,
        'user_count': user_count,
    })


def passwords(request):
    if request.user.is_authenticated:
        safe_objects = Safe.objects.filter(user=request.user).order_by('-updated_at')
        if request.method == 'POST':
            form = SafeForm(request.POST)
            if form.is_valid():
                new_safe_object = Safe(user=request.user,
                            purpose=form.cleaned_data['purpose'],
                            content=form.cleaned_data['content']
                            )
                new_safe_object.save()
                return redirect('/passwords')
        else:
            form = SafeForm
        return render(request, 'passwords.html', {
            'form': form,
            'safe_objects': safe_objects
        })

    else:
        return redirect('/login')


def password_view(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordCheck(request.POST)
            if form.is_valid():
                success = request.user.check_password(form.cleaned_data['password'])
                if success:
                    safe = Safe.objects.get(id=id, user=request.user)
                    return render(request, 'password_view.html', {'safe': safe})

                else:
                    return HttpResponse('<h3>You wrote bad password!</h3>')

        else:
            form = PasswordCheck()

        return render(request, 'password_check.html', {'form': form})

    else:
        return redirect('/login')


def password_delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordCheck(request.POST)
            if form.is_valid():
                success = request.user.check_password(form.cleaned_data['password'])
                if success:
                    safe = Safe.objects.get(id=id, user=request.user)
                    safe.delete()
                    return redirect('/passwords')

                else:
                    return HttpResponse('<h3>You wrote bad password!</h3>')

        else:
            form = PasswordCheck()

        return render(request, 'password_check.html', {'form': form})

    else:
        return redirect('/login')
