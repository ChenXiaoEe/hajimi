# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装 uv
RUN pip install uv

# 使用 uv 安装依赖
RUN uv pip install --system --no-cache -r pyproject.toml

# 运行应用
CMD ["python", "-m", "app.hajimi_king"]
