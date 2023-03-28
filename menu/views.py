from django.shortcuts import render


def rdirect(request, name):
    return render(request, 'app/home.html', {'name': name})
