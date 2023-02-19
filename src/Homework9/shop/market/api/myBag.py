import json
from django.views.generic import View
from ..models import MyBag
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class MyBagView(View):
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
        myBags = MyBag.objects.all()
        data = []
        for myBag in myBags:
            data.append({"total_price": myBag.total_price, "id": myBag.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        myBag = MyBag.objects.create(
            total_price=data["total_price"]
        )
        myBag.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.get_single(request, id)
        if request.method == "PATCH":
            return MyBagView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            myBag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return MyBagView.data_status({"id": myBag.id, "total_price": myBag.total_price})


    @staticmethod
    def delete(request, id):
        try:
            myBag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        myBag.delete()
        return MyBagView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            myBag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "total_price" in data:
            myBag.total_price = data["total_price"]
        myBag.save()
        return MyBagView.ok_status()
