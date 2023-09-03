from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

class StockApp(App):
    def build(self):
        return StockLayout()

class StockLayout(BoxLayout):
    def fetch_stock_data(self):
        symbol = self.ids.symbol_input.text
        api_url = f'https://api.example.com/stock/{symbol}'
        response = requests.get(api_url)
        data = response.json()
        self.ids.stock_data_label.text = f'Notowania: {data["price"]}'

if __name__ == '__main__':
    StockApp().run()
