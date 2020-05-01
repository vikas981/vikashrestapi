from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Test
from django.views.decorators.csrf import csrf_exempt
from .serializers import TestSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import BaseAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    lookup_field = 'id'
    authentication_classes = [BaseAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class TestAPIView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class TestDetails(APIView):
    def get_object(self, id):
        try:
            return Test.objects.get(id=id)
        except Test.DoesNotExist:
            return HttpResponse(status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        test = self.get_object(id)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    def put(self, request, id):
        test = self.get_object(id)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        test = self.get_object(id)
        test.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def test_list(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def test_detail(request, pk):
    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return HttpResponse(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TestSerializer(test)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        test.delete()
        return HttpResponse(status.HTTP_204_NO_CONTENT)
