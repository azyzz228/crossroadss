# Generated by Django 4.0.1 on 2022-04-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0009_categories_alter_gigs_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]