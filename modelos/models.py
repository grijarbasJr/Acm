from django.db import models


class Oil(models.Model):
    buy_date = models.DateTimeField(auto_now=True, null=False)
    oil_liters = models.IntegerField(null=False)
    oil_price = models.DecimalField(decimal_places=2, max_digits=5, null=False)


class Operator(models.Model):
    name = models.CharField(max_length=50, null=False)
    service_hours = models.IntegerField(null=False)
    money_advance = models.DecimalField(decimal_places=2, max_digits=5)
    total_hours_service_month = models.DecimalField(decimal_places=2, max_digits=5)


class Machine(models.Model):
    status_choices = (
        ("V","Vendido"),
        ("P","pertence"),
    )
    machine_secure_init = models.DateField(max_length=10, null=False)
    machine_secure_end = models.DateField(max_length=10, null=False)
    machine_status = models.CharField(max_length=10, choices=status_choices, blank=False, null=False)




