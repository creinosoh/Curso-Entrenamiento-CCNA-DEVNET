from genie.testbed import load
import json
import os


ruta_completa = os.path.abspath('testbed.yaml')
tb = load(ruta_completa)
def ejecutar_genie():
    try:
        # 1. Cargar el testbed
        print("Cargando el archivo testbed.yaml...")
        tb = load('testbed.yaml')
        device = tb.devices['CSR1000V']

        # 2. Conectar al router
        print(f"Conectando a {device.name}...")
        device.connect(log_stdout=True)

        # 3. Parsear el comando
        print("Obteniendo información de IPv6...")
        resultado = device.parse('show ipv6 interface brief')

        # 4. Crear directorio y guardar JSON (Requisito del examen)
        os.makedirs('interfaces_ipv6', exist_ok=True)
        ruta_archivo = 'interfaces_ipv6/resultado_ipv6.json'
        
        with open(ruta_archivo, 'w') as f:
            json.dump(resultado, f, indent=4)

        print(f"\n--- ÉXITO ---")
        print(f"La información se guardó correctamente en: {ruta_archivo}")
        
        # Desconectar
        device.disconnect()

    except Exception as e:
        print(f"\n--- ERROR ---")
        print(f"Detalle: {e}")

if __name__ == "__main__":
    ejecutar_genie()