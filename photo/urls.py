from django.conf.urls import url

from photo.views import UploadPhotoApiView

urlpatterns = [
    url(r'import/', UploadPhotoApiView.as_view(), name='import'),
]
