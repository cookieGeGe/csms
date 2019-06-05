import requests
from bs4 import BeautifulSoup

from mysqlbase import mysql_con


def get_company_url(name):
    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}

        base_url = 'https://www.qichacha.com'
        html = requests.get('https://www.qichacha.com/search?key=' + name, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        a_list = soup.find_all('a', attrs={'class': 'ma_h1'})
        if a_list:
            companyurl = soup.find_all('a', attrs={'class': 'ma_h1'})[0]['href']
            return base_url + companyurl
        else:
            return ''
    except:
        return ''


def get_all_company_name():
    query_sql = r"""select id,name,url from tb_company where url is null or url ='';"""
    return mysql_con.op_select(query_sql)


def update_company_url(url, id):
    update_sql = r"""update tb_company set url ='{}' where id={};""".format(url, id)
    return mysql_con.op_update(update_sql)


def main():
    company_name_list = get_all_company_name()
    for item in company_name_list:
        try:
            company_url = get_company_url(item['name'])
            if company_url != '':
                update_company_url(company_url, item['id'])
        except:
            continue
    print('update url success!')


if __name__ == '__main__':
    main()
