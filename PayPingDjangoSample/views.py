from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import PayPingPaySDK.pay as sdk

PAYPING_TOKEN = 'PUT_YOUR_PAYPING_TOKEN_HERE'

PAYPING_PAY_URL = 'https://api.payping.ir/v2/pay'

# Route to our ConfirmPayment callback method
RETURN_URL = 'http://localhost:8000/confirmpay'


# Home Page
def index(request):
    return render(request, "index.html")


# Create a Payment
def createpay(request):
    if request.POST:
        # Get data from form
        pay_data = request.POST.dict()
        payerName = pay_data.get("payerName")
        amount = pay_data.get("amount")
        payerIdentity = pay_data.get("payerIdentity")
        description = pay_data.get("description")
        print(payerName, amount, payerIdentity)

        # Get pay code from PayPing
        # except (amount*, returnURL*, token*) the rest can be None
        paycode = sdk.createpay(amount, RETURN_URL, payerName, payerIdentity, description, "YOUR OPTIONAL VALUE",
                                PAYPING_TOKEN)

        # Redirecting User to Gateway for payment
        return redirect(PAYPING_PAY_URL + '/gotoipg/' + paycode)
    else:
        return render(request, "index.html")


# Confirm a Payment
# Gets Called After Payment is Done By PayPing
@csrf_exempt
def confirmpay(request):
    if request.POST:
        # Get data from request
        pay_data = request.POST
        refid = pay_data.get("refid")

        # Your Optional Value
        clientRefId = pay_data.get("clientrefid")
        amount = 1000

        # Confirm Payment
        # All params required*
        payment_detail = sdk.confirmpay(amount, refid, PAYPING_TOKEN)

        # Get PaymentDetails
        cardnumber = payment_detail["cardNumber"]
        confirmed_amount = payment_detail["amount"]
        print(cardnumber, confirmed_amount)

        return render(request, "confirm.html")
    else:
        return render(request, "index.html")
