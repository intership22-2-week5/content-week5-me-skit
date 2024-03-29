# Generated by Django 4.0.6 on 2022-07-20 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devise', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(default='abierta', max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.item')),
            ],
            bases=('order.item',),
        ),
        migrations.CreateModel(
            name='InputDevise',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.item')),
                ('type', models.CharField(max_length=100)),
            ],
            bases=('order.item',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.item')),
                ('size', models.CharField(max_length=50)),
            ],
            bases=('order.item',),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.item')),
                ('orden', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('inputdevise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.inputdevise')),
            ],
            bases=('order.inputdevise',),
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('inputdevise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order.inputdevise')),
            ],
            bases=('order.inputdevise',),
        ),
    ]
