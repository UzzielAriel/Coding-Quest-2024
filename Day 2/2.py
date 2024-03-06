def hex(ip):
    ip_decimal = '.'.join(str(int(ip[i:i+2], 16)) for i in range(0, len(ip), 2))
    return ip_decimal

ship_internal_bytes = 0
passenger_wifi_bytes = 0

packet_headers = open("2.txt", "r")

for header in packet_headers:
    length = int(header[4:8], 16)
    source_ip = hex(header[24:32])
    destination_ip = hex(header[32:40])

    if source_ip.startswith("192.168.") or destination_ip.startswith("192.168."):
        ship_internal_bytes += length
    elif source_ip.startswith("10.0.") or destination_ip.startswith("10.0."):
        passenger_wifi_bytes += length

ratio = f"{ship_internal_bytes}/{passenger_wifi_bytes}"

print(":", ratio)
