from fastapi import FastAPI
from controllers.generateTestController import generate_test_Controller
from controllers.evaluateTestController import evaluate_test_controller


app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "Pong"}

@app.post("/api/test/generate-test")
async def generate_test_endpoint(request_data: dict):
    return await generate_test_Controller(request_data)


@app.post("/api/test/evaluate-test")
async def evaluate_test_endpoint(request_data: dict):
    return await evaluate_test_controller(request_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
