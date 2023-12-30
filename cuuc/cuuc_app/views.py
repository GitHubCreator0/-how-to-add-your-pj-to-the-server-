from django.shortcuts import render

def page_1(request):
    return render(request, 'p1.html')


def page_2(request):
    return render(request, 'p2.html')