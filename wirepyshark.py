'''wirepyshark

A tool to assist with locating the network port your device is connected to without having
to trace the cable physically. This requires a CDP capable device such as a Cisco Switch.

:Authors:
    @kor3n
:Version: 1.0.1
:Date: 27/09/2024
'''
import argparse
import scapy.layers.l2
from scapy.all import load_contrib, sniff, show_interfaces


def argument_parser() -> argparse.ArgumentParser.parse_args:
    '''Argument Parser

    Function to parse all arguments from the cli.

    Returns:
        argparse.ArgumentParser.parse_args: List of arguments that were passed in via the cli.
    '''
    args_parser: argparse.ArgumentParser = argparse.ArgumentParser()
    args_parser.add_argument('-i', '--interface', help='specify the interface', action='store')
    args_parser.add_argument('-l', '--list', help='list the interface(s)', action='store_true')
    args_parser.add_argument('-n', '--nooutput', help='dont output to file', action='store_true')

    return args_parser.parse_args()


def save_output(data: str, file_name: str = 'output.txt') -> None:
    '''Save Output

    Saves the output to a file, by default output.txt.

    Args:
        data (str): data to write to the output file.
        file_name (str): file name of the output file.
    '''
    with open(file_name, 'w', encoding='utf-8') as output:
        output.write(data)


def shark(interface: str) -> scapy.layers.l2.Dot3:
    '''Shark Function

    This uses scapy to capture the CDP information from a cisco switch. The `ether dst 01:00:0c:cc:cc:cc`
    command is used to capture the CDP information based on the MAC address.

    Args:
        interface (str): Interface to start capturing on.

    Returns:
        scapy.layers.l2.Dot3: Infomration from the Scapy Capture
    '''
    load_contrib("cdp")

    if interface == '':
        cdp_packet = sniff(filter='ether dst 01:00:0c:cc:cc:cc', count=1)
    elif interface != '':
        cdp_packet = sniff(filter='ether dst 01:00:0c:cc:cc:cc', count=1, iface=interface)

    return cdp_packet[0]


def main() -> None:
    '''Main Function

    This is the main function that calls other required functions to complete the script.
    '''
    args: argparse.ArgumentParser.parse_args = argument_parser()
    try:
        if args.list:
            show_interfaces()
        else:
            if args.interface is None:
                cdp_result: scapy.layers.l2.Dot3 = shark('')
            elif isinstance(args.interface, str):
                cdp_result: scapy.layers.l2.Dot3 = shark(args.interface)

            result: str = cdp_result['Device ID'].show(dump=True)
            result: str = result + cdp_result['Port ID'].show(dump=True)

            if args.nooutput:
                print(result)
            elif not args.nooutput:
                save_output(result)

    except Exception as expt:
        raise expt


if __name__ == '__main__':
    main()
