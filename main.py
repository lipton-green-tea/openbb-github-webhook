from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/event_handler")
async def handle(request: Request):
    print(request.json())
    return {"status": "ok"}