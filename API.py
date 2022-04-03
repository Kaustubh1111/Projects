import requests
url = 'https://api.textlocal.in/'
params = {'username':'yourusername@mailid.com',
          'apiKey':'yourGenerated-APIKey'
}

def check_balance(url):
    url = url+'balance'
    response = requests.get(url,params=params)
    return response.json()
def send_sms(url,params):
    url=url+'send'
    #Phone numbers inside braces {} in commas
    numbers={'9911111xxxx'}
    message = {'Hi, This is a Sample message'}
    params['numbers'] = numbers
    params['message'] = message
    response = requests.post(url,params=params)
    return response.json()

def inbox(url):
    url = url+'get_inboxes'
    response = requests.get(url,params=params)
    return response.json()