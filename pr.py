import requests
import json

def check(query_input):
    url = "http://65.2.152.64:9090/api/v1/query?"
    payload = {"query": query_input}

    try:
        response = requests.get(url, params=payload)

    except Exception as e:
        raise SystemExit(print("TIMEOUT: ", e))

    else:
        json_data = response.json()
        result_json = json_data['data']
        result = result_json["result"]

        for metric in result:
            metric_inst = metric['metric']
            metric_value = metric['value']
            status_value = metric_value[1]
            status = metric_inst
            for server in status['job']:
                print(server, end='')
            for ip_add in status['instance']:
                print(ip_add, end='')
            if int(status_value) == 1:
                print("\nstatus: OK")
            else:
                print("\nstatus: NOT OK")


check(query_input="up")
