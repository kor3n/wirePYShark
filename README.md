# wirePYshark
A tool to assist with locating the network port your device is connected to without having to trace the cable physically. This requires a CDP capable device such as a Cisco Switch.

## Requirements
- Python 3
- Scapy - Python Package 

#### Package Installation
```sh
pip install -r requirements.txt
```

## Usage
#### Run wirepyshark without listing the show_interfaces.
```sh
python wirepyshark.py
```

#### List the network interfaces on the pc you are running wirepyshark from.
```sh
wirepyshark.py -l
```

#### Run wirepyshark with a specific 'name' interface from the `-l, --list` command above.
```sh
python wirepyshark.py -i 'Intel(R) Ethernet Connection'
```

#### Don't output to file, only the screen
```sh
python wirepyshark.py -n
python wirepyshark.py -i 'Intel(R) Ethernet Connection' -n
```