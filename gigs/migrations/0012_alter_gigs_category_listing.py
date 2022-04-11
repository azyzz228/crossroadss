# Generated by Django 4.0.1 on 2022-04-10 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0011_alter_categories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigs',
            name='category',
            field=models.OneToOneField(default='Other', on_delete=django.db.models.deletion.SET_DEFAULT, to='gigs.categories'),
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=12)),
                ('approved', models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('pending', 'pending')], default='pending', max_length=7)),
                ('title', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=200)),
                ('category', models.OneToOneField(default='Other', on_delete=django.db.models.deletion.SET_DEFAULT, to='gigs.categories')),
            ],
        ),
    ]