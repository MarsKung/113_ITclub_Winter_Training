# filepath: /workspaces/113_ITclub_Winter_Training/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY ./Path_traversal.py /app/Path_traversal.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "Path_traversal:app", "--host", "0.0.0.0", "--port", "80"]