import string

def generate_prefixes():
    """
    生成8位精确前缀 (AIzaSy[A-Z][0-9])
    """
    prefixes = []
    # 第7位是A-Z
    for char7 in string.ascii_uppercase:
        # 第8位是A-Z或0-9
        for char8 in string.ascii_uppercase + string.digits:
            prefixes.append(f"AIzaSy{char7}{char8}")
    return prefixes

def generate_queries():
    """
    生成最终的GitHub搜索查询列表
    """
    queries = []
    prefixes = generate_prefixes()
    
    # 策略1: 仅使用前缀进行精确搜索
    # 使用引号确保精确匹配
    for prefix in prefixes:
        queries.append(f'"{prefix}" in:file')
        
    # 策略2: 结合常见文件名 (可以根据需要扩展)
    common_filenames = [
        "config", "settings", "prod", "dev", "env", "secret", "key"
    ]
    for prefix in prefixes:
        for filename in common_filenames:
            queries.append(f'"{prefix}" in:file filename:{filename}')

    # 策略3: 结合常见文件扩展名
    common_extensions = [
        "json", "yaml", "yml", "env", "ini", "conf", "py", "js", "go", "java", "log", "txt"
    ]
    for prefix in prefixes:
        for ext in common_extensions:
            queries.append(f'"{prefix}" in:file extension:{ext}')
            
    return list(set(queries)) # 去重

def save_queries_to_file(queries, filepath="../data/queries.txt"):
    """
    将查询列表保存到文件
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("# GitHub搜索查询配置文件 (由 rule_generator.py 生成)\n")
            f.write("# 每行一个查询语句，支持GitHub搜索语法\n")
            f.write("# 以#开头的行为注释，空行会被忽略\n\n")
            for query in sorted(queries):
                f.write(query + "\n")
        print(f"✅ 成功生成 {len(queries)} 条查询规则到 {filepath}")
    except IOError as e:
        print(f"❌ 写入文件时出错: {e}")

if __name__ == "__main__":
    generated_queries = generate_queries()
    # 注意: 脚本在utils目录下，所以queries.txt的路径是../queries.txt
    save_queries_to_file(generated_queries)
