# Generated by Django 4.2.15 on 2024-08-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_transaction', '0002_transaction_current_account_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=models.DecimalField(decimal_places=2, default=-500, max_digits=10), max_digits=10, null=True),
        ),
    ]
