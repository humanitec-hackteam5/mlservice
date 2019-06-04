from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from app.serializers import TrainSerializer


class TrainViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = TrainSerializer


class PredictView(views.APIView):

    def post(self):
        return Response(data={})
