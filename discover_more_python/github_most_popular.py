import requests 
r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
    'User-Agent': 'Holberton_School',
    'Authorization': 'token c1485ae8f00e64f0aa058a33db2554cdd8052cd6'
})
print r.json()
