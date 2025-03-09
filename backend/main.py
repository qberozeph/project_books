from fastapi import FastAPI as FastAPI_Class
from fastapi.middleware.cors import CORSMiddleware
from routers.books import router as books_router

app = FastAPI_Class()
app.include_router(books_router)

# Настройка CORS для браузера
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)