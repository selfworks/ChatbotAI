# Generated by Django 3.1.6 on 2021-02-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotweb', '0006_chatbotconversations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbotconversations',
            name='finishing_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
