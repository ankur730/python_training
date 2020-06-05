from django.shortcuts import render, redirect
from blog_posts.forms import ContactForm
from blog_posts.models import Contacts

# Create your views here.

def index(request):
    return render(request, 'blog_posts/index.html')

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        if request.method == "GET":
            form = ContactForm()
            return render(request, 'blog_posts/post_form.html' ,{'form':form})



def show(request):
    contactdata = Contacts.objects.all()
    return render(request, 'blog_posts/post_show.html',{'contactdata':contactdata})


def edit(request, id):
    contactdata = Contacts.objects.get(id = id)
    return render(request, 'blog_posts/post_edit.html', {'contactdata':contactdata})


def update(request, id):
    contactdata = Contacts.objects.get(id=id)
    form = ContactForm(request.POST, instance = contactdata)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'blog_posts/post_edit.html', {'contactdata': contactdata})

def delete(request, id):
    contactdata = Contacts.objects.get(id=id)
    contactdata.delete()
    return redirect('/show')

