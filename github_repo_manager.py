import os
import json
import asyncio
import aiofiles
from github import Github

# 配置 GitHub 访问令牌
GITHUB_TOKEN = "Your Token Here"
g = Github(GITHUB_TOKEN)

# 设置每分钟最大请求次数（即每个仓库删除的速率）
MAX_REQUESTS_PER_MINUTE = 40
REQUEST_INTERVAL = 60 / MAX_REQUESTS_PER_MINUTE  # 每个请求的间隔（秒）


async def export_repositories(username):
    """异步导出用户的所有仓库名称到一个 JSON 文件"""
    user = g.get_user(username)
    repos = user.get_repos()

    repo_names = [repo.name for repo in repos]

    async with aiofiles.open("exported_repos.json", "w") as f:
        await f.write(json.dumps(repo_names, indent=4))

    print(f"已导出 {len(repo_names)} 个仓库名称到 'exported_repos.json' 文件.")


async def import_repositories(file_path):
    """异步从 JSON 文件中导入仓库名称"""
    async with aiofiles.open(file_path, "r") as f:
        content = await f.read()
        repos = json.loads(content)
    print("导入的仓库名称：", repos)  # 打印导入的仓库名称
    return repos


def compare_repositories(original, imported):
    """比较原始和导入的仓库名称，返回要删除的仓库名称列表"""
    return [repo for repo in original if repo not in imported]


async def delete_repository(username, repo_name):
    """异步删除指定的仓库，并控制请求速率"""
    user = g.get_user(username)
    try:
        repo = user.get_repo(repo_name)
        repo.delete()
        print(f"已删除仓库: {repo_name}")
    except Exception as e:
        print(f"删除仓库 {repo_name} 时出错: {e}")
        if "Must have admin rights" in str(e):
            print(f"您没有权限删除仓库 {repo_name}。 请检查您的权限。")
        elif "404 Not Found" in str(e):
            print(f"仓库 {repo_name} 找不到，请确认名称是否正确。")
        else:
            print(f"其他错误: {e}")

    await asyncio.sleep(REQUEST_INTERVAL)  # 等待请求间隔


async def delete_repositories(username, repos_to_delete):
    """异步删除仓库列表"""
    await asyncio.gather(
        *(delete_repository(username, repo_name) for repo_name in repos_to_delete)
    )


async def main():
    username = input("请输入您的 GitHub 用户名: ")

    # 导出仓库名称到 JSON 文件
    await export_repositories(username)

    input("请准备好要导入的 'imported_repos.json' 文件，完成后按回车继续...")

    # 导入仓库名称
    imported_repos = await import_repositories("imported_repos.json")

    # 获取原始仓库名称并比较
    original_repos = await import_repositories("exported_repos.json")
    repos_to_delete = compare_repositories(original_repos, imported_repos)

    if repos_to_delete:
        print(f"以下仓库将在 GitHub 上被删除: {repos_to_delete}")
        confirm = input("确认删除这些仓库吗? (y/n): ")
        if confirm.lower() == "y":
            await delete_repositories(username, repos_to_delete)
        else:
            print("操作已取消.")
    else:
        print("没有需要删除的仓库.")


if __name__ == "__main__":
    asyncio.run(main())
