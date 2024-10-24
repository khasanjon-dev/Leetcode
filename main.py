import base64


def generate_qr_code(merchant_id, device_id):
    base_url = f"https://beepul.uz/actions/payment?qr=2&"

    url = f"m={merchant_id}&cr=860&ac.qurilma_id={device_id}&ac.merchant_id={merchant_id}"
    url_bytes = url.encode('utf-8')
    base64_encoded_url = base64.b64encode(url_bytes).decode('utf-8')

    return base_url + base64_encoded_url


qr = generate_qr_code(4092, "Sound Box")


def decode(base64_encoded_url):
    # Decode the base64 string
    decoded_bytes = base64.b64decode(base64_encoded_url)

    # Convert the bytes back into a string
    decoded_url = decoded_bytes.decode('utf-8')

    print(decoded_url)


decode("bT1Tb3VuZCBCb3gmY3I9ODYwJmFjLnF1cmlsbWFfaWQ9U291bmQgQm94JmFjLm1lcmNoYW50X2lkPTQwOTI=")
"https://beepul.uz/actions/payment?qr=2&bT1Tb3VuZCBCb3gmY3I9ODYwJmFjLnF1cmlsbWFfaWQ9U291bmQgQm94JmFjLm1lcmNoYW50X2lkPTQwOTI="