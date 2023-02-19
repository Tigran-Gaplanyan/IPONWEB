import json
from django.views.generic import View
from ..models import Customer
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


class CustomerView(View):
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
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            data.append({"user": customer.user, "id": customers.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.create(
            user=data["user"]
        )
        customer.save()
        return self.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.get_single(request, id)
        if request.method == "PATCH":
            return CustomerView.get_single(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return CustomerView.data_status({"id": customer.id, "user": customer.user})


    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        customer.delete()
        return CustomerView.ok_status()


    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "user" in data:
            customer.user = data["user"]
        customer.save()
        return CustomerView.ok_status()
