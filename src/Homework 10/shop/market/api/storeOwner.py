import json

#
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StoreOwnerSerializer
#
from ..models import StoreOwner

#
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StoreOwnerView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(request):
        categories = StoreOwner.objects.all()
        serializer = StoreOwnerSerializer(categories, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def get_single(request, pk):
        try:
            category = StoreOwner.objects.get(pk=pk)
        except StoreOwner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreOwnerSerializer(category)
        return Response(serializer.data)

    @api_view(['POST'])
    def post(request):
        serializer = StoreOwnerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.get_single(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.get_single(request, id)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            owner = StoreOwner.objects.get(pk=pk)
        except StoreOwner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def edit(request, pk):
        try:
            owner = StoreOwner.objects.get(pk=pk)
        except StoreOwner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreOwnerSerializer(owner, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
