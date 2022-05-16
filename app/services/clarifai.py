import os

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

CLARIFAI_API_KEY = os.environ["CLARIFAI_API_KEY"]
PAT = os.environ["PAT"]
USER_ID = "aligulzar"
APP_ID = "local-recipe"
MODEL_ID = "bd367be194cf45149e75f01d59f77ba7"

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)
userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)


def get_ingredient_name(image_bytes):
    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(base64=image_bytes)
                    )
                )
            ],
        ),
        metadata=(("authorization", "Key " + PAT),),
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception(
            "Post model outputs failed, status: "
            + post_model_outputs_response.status.description
        )

    output = post_model_outputs_response.outputs[0]

    return output.data.concepts[0].name
