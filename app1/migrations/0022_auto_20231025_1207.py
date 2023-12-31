# Generated by Django 3.2.22 on 2023-10-25 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_auto_20231025_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='adjust',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='balance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='cheque_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='inv_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='paidoff',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='pay_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='salcrd_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='term_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='upi_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='PaymentTerms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100, null=True)),
                ('days', models.IntegerField(null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
