from django.shortcuts import render
from .forms import ImageForm
from .model import Image

# Create your views here.
def home(request)
    if request.method == "post":
        form = ImageForm(request.POST,request.FILES)
        If form.is_valid():
            form.save()
form=ImageForm
    return render(request,'instagram/home.html' {'form':forms)
