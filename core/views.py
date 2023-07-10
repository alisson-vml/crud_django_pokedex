from django.shortcuts import render, redirect
from .models import Pokemon

def home(request):
    pokemons = Pokemon.objects.all()
    return render(request, "index.html", {"pokemons": pokemons})

def salvar(request):
    if request.method == 'POST':
        vnome= request.POST.get("nome")                     #obtém os novos valores do nome e da URL da foto do formulário.
        fotoUrl= request.POST.get("foto_url")
        Pokemon.objects.create(nome=vnome, foto_url=fotoUrl)#cria um novo objeto Pokemon com os valores informados nos inputs. 
        pokemons = Pokemon.objects.all()                    #recupera todos os objetos do modelo Pokemon.
        return redirect(home)                               #redireciona para a página home.
    return render(request, "index.html", {"pokemons": pokemons})

def editar( request, id):
    pokemon = Pokemon.objects.get(id=id)    #recupera o objeto Pokemon com o ID fornecido
    return render(request, "update.html", {"pokemon": pokemon}) #renderiza a página de update.

def update(request, id):
    vnome= request.POST.get("nome")         #obtém os novos valores do nome e da URL da foto do formulário.
    fotoUrl= request.POST.get("foto_url") 
    pokemon = Pokemon.objects.get(id=id)    #Em seguida, recupera o objeto Pokemon com o ID fornecido. 
    pokemon.nome = vnome                    #Os valores do nome e da URL da foto são atualizados no objeto pokemon. 
    pokemon.foto_url = fotoUrl              
    pokemon.save()                          #em seguida, o objeto é salvo no banco de dados usando pokemon.save().
    return redirect(home)                   #a requisição é redirecionada para a função home usando redirect(home).

def delete( request, id):
    pokemon = Pokemon.objects.get(id=id)
    pokemon.delete()
    return redirect(home)