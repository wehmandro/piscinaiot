# -*- coding: latin-1 -*-
import urllib2, json

class openweather:
    '''
    Uma classe simples que utiliza a api do openweathermap
    para fazer requisições de tempo
    https://openweathermap.org/api
    '''
    def __init__(self, chave, cidade):
        self.cidade = cidade
        self.chave = chave
        self.site = 'http://api.openweathermap.org/data/2.5/weather?id='
        self.update()

    def update(self):
        url = self.site + self.cidade + '&appid=' + self.chave
        resposta = urllib2.urlopen(url)
        dados_resposta = resposta.read()
        dados = json.loads(dados_resposta)
        self.dados = dados

    def temperatura(self):
        return self.dados['main']['temp'] - 273.1

    def pressao(self):
        return self.dados['main']['pressure']

    def humidade(self):
        return self.dados['main']['humidity']

    def temperatura_minima(self):
        return self.dados['main']['temp_min'] - 273.1

    def temperatura_maxima(self):
        return self.dados['main']['temp_max'] - 273.1

    def vento_speed(self):
        return self.dados['wind']['speed']
