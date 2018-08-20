from django.http import HttpResponseRedirect


def login_check(func):
    def is_login(request, *args, **kwargs):
        if request.session.has_key("id"):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie("url", request.get_full_path())
            return red

    return is_login
