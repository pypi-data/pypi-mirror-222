import glob
import http.server as hs
import json
import os
import pathlib
import posixpath
import socket
import urllib.parse
import yaml
from http import HTTPStatus

initializer = """window.onload = function() {{
  //<editor-fold desc="Changeable Configuration Block">

  // the following lines will be replaced by docker/configurator, when it runs in a docker-container
  window.ui = SwaggerUIBundle({{
    urls: {urls},
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  }});

  //</editor-fold>
}};
"""

initializer_cache = None


class SwaggerRequestHandler(hs.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/swagger-initializer.js':
            return self.send_initializer()
        return super().do_GET()

    def send_initializer(self):
        global initializer_cache
        if not initializer_cache:
            docs = []
            for ext, loader in [('*.y*ml', yaml.safe_load), ('*.json', json.load)]:
                for path in glob.glob(os.path.join(self.directory, '**', ext), recursive=True):
                    with open(path, encoding='utf8') as f:
                        spec = loader(f)
                        rel_path = os.path.relpath(path, self.directory)
                        docs.append({
                            'name': spec['info']['title'],
                            'url': '/docs/' + pathlib.Path(rel_path).as_posix(),
                        })
            js = initializer.format(urls=json.dumps(docs))
            initializer_cache = bytes(js, "utf8")
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/javascript')
        self.send_header('Content-Length', str(len(initializer_cache)))
        self.end_headers()
        self.wfile.write(initializer_cache)

    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        docs = False
        if path.startswith('/docs/'):
            path = path.removeprefix('/docs')
            docs = True
        # abandon query parameters
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        # Don't forget explicit trailing slash when normalizing. Issue17324
        trailing_slash = path.rstrip().endswith('/')
        try:
            path = urllib.parse.unquote(path, errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)
        words = path.split('/')
        words = filter(None, words)
        path = self.directory if docs else os.path.join(os.path.dirname(__file__), 'ui')
        for word in words:
            if os.path.dirname(word) or word in (os.curdir, os.pardir):
                # Ignore components that are not a simple file/directory name
                continue
            path = os.path.join(path, word)
        if trailing_slash:
            path += '/'
        return path


def main():
    import argparse
    import contextlib

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', metavar='ADDRESS',
                        help='bind to this address '
                             '(default: all interfaces)')
    parser.add_argument('-d', '--directory', default=os.getcwd(),
                        help='serve this directory '
                             '(default: current directory)')
    parser.add_argument('-p', '--protocol', metavar='VERSION',
                        default='HTTP/1.0',
                        help='conform to this HTTP version '
                             '(default: %(default)s)')
    parser.add_argument('port', default=8000, type=int, nargs='?',
                        help='bind to this port '
                             '(default: %(default)s)')
    args = parser.parse_args()

    # ensure dual-stack is not disabled; ref #38907
    class DualStackServer(hs.ThreadingHTTPServer):

        def server_bind(self):
            # suppress exception when protocol is IPv4
            with contextlib.suppress(Exception):
                self.socket.setsockopt(
                    socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            return super().server_bind()

        def finish_request(self, request, client_address):
            self.RequestHandlerClass(request, client_address, self,
                                     directory=args.directory)

    hs.test(
        HandlerClass=SwaggerRequestHandler,
        ServerClass=DualStackServer,
        port=args.port,
        bind=args.bind,
        protocol=args.protocol,
    )


if __name__ == '__main__':
    main()
