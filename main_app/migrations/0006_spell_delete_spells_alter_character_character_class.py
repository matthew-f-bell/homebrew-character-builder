# Generated by Django 4.0.3 on 2022-04-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_spells_delete_homebrew_spells_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('character_class', models.CharField(choices=[('Druid', 'druid'), ('Cleric', 'cleric'), ('Fighter', 'fighter'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Barbarian', 'barbarian'), ('Rogue', 'rogue'), ('Bard', 'bard'), ('Sorcerer', 'sorcerer'), ('Monk', 'monk'), ('Warlock', 'warlock'), ('Wizard', 'wizard')], max_length=50)),
                ('desc', models.CharField(max_length=2500)),
            ],
        ),
        migrations.DeleteModel(
            name='Spells',
        ),
        migrations.AlterField(
            model_name='character',
            name='character_class',
            field=models.CharField(choices=[('Druid', 'druid'), ('Cleric', 'cleric'), ('Fighter', 'fighter'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Barbarian', 'barbarian'), ('Rogue', 'rogue'), ('Bard', 'bard'), ('Sorcerer', 'sorcerer'), ('Monk', 'monk'), ('Warlock', 'warlock'), ('Wizard', 'wizard')], max_length=50),
        ),
    ]
