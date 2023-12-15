import httpx


def keys_serializer(text: str):
    if text.isalnum():
        res = ''
        for letter in text:
            if letter.isalpha():
                res += letter
        return res
    return text


#
# res = keys_serializer('1a2b3c4d5a6b7b8d9a10b11c12b13b14a15b16b17c18b19a20b21a22b23c24b25b26b27a28c29a30b')
# print(len(res))
# from datetime import datetime
#
# import httpx
#
# url = "http://127.0.0.1:8000/api/science/"
# context = {
#     'name': 'test_name',
#     'size': 20,
#     'keys': 'test_keys',
#     'author': 1
# }
# # http://127.0.0.1:8000/api/science/
# response = httpx.post(url, data=context)
# date = response.json()['created_at']
# datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
#
# # Format the datetime object using strftime
# formatted_time = datetime_object.strftime("%m/%d/%Y, %H:%M:%S")
# print(formatted_time)



# def get_test_id(text: str) -> int:
#     res = ''
#     for w in text:
#         if w.isnumeric():
#             res += w
#     return int(res)

base_url = 'http://127.0.0.1:8000/api'


def check_answer(keys: str):
    tru_answers = 0
    false_answers = 0
    url = f'{base_url}/science/18/'
    keys = keys_serializer(keys)
    response = httpx.get(url)
    keys_api = keys_serializer(response.json()['keys'])
    for k1, k2 in zip(keys, keys_api):
        if k1 == k2:
            tru_answers += 1
        else:
            false_answers += 1
    return tru_answers, false_answers


print(check_answer('1a2b3c4d5a6b7b8d9a10b11c12b13b14a15b16b17c18b19a20b21a22b23c24b25b26b27a28c29b30a'))
