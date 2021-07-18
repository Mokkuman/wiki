from django.shortcuts import render,redirect
from django import forms #para validar el formulario

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
    if request.method == 'POST':
        titulo  = request.GET['titulo']
        for entry in util.list_entries():
            if titulo.lower() in entry.lower():
                existencia=True;
        
        return render(request,"encyclopedia/newPage.html",{
        "exist":existencia
        })    
    else:
        return render(request,"encyclopedia/newPage.html")

def randomPage(request):
    return render(request,"encyclopedia/rdmPage.html")