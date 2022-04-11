# Generated by Django 4.0.1 on 2022-04-10 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0012_alter_gigs_category_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigs',
            name='category',
            field=models.ForeignKey(default='Other', on_delete=django.db.models.deletion.SET_DEFAULT, to='gigs.categories'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(default='Other', on_delete=django.db.models.deletion.SET_DEFAULT, to='gigs.categories'),
        ),
    ]
