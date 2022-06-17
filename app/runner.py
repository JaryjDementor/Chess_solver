from flask import Flask
from flask_restful import Api
from rest_views import Available_Moves, Validate_Move
from flask import Response

app = Flask(__name__)
api = Api()

api.add_resource(Available_Moves, "/api/v1/<string:figure>/<string:field>")

api.add_resource(
    Validate_Move, "/api/v1/<string:figure>/<string:field>/<string:dest_field>"
)

api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
