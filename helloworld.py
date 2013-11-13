import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):

    def putFeedControlUI(self):
        self.response.write("<div> </div>")
        return

    def getStreamURLs(user):
        return ["http://mikeschuresko.blogspot.com/feeds/posts/default"]

    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
        if user.user_id () !=
            users.User("michael.schuresko@gmail.com").user_id():
            self.response.write('<br/><br/>'
                                'Currently this app only works for its author')
            return
        self.putFeedControlUI ()
        url_list = self.getStreamURLs(user)
        
        for url in url_list:
            

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

