"""Movies Function"""
from django.shortcuts import render

# Create your views here.
def home(request):
    """Home function"""
    context = {
        "title": "MDB"
    }
    return render(request, 'index.html', context)
