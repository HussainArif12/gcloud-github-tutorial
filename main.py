from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def say_hi():
    return {"message": "Hello!"}
