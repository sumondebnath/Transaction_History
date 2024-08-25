# Generated by Django 4.2.15 on 2024-08-24 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='current_account',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, related_name='curr_transaction', to='bank_transaction.bankaccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='account_type',
            field=models.CharField(choices=[(1, 'Debit'), (2, 'Cradit')], max_length=10),
        ),
    ]
