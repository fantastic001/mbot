import json

from flask import Flask, request
import requests

class WebHookServer(object):
    
    def __init__(self, page_access_token, address="0.0.0.0", port=80, verify_token="", callback="/webhook"):
        self.app = Flask(__name__)
        self.hostname = address
        self.port = port
        self.verify_token = verify_token 
        self.callback = callback
        self.page_access_token = page_access_token 
        
        @self.app.route("/", methods = ["POST", "GET"])
        def root():
            if request.method == "GET":
                mode = request.args.get("hub.mode", "")
                token = request.args.get("hub.verify_token", "")
                challenge = request.args["hub.challenge"]
                if mode and token.strip():
                    if mode == "subscribe" and token == self.verify_token:
                        print(challenge)
                        return challenge
                    else:
                        print("Wrong token")
                        print("Should be %s" % token)
                        return ""
                else:
                    print("Not all parameters specified")
                    return ""
            else:
                data = request.json
                print(data)
                if data.get("object", "") == "page":
                    for entry in data["entry"]:
                        m = entry.get("messaging", [None])[0]
                        if m != None:
                            response = self.handle_message(m["sender"]["id"], m["message"]["text"], m["timestamp"])
                            if response != "" and response != None:
                                requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=%s" % self.page_access_token, json={
                                    "recipient": {
                                        "id": m["sender"]["id"]
                                    }, 
                                    "message": {
                                        "text": response 
                                    }
                                })
                return ""

    def serve(self):
        self.app.run(host=self.hostname, port=self.port, debug=False)

    def handle_message(self, sender_id, text, timestamp):
        if text == "hello":
            return "hello!"
        return None
