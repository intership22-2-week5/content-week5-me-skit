# Generated by Django 4.0.6 on 2022-07-19 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('creation_date', models.DateField()),
                ('estimated_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('arworklist', models.ManyToManyField(to='artwork.artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('creation_date', models.DateField()),
                ('arwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artwork.artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Exposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('portfolios', models.ManyToManyField(to='artwork.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='authors',
            field=models.ManyToManyField(to='artwork.author'),
        ),
    ]