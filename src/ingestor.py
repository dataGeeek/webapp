import sys
sys.path.append('.')
import src.helper.parseconfig
import asyncio
import websockets
import json
CFG = src.helper.parseconfig.get_config_file()

channel = CFG['ingestor']['channel']
endpoint = CFG['ingestor']['endpoint']
appkey = CFG['ingestor']['apikey']
async def listen():
    urlString = endpoint + '/v2?appkey=' + appkey
    print(urlString)
    async with websockets.connect(urlString) as websocket:
        request = {
            "action": "rtm/subscribe",
            "id": "20",
            "body": {
                "channel": channel
            }
        }
        await websocket.send(json.dumps(request))  # response to connect (should say connected..)
        print("> {}".format(request))

        greeting = await websocket.recv()
        print("< {}".format(greeting))
        while True:  # This is the message loop -- runs forever
            message = await websocket.recv()
            jsonMsg = json.loads(message)
            print(jsonMsg)  # prints the 'next' msg id (some serial number)
            # <=== include your message handler here ====>
asyncio.get_event_loop().run_until_complete(listen())

