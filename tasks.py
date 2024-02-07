# import json
#
#
# def check_answer(keys: dict, keys_api: dict) -> tuple:
#     true_answers, false_answers = {}, {}
#     for key in keys:
#         if key in keys_api and keys[key] == keys_api[key]:
#             true_answers[key] = keys[key]
#         else:
#             false_answers[key] = keys[key]
#     return json.dumps(true_answers, indent=2), json.dumps(false_answers, indent=2)
#
#
# def keys_serializer(text: str, api=False) -> json:
#     keys = {}
#     if text.isalnum():
#         res = ''
#         for letter in text:
#             if letter.isalpha():
#                 res += letter
#         text = res
#     for i, value in enumerate(text, 1):
#         keys.update({str(i): value})
#     if api:
#         keys = json.dumps(keys, indent=2)
#     return keys
#
#
# res = keys_serializer('1a2b3b4a5b6a7a8d9a10a11c12b13b')
# print(res)

'adsfasdfadsfasdfasfdadfasdfasd'