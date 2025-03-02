from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse


app = FastAPI()

@app.post("/files")
async def upload_file(upload_file: UploadFile):
    file = upload_file.file
    filename = upload_file.filename
    with open(filename, "wb") as f:
        f.write(file.read())
    return {"message": "File uploaded"}

@app.post("/multiple_files")
async def upload_files(upload_files: list[UploadFile]):
    for upload_file in upload_files:
      file = upload_file.file
      filename = upload_file.filename
      with open(filename, "wb") as f:
          f.write(file.read())
    return {"message": "File uploaded"}

@app.get("/files/{filename}")
async def get_file(filename: str):
    return FileResponse(filename)

async def get_file_streaming(filename: str):
    with open(filename, "rb") as file:
        while chunk := file.read(1024*1024):
            yield chunk

@app.get("/files/streaming/{filename}")
async def get_file(filename: str):
    return StreamingResponse(get_file_streaming(filename), media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)