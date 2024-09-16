# GitHub 仓库导出和删除工具

这个 Python 脚本允许用户将其 GitHub 仓库导出到 JSON 文件，并与另一个仓库列表进行比较，以识别哪些仓库可以被删除。

## 功能

- 将指定 GitHub 用户的所有仓库导出到 JSON 文件。
- 从 JSON 文件导入仓库列表。
- 比较原始仓库列表与导入的列表，确定哪些仓库应被删除。
- 异步删除不需要的仓库，并控制 API 请求速率。

## 先决条件

- Python 3.7 或以上版本。
- 拥有必要权限的 GitHub API 令牌（需要有删除仓库的管理员权限）。
- 安装所需的 Python 包：

```bash
pip install PyGithub aiofiles aiohttp
```

## 配置

1. **GitHub 令牌**: 在脚本中替换为你的 GitHub 访问令牌：

   ```python
   GITHUB_TOKEN = "你的_github令牌"
   ```

   你可以通过 GitHub 设置中的 [Developer settings](https://github.com/settings/tokens) 创建一个新的令牌。确保它具有所需的权限。

2. **速率限制**: 脚本配置为以每分钟 40 次请求的速率删除仓库。如果需要，可以修改 `MAX_REQUESTS_PER_MINUTE` 常量。

## 使用方法

1. 将脚本保存到本地计算机，命名为 `github_repo_manager.py`。

2. 运行脚本：

   ```bash
   python github_repo_manager.py
   ```

3. 按照提示操作：

   - 输入你的 GitHub 用户名。
   - 脚本会将你的仓库导出到 `exported_repos.json` 文件。
   - 准备好包含你想要保留的仓库名称的 `imported_repos.json` 文件，然后按回车键。
   - 脚本会告知你将要删除的仓库，并提示确认操作。
   - 如果确认，指定的仓库将从你的 GitHub 账户中删除。

## 文件结构

- `exported_repos.json`: 自动生成的文件，包含导出的仓库名称。
- `imported_repos.json`: 由用户准备的文件，用于导入希望保留的仓库。

## 注意事项

- 使用此脚本时要小心，因为它会永久删除你在 GitHub 账户中的仓库。确保你有备份或确认这些删除操作是有意的。
- 脚本需要管理员访问权限才能执行删除操作。
- 请确保安全地处理你的 GitHub 令牌，避免公开暴露。

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。
# Statement

> [!CAUTION]  
> 本分支仅用于个人开发提供学习研究，请勿直接使用任何附件。如出现任何有关源附件问题，本作者概不负责。

---

> [!CAUTION]  
> This branch is only for personal development, study and research. Please do not use any attachments directly. The author is not responsible for any problems with the source attachments.
