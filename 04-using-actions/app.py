from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"INFO": "Go to '/docs' endpoint"}