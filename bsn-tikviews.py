import requests, os, random, sys
tok = []
loop = 0
os.system('clear')
print('-------------------------------------------')
print('      \033[1;32m      AUTHOR : BILAL KHAN\033[1;37m')
print('-------------------------------------------')
link = input(' [+] Put Link : ')
print('-------------------------------------------\n')
print(' \033[1;97m1 Order >> 1k to 5k views')
print(' \033[1;97mYour Process Started in Background')
print('-------------------------------------------')
print('-------------------------------------------\n')
while True:
    try:
        headers = {'authority': 'n1provider.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','cache-control': 'no-cache','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://n1provider.com','pragma': 'no-cache','referer': 'https://n1provider.com/free','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','x-requested-with': 'XMLHttpRequest'}
        response = requests.get('https://n1provider.com/auth/signup', headers=headers)
        coki = str(response.cookies)
        token = coki.split("token=")[1].split(' ')[0]
        general_sessions=coki.split("general_sessions=")[1].split(' ')[0]
        cookies = {
            'token': token,
            'general_sessions': general_sessions
        }
        data = {
            'full_name': 'BILAL KHAN',
            'email': 'bilalkhan'+str(random.randint(0,999999999))+'@yahoo.com',
            'whatsapp': '348'+str(random.randint(00000000,9999999)),
            'password': 'bsn12345',
            're_password': 'bsn12345',
            'timezone': 'Asia/Karachi',
            'terms': 'on',
            'token': token,
        }
        create = requests.post('https://n1provider.com/auth/ajax_sign_up', cookies=cookies, headers=headers, data=data)
        #print(create.text)
        if 'success' in create.json()['status']:
            for i in range(10):
                cola = '\033[1;31m';colb= '\033[1;32m';colc= '\033[1;33m';cold= '\033[1;34m';cole= '\033[1;35m';colf= '\033[1;36m';colg= '\033[1;37m'
                clr = random.choice([cola,colb,colc,cold,cole,colf,colg])
                sys.stdout.write(f'\r\r{colg} [{clr} BSN{colg} ] -- {colg}[ Total Orders : {colb}{len(tok)}{colg} ]');sys.stdout.flush()
                data = {
                    'service': '9',
                    'link': link,
                    'token': token
                }
                post = requests.post('https://n1provider.com/free/ajax_free_order', headers=headers, cookies=cookies, data=data)
                if 'success' in post.json()['status']:
                    tok.append(token)
                    #print(post.text)
            loop+=1
    except Exception as e:
        print(e)
                   
