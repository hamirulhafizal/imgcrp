import PIL
import urllib.request
from PIL import ImageOps, ImageEnhance, ImageChops, ImageFilter, Image

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Photo


def home(request):
    photos = Photo.objects.all()

    myObj = Photo.objects.last()
    image_path = myObj.file.path

    return render(request, 'album/home.html', {'photos': photos})


def rotate_cw(request):

    # photos = Photo.file.path
    # print(photos)

    myObj = Photo.objects.last()

    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.rotate(-90)
    # out = img.transpose(PIL.Image.ROTATE_90)
    out.save(image_path)

    return redirect('effects')


def rotate_acw(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)
    out = img.rotate(90)
    out.save(image_path)

    return redirect('effects')


def flip_left_right(request):

    # photos = Photo.file.path
    # print(photos)

    myObj = Photo.objects.last()

    image_path = myObj.file.path

    img = Image.open(image_path)
    out = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    out.save(image_path)

    return redirect('effects')


def flip_top_bottom(request):

    # photos = Photo.file.path
    # print(photos)

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)
    out = img.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    out.save(image_path)

    return redirect('effects')


def image_transerve(request):

    # photos = Photo.file.path
    # print(photos)

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)
    out = img.transpose(PIL.Image.TRANSVERSE)
    out.save(image_path)

    return redirect('effects')


def resize_minus(request):

    myObj = Photo.objects.last()
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

    return redirect('effects')


def resize_plus(request):

    myObj = Photo.objects.last()
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

    return redirect('effects')


def brightness(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 1.5  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects')


def darkness(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Brightness(img)

    factor = 0.5  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects')


def blurness(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Sharpness(img)

    factor = 0.05  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects')


def sharpness(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # image brightness enhancer
    enhancer = ImageEnhance.Sharpness(img)

    factor = 2  # gives original image
    out = enhancer.enhance(factor)
    out.save(image_path)

    return redirect('effects')


def grayscale(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    out = ImageOps.grayscale(img)
    out.save(image_path)

    return redirect('effects')


def postarize(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # applying posterize method
    out = ImageOps.posterize(img, 2)
    out.save(image_path)

    return redirect('effects')


def filter(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # applying the rank filter
    out = img.filter(ImageFilter.RankFilter(size=3, rank=3 * 3 - 1))
    out.save(image_path)

    return redirect('effects')


def edges(request):

    myObj = Photo.objects.last()
    image_path = myObj.file.path
    img = Image.open(image_path)

    # Converting the image to greyscale, as edge detection
    # requires input image to be of mode = Greyscale (L)
    # image = img.convert("L")

    # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    out = img.convert("L").filter(ImageFilter.FIND_EDGES)

    # Saving the Image Under the name Edge_Sample.png
    out.save(image_path)

    return redirect('effects')


def delete(request):
    myObj = Photo.objects.last()

    if myObj is None:
        return redirect('effects')
    else:
        myObj.delete()
        return redirect('photo_list')


def save(request):
    myObj = Photo.objects.last()
    image_path = myObj.file.path
    image_name = myObj.file.name

    if myObj is None:
        return redirect('effects')
    else:
        myObj.save()

        urllib.request.urlretrieve(image_path, image_name)
        return redirect('effects')


class Effects(View):
    """Return the available effects."""

    def get(self, requests):
        """Return all the effects available."""

        templates = 'album/home.html'
        photos = Photo.objects.all()

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

        return render(requests, templates, {'effects': effects, 'photos': photos})

# Create list  to handle respective effects
