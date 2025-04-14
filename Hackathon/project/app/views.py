from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def tracking(request):
    return render(request, 'tracking.html')