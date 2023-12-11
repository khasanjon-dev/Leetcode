import httpx


url = f"http://localhost:8000/api/user/get-or-create/"
context = {
    'first_name': 'salom',
    'last_name': 'xayr',
    'telegram_id': 6961712212
}
response = httpx.post(url, data=context)
print()