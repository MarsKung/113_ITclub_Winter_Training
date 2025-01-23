# 使用官方的 Python 基礎映像
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY . .

# 暴露應用程式運行的端口
EXPOSE 8787

# 啟動 FastAPI 應用程式
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8787"]