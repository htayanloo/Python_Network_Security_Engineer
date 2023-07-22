from scapy.all import *
import time
from rich.console import Console
from rich.table import Table
from rich.live import Live
from scapy.layers.inet import IP, ICMP

# Initialize a dictionary to hold the IPs and their times
ip_dict = {}


def trace_route(ip_address):
    while True:
        time.sleep(5)
        for i in range(1, 28):
            packet = IP(dst=ip_address, ttl=i) / ICMP()
            # Send the packet and get a reply
            start_time = time.time()
            reply = sr1(packet, timeout=1, verbose=0)
            end_time = time.time()
            if reply is None:
                # If no reply, we break the loop
                # print("Hop %d: Request timed out" % i)
                pass
            else:
                # Intermediate hop or destination reached
                ip_dict[reply.src] = round((end_time - start_time) * 1000, 2)
                if reply.type == 0:  # Destination reached
                    return  # Exit the function once destination is reached
            # print(ip_dict)


console = Console()

with Live(console=console, refresh_per_second=1) as live:  # Refresh rate of 4 times per second
    while True:
        trace_route("8.8.8.8")
        # Create a new table for each update
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("IP Address", style="dim", width=20)
        table.add_column("Time (ms)")

        # Add rows to the table
        for ip, round_trip_time in ip_dict.items():
            table.add_row(ip, "%.2f" % round_trip_time)

        # Update the table in the Live display
        live.update(table)
        # Replace with the IP you wish to trace
        # 5 seconds delay between each trace. Adjust this value as per your needs.
