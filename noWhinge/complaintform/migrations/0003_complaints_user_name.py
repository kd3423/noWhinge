# Generated by Django 2.0.3 on 2018-04-10 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaintform', '0002_complaints_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='user_name',
            field=models.CharField(default='nowhinge@gmail.com', max_length=50),
        ),
    ]
