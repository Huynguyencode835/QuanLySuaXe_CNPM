import requests, hmac, hashlib, json, time,uuid

PARTNER_CODE = "MOMO"
ACCESS_KEY = "F8BBA842ECF85"
SECRET_KEY = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
MOMO_ENDPOINT = "https://test-payment.momo.vn/v2/gateway/api/create"

def create_momo_payment(amount, order_info, redirect_url, ipn_url):
    order_id = str(uuid.uuid4())
    request_id = str(uuid.uuid4())

    raw_signature = (
        f"accessKey={ACCESS_KEY}&amount={amount}&extraData=&"
        f"ipnUrl={ipn_url}&orderId={order_id}&orderInfo={order_info}&"
        f"partnerCode={PARTNER_CODE}&redirectUrl={redirect_url}&"
        f"requestId={request_id}&requestType=payWithATM"
    )

    signature = hmac.new(
        SECRET_KEY.encode(),
        raw_signature.encode(),
        hashlib.sha256
    ).hexdigest()

    payload = {
        "partnerCode": PARTNER_CODE,
        "accessKey": ACCESS_KEY,
        "requestId": request_id,
        "amount": str(amount),
        "orderId": order_id,
        "orderInfo": order_info,
        "redirectUrl": redirect_url,
        "ipnUrl": ipn_url,
        "extraData": "",
        "requestType": "payWithATM",
        "signature": signature,
        "lang": "vi"
    }

    response = requests.post(MOMO_ENDPOINT, json=payload).json()
    return response, order_id