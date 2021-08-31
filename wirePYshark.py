#!/usr/bin/env python3
import argparse
from scapy.all import *


# Function to parse all arguments from the cli
def argument_parser():
    # Initiate the argument parser
    args_parser = argparse.ArgumentParser()
    # Argument for adding the interface details
    args_parser.add_argument('-i', '--interface', help='specify the interface',
                             action='store')
    # Argument for listing the interfaces of all network devices
    args_parser.add_argument('-l', '--list', help='list the interface(s)',
                             action='store_true')
    # Argument for disabling the automatic file save function
    args_parser.add_argument('-n', '--nooutput', help='dont output to file',
                             action='store_true')
    # Return all the arguments
    return args_parser.parse_args()


# Function to save the result of the packet capture of to a file
def save_output(data):
    # Opens the file to be written
    with open('output.txt', 'w') as output:
        # Writes the data
        output.write(data)


# Perfom the packet capture on the CDP mac address, option to specify the
# interface within intf
def shark(intf=''):
    # Loads the CDP module
    load_contrib("cdp")
    # Checks to see if the intf varable has an interface specified
    if intf == '':
        # Packet Capture for the CDP mac
        cdp_packet = sniff(filter='ether dst 01:00:0c:cc:cc:cc', count=1)
    # Checks to see if the intf varable has an interface specified
    elif intf != '':
        # Packet Capture for the CDP mac specified interface
        cdp_packet = sniff(filter='ether dst 01:00:0c:cc:cc:cc', count=1,
                           iface=intf)
    # Returns the result of CDP filter
    return cdp_packet[0]


# Main function of the python program
def main():
    # Stores the result of the function argument_parser() within a variable
    args = argument_parser()
    # Main try function of the program
    try:
        # Checks if the list argument is flagged and presents the list of
        # network interfaces
        if args.list:
            scapy.interfaces.show_interfaces()
        else:
            # Uses the default inerface when one isnt specified
            if args.interface is None:
                cdp_result = shark()

            # Uses the specified interface
            elif type(args.interface) == str:
                cdp_result = shark(args.interface)

            # collate the results ready to be printed to the cli or saved
            # as a file
            result = cdp_result['Device ID'].show(dump=True)
            result = result + cdp_result['Port ID'].show(dump=True)

            # Disable file output if needed based off the flags closen
            # No file output
            if args.nooutput:
                print(result)

            # File output
            elif not args.nooutput:
                save_output(result)

    # Raise exception if needed
    except Exception as e:
        raise

# Run the python program as a script
if __name__ == '__main__':
    main()
