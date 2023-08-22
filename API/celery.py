from celery import shared_task
from datetime import timedelta
from API.models import *



@shared_task
def schedule_loan_payments(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        payment_date = loan.funded_date + timedelta(days=30)  

        for _ in range(6):
            Payment.objects.create(loan=loan, amount=loan.total_loan_amount / loan.loan_period, payment_date=payment_date)
            payment_date += timedelta(days=30 * 6)  

        loan.status = 'Completed'
        loan.save()
    except Loan.DoesNotExist:
        pass  

