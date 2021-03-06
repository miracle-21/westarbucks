# Generated by Django 4.0.5 on 2022-06-06 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_drink_alter_drink_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Allergy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'allergy_drinks',
            },
        ),
        migrations.AddField(
            model_name='allergy',
            name='category',
            field=models.ManyToManyField(through='products.Allergy_drink', to='products.drink'),
        ),
    ]
