from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def home(request):
        return render(request,'home/index.html')