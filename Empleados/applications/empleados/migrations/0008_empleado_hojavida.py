# Generated by Django 4.2.3 on 2023-08-04 02:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0007_remove_empleado_hojavida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hojaVida',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
