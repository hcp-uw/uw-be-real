from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage


class UploadImage(Resource):
    def __init__(self, user_network, user_content):
        self.user_network = user_network
        self.user_content = user_content

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("file", type=FileStorage, location="files")
        args = parse.parse_args()
        image_file: FileStorage = args["file"]
        image_bytes = image_file.read()

        print(image_bytes)
        print(self.user_network)
        print(self.user_content)
