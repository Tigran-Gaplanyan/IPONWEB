import json
from django.views.generic import View
from ..models import ItemCategory
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class ItemCategoryView(View):
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
        itemCategories = ItemCategory.objects.all()
        data = []
        for itemCategory in itemCategories:
            data.append({"name": itemCategory.name, "id": itemCategory.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        itemCategory = ItemCategory.objects.create(
            name=data["name"]
        )
        itemCategory.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.get_single(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            itemCategory = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemCategory.data_status({"id": itemCategory.id, "name": itemCategory.name})


    @staticmethod
    def delete(request, id):
        try:
            itemCategory = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        itemCategory.delete()
        return ItemCategoryView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            itemCategory = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            itemCategory.name = data["name"]
        itemCategory.save()
        return ItemCategoryView.ok_status()
