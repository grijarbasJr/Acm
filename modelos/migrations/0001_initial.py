# Generated by Django 3.1.4 on 2021-03-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_secure_init', models.DateField(max_length=10)),
                ('machine_secure_end', models.DateField(max_length=10)),
                ('machine_status', models.CharField(choices=[('V', 'Vendido'), ('P', 'pertence')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateTimeField(auto_now=True)),
                ('oil_liters', models.IntegerField()),
                ('oil_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('service_hours', models.IntegerField()),
                ('money_advance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_hours_service_month', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
