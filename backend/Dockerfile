FROM python
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic
CMD ["python", "main.py"]