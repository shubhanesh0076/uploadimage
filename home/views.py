from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UploadImage
import cv2
import base64
# Create your views here.


@login_required
def HomeView(request):
    template_name = "home/home.html"
    
    image_obj = UploadImage.objects.all()
    # for image in image_obj:
    #     with open(image.image , "rb") as image_file :
    #         data = base64.b64encode(image_file.read())
    #         print(data)
    #         # return data.decode('utf-8')
        # image = open(f'{image.image.url}', 'rb')
        # print("IMAGE: ",image )
    # image_read = image.read()
    # image_64_encode = base64.encodestring(image_read)
    # image_64_decode = base64.decodestring(image_64_encode) 
    # image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result
    # image_result.write(image_64_decode)
    context={
        "image_obj": image_obj,
    }
    return render(request, template_name, context)