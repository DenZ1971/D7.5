# Generated by Django 4.1.4 on 2022-12-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("DI", "Директор"),
                            ("AD", "Администратор"),
                            ("CO", "Повар"),
                            ("CA", "Кассир"),
                            ("CL", "Уборщик"),
                        ],
                        default="CA",
                        max_length=2,
                    ),
                ),
                ("labor_contract", models.IntegerField()),
            ],
        ),
    ]