#
from django.views.generic import View

#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#
from .serializers import StoreCategorySerializer

#
from ..models import StoreCategory


class StoreCategoryView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(request):
        categories = StoreCategory.objects.all()
        serializer = StoreCategorySerializer(categories, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def get_single(request, pk):
        try:
            category = StoreCategory.objects.get(pk=pk)
        except StoreCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreCategorySerializer(category)
        return Response(serializer.data)

    @api_view(['POST'])
    def post(request):
        serializer = StoreCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.get_single(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.get_single(request, id)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            store_category = StoreCategory.objects.get(pk=pk)
        except StoreCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        store_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def edit(request, pk):
        try:
            category = StoreCategory.objects.get(pk=pk)
        except StoreCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StoreCategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
