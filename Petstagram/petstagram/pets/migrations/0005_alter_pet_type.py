# Generated by Django 3.2.2 on 2021-06-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Parrot', 'Parrot'), ('Unknown', 'Unknown')], default='Unknown', max_length=7),
        ),
    ]
