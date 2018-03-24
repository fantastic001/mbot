
from src import * 


WebHookServer(open("token").read().strip(), port=563, verify_token=open("verify_token").read().strip()).serve()
