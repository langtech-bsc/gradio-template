import os
from traceback import print_exc
import boto3
from handler import ContentHandler
from dotenv import load_dotenv

load_dotenv()

endpoint_name = os.environ.get("AWS_ENDPOINT_NAME")
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
aws_region_name = os.environ.get("AWS_REGION_NAME")

boto_client = boto3.client(
    service_name='sagemaker-runtime',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region_name)

content_handler = ContentHandler()

def invoke_endpoint(
        input_, 
        model_parameters,
    ):
    try:
        response = boto_client.invoke_endpoint(
                            EndpointName=endpoint_name,
                            ContentType='application/json', 
                            Body=content_handler.transform_input(prompt=input_, model_kwargs=model_parameters)
                    )
        return content_handler.transform_output(response['Body'])
    except:
        print_exc()
        return None