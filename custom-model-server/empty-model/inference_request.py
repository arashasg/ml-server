import requests

inference_request = {
    "inputs": [
        {
          "name": "args",
          "shape": [1],
          "datatype": "BYTES",
          "data": ["Hi, how are you doing?"],
        }
    ]
}

res = requests.post("http://localhost:8080/v2/models/empty-model2/infer", json=inference_request).json()
print(res)