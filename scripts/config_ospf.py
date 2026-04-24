
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'devasc',
    'password': 'devasc',
}

config_commands = [
    'router ospf 123',
    'router-id 1.1.1.1',
    'network 0.0.0.0 255.255.255.255 area 0',
    'passive-interface default',
    'no passive-interface GigabitEthernet1',
    'no passive-interface GigabitEthernet2'
]

try:
    print("Conectando al router... (espera unos segundos)")
    with ConnectHandler(**device) as net_connect:
        print("Enviando comandos de OSPF...")
        # Enviamos los comandos y capturamos la salida
        output_config = net_connect.send_config_set(config_commands)
        print(output_config) # Esto imprimirá los comandos aplicándose
        
        print("\n--- Verificación: show running-config | section router ospf ---")
        verification = net_connect.send_command("show running-config | section router ospf")
        print(verification)

except Exception as e:
    print(f"Error: {e}")