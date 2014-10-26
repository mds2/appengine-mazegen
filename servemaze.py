import webapp2
from MazeGen import *
from time import gmtime, mktime
from google.appengine.api import memcache

from google.appengine.api import users

class ServeMaze(webapp2.RequestHandler):
    def width_and_height(self):
        return (45, 60)

    def build_maze(self):
        (w, h) = self.width_and_height ()
        self.gen = MazeGen(w, h)
        self.maze = self.gen.make_maze()
        self.render = MazeRender (self.maze)

    def get(self):
        user = users.get_current_user()
        self.response.headers['Content-Type'] = 'application/postscript'
        (w, h) = self.width_and_height ()
        self.build_maze ()
        ps = PsGen(w, h, self.response)
        self.render.spew(ps.process)
        ps.finish()

class ServeHugeMaze(ServeMaze):
    def width_and_height(self):
        return (60, 80)

class ServeLargeMaze(ServeMaze):
    def width_and_height(self):
        return (45, 60)

class ServeMediumMaze(ServeMaze):
    def width_and_height(self):
        return (27, 36)

class ServeSmallMaze(ServeMaze):
    def width_and_height(self):
        return (18, 24)


# TODO : Figure out what the code below means / does.
app = webapp2.WSGIApplication([('/huge_maze.ps', ServeHugeMaze),
                               ('/large_maze.ps', ServeLargeMaze),
                               ('/medium_maze.ps', ServeMediumMaze),
                               ('/small_maze.ps', ServeSmallMaze)],
                              debug=True)



