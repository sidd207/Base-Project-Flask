import os

ENV = os.environ.get('FLASK_ENV', 'development')

from commons.create_app import construct_flask_app
from flask_restx import Api

app = construct_flask_app()
config = app.config
api = Api(app)


from configurations import settings
from apis import routes

if __name__ == '__main__':
   app.run(debug=settings.DEBUG)