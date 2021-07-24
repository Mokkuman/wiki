from django.shortcuts import render,redirect
from django import forms #para validar el formulario

from .forms import newPageForm
import markdown, secrets
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", { #si esta vacio entonces solo muestro la lista del contenido
        "entries": util.list_entries()
    })

def entry(request,title): #Pa wachar la entry accedida desde url
    entryContent = util.get_entry(title)
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

        #process the data in form.cleaned_data
        tittle = form.cleaned_data['titulo']
        content = form.cleaned_data['contenido']
        if util.get_entry(tittle) is None: #si no existe
            util.save_entry(tittle,content) #guardando nuevo entry
            return redirect('entry',title=tittle)
        else: #ya existe :0
            return render(request,"encyclopedia/newPage.html",{
                'form': form,
                'exist': True #para validar en el html
            })
    return render(request,"encyclopedia/newPage.html",{
        'form':form,
        'exist':False
    })
    
def edit(request,title_edit):
    entryContent = util.get_entry(title_edit)
    form = newPageForm(request.POST or None)
#Editando lo que mostrará el form
    if entryContent is not None:
        form.fields['titulo'].initial = title_edit
        form.fields['titulo'].widget = forms.HiddenInput()
        form.fields['contenido'].initial = entryContent
        
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            util.save_entry(title_edit,contenido)
            
            return redirect('entry',title=title_edit)
        
    return render(request,"encyclopedia/edit.html",{
        'title':title_edit,
        'form':form
    })

    return render(request,"encyclopedia/edit.html")
    
    
def randomPage(request):
    entry = secrets.choice(util.list_entries())
    return redirect('entry', title=entry)