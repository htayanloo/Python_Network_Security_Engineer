import requests




def send_sms(receptor,message):
    token="4935715544676C487076716636596E786554787531513D3D"
    sender='10008663'
    sms_url = f"https://api.kavenegar.com/v1/{token}/sms/send.json?receptor={receptor}&sender={sender}&message={message}"
    response =requests.get(sms_url)
    print(response.status_code)
    print(response.text)


send_sms("09128387233","salam")