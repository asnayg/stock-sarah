# Generated by Django 2.1.4 on 2019-01-27 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0007_stockcliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordendevolucion',
            old_name='cliente_destino',
            new_name='cliente_origen',
        ),
    ]
