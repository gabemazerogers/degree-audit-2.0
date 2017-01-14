import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.getcwd(), os.pardir), 'scrap')))
import main

import falcon
from falcon_cors import CORS
import routes
import requests

ALLOWED_ORIGINS = ['http://localhost:3000', 'http://degree-audit-2.herokuapp.com']

# Taken from: http://hpincket.com/falcon-framework-cors-for-no-access-control-allow-origin.html
class CorsMiddleware(object):

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

main.init()

api = application = falcon.API(middleware=[CorsMiddleware()])

auth = routes.Auth()
courses = routes.Courses()

api.add_route('/auth/{username}/{password}', auth)
api.add_route('/courses/{token}/{group}', courses)
