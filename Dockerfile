FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "./app/AreYouLucky.py"]