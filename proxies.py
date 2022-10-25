from urllib.request import urlopen
import random


def random_proxy():
    proxies_source_url ="raw.githubusercontent.com"
    proxies_source_path ="/TheSpeedX/SOCKS-List/master/http.txt"
    response = urlopen(f"https://{proxies_source_url}{proxies_source_path}")
    proxies_list = response.read().decode('utf-8').split("\n")

    return proxies_list[random.randint(0, len(proxies_list) - 1)]


