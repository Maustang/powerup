from paste import deploy
import eventlet
from eventlet import wsgi


app = deploy.loadapp('config:/mnt/hgfs/pycharm/python/beats/etc/api-paste.ini',
                     name='beats')
wsgi.server(eventlet.listen(('',8888)), app)
