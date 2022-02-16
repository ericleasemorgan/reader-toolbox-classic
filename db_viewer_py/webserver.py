from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from web import html
from db import sqlite
from sqlite3 import OperationalError
from helper import helper


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index"]:
            self.send_response(html.RC_200)
            self.send_header(html.CONTENT_HEADER, html.HTML_CONTENT)
            self.end_headers()
            self.wfile.write(html.display("index").encode())
        else:
            self.send_response(html.RC_404)
            self.send_header(html.CONTENT_HEADER, html.HTML_CONTENT)
            self.end_headers()
            self.wfile.write(html.display("not_found").encode())

    def do_POST(self):
        if self.path.endswith("/query/run"):
            fields = self._get_form_params()
            query = fields.get("query")[0]
            database = fields.get("database")[0]
            db_file = helper.find_dbs().get(database)
            conn = sqlite.create_connection(db_file)
            results = sqlite.execute_query(conn, query)
            if isinstance(results, OperationalError):
                self.send_response(html.RC_200)
                self.send_header(html.CONTENT_HEADER, html.HTML_CONTENT)
                self.end_headers()
                out = html.display("index", content="query_err", results=results).encode()
                self.wfile.write(out)
            else:
                self.send_response(html.RC_200)
                self.send_header(html.CONTENT_HEADER, html.HTML_CONTENT)
                self.end_headers()
                out = html.display("rows", results=results).encode()
                self.wfile.write(out)
        else:
            self.send_response(html.RC_404)
            self.send_header(html.CONTENT_HEADER, html.HTML_CONTENT)
            self.end_headers()
            self.wfile.write(html.display("not_found").encode())

    def _get_form_params(self) -> dict:
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        content_len = int(self.headers.get('Content-length'))
        pdict['CONTENT-LENGTH'] = content_len
        if ctype == 'multipart/form-data':
            return cgi.parse_multipart(self.rfile, pdict)
        else:
            return {}


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), RequestHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()


if __name__ == '__main__':
    main()
