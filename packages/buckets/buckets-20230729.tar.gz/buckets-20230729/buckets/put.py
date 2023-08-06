import sys
import json
import time
import requests
from logging import critical as log

requests.packages.urllib3.disable_warnings()


def main():
    conf, key, version = sys.argv[1].split('/')

    with open(conf) as fd:
        conf = json.load(fd)

    data = sys.stdin.read()

    ts = time.time()
    for srv in conf['cluster']:
        try:
            url = '{}/{}/{}/{}'.format(srv, conf['bucket'], key, version)
            log('sending request - {}'.format(url))
            res = requests.put(url, headers={'x-token': conf['token']},
                               data=data, verify=False)

            log('status : {}'.format(res.status_code))

            if res.status_code in (401, 403):
                print(res.content.decode())
                exit(1)

            if 200 != res.status_code:
                continue

            content = res.json()
            content['time_ms'] = int((time.time() - ts) * 1000)
            print(json.dumps(content, indent=4, sort_keys=True))
            exit(0)
        except Exception as e:
            log(e)

    exit(1)


if '__main__' == __name__:
    main()
