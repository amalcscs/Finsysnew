# Generated by Django 3.2.22 on 2023-10-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_recurring_bill_recurringbill_item_repeatevery'),
    ]

    operations = [
        migrations.AddField(
            model_name='mjournal',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
