from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from daemon import runner
import sys

ip = sys.argv[1]
port = sys.argv[2]
ftpDir = sys.argv[3]

class FTP():
    def __init__(self, ip, port, ftpDir):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '$PREFIX/tmp/foo.pid'
        self.pidfile_timeout = 5
        self.ftpDir = ftpDir
        self.ip = ip
        self.port = port
    def run(self):

        authorizer = DummyAuthorizer()
        authorizer.add_anonymous(self.ftpDir, perm=('r', 'w'))
        handler = FTPHandler
        handler.authorizer = authorizer
        server = FTPServer(self.ip, self.port, handler)
        server.serve_forever()

app = FTP(ip, port, ftpDir)
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()