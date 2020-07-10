#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:26:05 2020

@author: bollam
"""
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

class httpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
#        self.log_request()
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path + " response from Raja").encode('utf-8'))
        
    def do_POST(self):
        logging.info("POST Request received")
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
        
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'test/html')
        self.end_headers()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
        
    serverUrl = ('127.0.0.1', 9099)
    httpd = HTTPServer(serverUrl, httpHandler) # (server_class, handler_class)
    logging.info("Http Server starting...")
    
    try:
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    logging.info("Http server closing...")
