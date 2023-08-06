from base64 import b64encode
from logging import Logger
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, ParseResult
from simpleworkspace.logproviders import DummyLogger 

class SimpleServer(http.server.SimpleHTTPRequestHandler):
    """
    Class should always be derived

    Methods for the caller:
    - UseLogger()
    - UseAuthorization_Basic()
    - Start()

    Methods that may be overridden:
    - GetPage_Index()
    - OnRequest_Action()
    - GetPage_Custom()
    """

    class Exceptions:
        class StopRequest(Exception):
            pass

    logger = DummyLogger.GetLogger()
    _config_server_port = None
    _config_auth_basicCredentials = None

    @classmethod
    def Configure(cls, port: int):
        cls._config_server_port = port

    @classmethod
    def UseLogger(cls, logger: Logger):
        cls.logger = logger

    @classmethod
    def UseAuthorization_Basic(cls, username, password):
        """Uses http basic auth before any request is accepted, one of username or password can be left empty"""
        cls._config_auth_basicCredentials = "Basic " + b64encode(f"{username}:{password}".encode()).decode()

    # override, original writes to standard outputs, which fails if app is pyw
    def log_message(self, format, *args):
        """Log an arbitrary message.

        This is used by all other logging functions.  Override
        it if you have specific logging wishes.

        The first argument, FORMAT, is a format string for the
        message to be logged.  If the format string contains
        any % escapes requiring parameters, they should be
        specified as subsequent arguments (it's just like
        printf!).

        The client ip and current date/time are prefixed to
        every message.

        Unicode control characters are replaced with escaped hex
        before writing the output to stderr.

        """

        message = format % args
        self.logger.debug("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), message.translate(self._control_char_table)))

    def GetPage_Index(self):
        pass

    def GetPage_Custom(self, parsedUrl:ParseResult):
        '''triggers for all paths except empty path'''
        return NotImplemented

    def OnRequest_Action(self, action: str, data: str|None):
        '''a simple default action handler, triggers only when no path is supplied, eg only localhost/?action=123'''
        pass

    def SendResponse_Raw(self, data: str, statusCode=200, contentType="text/html", customHeaders: dict[str, str] = {}):
        self.send_response(statusCode)
        customHeaders["Content-type"] = contentType  # incase of duplicate, contentType param is preffered
        for key, value in customHeaders.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data.encode())
        pass

    def _Routine_BasicAuth(self):
        if self._config_auth_basicCredentials is None:
            # no auth configured
            return

        if self.headers.get("Authorization") == self._config_auth_basicCredentials:
            return

        self.SendResponse_Raw("Authorization required.", 401, customHeaders={"WWW-Authenticate": 'Basic realm="Login Required"'})
        raise self.Exceptions.StopRequest()

    def do_GET(self):
        try:
            self._Routine_BasicAuth()  # throws a stoprequest exception if not passed
            
            parsedUrl = urlparse(self.path)
            query_components = parse_qs(parsedUrl.query)
            if(parsedUrl.path == '/'):
                if(parsedUrl.query == ''):
                    self.GetPage_Index()
                elif "action" in query_components:
                    action = query_components["action"][0]
                    data = query_components['data'][0] if 'data' in query_components else None
                    self.OnRequest_Action(action, data)
            else:
                res = self.GetPage_Custom(parsedUrl)
                if(res == NotImplemented):
                    return self.SendResponse_Raw("Not Found", 404)

        except self.Exceptions.StopRequest:
            return  # a graceful request cancellation

    @classmethod
    def Start(cls):
        with socketserver.ThreadingTCPServer(("", cls._config_server_port), cls) as httpd:
            cls.logger.info(f"Server started at port {cls._config_server_port}")
            httpd.serve_forever()
        pass


# a = SimpleServer
# a.Configure(80)
# a.Start()