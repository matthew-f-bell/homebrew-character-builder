# Generated by Django 4.0.3 on 2022-04-10 23:23

from django.db import migrations
import main_app.managers


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_spell_options_alter_character_spells'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', main_app.managers.CustomUserManager()),
            ],
        ),
    ]
