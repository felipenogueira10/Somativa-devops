from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste1")
async def funcaoteste(true=None):
    return {"teste": true, "num_aleatorio": random.radint (0, 1000)}