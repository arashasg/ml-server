from mlserver import MLModel
from mlserver.types import InferenceRequest, InferenceResponse

class MyCustomRuntime(MLModel):

  async def load(self) -> bool:
    return True

  async def predict(self, payload: InferenceRequest) -> int:
    print("\n \n \n \n")
    print(payload)
    print("\n\n\n\n")
    return 1 + 1