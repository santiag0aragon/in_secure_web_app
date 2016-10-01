from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from messages_app.models import NotificationUser
from messages_app.views import load_user_objects


def login(request):
    """
    Manages a login request.
    """
    args = {}
    args.update(csrf(request))
    return render_to_response('datata_profile/login/login.html', args)


def auth_view(request):
    """
    Controls the auth requests
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/messages/main')
    else:
        return HttpResponseRedirect('/accounts/invalid/')


def invalid_login(request):
    """
    Controls the invalid login attempts requests
    """
    args = load_user_objects(request)
    auth.logout(request)
    args['user'] = request.user
    return render_to_response('datata_profile/login/invalid_login.html', args)


@login_required
def logout(request):
    """
    Controls the logout requests
    """
    args = load_user_objects(request)
    auth.logout(request)
    args['user'] = request.user
    return render_to_response('datata_profile/login/logout.html', args)

