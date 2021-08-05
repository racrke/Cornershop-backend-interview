import json
import uuid

from django.core import serializers
from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rest_framework import status
from rest_framework.views import APIView

from norasystem.models import *
from norasystem.slack import *


class MenuView(APIView):
    def get(self, request, *args, **kwargs):
        """
        Shows today's menu
        """
        try:
            m = Menu.objects.get(pk=kwargs["uuid"])
            dishes = Dish.objects.filter(menu_id=kwargs["uuid"])
            dishes_json = serializers.serialize("json", dishes)
        except Menu.DoesNotExist:
            raise Http404("Menu does not exist")
        return HttpResponse(dishes_json, content_type="application/json")

    def post(self, request):
        """
        Creates a new menu
        """
        m = Menu.objects.create(uuid=str(uuid.uuid4()))
        m.save()
        data = json.loads(request.body)
        for dish in data["dishes"]:
            d = Dish.objects.create(menu=m, name=dish["name"])
            d.save()
        return HttpResponse(
            json.dumps({"result": "success"}), content_type="application/json"
        )


@csrf_exempt
@require_POST
def create_request(request):
    """
    Creates a new dish request
    """
    try:
        data = json.loads(request.body)
        employee = Employee.objects.get(phone_number=data["phone_number"])
        dish = Dish.objects.get(pk=data["dish_id"])
        request = Request.objects.create(employee=employee)
        request.save()
        req_dish = RequestedDish.objects.create(
            dish=dish, request=request, notes=data["notes"]
        )
        req_dish.save()
    except Exception as e:
        print(e)
        return HttpResponse({"error": e}, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(
        json.dumps({"result": "success"}), content_type="application/json"
    )


@csrf_exempt
@require_POST
def create_employee(request):
    """
    Creates a new employee
    """
    try:
        data = json.loads(request.body)
        e = Employee.objects.create(
            full_name=data["full_name"],
            slack_id=data["slack_id"],
            phone_number=int(data["phone_number"]),
        )
        e.save()
    except Exception as e:
        return HttpResponse({"error": e}, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse(
        json.dumps({"result": "success"}), content_type="application/json"
    )


@csrf_exempt
@require_GET
def show_today(request, uuid):
    """
    Shows today's clients, choices and specifications
    """
    query = RequestedDish.objects.values(
        "request__employee__full_name", "dish__menu__uuid", "dish__name", "notes"
    ).filter(dish__menu__uuid=uuid)
    resp = list(query)
    return JsonResponse(resp, safe=False)
