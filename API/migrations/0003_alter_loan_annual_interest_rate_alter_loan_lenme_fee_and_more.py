# Generated by Django 4.2.4 on 2023-08-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_loan_loan_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='annual_interest_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='lenme_fee',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_period',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan',
            name='total_loan_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
