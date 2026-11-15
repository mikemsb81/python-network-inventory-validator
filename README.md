# Python Network Inventory Validator

## Purpose
Check a device inventory for invalid and duplicate IP addresses
before using it for network tasks.

## How it works
- Reads devices from a CSV file.
- Validates IP addresses using Python's ipaddress module.
- Uses a dictionary to track addresses and their first device.
- Flags repeated addresses and skips invalid entries.

## Run
python3 inventory_validator.py

## Save a report
python3 inventory_validator.py > inventory_report.txt

## Testing completed
- Detected an invalid address: 192.168.10.999.
- Detected R2 using the same address as R1.
- Accepted all five addresses after correcting the inventory.

## Limitations
This script checks inventory data. It does not connect to devices
or verify that they are online. Repeated addresses are flagged
across the entire file, without considering separate VRFs or sites.
