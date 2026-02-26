from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "esta madre jala"