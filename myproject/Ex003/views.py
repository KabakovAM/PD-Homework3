from django.shortcuts import render
import random

def coin(request, num):
    result = []
    for _ in range(num):
        a = random.choice(['Орёл', 'Решка'])
        result.append(a)
    context = {'result': result, 'title': 'Монетка'}
    return render(request, 'Ex003/result.html', context)

def cube(request, num):
    result = []
    for _ in range(num):
        a = random.randint(1,6)
        result.append(a)
    context = {'result': result, 'title': 'Кубик'}
    return render(request, 'Ex003/result.html', context)

def num(request, num):
    result = []
    for _ in range(num):
        a = random.randint(0,100)
        result.append(a)
    context = {'result': result, 'title': 'Номер'}
    return render(request, 'Ex003/result.html', context)