import csv
import ipaddress

seen_addresses = {}


with open("devices.csv", newline="") as file:
    inventory = csv.DictReader(file)


    for device in inventory:
        hostname = device["hostname"]
        address = device["ip_address"].strip()

        try:
            parsed_address = ipaddress.ip_address(address)
        except ValueError:
            print(f"INVALID: {hostname} - {address}")
            continue

        if parsed_address in seen_addresses:
            original_device = seen_addresses[parsed_address]
            print(f"DUPLICATE: {hostname} - {address} already used by {original_device}")
        else:
            seen_addresses[parsed_address] = hostname
            print(f"VALID: {hostname} - {address}")
