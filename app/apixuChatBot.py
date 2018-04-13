import requests
import pprint

KEY = "e312e89387d7487386e163240180804"
URL = "http://api.apixu.com"

# def _get(url,params):

def get_history_weather(args=None):
    url = URL + "/v1/history.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url,params).json()
    return response


def get_data_curent_weather(args=None):
    url = URL + "/v1/current.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url, params).json()
    return response


def get_forecast_weather(args=None):
    url = URL + "/v1/forecast.json"
    params = {}
    params['key'] = KEY
    params['lang'] = "vi"
    if args != None:
        params.update(args)
    response = requests.get(url, params).json()
    return response

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=2)
    # params = {}
    # params['q'] = "hanoi"
    # params['key'] = KEY
    # params['dt'] = "2018 - 04 - 09"
    # params['lang'] = "vi"
    args = {'q':'hanoi','hour':'0','dt':'2018 - 04 - 13',}
    json_data = get_forecast_weather(args)
    pp.pprint(json_data)

    # time2 = datetime.datetime.time
    # print(time2)

    # print(time.time())

