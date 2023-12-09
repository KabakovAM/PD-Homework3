from django.shortcuts import render


def about_django(request):
    return render(request, 'Ex001/about_django.html')

def about_me(request):
    return render(request, 'Ex001/about_me.html')
