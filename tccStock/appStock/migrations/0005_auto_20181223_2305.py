# Generated by Django 2.1.4 on 2018-12-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0004_auto_20181223_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes Destinos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
