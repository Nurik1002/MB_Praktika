from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageUploadForm
from .img_filters import gaussian_blur, unsharp_mask, median_blur, clahe_filter 
from django.conf import settings
from django.core.files.storage import default_storage
import cv2
import numpy as np
import base64

def img_filters(request):
    if request.method == 'POST':
        # Check if an image was actually selected
        if 'image' in request.FILES:
            # Get the uploaded image
            image_file = request.FILES['image']

            # Save the uploaded image to temporary storage
            image_path = default_storage.save('temp.jpg', image_file)
            full_path = settings.MEDIA_ROOT + '/' + image_path

            # Apply the filter based on user selection
            filter_type = request.POST.get('filter')
            if filter_type == 'clahe':
                processed_img = clahe_filter(full_path)
            elif filter_type == 'gaussian':
                processed_img = gaussian_blur(full_path)
            elif filter_type == 'unsharp':
                processed_img = unsharp_mask(full_path)
            elif filter_type == 'median':
                processed_img = median_blur(full_path)
          

            _, buffer = cv2.imencode('.jpg', processed_img)
            processed_image_data = base64.b64encode(buffer).decode('utf-8')

            
            return render(request, 'image_filters/filters.html',   {'processed_image': processed_image_data,    'original_image_path': image_path})
        else:
            return render(request, 'image_filters/filters.html', {'error': 'Please select an image.'})
    else:
        return render(request, 'image_filters/filters.html')