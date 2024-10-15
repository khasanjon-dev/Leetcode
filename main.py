import base64


def generate_qr_code(merchant_id, device_id):
    base_url = f"https://beepul.uz/new/payment?qr=2&"

    url = f"m={merchant_id}&ac.qurilma_id={device_id}"
    url_bytes = url.encode('utf-8')
    base64_encoded_url = base64.b64encode(url_bytes).decode('utf-8')

    return base_url + base64_encoded_url


print(generate_qr_code(833, "Test qurilma 1"))


def decode(base64_encoded_url):
    # Decode the base64 string
    decoded_bytes = base64.b64decode(base64_encoded_url)

    # Convert the bytes back into a string
    decoded_url = decoded_bytes.decode('utf-8')

    print(decoded_url)


decode("bT04MzMmY3I9ODYw")
