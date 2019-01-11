# HT https://stackoverflow.com/a/52234729/179583

import json
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 8888

class Handler(BaseHTTPRequestHandler):
  def do_POST(self):
    # request
    req_size = int(self.headers.getheaders('content-length')[0])
    body = self.rfile.read(req_size)
    data = json.loads(body)
    if False:
        # anonymize some data for screenshot
        data['session']['user']['userId'] = "amzn1.ask.account.ABC123"
        data['context']['System']['device']['deviceId'] = "amzn1.ask.device.ABC123"
        data['context']['System']['apiAccessToken'] = "sample123"
        data['context']['System']['user']['userId'] = data['session']['user']['userId']
    print json.dumps(data, indent=4)
    
    # response
    reply = {
        'version': "1.0",
        'response': {
            'outputSpeech': {
                'type': "PlainText",
                'text': "Your request has been received. Have a nice day."
            }
        }
    }
    self.send_response(200)
    self.send_header('Content-Type','application/json')
    self.end_headers()
    self.wfile.write(json.dumps(reply)+'\n')

print "Starting on port", PORT_NUMBER
server = HTTPServer(('', PORT_NUMBER), Handler)
server.serve_forever()
