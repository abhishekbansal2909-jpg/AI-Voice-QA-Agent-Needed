from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
  return {"message": "The AI Voice Agent code is stored on Github!"}
