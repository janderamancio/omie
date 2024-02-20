import requests

cookies = {
    '_gcl_au': '1.1.1417537814.1708443901',
    '_vwo_uuid_v2': 'D98F9F0347C329382A47CD443D59DABA8|d25ba7eee931774116d84123489ea0b5',
    '_gid': 'GA1.3.57801626.1708443902',
    '_vwo_uuid': 'D98F9F0347C329382A47CD443D59DABA8',
    '_vwo_ds': '3%241708443864%3A32.53050777%3A%3A',
    '_vis_opt_s': '1%7C',
    '_vis_opt_test_cookie': '1',
    '_hjSession_1063729': 'eyJpZCI6Ijk2NmQwNDJiLWE1MmEtNDM0ZS1iMTliLTAwMDQ2Y2M0ZTA0NCIsImMiOjE3MDg0NDM5MDE5NjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
    '_tt_enable_cookie': '1',
    '_ttp': 'mY1x8bwWoF8lzz4XIPTKrm0aIgv',
    '_clck': 'a6lceg%7C2%7Cfjf%7C0%7C1511',
    '__hstc': '86978119.80d1607fc89ab156889602b6dd4542c8.1708443902895.1708443902895.1708443902895.1',
    'hubspotutk': '80d1607fc89ab156889602b6dd4542c8',
    '__hssrc': '1',
    'userType': 'usuario_plataforma',
    'intercom-id-iirbswk2': '3d0e285c-86d2-4537-9481-8feba8b6df75',
    'intercom-session-iirbswk2': '',
    'intercom-device-id-iirbswk2': '0009d348-38bc-4272-b46e-e57bebf3e933',
    '_gcl_aw': 'GCL.1708444137.CjwKCAiAuNGuBhAkEiwAGId4akDO54ILwe492jt6MGzGEcZw6OwTonazR1nKETu2Kf3_VlbaprVnEBoClagQAvD_BwE',
    '_gac_UA-149834334-1': '1.1708444137.CjwKCAiAuNGuBhAkEiwAGId4akDO54ILwe492jt6MGzGEcZw6OwTonazR1nKETu2Kf3_VlbaprVnEBoClagQAvD_BwE',
    '_hjSessionUser_1063729': 'eyJpZCI6IjIxNjdlZWRkLTJiMWItNTkxOS04YmFiLWNmMzk0NjQ1MGVmZiIsImNyZWF0ZWQiOjE3MDg0NDM5MDE5NjMsImV4aXN0aW5nIjp0cnVlfQ==',
    'AERUSS': 'u45bqpupvdrfcv36li93si9sr5',
    '_uetsid': '02661230d00711ee80a2b96d1d4eb633',
    '_uetvid': '02660d40d00711eeb3aced5fa66d8855',
    '_vwo_sn': '0%3A4%3A%3A%3A1',
    '_ga': 'GA1.3.1920265796.1708443902',
    'cto_bundle': 'O3lJ3l9jajA4bnFkRnZqdmsxckhxVzYlMkJXYyUyQmQ1UUhPSlRCMzFyV0RtTHFzOCUyRmo2JTJGJTJCWDczWlZQWTFCcnNIU3hiTyUyRnhLWW04bzdla3k2Qmw3RWFTOTNMakVzJTJGYWhvJTJCZjJoTUUzQlhxVklKN1VFJTJCVTNVa25yJTJCQVJKN1VBOThMQ0ViQ1NZbGhBQUNzTXFiNU5qNU1qMGt6WGhsUSUzRCUzRA',
    '__hssc': '86978119.4.1708443902895',
    '_clsk': '19olcve%7C1708444343971%7C4%7C1%7Cs.clarity.ms%2Fcollect',
    '_ga_JJP72HHWTW': 'GS1.1.1708443901.1.1.1708444414.60.0.0',
}

headers = {
    'authority': 'app.omie.com.br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.1417537814.1708443901; _vwo_uuid_v2=D98F9F0347C329382A47CD443D59DABA8|d25ba7eee931774116d84123489ea0b5; _gid=GA1.3.57801626.1708443902; _vwo_uuid=D98F9F0347C329382A47CD443D59DABA8; _vwo_ds=3%241708443864%3A32.53050777%3A%3A; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _hjSession_1063729=eyJpZCI6Ijk2NmQwNDJiLWE1MmEtNDM0ZS1iMTliLTAwMDQ2Y2M0ZTA0NCIsImMiOjE3MDg0NDM5MDE5NjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _tt_enable_cookie=1; _ttp=mY1x8bwWoF8lzz4XIPTKrm0aIgv; _clck=a6lceg%7C2%7Cfjf%7C0%7C1511; __hstc=86978119.80d1607fc89ab156889602b6dd4542c8.1708443902895.1708443902895.1708443902895.1; hubspotutk=80d1607fc89ab156889602b6dd4542c8; __hssrc=1; userType=usuario_plataforma; intercom-id-iirbswk2=3d0e285c-86d2-4537-9481-8feba8b6df75; intercom-session-iirbswk2=; intercom-device-id-iirbswk2=0009d348-38bc-4272-b46e-e57bebf3e933; _gcl_aw=GCL.1708444137.CjwKCAiAuNGuBhAkEiwAGId4akDO54ILwe492jt6MGzGEcZw6OwTonazR1nKETu2Kf3_VlbaprVnEBoClagQAvD_BwE; _gac_UA-149834334-1=1.1708444137.CjwKCAiAuNGuBhAkEiwAGId4akDO54ILwe492jt6MGzGEcZw6OwTonazR1nKETu2Kf3_VlbaprVnEBoClagQAvD_BwE; _hjSessionUser_1063729=eyJpZCI6IjIxNjdlZWRkLTJiMWItNTkxOS04YmFiLWNmMzk0NjQ1MGVmZiIsImNyZWF0ZWQiOjE3MDg0NDM5MDE5NjMsImV4aXN0aW5nIjp0cnVlfQ==; AERUSS=u45bqpupvdrfcv36li93si9sr5; _uetsid=02661230d00711ee80a2b96d1d4eb633; _uetvid=02660d40d00711eeb3aced5fa66d8855; _vwo_sn=0%3A4%3A%3A%3A1; _ga=GA1.3.1920265796.1708443902; cto_bundle=O3lJ3l9jajA4bnFkRnZqdmsxckhxVzYlMkJXYyUyQmQ1UUhPSlRCMzFyV0RtTHFzOCUyRmo2JTJGJTJCWDczWlZQWTFCcnNIU3hiTyUyRnhLWW04bzdla3k2Qmw3RWFTOTNMakVzJTJGYWhvJTJCZjJoTUUzQlhxVklKN1VFJTJCVTNVa25yJTJCQVJKN1VBOThMQ0ViQ1NZbGhBQUNzTXFiNU5qNU1qMGt6WGhsUSUzRCUzRA; __hssc=86978119.4.1708443902895; _clsk=19olcve%7C1708444343971%7C4%7C1%7Cs.clarity.ms%2Fcollect; _ga_JJP72HHWTW=GS1.1.1708443901.1.1.1708444414.60.0.0',
    'if-modified-since': 'Tue, 20 Feb 2024 15:52:58 GMT',
    'referer': 'https://www.omie.com.br/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


json_data = {
    'email': 'janderamancio@gmail.com',
    'password': 'Fjfaa9131',
}

response = requests.get('https://app.omie.com.br/login/', cookies=cookies, headers=headers,json=json_data)
print(response)
