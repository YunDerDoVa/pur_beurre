# Generated by Django 3.0.7 on 2020-06-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0008_auto_20200614_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutriment',
            name='quantity',
        ),
        migrations.CreateModel(
            name='FoodNutriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodfinder.Food')),
                ('nutriment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodfinder.Nutriment')),
            ],
        ),
    ]