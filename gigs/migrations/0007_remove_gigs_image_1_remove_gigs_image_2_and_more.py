# Generated by Django 4.0.1 on 2022-02-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0006_alter_gigs_image_1_alter_gigs_image_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gigs',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='gigs',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='gigs',
            name='image_3',
        ),
        migrations.AddField(
            model_name='gigs',
            name='is_deleted',
            field=models.CharField(default='no', max_length=12),
        ),
        migrations.AddField(
            model_name='gigs',
            name='nickname',
            field=models.CharField(default='testing', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gigs',
            name='approved',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('pending', 'pending')], default='pending', max_length=7),
        ),
        migrations.AlterField(
            model_name='gigs',
            name='category',
            field=models.CharField(choices=[('data analysis', 'data analysis'), ('graphic design', 'graphic design'), ('music', 'music'), ('photography', 'photography'), ('sales & marketing', 'sales & marketing'), ('software development', 'software development'), ('videography', 'videography')], max_length=200),
        ),
        migrations.AlterField(
            model_name='gigs',
            name='title',
            field=models.CharField(max_length=65),
        ),
    ]