from models import NotificationUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from forms import NotificationForm
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt  # CSRF
def main(request):
    """
    Loads the main page of the app. Render all the corresponding user
    messages and the new message form.

    Is tagged with a @csrf_exempt Tag to avoid the csrf protection that
    is set up by default.
    """
    args = load_user_objects(request)
    user = request.user
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = user
            f.save()
    else:
        form = NotificationForm()
    args = load_user_objects(request)
    args['form'] = form
    args.update(csrf(request))
    return render(request, 'datata_notification/notification/db.html', args)


@login_required
def load_user_objects(request):
    """
    Loads user objects needed to render the templates
    i.e.
        + User
        + User notification
    """
    user = request.user
    n_user = NotificationUser.objects.filter(user=user, viewed=False)
    args = {}
    args['user'] = user
    args['notifications_user'] = n_user
    return args


@login_required
def show_notification(request, notification_id):
    """
    Render the user messages
    """
    n = NotificationUser.objects.get(id=notification_id)
    return render_to_response(
        "messages/notification/notification.html",
        {"notification": n})


@login_required
def delete_notification(request, notification_id):
    """
    Mark as deleted a notification upon user request
    """
    n = NotificationUser.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect("/messages/main/")


def csrf_test(request):
    """
    Runs a an CSRF example. If this url is runned an script post a
    message titled Easy Game on the user behalf.
    """
    return render(request, 'datata_notification/notification/db_2.html')
