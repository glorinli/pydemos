from urllib import request
import json
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def call_rc_webhook(hook_url, payload):
    json_data = json.dumps(payload)
    # print('Json data')
    print(json_data)

    req = request.Request(hook_url, data=json_data.encode())
    req.add_header('Content-Type', 'application/json')

    res_data = request.urlopen(req)
    res = res_data.read()
    print("Result:")
    print(res)


def call_rc_webhook_card(hook_url):
    payload = {
        "attachments": [
            {
                "type": "Card",
                "fallback": "Something bad happened",
                "color": "#00ff2a",
                "title": "Title",
                "text": "Text",
                "author_name": "Test",
                "author_icon": "",
                "author_link": "",
                "fields": [
                    {
                        "title": "Item",
                        "value": "Item Value"
                    }
                ]
            }
        ]
    }

    call_rc_webhook(hook_url, payload)


if __name__ == '__main__':
    hook_url = os.getenv("RC_ME_CONVERSATION_INCOMING_WEBHOOK")
    print(hook_url)
    call_rc_webhook_card(str(hook_url))
