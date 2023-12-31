# Generated by Django 4.2.4 on 2023-08-22 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_period', models.IntegerField()),
                ('loan_date', models.DateField()),
                ('annual_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lenme_fee', models.DecimalField(decimal_places=2, default=3, max_digits=5)),
                ('total_loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=50)),
                ('accepted', models.BooleanField(default=False)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.borrower')),
                ('investor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.investor')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.loan')),
            ],
        ),
    ]
