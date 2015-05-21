import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write ('<html> <head>')
        self.response.write ('<link rel="icon" href="statics/favicon.ico">')
        self.response.write ('</head><body>')
        self.response.write ('<h2>Online maze generation,</h2>')
        self.response.write ('<p>From here, you can download ...')
        self.response.write ('<ul>')
        self.response.write ('<li><a href="medium_maze.ps">a medium maze</a>'
                             '</li>')
        self.response.write ('<li><a href="small_maze.ps">a small maze</a>'
                             '</li>')
        self.response.write ('<li><a href="large_maze.ps">a large maze</a>'
                             '</li>')
        self.response.write ('<li><a href="huge_maze.ps">an even larger maze'
                             '</a>'
                             '</li>')
        self.response.write ('</ul><br/>')
        self.response.write ('</p><p>')
        self.response.write ('Note that downloading one of these mazes a second'
                             ' (or third, etc.) time will result in a different'
                             ' maze on each download.')
        self.response.write ('</p>')
        self.response.write ('<p>(inspired by ')
        self.response.write ('<i><a '
                             'href="'
                             'http://www.ccs.neu.edu/home/shivers/mazes.html'
                             '" target="_blank">'
                             'http://www.ccs.neu.edu/home/shivers/mazes.html'
                             '</a></i>)</p>')
        self.response.write ('<p>Basic code for maze generation available at '
                             '<a href="https://github.com/mds2/mazegen" '
                             'target="_blank">https://github.com/mds2/mazegen'
                             '</a></p>')
        self.response.write ('<p>Code to make this appengine page available at '
                             '<a href="https://github.com/mds2/appengine-mazegen'
                             '" target="_blank">'
                             'https://github.com/mds2/appengine-mazegen</a></p>')

        self.response.write ('<hr/>')
        self.response.write ('<i><a href="http://mikeschuresko.blogspot.com/"'
                             ' target="_blank">'
                             'http://mikeschuresko.blogspot.com/'
                             '</a></i>')
        self.response.write ('</body></html>')


            

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

