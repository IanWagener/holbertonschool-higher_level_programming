import requests 
r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
    'User-Agent': 'Holberton_School',
    'Authorization': 'token c1485ae8f00e64f0aa058a33db2554cdd8052cd6'
})
with open('/tmp/15', 'w') as f:
    f.write(str(r.json()))
print ("The file was saved!")
