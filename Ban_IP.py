import requests
import re
pattern=r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
count=0
data=re.findall(pattern,requests.get('https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt').text)
Progress_Count=len(data)
Master_JSON="["
for line in data:
    JSON_String=f'<"ip":"{line}","created":"2024-03-16 03:22:20 +0000", "source": "NeoGeekJr", "expires": "forever","reason": "Banned for Malcious IP">'
    JSON_String=JSON_String.replace('<','{').replace('>','}')
    Master_JSON+=JSON_String+','
    count+=1
Master_JSON=Master_JSON[:-1]+']'
with open('banned-ips.json','w') as file:
    file.write(Master_JSON)
file.close()
