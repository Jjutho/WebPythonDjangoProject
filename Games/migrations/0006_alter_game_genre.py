# Generated by Django 4.1.2 on 2022-11-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0005_alter_game_release_date_alter_game_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('FPS', 'Firstpersonshooter'), ('SIM', 'Simulation'), ('CB', 'Citebuilder'), ('HG', 'Horrorgame'), ('RPG', 'Roleplayinggame'), ('RC', 'Racinggame')], max_length=3),
        ),
    ]