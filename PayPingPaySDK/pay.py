import requests
import json

# PayPing Pay APIs Address
PAYPING_PAY_URL = 'https://api.payping.ir/v2/pay'


# Creates a payment and returns a PayCode
def createpay(amount, returnUrl, payer_name, payerIdentity, description, clientRefId, token):
    if token is None:
        raise Exception("Token is None")

    if amount is None:
        raise Exception("Amount is None")

    if returnUrl is None:
        raise Exception("ReturnUrl is None")

    # Build Request
    url = PAYPING_PAY_URL
    headers = {'Authorization': f'Bearer {token}', 'Content-type': 'application/json'}
    postobject = {
        "amount": int(amount),
        "returnUrl": returnUrl,
        "payer_name": payer_name,
        "payerIdentity": payerIdentity,
        "description": description,
        "clientRefId": clientRefId
    }

    # Send Create Payment Request
    try:
        res = requests.post(url, data=json.dumps(postobject), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Convert Response Text to Json
    jsonres = json.loads(res.text)

    # Return Pay Code
    return jsonres["code"]


# Confirm a Payment and return Payment Details
def confirmpay(amount, refId, token):
    if token is None:
        raise Exception("Token is None")

    if amount is None:
        raise Exception("Amount is None")

    if refId is None:
        raise Exception("RefId is None")

    # Build Request
    url = PAYPING_PAY_URL
    headers = {'Authorization': f'Bearer {token}', 'Content-type': 'application/json'}
    postobject = {
        "amount": amount,
        "refId": refId
    }

    # Send Confirm Payment Request
    try:
        res = requests.post(url + '/verify', data=json.dumps(postobject), headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Convert Response Text to Json
    jsonres = json.loads(res.text)

    # Return Pay Code
    return jsonres
