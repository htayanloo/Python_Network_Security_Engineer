from flask import Flask, jsonify, request
from ping3 import ping
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import sys

app = Flask(__name__)

# Store history of last 10 pings for each host
history = {}


def ping_host(host):
    latency = ping(host)
    if latency is None:
        return (host, 'unavailable', 10000)  # large value for 'unavailable'
    else:
        return (host, f'{int(latency * 1000)} ms', latency * 1000)


def concurrent_ping(hosts):
    # Initialize history
    for host in hosts:
        history[host] = deque(maxlen=50)

    with ThreadPoolExecutor(max_workers=len(hosts)) as executor:
        results = list(executor.map(ping_host, hosts))

    # Update history and create a dictionary for JSON response
    response = []

    for host, ping_response, latency_ms in results:
        history[host].append(latency_ms)
        host_response = {
            'host': host,
            'ping_response': ping_response,
            'last_50_responses': list(history[host])
        }
        response.append(host_response)

    return response


@app.route('/ping', methods=['POST'])
def ping_route():
    hosts = request.get_json().get('hosts', [])
    return jsonify(concurrent_ping(hosts))


if __name__ == "__main__":
    app.run(debug=True)
