# 使用輕量級 Python
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 安裝 Flask (作為 API Server)
# 如果你需要 pandas, numpy, matplotlib 都在這裡加上
RUN pip install flask pandas numpy

# 複製 server 程式碼
COPY server.py .

# 暴露 Port
EXPOSE 8000

# 啟動 Server
CMD ["python", "server.py"]
