from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/book_folks", tags=["frontend"])
async def get_html():
    return FileResponse("templates/book_folks.html")

@router.get("/static/js/book_folks.js", tags=["frontend"])
async def get_js():
    return FileResponse("static/js/book_folks.js")

@router.get("/static/css/book_folks.css", tags=["frontend"])
async def get_css():
    return FileResponse("static/css/book_folks.css")