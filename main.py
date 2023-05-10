from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"Placeholder"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



    