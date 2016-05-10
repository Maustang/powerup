import routes
import webob
import webob.dec

class BeatApp(object):
    map = routes.Mapper()
    map.connect('index', '/', method='index')
    map.connect('create', '/create/{name}', method='create')
    
    @webob.dec.wsgify
    def __call__(self, req):
        '''
        Glue.  A WSGI app is a callable; thus in order to make this object an application, 
        we define __call__ to make it callable.  We then ask our Mapper to do some routing,
        and dispatch to the appropriate method.  That method must return a webob.Response.
        '''
        results = self.map.routematch(environ=req.environ)
        if not results:
            return webob.exc.HTTPNotFound()
        match, route = results
        link = routes.URLGenerator(self.map, req.environ)
        req.urlvars = ((), match)
        kwargs = match.copy()
        method = kwargs.pop('method')
        req.link = link
        return getattr(self, method)(req, **kwargs)
    
    def index(self, req):
        return webob.Response(body="hello in index.")
    
    def create(self, req, name):
        return webob.Response(body="creating with name %s" % name)


def app_factory(global_config, **local_config):
    return BeatApp()
