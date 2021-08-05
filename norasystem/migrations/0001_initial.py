# Generated by Django 3.0.8 on 2021-08-05 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('slack_id', models.CharField(max_length=9)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RequestedDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=100)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norasystem.Dish')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norasystem.Request')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='dishes',
            field=models.ManyToManyField(through='norasystem.RequestedDish', to='norasystem.Dish'),
        ),
        migrations.AddField(
            model_name='request',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norasystem.Employee'),
        ),
        migrations.AddField(
            model_name='dish',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norasystem.Menu'),
        ),
    ]
