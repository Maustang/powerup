def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['This is Ishant']
 
def app_factory(global_config, **local_config):
    return application
