# Generated by Django 4.1.6 on 2023-04-27 04:30

from django.db import migrations, models
import django.db.models.deletion


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
            name="Dept",
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
            name="Position",
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
                ("title", models.CharField(max_length=150)),
                (
                    "subtitle",
                    models.CharField(blank=True, default="", max_length=150, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("order", models.IntegerField(default=1)),
                ("number", models.IntegerField(blank=True, null=True)),
                ("pic", models.ImageField(default="", upload_to="team")),
                (
                    "cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="team.cat"
                    ),
                ),
                (
                    "dept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="team.dept"
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="team.position"
                    ),
                ),
            ],
        ),
    ]