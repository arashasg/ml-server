from mlserver import MLModel
from mlserver.types import InferenceRequest, InferenceResponse

class MyCustomRuntime(MLModel):

  async def load(self) -> bool:
    return True

  async def predict(self, payload: InferenceRequest) -> int:
    print("\n \n \n \n")
    print(payload)
    print("\n\n\n\n")
    return InferenceResponse(
      # Include any actual outputs from inference
      outputs=[],
      parameters=Parameters(headers={"foo": "bar"})
    )