
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from forms import UserCreationForm
from models import WeakUser


def create_user(request):
    """
    Creates a new user storing the password in plain text.
    """
    args = dict()
    user = request.user
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            w_user = WeakUser()
            f.save()
            w_user.user = f
            w_user.weak_pwd = f.password
            w_user.save()
            return HttpResponseRedirect("/messages/main/")
    else:
        form = UserCreationForm()
    args['form'] = form
    args.update(csrf(request))
    return render(request, 'datata_profile/login/create_user.html', args)
