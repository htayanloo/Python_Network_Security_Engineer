from ping3 import ping
from rich.console import Console
from rich.table import Table
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import time
import sys

console = Console()

# Store history of last 10 pings for each host
history = {}


def ping_host(host):
    latency = ping(host)
    if latency is None:
        return (host, 'unavailable', 10000)  # large value for 'unavailable'
    else:
        return (host, f'{int(latency * 1000)} ms', latency * 1000)


def get_colored_sparkline(values):
    sparkline = ''
    for value in values:
        if value >= 100:
            sparkline += '[red]▄[/red]'
        elif value >= 50:
            sparkline += '[yellow]▄[/yellow]'
        else:
            sparkline += '[green]▄[/green]'
    return sparkline


def concurrent_ping(hosts):
    # Initialize history
    for host in hosts:
        history[host] = deque(maxlen=50)

    while True:
        with ThreadPoolExecutor(max_workers=len(hosts)) as executor:
            results = list(executor.map(ping_host, hosts))

        # Update history and create a table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Host")
        table.add_column("Ping Response")
        table.add_column("Last 50 Responses (Sparkline)")

        for host, response, latency_ms in results:
            history[host].append(latency_ms)
            sparkline = get_colored_sparkline(list(history[host]))
            table.add_row(host, response, sparkline)

        # Clear the console and print the table
        console.clear()
        console.print(table)

        time.sleep(1)  # Wait for 1 second


if len(sys.argv) == 1:
    print("use command :: main  1.1.1.1 4.2.2.4 8.8.8.8")
else:
    hosts = sys.argv[1:]

    concurrent_ping(hosts)
