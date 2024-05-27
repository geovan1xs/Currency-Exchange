import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
import requests
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle



GUI = Builder.load_file("tela.kv")


class Gerenciador(ScreenManager):
    def build(self):
        return GUI



    def Dolar(self):
        self.root.ids["moedausd"].text = f"Dólar R${self.pegar_cotacao('USD')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


class Menu(Screen):
   pass


class Inicio(Screen):
    pass

class Mybox(BoxLayout):
    pass

class Dolar(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)
    def change_screen(self, dt):
        self.ids["moedaeua"].text = f"O valor do Dólar é de R$ {self.pegar_cotacao('USD')} atualmente"
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao




class Euro(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)

    def change_screen(self, dt):
        self.ids["moedaeur"].text = f"O valor do Euro é de R$ {self.pegar_cotacao('EUR')} atualmente"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao


class Bitcoin(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)

    def change_screen(self, dt):
        self.ids["moedabtc"].text = f"O valor do Bitcoin é de R$ {self.pegar_cotacao('BTC')} atualmente"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao


class Iene(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)

    def change_screen(self, dt):
        self.ids["moedajpy"].text = f"O valor do Iene é de R$ {self.pegar_cotacao('JPY')} atualmente"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao


class Libra(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)

    def change_screen(self, dt):
        self.ids["moedagbp"].text = f"O valor da Libra Esterlina é de R$ {self.pegar_cotacao('GBP')} atualmente"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao


class Peso(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen)

    def change_screen(self, dt):
        self.ids["moedaars"].text = f"O valor do Peso Argentino é de R$ {self.pegar_cotacao('ARS')} atualmente"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]

        return cotacao


class Apppi(App):
    def build(self):
        sm = Gerenciador()
        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Dolar(name= "dolar"))
        sm.add_widget(Euro(name="euro"))
        sm.add_widget(Bitcoin(name="bitcoin"))
        sm.add_widget(Iene(name="iene"))
        sm.add_widget( Libra(name="libra"))
        sm.add_widget(Peso(name="peso"))
        return sm





Apppi().run()