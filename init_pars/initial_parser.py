import requests
import json
import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    request = socket.recv()
    socket.send_string("respond")
    print("Received request: ", request)
    requests.post('localhost:11223/media-request', data=request)

