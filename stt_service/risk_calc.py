from base64 import b64decode
import re
from config import Config

logger = Config.logger

list1 = ("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxh"
         "Y2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
list2 = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="

list1 = b64decode(list1).decode().strip().split(',')
list2 = b64decode(list2).decode().strip().split(',')


def risk_percent(lower_text: str):
    counter = 0
    for word in list1:
        result = re.findall(pattern=f'{word.lower()}', string=lower_text)
        counter += len(result) * 2

    for word in list2:
        result = re.findall(pattern=f'{word.lower()}', string=lower_text)
        counter += len(result)

    percent = counter / len(lower_text.split()) * 100
    reduced_number = float('%.2f' % percent)

    logger.info(f'risk_percent: {reduced_number}')
    return reduced_number


def risk_rank(lower_text: str):
    counter = 0
    for word in list1:
        if word.lower() in lower_text:
            counter += 2

    for word in list2:
        if word.lower() in lower_text:
            counter += 1

    logger.info(f'words from list exist in the text: {counter}')

    if counter <= 5:
        return "none"
    if counter < 15:
        return "medium"
    return "high"