import network
import time
import urequests
import random
# Configura el módulo Wi-Fi en modo estación (STA)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # Activa la interfaz Wi-Fi

# Conéctate a la red Wi-Fi
ssid = 'fogel'  # Reemplaza con el nombre de tu red Wi-Fi
password = '123456789'  # Reemplaza con la contraseña
wlan.connect(ssid, password)

# Espera a que se conecte
while not wlan.isconnected():
    print("Conectando...")
    time.sleep(1)

# Una vez conectado, imprime los detalles
print("Detalles de conexión:", wlan.ifconfig())

API_KEY = "F3JXY98XMVNZEU9S"  # Reemplaza con tu clave de API de ThingSpeak

# Función para enviar datos a ThingSpeak
def enviar_dato(valor):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={valor}"
    try:
        respuesta = urequests.get(url)
        print("Respuesta:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar:", e)

# Enviar datos aleatorios cada 15 segundos
while True:
    valor = random.randint(10, 100)  # Genera un número aleatorio entre 10 y 100
    print(f"Enviando: {valor}")
    enviar_dato(valor)
    time.sleep(5)  # Espera 15 segundos