import socket

import requests


def send_exception(message, channel='#exceptions'):
    url = 'https://hooks.slack.com/services/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'
    message = ':rat: {hostname}-{environment} ```{message}```'.format(
        message=message,
        hostname=socket.gethostname(),
        environment='dev'
    )
    requests.post(
        url,
        json={
            'text': message,
            'channel': channel,
        },
    )
