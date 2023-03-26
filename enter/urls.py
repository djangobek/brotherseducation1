from django.urls import path
from .views import *

urlpatterns = [
    path('', courseBar, name='maindir'),
    path("natijalar/", Table.as_view(), name="mianexammet"),
    path("registration/", blog_post, name='registration'),
    path("kurslar/", Newfilebar, name='kurslarim'),
    path("izohlar/",feedback_view, name='feedback' )
]