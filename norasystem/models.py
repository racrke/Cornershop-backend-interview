from django.db import models

# Create your models here.


class Menu(models.Model):
    """
    A colecction of dishes
    """

    uuid = models.CharField(max_length=36, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Dish(models.Model):
    """
    Food or Dish entity
    """

    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Employee(models.Model):
    """
    The employee who requests
    """

    full_name = models.CharField(max_length=30)
    slack_id = models.CharField(max_length=9)
    phone_number = models.IntegerField()


class Request(models.Model):
    """
    One or many dish Requests from the menu
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, through="RequestedDish")


class RequestedDish(models.Model):
    """
    A requested dish
    """

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)
