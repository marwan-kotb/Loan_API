from django.urls import path
from API.views import submit_loan_request, submit_loan_offer, accept_loan_offer, fund_loan, get_all_loans

urlpatterns = [
    path('api/loan/submit-request/', submit_loan_request),
    path('api/loan/submit-offer/', submit_loan_offer),
    path('api/loan/accept-offer/', accept_loan_offer),
    path('api/loan/fund-offer/', fund_loan),
    path('api/loan/all/', get_all_loans),

]