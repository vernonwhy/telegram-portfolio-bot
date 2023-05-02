import requests

def get_health_value(account: str) -> str:
    url = 'https://api.debank.com/portfolio/project_list?user_addr=' + account
    response = requests.get(url)

    if response.ok:
        dict = response.json()
        data = dict['data']
        for x in data:
            if x['id'] == 'bsc_venus':
                health_value = x['portfolio_item_list'][0]['detail']['health_rate']
                return round(health_value, 2)

    else:
        print('Error:', response.status_code)