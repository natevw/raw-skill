# HT https://stackoverflow.com/a/52234729/179583

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json

PORT_NUMBER = 8888

class Handler(BaseHTTPRequestHandler):
  def do_POST(self):
    # request
    req_size = int(self.headers.getheaders('content-length')[0])
    body = self.rfile.read(req_size)
    print body
    
    # response
    reply = {'hello':'world', 'received':body}
    self.send_response(200)
    self.send_header('Content-Type','application/json')
    self.end_headers()
    self.wfile.write(json.dumps(reply)+'\n')

print "Starting on port", PORT_NUMBER
server = HTTPServer(('', PORT_NUMBER), Handler)
server.serve_forever()
