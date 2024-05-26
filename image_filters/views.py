from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .img_filters import gaussian_blur, unsharp_mask, median_blur  
from django.conf import settings  
from django.core.files.storage import default_storage  
import cv2

def img_filters(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            filename = image.name
            image_path = settings.MEDIA_ROOT + '/' + filename
            default_storage.save(filename, image)

            if 'gaussian_blur' in request.POST:
                processed_img = gaussian_blur(image_path)
            elif 'unsharp_mask' in request.POST:
                processed_img = unsharp_mask(image_path)
            elif 'median_blur' in request.POST:
                processed_img = median_blur(image_path)
            else:
                processed_img = cv2.imread(image_path)

            processed_filename = 'processed_' + filename
            cv2.imwrite(settings.MEDIA_ROOT + '/' + processed_filename, processed_img)

            context = {'processed_image': processed_filename}
            return render(request, 'image_filters/filters.html', context)
    else:
        form = ImageUploadForm()
    return render(request, 'image_filters/filters.html', {'form': form})