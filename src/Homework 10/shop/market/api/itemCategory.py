#
from django.views.generic import View

#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#
from .serializers import ItemCategorySerializer

#
from ..models import ItemCategory


class ItemCategoryView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(request):
        categories = ItemCategory.objects.all()
        serializer = ItemCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def post(self, request):
        serializer = ItemCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.get_single(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.get_single(request, id)

    @api_view(['GET'])
    def get_single(request, pk):
        try:
            category = ItemCategory.objects.get(pk=pk)
        except ItemCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['DELETE'])
    def delete(self, request, pk):
        try:
            category = ItemCategory.objects.get(pk=pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ItemCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update_item_category(request, pk):
        try:
            item_category = ItemCategory.objects.get(pk=pk)
        except ItemCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemCategorySerializer(item_category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
