import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def get_https_proxy_1():
    # site: http://free-proxy.cz/zh/proxylist/country/all/https/ping/all
    proxys = []
    for i in range(1,6):
        res = requests.get(f'http://free-proxy.cz/zh/proxylist/country/all/https/ping/all/{i}', headers=headers)
        print(res.status_code)
        assert(res.status_code==200)
        soup = BeautifulSoup(res.text, 'html.parser')
        tbody = soup.select('#proxy_list > tbody')[0]
        trs = tbody.find('tr')
        for tr in trs:
            tds = tr.find('td')
            proxys.append({
                'ip': tds[0].text,
                'port': tds[1].text,
                'protocol': tds[2].text,
            })
    return proxys

def get_https_proxy_2():
    # site: http://www.freeproxylists.net/zh/?pr=HTTPS&page=1
    proxys = []
    for i in range(1,5):
        res = requests.get(f'http://www.freeproxylists.net/zh/?pr=HTTPS&page={i}', headers=headers)
        print(res.status_code)
        assert(res.status_code==200)
        soup = BeautifulSoup(res.text, 'html.parser')
        tbody = soup.select('body > div:nth-child(3) > div:nth-child(2) > table > tbody')[0]
        trs = tbody.find('tr')
        for tr in trs:
            if tr.attrs['class'] == 'Caption':
                continue
            tds = tr.find('td')
            proxys.append({
                'ip': tds[0].text,
                'port': tds[1].text,
                'protocol': tds[2].text,
            })
    return proxys

def get_https_proxy_2():
    # site: http://www.freeproxylists.net/zh/?pr=HTTPS&page=1
    proxys = []
    for i in range(1,5):
        res = requests.get(f'http://www.freeproxylists.net/zh/?pr=HTTPS&page={i}', headers=headers)
        print(res.status_code)
        assert(res.status_code==200)
        soup = BeautifulSoup(res.text, 'html.parser')
        tbody = soup.select('body > div:nth-child(3) > div:nth-child(2) > table > tbody')[0]
        trs = tbody.find('tr')
        for tr in trs:
            if tr.attrs['class'] == 'Caption':
                continue
            tds = tr.find('td')
            proxys.append({
                'ip': tds[0].text,
                'port': tds[1].text,
                'protocol': tds[2].text,
            })
    return proxys

def get_https_proxy_3():
    # source: https://github.com/clarketm/proxy-list/blob/master/proxy-list.txt
    proxys = []
    res = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt', headers=headers)
    assert(res.status_code==200)
    lines = res.text.split('\n')
    for line in lines[10:-2]:
        data = line.split(' ')
        if len(data[1].split('-')) == 3 and data[1].split('-')[2] == 'S':
            proxys.append({
                'ip': data[0].split(':')[0],
                'port': data[0].split(':')[1],
                'protocol': 'HTTPS',
            })
    return proxys
# PubProxy provides a free, robust API to narrow down the proxy to your desired specification.

if __name__ == "__main__":
    p = get_https_proxy_3()
    print(p)