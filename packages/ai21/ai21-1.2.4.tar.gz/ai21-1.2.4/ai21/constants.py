DEFAULT_API_VERSION = 'v1'
STUDIO_HOST = 'https://api.ai21.com'

SAGEMAKER_ENDPOINT_KEY = 'sm_endpoint'
DESTINATION_KEY = 'destination'
BEDROCK_HOST_FORMAT = 'bedrock.{region_name}.amazonaws.com'
BEDROCK_URL_FORMAT = f'https://{BEDROCK_HOST_FORMAT}'

SAGEMAKER_MODEL_PACKAGE_NAMES = [
    'j2-light',
    'j2-mid',
    'j2-ultra',
    'gec',
    'contextual-answers',
    'paraphrase',
    'summarize',
]