#
from django.views.generic import View

from .serializers import PurchaseSerializer
#
from ..models import Purchase, Customer, Item

#
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PurchaseView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get_single(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        customer_id = serializer.data['customer']
        customer = Customer.objects.get(id=customer_id)
        total_price = instance.calculate_total_price()
        return Response({'purchase': serializer.data, 'total_price': total_price})

    @api_view(['POST'])
    def post(self, request, *args, **kwargs):
        customer_id = request.data['customer']
        item_ids = request.data['items']
        items = Item.objects.filter(id__in=item_ids)
        purchase = Purchase.objects.create(customer_id=customer_id)
        purchase.items.set(items)
        purchase.save()
        total_price = purchase.calculate_total_price()
        return Response({'purchase': PurchaseSerializer(purchase).data, 'total_price': total_price}, status=201)

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.get_single(request, id)
        if request.method == "PATCH":
            return PurchaseView.get_single(request, id)

    @api_view(['GET'])
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = []
        for purchase in serializer.data:
            customer_id = purchase['customer']
            customer = Customer.objects.get(id=customer_id)
            total_price = Purchase.objects.get(id=purchase['id']).calculate_total_price()
            data.append({'purchase': purchase, 'total_price': total_price})
        return Response(data)

    @api_view(['DELETE'])
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        customer_id = instance.customer.id
        total_price = instance.calculate_total_price()
        self.perform_destroy(instance)
        return Response({'customer_id': customer_id, 'total_price': total_price})

    @api_view(['PUT'])
    def edit(request, customer_id):
        try:
            data = request.data

            purchase_items = Purchase.objects.filter(customer_id=customer_id)
            serializer = PurchaseSerializer(purchase_items, data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            total_price = sum(item.price * item.quantity for item in purchase_items)

            return Response({"total_price": total_price})
        except:
            return Response(status=400)
