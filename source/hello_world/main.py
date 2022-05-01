from fastapi import FastAPI

# Instantiate the App
app = FastAPI()

# Define a GET on the specified endpoint
@app.get("/")
async def say_hello():
    return {'greeting':"Hello World!"}