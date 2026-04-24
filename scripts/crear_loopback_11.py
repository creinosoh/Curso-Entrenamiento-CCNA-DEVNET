from ncclient import manager
import sys

# Datos de conexión al router
router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "devasc",
    "password": "devasc",
    "hostkey_verify": False
}

# Configuración XML: Crea la Loopback 11 y la apaga
config_xml = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>11</name>
                <description>Loopback creada para examen - Estado Down</description>
                <ip>
                    <address>
                        <primary>
                            <address>11.11.11.11</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
                <shutdown/>
            </Loopback>
        </interface>
    </native>
</config>
"""

try:
    with manager.connect(**router) as m:
        response = m.edit_config(target='running', config=config_xml)
        print("¡Éxito! La interfaz Loopback 11 ha sido creada.")
        print("Estado configurado: Administrativamente apagada (shutdown).")
except Exception as e:
    print(f"Error al conectar o configurar: {e}")