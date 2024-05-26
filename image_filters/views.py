from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageUploadForm
from .img_filters import gaussian_blur, unsharp_mask, median_blur, clahe_filter
from django.conf import settings
from django.core.files.storage import default_storage
import cv2
import numpy as np

def img_filters(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            filename = image.name
            image_path = settings.MEDIA_ROOT + '/' + filename
            default_storage.save(filename, image)

            filter_name = request.POST.get('filter_name')  

            if filter_name == 'gaussian_blur':
                processed_img = gaussian_blur(image_path)
            elif filter_name == 'unsharp_mask':
                processed_img = unsharp_mask(image_path)
            elif filter_name == 'median_blur':
                processed_img = median_blur(image_path)
            elif filter_name == 'clahe':
                processed_img = clahe_filter(image_path)  # Call the new filter function
            else:
                processed_img = cv2.imread(image_path)

            processed_filename = 'processed_' + filename
            cv2.imwrite(settings.MEDIA_ROOT + '/' + processed_filename, processed_img)

            return JsonResponse({
                'success': True,
                'processed_image': processed_filename, 
                'media_url': settings.MEDIA_URL 
            })
    else:
        form = ImageUploadForm()
    return render(request, 'image_filters/filters.html', {'form': form})