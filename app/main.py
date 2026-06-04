
from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="FastAPI CRUD App")

# Root endpoint
@app.get("/getrequest")
async def get_request():
    return "Hihi"

# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
