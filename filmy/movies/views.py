# Create your views here.
from django.shortcuts import render
from .models import Film
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    filmy = Film.objects.select_related('reziser').all()  # Optimalizace pro foreign key
    return render(request, 'movies/index.html', {'filmy': filmy})
 
def seznam_filmu(request):
    filmy = Film.objects.all()
    return render(request, 'movies/index.html', {'movies': filmy})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movies')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})