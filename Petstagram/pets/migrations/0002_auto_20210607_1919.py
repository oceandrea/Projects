# Generated by Django 3.2.2 on 2021-06-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
