from django.conf.urls import url
from django.urls import path


from . import views

app_name = 'upload'

urlpatterns = [
    path('upload-file/', views.upload, name='upload_file'),
]