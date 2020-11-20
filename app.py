from flask import Flask
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine, MetaData


# Set-up REST API
app = Flask(__name__)
rest = Api(app)

class Contact(Resource):
    def post(self):
        # Connect to DB
        engine = create_engine('sqlite:///database/internship.db')
        tables = MetaData()
        tables.reflect(bind=engine)
        tables = tables.tables
        conn = engine.connect()

        parser = reqparse.RequestParser(bundle_errors=True)

        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('subject', type=str, required=True)
        parser.add_argument('message', type=str, required=True)
        args = parser.parse_args()
        print(args)
        for field in args:
            if len(field) == 0:
                return 'Missing required arguments', 400

        conn.execute(tables['contact'].insert().values(name = args['name'].strip(), email = args['email'].strip().lower(),
                                                   subject = args['subject'].strip(), message = args['message'].strip()))
        return 201

rest.add_resource(Contact, '/contact')


# Serve Vue app statically
@app.route('/')
def main():
    return app.send_static_file('dist/index.html')


if __name__ == '__main__':
    app.run()
