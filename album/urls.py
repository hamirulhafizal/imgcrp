from django.urls import path
from django.conf.urls import url
from . import views, effects
from .effects import Effects
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

                  path('', effects.home, name='home'),
                  url(r'photo_list/', views.photo_list, name='photo_list'),
                  url(r'compare/', views.compare, name='compare'),

                  url(r'^effects/(?P<id_image>[0-9]+)/$', Effects.as_view(), name='effects'),

                  url(r'^rotate_cw/(?P<id_image>[0-9]+)/$', effects.rotate_cw, name='rotate_cw'),
                  url(r'^rotate_acw/(?P<id_image>[0-9]+)/', effects.rotate_acw, name='rotate_acw'),
                  url(r'flip_left_right/(?P<id_image>[0-9]+)/', effects.flip_left_right, name='flip_left_right'),
                  url(r'flip_top_bottom/(?P<id_image>[0-9]+)/', effects.flip_top_bottom, name='flip_top_bottom'),
                  url(r'image_transerve/(?P<id_image>[0-9]+)/', effects.image_transerve, name='image_transerve'),
                  url(r'resize_plus/(?P<id_image>[0-9]+)/', effects.resize_plus, name='resize_plus'),
                  url(r'resize_minus/(?P<id_image>[0-9]+)/', effects.resize_minus, name='resize_minus'),
                  url(r'brightness/(?P<id_image>[0-9]+)/', effects.brightness, name='brightness'),
                  url(r'darkness/(?P<id_image>[0-9]+)/', effects.darkness, name='darkness'),
                  url(r'blurness/(?P<id_image>[0-9]+)/', effects.blurness, name='blurness'),
                  url(r'sharpness/(?P<id_image>[0-9]+)/', effects.sharpness, name='sharpness'),
                  url(r'grayscale/(?P<id_image>[0-9]+)/', effects.grayscale, name='grayscale'),
                  url(r'postarize/(?P<id_image>[0-9]+)/', effects.postarize, name='postarize'),
                  url(r'filter/(?P<id_image>[0-9]+)/', effects.filter, name='filter'),
                  url(r'edges/(?P<id_image>[0-9]+)/', effects.edges, name='edges'),
                  url(r'delete/(?P<id_image>[0-9]+)/', effects.delete_id, name='delete_id'),
                  url(r'dlt/', effects.dlt, name='dlt'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)