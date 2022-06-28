from django.shortcuts import render


def username_view(request, username):
    return render(request, 'users/user.html', context={'username': username})
