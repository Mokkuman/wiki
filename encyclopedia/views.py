from django.shortcuts import render,redirect
from django import forms #para validar el formulario

from .forms import newPageForm
import markdown
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", { #si esta vacio entonces solo muestro la lista del contenido
        "entries": util.list_entries()
    })

def entry(request,title): #Pa wachar la entry accedida desde url
    entryContent = util.get_entry(title) #Obtengo valor del entry
    if entryContent is not None: #hay contenido
        return render(request, "encyclopedia/entryCont.html",{
            "entryTtle":title,
            "content":markdown.markdown(entryContent)
        })
    else: #si no hay contenido, entonces muestra pagina no encontrada
        return render(request,"encyclopedia/notFound.html")

def search(request):
    if request.method == "GET": #está lleno
        query = request.GET['q']
        
        if (util.get_entry(query) is not None):#busqueda con nombre igual
            return redirect('entry',title=query)
        else:
            lista = []
            for entry in util.list_entries():
                if query.lower() in entry.lower():
                    lista.append(entry)
                    
            if len(lista) == 0:
                return render(request,"encyclopedia/notFound.html")
            else:
                return render(request, "encyclopedia/srchResults.html",{
                    "searched":query,
                    "coincidencias":lista
                })

def newPage(request):
    form = newPageForm(request.POST or None)
    if form.is_valid():
        
        form.save()  
    return render(request,"encyclopedia/newPage.html",{
        'form':form
    })
    # if request.method == 'POST':
    #     form = newPageForm(request.POST)
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         title = form.cleaned_data['title']
    #         # redirect to a new URL:
    #         if(util.get_entry(title)) is None:
    #             util.save_entry(title)
    #         return redirect('entry',title='title')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = newPage(request)

    # return render(request, 'encyclopedia/newPage    .html', {'form': form})

    # if request.method == 'POST':
    #     titulo  = request.GET['titulo']
    #     for entry in util.list_entries():
    #         if titulo.lower() in entry.lower():
    #             existencia=True;
        
    #     return render(request,"encyclopedia/newPage.html",{
    #     "exist":existencia
    #     })    
    # else:
    #     return render(request,"encyclopedia/newPage.html")

def randomPage(request):
    return render(request,"encyclopedia/rdmPage.html")