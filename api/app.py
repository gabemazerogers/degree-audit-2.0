import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.getcwd(), os.pardir), 'scrap')))
import main

import falcon
import routes

main.init()

api = application = falcon.API()

auth = routes.Auth()
courses = routes.Courses()

api.add_route('/auth/{username}/{password}', auth)
api.add_route('/courses/{token}/{group}', courses)
