import sys
import json
import requests
from logging import critical as log

requests.packages.urllib3.disable_warnings()


def main():
    argv = sys.argv[1].split('/')

    if sys.argv[1].startswith('https://'):
        conf = dict(bucket=argv[-2], cluster=['/'.join(argv[:-2])],
                    token='')
        user = argv[-1]
    else:
        conf, user = argv
        with open(conf) as fd:
            conf = json.load(fd)

    for srv in conf['cluster']:
        try:
            url = '{}/{}/{}'.format(srv, conf['bucket'], user)
            log('sending request - {}'.format(url))
            res = requests.post(url, headers={'x-token': conf['token']},
                                verify=False)

            log('status : {}'.format(res.status_code))

            if 200 == res.status_code:
                obj = res.json()
                print(json.dumps(obj, indent=4, sort_keys=4))
                exit(0)
        except Exception as e:
            log(e)

    exit(1)


if '__main__' == __name__:
    main()
