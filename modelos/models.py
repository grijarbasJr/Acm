from django.db import models


class Oil(models.Model):
    buy_date = models.DateTimeField(auto_now=True, null=False)
    oil_liters = models.IntegerField(null=False)
    oil_price = models.DecimalField(decimal_places=2, max_digits=10, null=False)


class Operator(models.Model):
    name = models.CharField(max_length=50, null=False)
    service_hours = models.IntegerField(null=False)
    money_advance = models.DecimalField(decimal_places=2, max_digits=10)
    total_hours_service_month = models.DecimalField(decimal_places=2, max_digits=10)


class Machine(models.Model):
    status_choices = (
        ("V", "Vendido"),
        ("P", "Pertence"),
    )
    machine_secure_init = models.DateField(max_length=10, null=False)
    machine_secure_end = models.DateField(max_length=10, null=False)
    machine_status = models.CharField(max_length=10, choices=status_choices, blank=False, null=False)
    machine_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.machine_name}"


class Revision(models.Model):
    status_choices = (
        ("P", "Parcial"),
        ("G", "Geral"),
    )
    machine_revision = models.CharField(max_length=10, choices=status_choices, blank=False, null=False)
    machine_revision_date = models.DateField(max_length=10, null=False)
    machine_revision_orin = models.IntegerField(null=False)


class Service(models.Model):
    machine_service_name = models.ForeignKey(Machine, on_delete=models.RESTRICT)
    service_operator = models.CharField(max_length=50, blank=False, null=False)
    initial_orin = models.IntegerField(null=False)
    final_orin = models.IntegerField(null=False)
    service_client = models.CharField(max_length=50, null=False)
    money_advance = models.DecimalField(decimal_places=2, max_digits=10)
    hour_valor = models.DecimalField(decimal_places=2, max_digits=4)
    total_value_service = models.DecimalField(decimal_places=2, max_digits=10)


class Smachines(models.Model):
    status_choices = (
        ("P", "Pago"),
        ("G", "Não pago"),
    )
    sec_name_machine = models.ForeignKey(Machine, on_delete=models.RESTRICT)
    secure_final_date = models.DateField(max_length=10, null=False)
    secure_initial_date = models.DateField(max_length=10, null=False)
    secure_text_d = models.CharField(max_length=50, blank=False, null=False)
    s_parcel_numb = models.IntegerField(null=False)
    s_parcel_total = models.DecimalField(decimal_places=2, max_digits=4)
    s_parc_pag = models.CharField(max_length=10, choices=status_choices, blank=False, null=False)


class Parcmachine(models.Model):
    status_choices = (
        ("P", "Pago"),
        ("G", "Não pago"),
    )
    parc_name_machine = models.ForeignKey(Machine, on_delete=models.RESTRICT)
    parc_machine_value = models.DecimalField(decimal_places=2, max_digits=10)
    parc_parcel = models.IntegerField(null=False)
    parc_pag = models.CharField(max_length=10, choices=status_choices, blank=False, null=False)
















