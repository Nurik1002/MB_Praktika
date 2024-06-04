from django.shortcuts import render, redirect
from django.http import Http404
from django.conf import settings
from django.contrib import admin  
import os

from .models import Image
from .predict import load_image, predict

def brain_view(request):
    context = {}
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        obj = Image(image=uploaded_file) 
        obj.user = request.user
        obj.save()

        img = load_image(os.path.join(settings.BASE_DIR, obj.image.path))
        pred, foiz = predict(img)

        context["image_url"] = obj.image.url
        context["predict"] = pred
        context["foiz"] = round(foiz * 100, 2)

        return render(request, "ailab/brain.html", context=context)

    return render(request, "ailab/brain.html", context)