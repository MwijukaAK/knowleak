from rest_framework import generics, mixins
from rest_framework.response import Response
from .serializers import ReadingSerializer
from app.models import Reading

class ReadingListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	permission_classes = []
	authentication_classes = []
	queryset = Reading.objects.all()
	serializer_class = ReadingSerializer

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ReadingDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
	permission_classes = []
	authentication_classes = []
	queryset = Reading.objects.all()
	serializer_class = ReadingSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)