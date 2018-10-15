from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Sua conta foi desativada.")
        else:
            print("Informações de login inválidas: {0}, {1}".format(username, password))
            print(request.errors)
            return HttpResponse("Informações de login inválidas foram inseridas.")

    else:
        return render(request, 'rango/login.html', {})
