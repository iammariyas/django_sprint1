from django.shortcuts import render


# Create your views here.
def about(request):
    """Описание"""
    return render(request, 'pages/about.html')


def rules(request):
    """Описание"""
    return render(request, 'pages/rules.html')