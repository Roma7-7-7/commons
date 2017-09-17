from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8000


class TraceHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.__handle_request()

    def do_GET(self):
        self.__handle_request()

    def do_POST(self):
        self.__handle_request()

    def do_PUT(self):
        self.__handle_request()

    def do_PATCH(self):
        self.__handle_request()

    def do_DELETE(self):
        self.__handle_request()

    def __handle_request(self):
        print('--------------------------------------------')
        print('Method: %s' % self.command)

        print('Path: %s' % self.path)

        params = self.__parse_params()
        if params:
            print('Params:')
            for key, value in params.items():
                print('\t%s: %s' % (key, value))

        print('Headers:')
        for key, value in self.headers.items():
            print('\t%s: %s' % (key, value))

        body = self.__get_body()
        if body:
            print('Body:')
            print(body)

        self.send_response(200, '')

    def __parse_params(self):
        return parse_qs(urlparse(self.path).query)

    def __get_body(self):
        content_length = self.headers['Content-Length']
        if not content_length:
            return None

        return self.rfile.read(int(content_length))


if __name__ == '__main__':
    print('Starting server')
    try:
        server = HTTPServer(('', PORT), TraceHTTPRequestHandler)
        server.serve_forever()
    except Exception as e:
        print('Error')
        print(e)
