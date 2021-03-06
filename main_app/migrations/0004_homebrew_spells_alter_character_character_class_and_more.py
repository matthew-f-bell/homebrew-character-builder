# Generated by Django 4.0.3 on 2022-04-09 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_character_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homebrew_Spells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('desc', models.CharField(max_length=2500)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.CharField(choices=[('Monk', 'monk'), ('Bard', 'bard'), ('Warlock', 'warlock'), ('Rogue', 'rogue'), ('Paladin', 'paladin'), ('Barbarian', 'barbarian'), ('Wizard', 'wizard'), ('Cleric', 'cleric'), ('Ranger', 'ranger'), ('Druid', 'druid'), ('Fighter', 'fighter'), ('Sorcerer', 'sorcerer')], max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user'),
        ),
    ]
