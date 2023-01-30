# Generated by Django 4.1.2 on 2023-01-29 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0003_merge_0002_game_product_data_pdf_0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='age_rating',
            field=models.CharField(choices=[('', 'Nothing selected'), ('0+', 'from 0'), ('6+', 'from 6'), ('12+', 'from 12'), ('16+', 'from 16'), ('18+', 'from 18')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('', 'Nothing selected'), ('FPS', 'First Person Shooter'), ('SIM', 'Simulation'), ('CB', 'City Builder'), ('HG', 'Horror Game'), ('RPG', 'Role Playing Game'), ('RC', 'Racing Game')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]