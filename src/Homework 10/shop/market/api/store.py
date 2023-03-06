import json

#
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StoreSerializer
#
from ..models import Store

#
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StoreView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def get_single(request, pk):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store)
        return Response(serializer.data)

    @api_view(['POST'])
    def post(request):
        serializer = StoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.get_single(request, id)
        if request.method == "PATCH":
            return StoreView.get_single(request, id)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def edit(request, pk):
        try:
            store = Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
