import requests
import json

url = "https://ipapi.com/ip_api.php?ip={}"
ip ='196.180.177.45'

req = requests.get(url.format(ip))
if req.status_code:
    data = json.loads(req.text)
    print(data)

print('ok')

ip = data['ip']
latitude = data['latitude']
longitude = data['longitude']
pays = data['country_name']
ville = data['city']
reseau = data['connection']['isp']
paye = data['currency']['symbol']
region_code = data['region_code']
region_name = data['region_name']

print('=================\r\n')

print(ip,latitude,longitude,pays,ville,reseau,paye,region_code,region_name)


def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip