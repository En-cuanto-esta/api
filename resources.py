import requests
from bs4 import BeautifulSoup

#Fuente en paralelo vzla
def resource_en_paralelo():
    url = requests.get("https://enparalelovzla.com/")
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('input', {'id': 'PM'})
    format_result = result.get('value')

    return format_result

#Fuente Banco central de Venezuela
def resource_bcv():
    url = requests.get("http://www.bcv.org.ve/")
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div', {'id': 'dolar'}).find('div', {'class':'recuadrotsmc'}).find('strong')

    return result.text

#Fuente Yadio.io
def resource_yadio_io():
    result = requests.get("https://api.yadio.io/convert/1/USD/VES").json()
    return result['result']

#Desde ExchangeMonitor
def resource_cambios_rya():
    url = requests.get("https://exchangemonitor.net/estadisticas/ve/cambios-rya")
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div',{'class': 'inicio'}).find('h2')

    return result.text

#Fuente Localbitcoin
def resource_localbitcoins():
    url = requests.get("https://exchangemonitor.net/estadisticas/ve/localbitcoins")
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div',{'class': 'inicio'}).find('h2')
    return result.text

#Fuente Akbfintech
def resource_akb_fintech():
    url = requests.get("https://exchangemonitor.net/estadisticas/ve/akb-fintech")
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('div', {'class': 'inicio'}).find('h2')

    return result.text
if __name__ == '__main__':
    print(resource_akb_fintech())
