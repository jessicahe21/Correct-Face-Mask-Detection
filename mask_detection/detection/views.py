from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import image_classification
from .py_templates.my_model import image_pred
import urllib.parse

# Create your views here.

def index(request):
    return render(request, 'detection/interface.html')

def predictImage(request):
    img = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(img.name, img)
    filePathName = fs.url(filePathName)
    parsed_name = urllib.parse.unquote(filePathName)

    out = image_pred(parsed_name)
    out = {0:'Correct', 1:'Incorrect'}[int(out)]
    
    context = {'filePathName':filePathName, 'pred':out}
    return render(request, 'detection/interface.html', context) 
