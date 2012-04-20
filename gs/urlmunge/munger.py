# coding=utf-8
from repoze.vhm.utils import setServerURL

class MungeServerUrl(object):

    def __init__(self, wrap_app):
        self.wrap_app = wrap_app
    
    def __call__(self, environ, start_response):
        setServerURL(environ)
        retval = self.wrap_app(environ, start_response)
        return retval

def make_munger(app, global_conf):
    retval = MungeServerUrl(app)
    return retval

