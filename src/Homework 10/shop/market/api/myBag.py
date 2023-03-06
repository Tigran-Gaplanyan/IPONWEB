#
from django.views.generic import View

#
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#
from .serializers import MyBagSerializer

#
from ..models import MyBag, Item


class MyBagView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = MyBag.objects.all()
    serializer_class = MyBagSerializer

    def get_single(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        customer_id = serializer.data['customer']
        customer = User.objects.get(id=customer_id)
        total_price = instance.calculate_total_price()
        return Response({'my_bag': serializer.data, 'total_price': total_price})

    @api_view(['GET'])
    def get(self, request):
        user = self.request.user
        my_bag = MyBag.objects.filter(customer=user).first()
        serializer = self.get_serializer(my_bag)
        total_price = my_bag.calculate_total_price()
        return Response({'my_bag': serializer.data, 'total_price': total_price})

    @api_view(['POST'])
    def post(self, request):
        customer = self.request.user
        items = request.data.get('items')
        my_bag = MyBag.objects.filter(customer=customer).first()
        if my_bag is None:
            my_bag = MyBag.objects.create(customer=customer)
        for item_id in items:
            item = Item.objects.get(id=item_id)
            my_bag.items.add(item)
        my_bag.save()
        serializer = self.get_serializer(my_bag)
        total_price = my_bag.calculate_total_price()
        return Response({'my_bag': serializer.data, 'total_price': total_price}, status=status.HTTP_201_CREATED)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.get_single(request, id)
        if request.method == "PATCH":
            return MyBagView.get_single(request, id)

    @api_view(['DELETE'])
    def delete(self, request, pk=None):
        my_bag = MyBag.objects.get(id=pk)
        if my_bag.customer == self.request.user:
            my_bag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @api_view(['PUT'])
    def edit(request, customer_id):
        try:
            data = request.data

            bag_items = MyBag.objects.filter(customer_id=customer_id)
            serializer = MyBagSerializer(bag_items, data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            total_price = sum(item.price * item.quantity for item in bag_items)

            return Response({"total_price": total_price})
        except:
            return Response(status=400)
