# Generated by Django 4.1.2 on 2024-07-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='precio',
            field=models.IntegerField(),
        ),
    ]