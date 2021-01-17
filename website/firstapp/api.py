from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firstapp.serializers import uniinfserializer, Program_Highlightsserializer
from firstapp.models import Uniinf, Program_Highlights
from rest_framework.authentication.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class universities(APIView):
    def get(self, request):
        model = Uniinf.objects.all()
        serializer = uniinfserializer(model, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = uniinfserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

class universitydetail(APIView):
    def get(self, request, Rank):
        try:
            model = Uniinf.objects.get(id = Rank)
        except Uniinf.DoesNotExist:
            return Response(f"Rank {Rank} with University NOT FOUND.", status=status.HTTP_404_NOT_FOUND)
        serializer = uniinfserializer(model)
        return Response(serializer.data)

