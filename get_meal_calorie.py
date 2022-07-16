import requests
from bs4 import BeautifulSoup
import re

def main(detect_word):
    url="https://ssl.mobadai.jp/m/index.php?np=28c4&c=swps2&mspid=quicksearch"
    query={
        "np": "9fd1",
        "c": "swps2",
        "mspid": "quickdelegate",
        "qcsword": detect_word
    }
    headers={
        "Accept": '*/*',
        "Accept-Encoding": 'gzip, deflate, br',
        "Accept-Language": 'ja,en-US;q=0.9,en;q=0.8',
        "Connection": 'keep-alive',
        "Host": 'ssl.mobadai.jp',
        "Referer": 'https://ssl.mobadai.jp/m/index.php?np=28c4&c=swps2&mspid=quicksearch',
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Site": 'same-origin',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    response = requests.get(url,params=query,headers=headers)
    soup = BeautifulSoup(response.content,'html.parser')
    datas = soup.find_all('object')
    return_array = []
    p ="\(([^*]*)\)"
    for i in range(0,4):
        unit2_exist = re.search(p,datas[i].find('name').text)
        meal_dict ={
            "name":datas[i].find('name').text,
            "unit1":datas[i].find('unit').text,
            "unit2":unit2_exist.group().replace('(','').replace(')','')if unit2_exist!=None else "",
            "calorie":datas[i].find('stuff_e').text
        }
        return_array.append(meal_dict)
    print(return_array)
    return return_array

# main('カレー')
name = "カレー"

def meal_database() :
    main(name)
# print(meal_database())