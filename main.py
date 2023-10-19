# Sky Disco Bar Project

from scapy.all import ARP, Ether, srp

# Define la dirección de destino para el escaneo (10.1.0.0/16)
target_ip = "10.1.0.0/16"

# Crea un paquete ARP para solicitar las direcciones IP de los hosts en la red
arp = ARP(pdst=target_ip)

# Crea un paquete Ethernet para encapsular el paquete ARP
ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

# Combina el paquete Ethernet y el paquete ARP
packet = ethernet/arp

# Envía el paquete y recibe las respuestas
result = srp(packet, timeout=3, verbose=0)[0]

# Procesa las respuestas
for sent, received in result:
    print(f"IP: {received.psrc} - MAC: {received.hwsrc}")
