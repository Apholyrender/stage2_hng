import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router as user_routers

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    )

app.include_router(user_routers)

if __name__ == "__main__":
    uvicorn.run(app = "main:app", port= 5000, reload=True) 