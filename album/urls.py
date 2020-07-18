from django.urls import path
from django.conf.urls import url
from . import views, effects
from .effects import Effects

urlpatterns = [

    url(r'^$', views.photo_list, name='photo_list'),
    url('compare/', views.compare, name='compare'),
    url('effects/', Effects.as_view(), name='effects'),
    url('rotate_cw/', effects.rotate_cw, name='rotate_cw'),
    url('rotate_acw/', effects.rotate_acw, name='rotate_acw'),
    url('flip_left_right/', effects.flip_left_right, name='flip_left_right'),
    url('flip_top_bottom/', effects.flip_top_bottom, name='flip_top_bottom'),
    url('image_transerve/', effects.image_transerve, name='image_transerve'),
    url('resize_plus/', effects.resize_plus, name='resize_plus'),
    url('resize_minus/', effects.resize_minus, name='resize_minus'),
    url('brightness/', effects.brightness, name='brightness'),
    url('darkness/', effects.darkness, name='darkness'),
    url('blurness/', effects.blurness, name='blurness'),
    url('sharpness/', effects.sharpness, name='sharpness'),
    url('grayscale/', effects.grayscale, name='grayscale'),
    url('postarize/', effects.postarize, name='postarize'),
    url('filter/', effects.filter, name='filter'),
    url('edges/', effects.edges, name='edges'),
    url('delete/', effects.delete, name='delete'),
    url('save/', effects.save, name='save'),
    url('rotate/', views.rotate, name='rotate'),

    # path('home/', views.home, name='home'),

]
