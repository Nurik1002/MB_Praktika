from django.core.files.storage import default_storage
from django.conf import settings
import cv2



def gaussian_blur(image_path, kernel_size=(5, 5)):
    img = cv2.imread(image_path)
    blurred_img = cv2.GaussianBlur(img, kernel_size, 0)
    return blurred_img

def unsharp_mask(image_path, strength=1.0, threshold=10):
    img = cv2.imread(image_path)
 
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    diff = img - blurred

    diff = diff * strength
    sharp_img = img + diff

    sharp_img = cv2.normalize(sharp_img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    return sharp_img

def median_blur(image_path, kernel_size=5):
    img = cv2.imread(image_path)
    blurred_img = cv2.medianBlur(img, kernel_size)
    return blurred_img

