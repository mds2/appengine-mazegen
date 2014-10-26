import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write ('<html> <head>')
        self.response.write ('<link rel="icon" href="statics/favicon.ico">')
        self.response.write ('</head><body>')
        if user:
            self.response.write ('<h2>Hello, ' + user.nickname() + '</h2>')
            self.response.write ('<p>From here, you can download ...')
            self.response.write ('<ul>')
            self.response.write ('<li><a href="large_maze.ps">a large maze</a>'
                                 '</li>')
            self.response.write ('<li><a href="huge_maze.ps">an even larger maze'
                                 '</a>'
                                 '</li>')
        else:
            self.response.write ('<h2>Hello</h2>')
            self.response.write ('<p><small>You can <a href="' +
                                 users.create_login_url(self.request.uri) +
                                 '">login</a>* to access larger mazes' +
                                 '</small></p>'
                )
            self.response.write ('<p>Or you can download ...<ul>')
        self.response.write ('<li><a href="medium_maze.ps">a medium maze</a>'
                             '</li>')
        self.response.write ('<li><a href="small_maze.ps">a small maze</a>'
                             '</li>')
        self.response.write ('</ul><br/>')
        self.response.write ('<p>(inspired by ')
        self.response.write ('<i><a '
                             'href="'
                             'http://www.ccs.neu.edu/home/shivers/mazes.html'
                             '" target="_blank">'
                             'http://www.ccs.neu.edu/home/shivers/mazes.html'
                             '</a></i>)</p>')
        self.response.write ('<p>Code available at '
                             '<a href="https://github.com/mds2/mazegen" '
                             'target="_blank">https://github.com/mds2/mazegen'
                             '</a>')
        if not user:
            self.response.write ('<br/><br/><p>* <small>'
                                 'I could, theoretically, record'
                                 ' which users had logged in to access large '
                                 'mazes.'
                                 ' So far I have been too lazy to write the '
                                 'code to do so</small></p>')
        self.response.write ('<hr/>')
        self.response.write ('<i><a href="http://mikeschuresko.blogspot.com/"'
                             ' target="_blank">'
                             'http://mikeschuresko.blogspot.com/'
                             '</a></i>')
        self.response.write ('</body></html>')


            

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

