# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

videos = {}

def abort_nonexisting_ids(video_id):
    if video_id not in videos:
        abort(404, message= "Could not find video...")

def abort_existing_ids(video_id):
    if video_id in videos:
        abort(409, message= "There is already an existing video with that id...")

class Video(Resource):
    def get(self, video_id):
        abort_nonexisting_ids(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_existing_ids(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 #send response that this video id was created

    def delete(self, video_id):
        abort_nonexisting_ids(video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

