import socket
from datetime import datetime
from flask import Flask, request

# Konfiguracja serwera
HOST = '0.0.0.0'  # Serwer nasłuchuje na wszystkich interfejsach sieciowych
PORT = 8080  # Port, na którym serwer nasłuchuje

app = Flask(__name__)

def log_info():
    # Pobranie informacji o dacie i czasie uruchomienia serwera
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Pobranie adresu IP klienta
    client_address = request.remote_addr

    # Wyświetlanie informacji w logach
    print(f"Serwer uruchomiony: {current_time}")
    print(f"Autor serwera: Sebastian Slupny")
    print(f"Port nasłuchiwania: {PORT}")
    print(f"Adres IP klienta: {client_address}")

@app.route('/')
def hello():
    # Logowanie informacji o kliencie
    log_info()

    # Przygotowanie odpowiedzi dla klienta
    response = f"Adres IP klienta: {request.remote_addr}\n"
    response += f"Data i godzina w strefie czasowej : {datetime.now()}\n"

    return response

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
