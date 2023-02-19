import json
from django.views.generic import View
from ..models import StoreCategory
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class StoreCategoryView(View):
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
        storeCategories = StoreCategory.objects.all()
        data = []
        for storeCategory in storeCategories:
            data.append({"name": storeCategory.name, "id": storeCategory.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        storeCategory = StoreCategory.objects.create(
            name=data["name"]
        )
        storeCategory.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.get_single(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            storeCategory = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreCategoryView.data_status({"id": storeCategory.id, "name": storeCategory.name})


    @staticmethod
    def delete(request, id):
        try:
            storeCategory = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        storeCategory.delete()
        return StoreCategoryView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            storeCategory = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            storeCategory.name = data["name"]
        storeCategory.save()
        return StoreCategoryView.ok_status()
