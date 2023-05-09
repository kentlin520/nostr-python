#!/usr/bin/env python3

import time
import json
import ssl
import asyncio
import websockets
#from nostr.relay_manager import RelayManager
import secp256k1
#rom hashlib import sha256
#from nostr.key import PrivateKey
import argparse
RELAY_Timeout_DURATION = 60




async def send_message(host,messages):
    uri = "wss://{}".format(host)
    event = {
        'id': None,
        'sig': None,
        'content':messages,
        'created_at':None,
        'kind':1,
        'pubkey': None,
        'tag':[]
    }

    data = [0,event['kind'],event['tag'],event['content']]
    serialzed = json.dumps(data,separators=(',',':'),ensure_ascii=False).encode()

    async with websockets.connect(uri) as websocket:
        payload = [
            'EVENT',
            event
        ]
        await websocket.send(json.dumps(payload))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host')
    parser.add_argument('--message')
    args = parser.parse_args()
    asyncio.run(send_message(args.host,args.message))