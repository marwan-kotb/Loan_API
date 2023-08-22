from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Borrower, Investor, Loan
from .serializers import LoanSerializer

from .celery import schedule_loan_payments

from datetime import date



@api_view(['POST'])
def submit_loan_request(request):

    borrower = request.data.get('borrower')
    loan_amount = request.data.get('loan_amount')
    loan_period = request.data.get('loan_period')

   
    try:
        borrower = Borrower.objects.get(name=borrower)
        loan =  Loan.objects.create(
            borrower=borrower,
            loan_amount=loan_amount,
            loan_date=date.today(),
            loan_period=loan_period,
            status='Pending',
            accepted=False
        )
    except Borrower.DoesNotExist:
        return Response('Invalid loan', status=status.HTTP_400_BAD_REQUEST)
   

    return Response('Loan offer submitted successfully', status=status.HTTP_200_OK)

@api_view(['POST'])
def submit_loan_offer(request):
    loan_id = request.data.get('loan_id')
    investor_name = request.data.get('investor_name')
    annual_interest_rate = float(request.data.get('annual_interest_rate'))

    try:
        loan = Loan.objects.get(id=loan_id)
        investor = Investor.objects.get(name=investor_name)
    except (Loan.DoesNotExist, Investor.DoesNotExist):
        return Response('Invalid loan or investor', status=status.HTTP_400_BAD_REQUEST)


    loan.investor = investor
    loan.status = 'Offered'
    loan.annual_interest_rate = annual_interest_rate
    loan.lenme_fee = 3
    loan.total_loan_amount = float(loan.loan_amount) + float(float(loan.loan_amount) * (float(loan.annual_interest_rate) / 100)) + float(loan.lenme_fee)
    loan.save()


    
    
    return Response('Loan offer submitted successfully', status=status.HTTP_200_OK)


@api_view(['POST'])
def accept_loan_offer(request):
    loan_id = request.data.get('loan_id')

    try:
        loan = Loan.objects.get(id=loan_id)
    except Loan.DoesNotExist:
        return Response('Invalid loan', status=status.HTTP_400_BAD_REQUEST)

    loan.accepted = True
    loan.status = 'Accepted'
    loan.save()

    return Response('Loan offer accepted successfully', status=status.HTTP_200_OK)

@api_view(['POST'])
def fund_loan(request):
    loan_id = request.data.get('loan_id')
    investor_name = request.data.get('investor_name')

    try:
        loan = Loan.objects.get(id=loan_id)
        investor = Investor.objects.get(name=investor_name)
        amount = loan.total_loan_amount
    except (Loan.DoesNotExist, Investor.DoesNotExist):
        return Response('Invalid loan or investor', status=status.HTTP_400_BAD_REQUEST)

    if investor.balance < amount:
        return Response('Insufficient balance', status=status.HTTP_400_BAD_REQUEST)

    investor.balance -= amount
    investor.save()

    loan.status = 'Funded'
    loan.save()

    schedule_loan_payments.delay(loan.id)

    return Response('Loan funded successfully', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_loans(request):
    loans = Loan.objects.all()
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

