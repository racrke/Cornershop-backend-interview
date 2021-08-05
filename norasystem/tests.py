import json
import uuid

from django.test import Client, TestCase
from django.urls import reverse

from norasystem.models import *


# Create your tests here.
class MenuTest(TestCase):
    """
    Test for Menu creation, Menu viewing
    """

    client = Client()

    def test_menu_show(self):
        menu_id = str(uuid.uuid4())
        m = Menu.objects.create(uuid=menu_id)
        m.save()
        Dish.objects.create(menu=m, name="test dish 1").save()
        Dish.objects.create(menu=m, name="test dish 2").save()

        response = self.client.get("/api/menu/" + menu_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 2)

    def test_menu_create(self):

        response = self.client.post(
            "/api/menu",
            json.dumps({"dishes": [{"name": "Pizza"}, {"name": "Pollo"}]}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)


class EmployeeTest(TestCase):
    """
    Test for Employee creation
    """

    client = Client()

    def test_employe_create(self):
        response = self.client.post(
            "/api/employee",
            json.dumps(
                {
                    "phone_number": 811006092,
                    "slack_id": "ABCJDKEHF",
                    "full_name": "Employee test",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)


class RequestTest(TestCase):
    """
    Tests for Dish request and viewing orders (admin)
    """

    client = Client()

    def test_requested_dish_integral(self):
        """
        Creates a menu with two dishes, then an employee makes a request
        from the menu. Finally, The admin can view the order.
        """

        menu_id = str(uuid.uuid4())
        m = Menu.objects.create(uuid=menu_id)
        m.save()
        d1 = Dish.objects.create(menu=m, name="test dish 1")
        d1.save()
        d2 = Dish.objects.create(menu=m, name="test dish 2")
        d2.save()

        Employee.objects.create(
            full_name="Employee test", phone_number=811006092
        ).save()

        # Verifies Dish request is created successfully
        response = self.client.post(
            "/api/request",
            json.dumps(
                {
                    "phone_number": 811006092,
                    "dish_id": d1.id,
                    "notes": "No specifications",
                }
            ),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

        # Verifies admin can view the orders and specifications
        response = self.client.get("/api/report/" + menu_id)
        self.assertEqual(len(json.loads(response.content)), 1)
