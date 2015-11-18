import cherrypy

class StaticAndDynamic(object):
    _cp_config = {'tools.staticdir.on' : True,
                  'tools.staticdir.dir' : '/home/coventry/bernie/outreach/gobernie',
                  'tools.staticdir.index' : 'index.html',
    }

    @cherrypy.expose
    def do_contact(self, **params):
        """Stuff to make a contact happen."""
        pass


cherrypy.quickstart(StaticAndDynamic())
