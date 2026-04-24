from genie.testbed import load
import json
import os
import re

testbed_file = '/home/devasc/Curso-Entrenamiento-CCNA-DEVNET/scripts/testbed.yaml'

try:
    print("--- Conectando al Router CLAUDIA-REINOSO ---")
    tb = load(testbed_file)
    device = tb.devices['CSR1000V']
    device.connect(log_stdout=False)

    print("--- Capturando salida de IPv6 ---")
    raw_output = device.execute('show ipv6 interface brief')
    
    # Creamos un diccionario manualmente para que el JSON sea válido y útil
    parsed_data = {"interfaces": {}}
    
    # Expresión regular para capturar Interfaz, Estado y Direcciones
    lines = raw_output.strip().split('\n')
    current_intf = None

    for line in lines:
        if 'show ipv6' in line or 'CLAUDIA' in line: continue
        
        # Match para línea de interfaz: Nombre [status/protocol]
        match_intf = re.match(r'^(\S+)\s+\[([^\]]+)\]', line)
        if match_intf:
            current_intf = match_intf.group(1)
            parsed_data["interfaces"][current_intf] = {
                "status": match_intf.group(2),
                "ipv6": []
            }
        elif current_intf and line.strip() and "unassigned" not in line:
            # Captura direcciones IPv6 (Global o Link-local)
            parsed_data["interfaces"][current_intf]["ipv6"].append(line.strip())

    # Guardar resultado (REQUISITO DEL EXAMEN)
    os.makedirs('interfaces_ipv6', exist_ok=True)
    ruta_final = 'interfaces_ipv6/resultado_ipv6.json'
    
    with open(ruta_final, 'w') as f:
        json.dump(parsed_data, f, indent=4)

    print(f"\n✅ ¡ÉXITO TOTAL!")
    print(f"Archivo generado en: {ruta_final}")
    device.disconnect()

except Exception as e:
    print(f"\n❌ Error: {e}")