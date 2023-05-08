# nostr-python
a nostr protocol with python


client:
1. Connect to relay -  
  websockets :  https://relay.nekolicio.us/
  nostr-watcher : https://relay.nekolicio.us/watcher/
  
2. Send event (ref protocol)- in json
```
["EVENT", <event JSON >] :

{
  "id": <32-bytes lowercase hex-encoded sha256 of the serialized event data>,
  "pubkey": <32-bytes lowercase hex-encoded public key of the event creator>,
  "created_at": <unix timestamp in seconds>,
  "kind": <integer>,
  "tags": [
    ["e", <32-bytes hex of the id of another event>, <recommended relay URL>],
    ["p", <32-bytes hex of a pubkey>, <recommended relay URL>],
    ... // other kinds of tags may be included later
  ],
  "content": <arbitrary string>,
  "sig": <64-bytes hex of the signature of the sha256 hash of the serialized event data, which is the same as the "id" field>
 }
```
simplied as -

```
["EVENT", <event JSON >] :

{
  "id": ...,
  "pubkey": ...,
  "created_at": ...,
  "kind": 1,
  "tags": [],
  "content": "First try nostr-python OK !",
  "sig": ...
 }
```

3. Disconnect
