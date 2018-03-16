import json

from flask import Flask, request

class WebHookServer(object):
    
    def __init__(self, address="0.0.0.0", port=80, verify_token="", callback="/webhook"):
        self.app = Flask(__name__)
        self.hostname = address
        self.port = port
        self.verify_token = verify_token 
        self.callback = callback

        @self.app.route(self.callback, methods=["POST"])
        def f():
            if request.method == "GET":
                mode = request.args.get("hub.mode", "")
                token = request.args.get("hub.verify_token", "")
                challenge = request.args.get("hub.challenge", "")
                if mode and token:
                    if mode == "subscribe" and token == self.verify_token:
                        return challenge
            else:
                data = request.json()
                if data.get("object", "") == "page":
                    for entry in data["entry"]:
                        m = entry["messaging"][0]
                        print(m)


        
        @self.app.route("/")
        def root():
            return {}

    def serve(self):
        self.app.run(host=self.hostname, port=self.port, debug=False)

