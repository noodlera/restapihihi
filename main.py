from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/echo/{msg}")
def echo(msg: str):
    return {"you_sent": msg}
