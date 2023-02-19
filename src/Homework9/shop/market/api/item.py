import json
from django.views.generic import View
from ..models import Item
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class ItemView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            status=200,
            content_type="application/json",
        )

    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}),
            status=200,
            content_type="application/json"
        )

    def get(self, request):
        items = Item.objects.all()
        data = []
        for item in items:
            data.append({"name": item.name, "id": item.id, "price": item.price, "quantity": item.quantity})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
        )
        item.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.get_single(request, id)
        if request.method == "PATCH":
            return ItemView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemView.data_status({"id": item.id, "name": item.name, "price": item.price, "quantity": item.quantity})


    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        item.delete()
        return ItemView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            item.name = data["name"]
        if "price" in data:
            item.price = data["price"]
        if "quantity" in data:
            item.quantity = data["quantity"]
        item.save()
        return ItemView.ok_status()
