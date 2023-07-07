from django.shortcuts import render, redirect
from .models import Pokemon

def home(request):
    pokemons = Pokemon.objects.all()
    return render(request, "index.html", {"pokemons": pokemons})

def salvar(request):
    vnome= request.POST.get("nome")
    Pokemon.objects.create(nome=vnome)
    pokemons = Pokemon.objects.all()
    return render(request, "index.html", {"pokemons": pokemons})

def editar( request, id):
    pokemon = Pokemon.objects.get(id=id)
    return render(request, "update.html", {"pokemon": pokemon})

def update(request, id):
    vnome= request.POST.get("nome")
    pokemon = Pokemon.objects.get(id=id)
    pokemon.nome = vnome
    pokemon.save()
    return redirect(home)

def delete( request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.delete()
    return redirect(home)