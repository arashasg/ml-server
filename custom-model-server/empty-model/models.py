from mlserver import MLModel
from mlserver.types import InferenceRequest, InferenceResponse

class MyCustomRuntime(MLModel):

  async def load(self) -> bool:
    return True

  async def predict(self, payload: InferenceRequest) -> InferenceResponse:
    return InferenceResponse(
      outputs=[1, 2, 3]
    )