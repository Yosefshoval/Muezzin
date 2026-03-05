from base64 import b64decode
import re
# from config import Config
#
# logger = Config.logger

list1 = ("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxh"
         "Y2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
list2 = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="

list1 = b64decode(list1).decode()
list2 = b64decode(list2).decode()


def risk_percent(lower_text: str):
    counter = 0
    for word in list1.strip().split(','):
        result = re.findall(pattern=f'{word.lower()}', string=lower_text)
        counter += len(result) * 2

    for word in list2.strip().split(','):
        result = re.findall(pattern=f'{word.lower()}', string=lower_text)
        counter += len(result)

    percent = counter / len(lower_text.split()) * 100
    return float('%.2f' % percent)


def risk_rank(lower_text: str):
    counter = 0
    for word in list1.strip().split(','):
        if word.lower() in lower_text:
            counter += 2

    for word in list2.strip().split(','):
        if word.lower() in lower_text:
            counter += 1
    print(counter)
    if counter <= 5:
        return "none"
    if counter <= 12:
        return "medium"
    return "high"