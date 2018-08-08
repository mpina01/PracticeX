import subprocess
import requests
import sys
import json
import time
import os

proj_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(proj_path, "hosts.txt"), "r") as f:
    hostnames = f.readlines()

hostnames = [x.strip() for x in hostnames]

monocle_host = 'http://monitoring3:8500/message/31501/OOBM_'
monocle_history = 'http://monitoring3:8500/history/31501/OOBM_'  

for hostname in hostnames:
    status = 'rag-red'
    try:
        response = subprocess.check_output(['ping', '-c', '1', hostname],stderr=subprocess.STDOUT, universal_newlines=True)
        status = 'rag-green'
    except subprocess.CalledProcessError:
        response = None

    if status == 'rag-green':
        data = '{ "status" : "' + status + '"}' 
        r = requests.post(monocle_host + hostname, data)
    else:
        r = requests.get(monocle_history + hostname + "?sort=-1&limit=1")
        message = r.json()[0] 

        last_timestamp = message['timestamp']
        current_timestamp = int(time.time()) * 1000
        time_difference = current_timestamp - last_timestamp

        if 86400000 > time_difference >= 300000:
            if message['status'] != 'rag-amber' and message['status'] != 'rag-red':
                data = '{ "status" : "rag-amber", "message" : "This device has been unreachable for more than 5 minutes"}'
                r = requests.post(monocle_host + hostname, data)
        elif time_difference >= 86400000:
            if message['status'] != 'rag-red':
                data = '{ "status" : "rag-red", "message" : "This device has been unreachable for more than 24 hours"}'
                r = requests.post(monocle_host + hostname, data)
