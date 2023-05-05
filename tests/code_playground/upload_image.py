from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from src.controller.api_utils.user_content import UserContent
from src.controller.api_utils.user_network import UserNetwork


class UploadImage(Resource):
    def __init__(self, user_network: UserNetwork, user_content: UserContent):
        self.user_network: UserNetwork = user_network
        self.user_content: UserContent = user_content

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("file", type=FileStorage, location="files")
        args = parse.parse_args()
        image_file: FileStorage = args["file"]

        url = self.user_content._s3_upload_profile_image(
            "tgr-user-profile-us-west-0", "hoeli/test3.png", image_file
        )
        print(url)
        return url
