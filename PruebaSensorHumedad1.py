import machine
import time

# Configura el pin del sensor de humedad
pin_sensor_humedad = machine.ADC(26)  # Ajusta el número del pin según tu conexión

# Ajusta el umbral de humedad según tus necesidades
umbral_humedad = 1000

# Función para leer el sensor de humedad
def leer_humedad():
    valor_sensor_humedad = pin_sensor_humedad.read()
    return valor_sensor_humedad

# Función para determinar si es necesario regar
def necesidad_riego(valor_humedad, umbral):
    return valor_humedad < umbral

# Bucle principal
while True:
    valor_humedad = leer_humedad()
    print("Valor de humedad:", valor_humedad)

    if necesidad_riego(valor_humedad, umbral_humedad):
        print("¡Es necesario regar!")
    else:
        print("La humedad es suficiente. No es necesario regar.")

    time.sleep(2)  # Espera 1 hora (puedes ajustar este tiempo según tus necesidades)
