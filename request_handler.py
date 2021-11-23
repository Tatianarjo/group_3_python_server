from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from users import create_user, login_user, get_single_user, get_all_users
from categories import get_all_categories, get_single_category, create_category


class RareRequestHandler(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
        # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

    # No query string parameter
        else:
            id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    #This handles any GET request

    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)
        if len(parsed) == 2:
            ( resource, id ) = parsed

        if resource == "users":
            if id is not None:
                response = f"{get_single_user(id)}"
            else:
                response = f"{get_all_users()}"

        elif resource == "categories":
            if id is not None:
                response = f"{get_single_category(id)}"
            else:
                response = f"{get_all_categories()}" 

        self.wfile.write(response.encode())

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        raw_body = self.rfile.read(content_len)
        post_body = json.loads(raw_body)

        resource = None
        
        response = None
        new_user = None
        new_category = None
        
        if self.path == '/login':
            user = login_user(post_body)
            if user:
                response = {
                    'valid': True,
                    'token': user.id
                }
                self._set_headers(200)
            else:
                response = { 'valid': False }
                self._set_headers(404)

        if self.path == '/register':
            try:
                new_user = create_user(post_body)
                response = {
                    'valid': True,
                    'token': new_user.id
                }
            except Exception as e:
                response = {
                    'valid': False,
                    'error': str(e)
                }
            self._set_headers(201)
        
        if resource == "users":
            new_user = create_user(post_body)
        #Creating a new category here
        if resource == "categories":
            new_category = create_category(post_body)

        #encodes the new category and sends in the response
            self.wfile.write(f"{new_user}".encode())
            self.wfile.write(f"{new_category}".encode())

        self.wfile.write(json.dumps(response).encode())


def main():
    host = ''
    port = 8088
    print(f'listening on port {port}!')
    HTTPServer((host, port), RareRequestHandler).serve_forever()


if __name__ == "__main__":
    main()
