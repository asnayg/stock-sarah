# Generated by Django 2.1.4 on 2018-12-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0002_auto_20181222_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('S', 'Stock'), ('B', 'BackUp'), ('U', 'En USO')], default='S', max_length=1),
        ),
    ]
