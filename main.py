# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the the video")
video_put_args.add_argument("views", type=str, help="Views of the video")
video_put_args.add_argument("likes", type=str, help="Likes on the video")

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id ]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id:args}

api.add_resource(Video, "/video/<int:video_id>")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

