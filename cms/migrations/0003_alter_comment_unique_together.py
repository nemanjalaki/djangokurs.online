# Generated by Django 4.2 on 2023-04-24 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('body', 'post')},
        ),
    ]
