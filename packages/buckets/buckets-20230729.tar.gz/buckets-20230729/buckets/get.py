import sys
import time
import json
import requests
from logging import critical as log

requests.packages.urllib3.disable_warnings()


def main():
    conf, key = sys.argv[1].split('/')

    with open(conf) as fd:
        conf = json.load(fd)

    ts = time.time()
    for srv in conf['cluster']:
        try:
            url = '{}/{}/{}'.format(srv, conf['bucket'], key)
            log('sending request - {}'.format(url))
            res = requests.get(url, verify=False)

            log('status : {}'.format(res.status_code))

            if 404 == res.status_code:
                print(res.content.decode())
                exit(1)

            if 200 != res.status_code:
                print(res.content.decode())
                continue

            print('bucket   : {}'.format(res.headers['x-bucket']))
            print('key      : {}'.format(res.headers['x-key']))
            print('version  : {}'.format(res.headers['x-version']))
            print('length   : {}'.format(res.headers['content-length']))
            print('mimetype : {}'.format(res.headers['content-type']))

            content = res.content
            print('time_ms  : {}'.format(int((time.time() - ts) * 1000)))

            print('')
            print(content)
            exit(0)
        except Exception as e:
            log(e)

    exit(1)


if '__main__' == __name__:
    main()
