# Generated by Django 2.1.4 on 2018-12-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0003_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ordendevolucion',
            name='orden_salida',
        ),
        migrations.RemoveField(
            model_name='ordensalida',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='ordendevolucion',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='appStock.Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('A', 'Redes'), ('B', 'TV'), ('C', 'Insumo')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='ordendevolucion',
            name='cliente_destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='appStock.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordensalida',
            name='cliente_destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='appStock.Cliente'),
            preserve_default=False,
        ),
    ]