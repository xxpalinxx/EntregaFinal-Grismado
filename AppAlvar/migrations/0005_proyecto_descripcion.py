# Generated by Django 5.0.3 on 2024-03-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAlvar', '0004_alter_proyecto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
