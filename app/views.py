from google.cloud import vision

from rest_framework import views, status, permissions
from rest_framework.response import Response


class ImageLabelsView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        url = request.data.get('url')
        if not url:
            return Response({'detail': 'Please provide image URL'}, status=status.HTTP_400_BAD_REQUEST)

        client = vision.ImageAnnotatorClient()
        response = client.annotate_image({
            'image': {'source': {'image_uri': url}},
            'features': [{'type': vision.enums.Feature.Type.LABEL_DETECTION}],
        })
        return Response([{'label': item.description, 'score': item.score} for item in response.label_annotations])
