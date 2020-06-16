# Generated by Django 3.0.7 on 2020-06-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0005_food_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='nutriments',
        ),
        migrations.AddField(
            model_name='food',
            name='nutriment_set',
            field=models.ManyToManyField(to='foodfinder.Nutriment'),
        ),
    ]