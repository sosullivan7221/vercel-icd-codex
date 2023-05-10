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

@app.get("/payer/{value}")
def payer(value):
    print("value: ", value)
    filtered = df[df["PAYER"] == value]
    if len(filtered) <= 0:
        return {"There is nothing here"}
    else:
        return filtered.to_json(orient="records")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



    