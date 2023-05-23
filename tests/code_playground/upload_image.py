from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from src.model.data_access.user_content import UserContent
from src.model.data_access.user_network import UserNetwork

# Marshallow imports
from marshmallow import (
    Schema,
    fields,
    ValidationError,
)


class UploadImageValidator(Schema):
    image = fields.Raw(required=True, type="file")


class UploadImage(Resource):
    def __init__(self, user_network: UserNetwork, user_content: UserContent):
        self.user_network: UserNetwork = user_network
        self.user_content: UserContent = user_content

    def post(self):
        # UploadImageValidator().load()

        files = request.files.getlist("file")
        print(files)

        parse = reqparse.RequestParser()
        parse.add_argument("file", type=FileStorage, location="files")
        args = parse.parse_args()
        image_file: FileStorage = args["file"]
        # print(image_file.filename)
        # print(type(image_file))
        # url = self.user_content._s3_upload_profile_image(
        #     "tgr-user-profile-us-west-0", "hoeli/test3.png", image_file
        # )
        # print(url)
        # return url
