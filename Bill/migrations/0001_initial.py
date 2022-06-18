# Generated by Django 4.0.3 on 2022-06-15 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Fruitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1)),
                ('totalPrice', models.IntegerField(default=0)),
                ('code', models.IntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Bill',
            },
        ),
        migrations.CreateModel(
            name='DetailBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bill.bill')),
                ('fruit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Fruitapp.fruits')),
            ],
            options={
                'db_table': 'Detailbill',
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='LisFruits',
            field=models.ManyToManyField(through='Bill.DetailBill', to='Fruitapp.fruits'),
        ),
    ]