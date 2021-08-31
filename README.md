# wirePYshark
A tool to assist onsite personnel with locating the network port without having to trace the cable physically.

## Requirements
- Python 3.2
- Scapy - Python Package 

#### Package Installation
> pip install -r requirements.txt

## Usage
Run wirePYshark without listing the show_interfaces
> wirePYshark.py

List the network interfaces on the pc you are running wirePYshark from
> wirePYshark.py -l

Run wirePYshark with a specific 'name' interface from the -l, --list command above
> wirePYshark.py -i 'Intel(R) Ethernet Connection'

Don't output to file, only the screen
> wirePYshark.py -n
