from fastapi import FastAPI
import pandas as pd
import uvicorn

app = FastAPI()

df = pd.read_csv('./data/rxsummary_small2018.csv')

@app.get("/")
def home():
    return {"Placeholder"}

@app.get("/preview")
def preview():
    top1rows=df.head(1)
    result = top1rows.to_json(orient="records")
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



    