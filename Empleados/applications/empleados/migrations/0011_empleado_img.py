# Generated by Django 4.2.3 on 2023-09-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0010_empleado_nombrecompleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
