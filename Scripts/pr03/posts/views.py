from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect

from .forms import PostForm
from .models import Post, Author, Comments


def posts_home(request):
    home='Basic2 render'
    return render_to_response('basic2.html',{'name':home})

def posts_detail(request,id=None):
    instance=get_object_or_404(Post,id=id)
    context={
        'title':'Post detail',
        'instance':instance
    }
    return render(request,'posts_detail.html',context)

def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        'title':instance.title,
        'instance':instance,
        'form':form
    }
    return render(request, 'posts_create.html', context)

def posts_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return HttpResponseRedirect(instance.get_absolute_url())

def posts_create(request):
    #form=PostForm()
    #if request.method=='POST':
        #print(request.POST.get('title'))
        #print(request.POST.get('content'))
        #title=request.POST.get('title')
        #content=request.POST.get('content')
        #Post.objects.create(title=title, content=content)
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        HttpResponseRedirect(instance.get_absolute_url())
    context={
        'form':form
    }
    return render(request,'posts_create.html',context)

def posts_list(request):
    queryset=Post.objects.all()
    context={'queryset':queryset,'title':'Posts List'}
    return render(request,'index.html',context)