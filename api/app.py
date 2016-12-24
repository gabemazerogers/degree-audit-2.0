import falcon
import routes

api = application = falcon.API()

auth = routes.Auth()
courses = routes.Courses()

api.add_route('/auth/{username}/{password}', auth)
api.add_route('/courses/{token}/{group}', courses)
