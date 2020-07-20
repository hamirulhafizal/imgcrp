import PIL
import urllib.request
from PIL import ImageOps, ImageEnhance, ImageChops, ImageFilter, Image

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Photo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView

from django.shortcuts import get_object_or_404

from django.urls import reverse


def home(request):
    return redirect('photo_list')


def rotate_cw(requests, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.rotate(-90)
    out.save(image_path, "PNG")

    return redirect('effects', id_image)


def rotate_acw(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.rotate(90)
    out.save(image_path, "PNG")

    return redirect('effects', id_image)


def flip_left_right(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    out.save(image_path, "PNG")

    return redirect('effects', id_image)


def flip_top_bottom(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    out.save(image_path, "PNG")

    return redirect('effects', id_image)


def image_transerve(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.transpose(PIL.Image.TRANSVERSE)
    out.save(image_path, "PNG")

    return redirect('effects', id_image)


def resize_minus(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    width = img.size[0]
    height = img.size[1]

    a = width - 50
    b = height - 50

    size = (a, b)

    # resize image
    out = img.resize(size)
    # save resized image
    out.save(image_path, quality=95)

    return redirect('effects', id_image)


def resize_plus(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)
    width = img.size[0]
    height = img.size[1]

    a = width + 50
    b = height + 50

    size = (a, b)

    # resize image
    out = img.resize(size)
    # save resized image
    out.save(image_path, quality=95)

    return redirect('effects', id_image)


def brightness(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 1.5  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects', id_image)


def darkness(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 0.5  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects', id_image)


def blurness(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 0.05  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects', id_image)


def sharpness(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path

    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 2  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects', id_image)


def grayscale(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path
    img = Image.open(image_path)

    out = ImageOps.grayscale(img)
    out.save(image_path)

    return redirect('effects', id_image)


def postarize(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path
    img = Image.open(image_path)

    # applying posterize method
    out = ImageOps.posterize(img, 2)
    out.save(image_path)

    return redirect('effects', id_image)


def filter(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path
    img = Image.open(image_path)

    # applying the rank filter
    out = img.filter(ImageFilter.RankFilter(size=3, rank=3 * 3 - 1))
    out.save(image_path)

    return redirect('effects', id_image)


def edges(request, id_image):
    myObj = Photo.objects.get(pk=id_image)
    image_path = myObj.file.path
    img = Image.open(image_path)

    # Converting the image to greyscale, as edge detection
    # requires input image to be of mode = Greyscale (L)
    # image = img.convert("L")

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    out = img.convert("L").filter(ImageFilter.FIND_EDGES)

    # Saving the Image Under the name Edge_Sample.png
    out.save(image_path)
    return redirect('effects', id_image)


def delete_id(request, id_image):
    myObj = Photo.objects.get(pk=id_image)

    if myObj is None:
        return redirect('effects')
    else:
        myObj.delete()
        return redirect('photo_list')


def dlt(request):
    myObj = Photo.objects.all()

    if myObj is None:
        return redirect('effects')
    else:
        myObj.delete()
        return redirect('photo_list')


class Effects(LoginRequiredMixin, TemplateView, RedirectView):
    login_url = '/login/'
    redirect_field_name = 'effects'
    raise_exception = True

    """Return the available effects."""

    templates = 'album/home.html'

    def get(self, request, id_image):
        if not request.user.is_authenticated:
            return render(request, 'registrarion/login_error.html')
        img1 = Photo.objects.filter(pk=id_image)
        pk = id_image

        """Return all the effects available."""

        effects = {
            "rotate_cw": rotate_cw,
            "rotate_acw": rotate_acw,
            "flip_left_right": flip_left_right,
            "flip_top_bottom": flip_top_bottom,
            "image_transerve": image_transerve,
            "resize_minus": resize_minus,
            "resize_plus": resize_plus,
            "brightness": brightness,
            "darkness": darkness,
            "blurness": blurness,
            "sharpness": sharpness,
            "grayscale": grayscale,
            "postarize": postarize,
            "filter": filter,
            "edges": edges,
        }

        return render(request, self.templates, {'img1': img1, 'effects': effects, 'pk': pk})
