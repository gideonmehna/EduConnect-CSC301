# Generated by Django 4.1.7 on 2023-04-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0004_alter_diet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
