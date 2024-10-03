# Generated by Django 5.1.1 on 2024-10-03 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='Balance')),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cost', models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='Cost')),
                ('size', models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='Size')),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game_Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='task1.buyer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='task1.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(through='task1.Game_Buyer', to='task1.buyer'),
        ),
    ]
