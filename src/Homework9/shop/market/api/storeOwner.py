import json
from django.views.generic import View
from ..models import StoreOwner
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class StoreOwnerView(View):
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
        storeOwners = StoreOwner.objects.all()
        data = []
        for storeOwner in storeOwners:
            data.append({"user": storeOwner.user, "id": storeOwner.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        storeOwner = StoreOwner.objects.create(
            user=data["user"]
        )
        storeOwner.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.get_single(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            storeOwner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status({"id": storeOwner.id, "user": storeOwner.user})


    @staticmethod
    def delete(request, id):
        try:
            storeOwner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        storeOwner.delete()
        return StoreOwnerView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            storeOwner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "user" in data:
            storeOwner.user = data["user"]
        storeOwner.save()
        return StoreOwnerView.ok_status()
