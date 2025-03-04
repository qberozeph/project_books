from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/book_folks", tags=["frontend", "book_folks"])
async def get_html_book_folks():
    return FileResponse("templates/book_folks.html")

@router.get("/static/js/book_folks.js", tags=["frontend", "book_folks"])
async def get_js_book_folks():
    return FileResponse("static/js/book_folks.js")

@router.get("/static/css/book_folks.css", tags=["frontend", "book_folks"])
async def get_css_book_folks():
    return FileResponse("static/css/book_folks.css")

@router.get("/book_add", tags=["frontend", "book_add"])
async def get_html_book_add():
    return FileResponse("templates/book_add.html")

@router.get("/static/js/book_add.js", tags=["frontend", "book_add"])
async def get_js_book_add():
    return FileResponse("static/js/book_add.js")

@router.get("/static/css/book_add.css", tags=["frontend", "book_add"])
async def get_css_book_add():
    return FileResponse("static/css/book_add.css")