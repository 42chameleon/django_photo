from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from photo.models import Photo
from photo.serializers import UploadSerializer


class UploadPhotoApiView(APIView):
    pareser_classes = (MultiPartParser, FormParser)
    serializer_class = UploadSerializer

    def post(self, request, format=None):
        upload = self.serializer_class(data=request.FILES)

        if upload.is_valid():
            image = Photo(image=upload.validated_data['image'])
            image.save()
            return Response({'success': 'Imported successfully'})
        else:
            return Response(upload.errors, status=400)
