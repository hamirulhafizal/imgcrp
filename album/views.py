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
from . import views
from django.views.generic.base import TemplateView
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from PIL import Image, ImageOps, ImageFilter, ImageChops, ImageEnhance

from django.shortcuts import get_object_or_404


def compare(request):
    photos = Photo.objects.all()
    return render(request, 'album/compare.html', {'photos': photos})


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('effect')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})


def photo_list_pk(request, id_image):
    try:
        photos = Photo.objects.get(id=id_image)
        photos_pk = get_object_or_404(Photo, id=id_image)
        form = PhotoForm()
        return render(request, 'album/home.html', {'photos_pk': photos_pk, 'photos': photos})

    except Photo.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
