#!/usr/bin/env python3

import time
import secp256k1
import json
import asyncio
import websockets
#from hashlib import sha256
#from nostr.key import PrivateKey
import argparse



if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--host')
  parser.add_argument('--message')
  args = parser.parse_args()
  #asyncio.run(send_message(args.host,args.message))
 