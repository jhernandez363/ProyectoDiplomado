import network, time, urequests
from machine import Pin
from utime import sleep, sleep_ms, ticks_us
from dht import DHT22


sensor_dht = DHT22(Pin(4))

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

if conectaWifi ("Wokwi-GUEST", ""):
  print ("Conexión exitosa!")
  print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())

  #url = ("https://api.thingspeak.com/channels/2403598/feeds.json?api_key=1MBUR9MTMOZ8PJIN")
  url = ("https://api.thingspeak.com/update?api_key=OHMUG6OQDBL4RZU6&field1")
    
 

  while True:
    sensor_dht.measure()
    temp = sensor_dht.temperature()
    hum = sensor_dht.humidity() 
    print("Temp: {}°C, Hum: {}%".format(temp, hum))
    respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum)) # si necesito enviar mas informacion repito mas field
    print(respuesta.text)
    print (respuesta.status_code)
    respuesta.close ()

 
else:
  print ("Imposible conectar")
  miRed.active (False)
