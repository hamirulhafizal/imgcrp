"""
Definition of views.
"""
import os
import shutil
import pathlib

from django import template
from datetime import datetime
from django.db import models
from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm
from django.views.generic.base import TemplateView
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View

from PIL import Image, ImageOps, ImageFilter, ImageChops, ImageEnhance


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('effects')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})


def compare(request):
    photos = Photo.objects.all()
    return render(request, 'album/compare.html', {'photos': photos})


def rotate(request):
    """Renders the contact page."""

    # photos = Photo.file.path
    # print(photos)

    myObj = Photo.objects.last()

    image_path = myObj.file.path

    img = Image.open(image_path)
    img_90 = img.rotate(270)
    img_90.save(image_path)

    return redirect('effects')
    # return redirect('home')

# class Effects(TemplateView):
#
#     template_name = "effects.html"
#
#     def get_context_data(self, *args, **kwargs):
#
#         context = super(Effects, self).get_context_data(*args, **kwargs)
#         context["title"] = "this is title"
#         return context
