from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})

def colorspace(request):
    return render(request, 'colorspace.html')


def morphology(request):
    return render(request, 'morphology.html')

def edge(request):
    return render(request, 'edge.html')

def blur(request):
    return render(request, 'blur.html')

def imgflip(request):
    return render(request, 'imgflip.html')

def togrey(request):
    return render(request, 'togrey.html')

def torgb(request):
    return render(request, 'torgb.html')

def rgbtobgf(request):
    return render(request, 'rgbtobgf.html')

def erod(request):
    return render(request, 'erod.html')

def dilafe(request):
    return render(request, 'dilafe.html')

def morfopen(request):
    return render(request, 'morfopen.html')

def morfclose(request):
    return render(request, 'morfclose.html')

def morfgradiant(request):
    return render(request, 'morfgradiant.html')

def innerblur(request):
    return render(request, 'innerblur.html')

def gausianblur(request):
    return render(request, 'gausianblur.html')

def medianblur(request):
    return render(request, 'medianblur.html')

def bileteralfilter(request):
    return render(request, 'bileteralfilter.html')

def yuzseksen(request):
    return render(request, 'yuzseksen.html')

def artidoksan(request):
    return render(request, 'artidoksan.html')

def eksidoksan(request):
    return render(request, 'eksidoksan.html')

