FROM python:3.13
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cahce-d~ir -r requirements.txt
COPY . .
CMD ["python", "main.py"]