import requests

import numpy as np

from mlserver.types import InferenceRequest
from mlserver.codecs import NumpyCodec

x_0 = np.array([28.0])
inference_request = InferenceRequest(
    inputs=[
        NumpyCodec.encode_input(name="", payload=x_0)
    ]
)
res = requests.post("http://localhost:8080/v2/models/empty-model/infer", json=inference_request.dict()).json()
print(res)