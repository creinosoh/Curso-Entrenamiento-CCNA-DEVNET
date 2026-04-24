# Examen Final Práctico - CCNA DEVNET
**Estudiante:** Claudia  
**Sede:** San Joaquin 
**Docente:** Víctor Araneda Serrano  
**Ramo:** DRY7122 S.A

## Descripción del Proyecto
[cite_start]Este repositorio contiene la implementación de soluciones de programación y virtualización de redes solicitadas para el proceso de modernización tecnológica de la empresa **DRY7122 S.A**. El proyecto abarca desde la gestión de identidades y seguridad de datos hasta la automatización de infraestructura de red mediante protocolos modernos.

## Estructura del Repositorio
* [cite_start]**scripts/**: Contiene la lógica de negocio, incluyendo la gestión de usuarios en SQLite con hashing de contraseñas (Puerto 7890) [cite: 30] [cite_start]y scripts de configuración de red mediante `netmiko` y `ncclient`[cite: 44, 54].
* [cite_start]**docker/**: Automatización del despliegue del sitio web en contenedores utilizando el puerto 7529.
* [cite_start]**evidence/**: Capturas de pantalla que validan el cumplimiento de cada requerimiento con registro de fecha y hora.
* [cite_start]**SD-WAN_Theory-Item-6.md**: Documentación teórica sobre tecnologías SD-WAN y planos de control/datos[cite: 64, 65].

## Tecnologías Utilizadas
* **Lenguajes:** Python (Requests, Tabulate, Netmiko, NCCLient)[cite: 18].
* [cite_start]**Automatización:** Ansible (Playbooks de respaldo) y pyATS (Genie).
* [cite_start]**Virtualización:** Docker y Cisco CSR1000v[cite: 17, 36].
* **Protocolos de Red:** NETCONF, RESTCONF, OSPF, SSH[cite: 43, 54].
* [cite_start]**Gestión de APIs:** Postman (vManage SD-WAN y RESTCONF)[cite: 46, 61].

## Instrucciones de Ejecución
1.  [cite_start]**Gestión de Usuarios:** Ejecutar `scripts/DB-Browser-SQL-Lite-app.py` para iniciar el servicio web en el puerto 7890[cite: 30].
2.  [cite_start]**Despliegue Docker:** Utilizar el script `docker/ejecutar_docker.sh` para levantar el contenedor en el puerto 7529[cite: 37, 40].
3.  [cite_start]**Configuración de Red:** Los scripts dentro de `scripts/` permiten la automatización de Loopbacks y enrutamiento OSPF en el router CSR1000v.