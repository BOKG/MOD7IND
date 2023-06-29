from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class Home(ListView):
    def get(self, request):
        return render(request, 'home.html', {})
    
