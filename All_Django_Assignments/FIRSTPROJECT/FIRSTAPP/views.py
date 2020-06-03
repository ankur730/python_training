from django.shortcuts import render
from FIRSTAPP.models import Detail

# Create your views here.

def home(request):
    return render(request, 'FIRSTAPP/home.html')
