# Generated by Django 4.1.3 on 2022-11-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pruebaping_equipo_alter_pruebaping_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pruebaping',
            name='fechaPrueba',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]