from pyexpat.errors import messages
from unicodedata import category, name
from django.shortcuts import render,redirect
from .models import Category,Photo
import os

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)
    
    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {'categories': categories,'photos':photos}
    return render(request,'photos/gallery.html',context)

def viewphoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def deletephoto(request,pk):
    photo = Photo.objects.get(id=pk)
    image = request.FILES.get('image')
    photo.delete()
    if len(photo.image)>0 :
        os.remove(photo.image.path)
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories,'photos':photos}
    return render(request,'photos/gallery.html',context)


def addphoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(category=category,description = data['description'],
            image = image)

        return redirect('gallery')

        # print('data',data)
        # print('image',image)

    context = {'categories': categories}
    return render(request,'photos/add.html',context)