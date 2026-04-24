from ncclient import manager

# Estos son los datos para que el script sepa a qué router conectarse
router = {
    "host": "192.168.56.101", # IP del router que vimos en tu captura
    "port": 830,              # Puerto estándar de NETCONF
    "username": "admin",
    "password": "cisco",      # Cambia si usas otra clave en el router
    "hostkey_verify": False
}

# Este es el "mensaje" en formato XML que le envía las instrucciones al router
config_xml = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CLAUDIA-REINOSO</hostname>
        <interface>
            <Loopback>
                <name>22</name>
                <ip>
                    <address>
                        <primary>
                            <address>22.22.22.22</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

# Aquí se ejecuta la conexión y se envía la configuración
with manager.connect(**router) as m:
    m.edit_config(target='running', config=config_xml)
    print("¡Listo! Hostname cambiado y Loopback 22 creada.")