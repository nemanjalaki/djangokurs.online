# Generated by Django 4.2 on 2023-04-24 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_comment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set(),
        ),
    ]
