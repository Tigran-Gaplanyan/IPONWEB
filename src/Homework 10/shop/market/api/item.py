#
from django.views.generic import View

#
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#
from .serializers import ItemSerializer

#
from ..models import Item


class ItemView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def get_single(request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)
        return Response(serializer.data)

    @api_view(['POST'])
    def post(request):
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.get_single(request, id)
        if request.method == "PATCH":
            return ItemView.get_single(request, id)

    @api_view(['DELETE'])
    def delete(request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    def edit(request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
