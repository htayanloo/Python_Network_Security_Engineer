from kavenegar import *
try:
    api = KavenegarAPI('4935715544676C487076716636596E786554787531513D3', timeout=20)
    params = {
        'sender': '10008663',#optional
        'receptor': '09128387233,09128387233',#multiple mobile number, split by comma
        'message': 'test',
    }
    response = api.sms_send(params)
    print(response)
except APIException as e:
    print(e)
except HTTPException as e:
    print(e)