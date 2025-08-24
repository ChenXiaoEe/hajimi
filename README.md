# 👑 Hajimi King Project 👑

这是一个用于在 GitHub 上搜索 API 密钥的工具，由 ChenXiaoEe 进行维护和部署。

注意：本项目正处于beta期间，所以功能、结构、接口等等都有可能变化，不保证稳定性，请自行承担风险。

## 🚀 核心功能

1.  **GitHub代码搜索** 🔍 - 基于自定义查询表达式搜索 Gemini API 密钥。
2.  **代理支持** 🌐 - 支持通过代理进行访问，提高稳定性。
3.  **增量扫描** 📊 - 记录已扫描的文件，避免重复工作。
4.  **智能过滤** 🚫 - 自动过滤非代码文件，专注有效信息。
5.  **外部同步** 🔄 - 支持将密钥同步到其他密钥管理服务。

## 📋 目录

- [本地部署](#-本地部署)
- [Docker部署](#-docker部署)
- [配置变量说明](#-配置变量说明)

---

## 🖥️ 本地部署

### 1. 环境准备

```bash
# 确保已安装 Python 3.11+
python --version

# 安装 uv 包管理器
pip install uv
```

### 2. 项目设置

```bash
# 克隆项目
git clone https://github.com/ChenXiaoEe/hajimi.git
cd hajimi

# 复制配置文件
cp env.example .env
cp queries.example queries.txt
```

### 3. 配置环境变量

编辑 `.env` 文件，**必须**配置 GitHub Token：

```ini
# 必填：GitHub访问令牌，多个用逗号分隔
GITHUB_TOKENS=ghp_your_token1,ghp_your_token2
```

> 💡 **获取GitHub Token**：访问 [GitHub Settings > Tokens](https://github.com/settings/tokens)，创建具有 `public_repo` 权限的访问令牌。

### 4. 安装依赖并运行

```bash
# 安装项目依赖
uv pip install -r pyproject.toml

# 创建数据目录
mkdir -p data

# 运行程序
python app/hajimi_king.py
```

---

## 🐳 Docker 部署

本项目已配置好 `Dockerfile` 和 `docker-compose.yml`，可以轻松地通过 Docker 运行。

### 1. 准备配置文件

```bash
# 复制 .env 配置文件
cp env.example .env

# 复制查询文件
cp queries.example queries.txt

# 编辑 .env 文件，填入你的 GitHub Token
# GITHUB_TOKENS=ghp_your_token1,ghp_your_token2
```

### 2. 启动服务

使用 Docker Compose 构建并启动服务：

```bash
# 后台启动服务
docker compose up --build -d

# 查看实时日志
docker compose logs -f

# 停止服务
docker compose down
```

### 3. 部署到云平台 (如 ClawCloud)

1.  将本项目推送到您的 GitHub 仓库。
2.  在 ClawCloud 或其他 PaaS 平台上，创建一个新应用。
3.  连接到您的 GitHub 仓库。
4.  平台会自动检测 `Dockerfile` 并进行构建。
5.  **重要**: 在平台的 "环境变量" 设置中，添加您 `.env` 文件里的所有配置。
6.  启动部署。

---

## ⚙️ 配置变量说明

所有环境变量都可以在 `.env` 文件中进行配置。

### 🔴 必填配置

| 变量名 | 说明 | 示例值 |
|---|---|---|
| `GITHUB_TOKENS` | GitHub API访问令牌，多个用逗号分隔。 | `ghp_token1,ghp_token2` |

### 🟡 重要配置

| 变量名 | 默认值 | 说明 |
|---|---|---|
| `PROXY` | | 代理服务器地址，格式：`http://user:pass@proxy:port`。 |
| `DATA_PATH` | `/app/data` | 数据存储目录路径。 |
| `QUERIES_FILE` | `queries.txt` | 搜索查询配置文件路径。 |
| `HAJIMI_CHECK_MODEL` | `gemini-2.5-flash` | 用于验证Key有效的模型。 |

*(为简洁起见，其他可选配置请参考 `env.example` 文件)*

---

## 🔒 安全注意事项

-   ✅ GitHub Token 权限最小化（只需 `public_repo` 读取权限）。
-   ✅ 定期轮换 GitHub Token。
-   ✅ 不要在 Git 仓库中提交包含真实密钥的 `.env` 文件。
