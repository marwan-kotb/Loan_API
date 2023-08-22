from django.db import models

class Borrower(models.Model):
    name = models.CharField(max_length=100)

class Investor(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, null=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_period = models.IntegerField()
    loan_date = models.DateField()
    annual_interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    lenme_fee = models.DecimalField(max_digits=5, decimal_places=2, default=3, null=True)
    total_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=50)
    accepted = models.BooleanField(default=False)

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()