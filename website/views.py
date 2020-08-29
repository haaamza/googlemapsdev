from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    if request.method =='POST':
        return render(request,'addReview.html', {'address':request.POST.get('address'),
                                                'lat':request.POST.get('lat'),
                                                'lng':request.POST.get('lng')})
    p = Property.objects.all()
    return render(request, 'home.html',{'properties':p})

def review(request):
    if request.method == 'POST':
        p = Property(address=request.POST.get('address'),
                    title=request.POST.get('title'),
                    description=request.POST.get('description'),
                    lat=request.POST.get('lat'),
                    lng=request.POST.get('lng'))
        p.save()
        return redirect('home')
    return render(request, 'addReview.html',{})
