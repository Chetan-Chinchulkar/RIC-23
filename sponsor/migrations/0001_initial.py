# Generated by Django 4.1.6 on 2023-05-06 17:32

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cat",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Sponsor",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("pic", models.ImageField(upload_to="sponsor")),
                ("text", ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name="SponsorReg",
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
                ("company_name", models.CharField(max_length=255)),
                ("company_email", models.EmailField(default="", max_length=254)),
                ("poc_name", models.CharField(default="", max_length=255)),
                ("poc_email", models.EmailField(default="", max_length=254)),
                (
                    "poc_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "poc_designation",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "type_sponsor",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Monetary Sponsorship", "Monetary Sponsorship"),
                            ("In Kind Sponsorship", "In Kind Sponsorship"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Title Sponsorship", "Title Sponsorship"),
                            ("Co Sponsorship", "Co Sponsorship"),
                            ("Platinum Sponsorship", "Platinum Sponsorship"),
                            ("Gold Sponsorship", "Gold Sponsorship"),
                            ("Silver Sponsorship", "Silver Sponsorship"),
                            ("Bronze Sponsorship", "Bronze Sponsorship"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("logo", models.ImageField(upload_to="sponsor")),
            ],
        ),
        migrations.CreateModel(
            name="OurSponsor",
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
                ("name", models.CharField(max_length=150)),
                ("pic", models.ImageField(default="", upload_to="oursponsor")),
                (
                    "cat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsor.cat",
                    ),
                ),
            ],
        ),
    ]
