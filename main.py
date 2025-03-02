from fastapi import FastAPI as FastAPI_Class
from fastapi.middleware.cors import CORSMiddleware

from routers.users import router as users_router
from routers.files import router as files_router

app = FastAPI_Class()

app.include_router(users_router)
app.include_router(files_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["http://localhost:8000"],
    allow_headers=["http://localhost:8000"],
)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="localhost", port=8000)