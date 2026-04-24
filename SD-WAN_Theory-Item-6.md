# Ítem 6: Fundamentos de SD-WAN

## 1. Tecnologías SD-WAN en el Mercado
En la actualidad, existen diversas soluciones de redes definidas por software (SD-WAN). Las más destacadas son:

* **Cisco SD-WAN (Viptela):** Solución empresarial robusta basada en controladores separados para gestión, control y datos.
* **Cisco Meraki:** Enfoque simplificado y gestionado 100% desde la nube.
* **Fortinet (Secure SD-WAN):** Integra funciones de seguridad avanzadas (NGFW) directamente en la solución WAN.
* **VMware (VeloCloud):** Especializada en la optimización de aplicaciones en entornos multi-cloud.
* **Aruba (Silver Peak):** Enfocada en la aceleración de rendimiento y visibilidad de red.

## 2. Operación de los Planos en SD-WAN
La arquitectura SD-WAN se basa en la separación de funciones para mejorar la escalabilidad y flexibilidad:

### Plano de Control (Control Plane)
Es el **cerebro** de la solución. En Cisco SD-WAN, es gestionado por los controladores **vSmart**.
* **Función:** Establece la topología de la red y distribuye las políticas de ruteo y seguridad.
* **Protocolo:** Utiliza **OMP** (Overlay Management Protocol) para intercambiar información de ruteo sin tocar los datos de tráfico del usuario.

### Plano de Datos (Data Plane)
Es el **músculo** de la red. Ejecutado por los routers de borde denominados **WAN Edges** (vEdge o cEdge).
* **Función:** Se encarga del reenvío de paquetes de datos del usuario.
* **Mecanismo:** Crea túneles **IPsec** seguros sobre cualquier medio de transporte (MPLS, Internet, 4G/5G) para mover la información de forma cifrada siguiendo las instrucciones del plano de control.