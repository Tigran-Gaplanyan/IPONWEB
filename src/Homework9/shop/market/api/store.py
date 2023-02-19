import json
from django.views.generic import View
from ..models import Store
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class StoreView(View):
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
        stores = Store.objects.all()
        data = []
        for store in stores:
            data.append({"name": store.name, "id": store.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        store = Store.objects.create(
            name=data["name"]
        )
        store.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.get_single(request, id)
        if request.method == "PATCH":
            return StoreView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreView.data_status({"id": store.id, "name": store.name})


    @staticmethod
    def delete(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        store.delete()
        return StoreView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            store.name = data["name"]
        store.save()
        return StoreView.ok_status()
