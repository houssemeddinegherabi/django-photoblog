# Generated by Django 2.0.1 on 2018-02-04 01:01

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180203_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='featured_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='page',
            name='homepage_featured',
            field=models.BooleanField(default=False),
        ),
    ]