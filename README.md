# 1. 建立 Image (假設叫 code-interpreter-img)
docker build -t code-interpreter-img .

# 2. 啟動長駐容器 (名字叫 python_interpreter，映射本地 8000 port)
docker run -d -p 8000:8000 --name python_interpreter code-interpreter-img
