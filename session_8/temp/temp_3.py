import os
import pwd
import pam
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def pam_auth(username, password):
    try:
        return pam.authenticate(username, password, service='ftp')
    except pam.exception.PAMError:
        return False

class LocalUnixAuthorizer(UnixAuthorizer):
    def validate_authentication(self, username, password, handler):
        if pam_auth(username, password):
            return username
        return None

if __name__ == '__main__':
    # Set the FTP server parameters
    address = ('0.0.0.0', 21)  # Use 0.0.0.0 to listen on all available interfaces
    authorizer = LocalUnixAuthorizer()

    # Instantiate FTP handler and FTP server
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(address, handler)

    # Start the server
    server.serve_forever()
