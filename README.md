git学习笔记（https://www.cnblogs.com/dc-s/p/18857953)
什么是 Git？
Git 是一个版本控制系统，用于在软件开发过程中跟踪源代码的更改。它允许多个开发人员同时处理一个项目，而不会覆盖彼此的工作。

安装 Git
Windows / macOS / Linux：
从git-scm.com下载并安装 Git 。
验证安装：
git --version
初始配置
设置您的身份：

git config --global user.name "Your Name"
git config --global user.email "you@example.com"
查看您的配置：

git config --list
创建和克隆存储库
创建一个新的本地存储库：
mkdir my-project
cd my-project
git init
克隆现有存储库：
git clone https://github.com/username/repo-name.git
基本 Git 工作流程
检查状态：
git status
阶段文件：
git add filename     # Add specific file
git add .            # Add all changes
提交更改：
git commit -m "Meaningful commit message"
查看提交历史：
git log
git log --oneline
分支与合并
创建新分支：
git branch new-branch
切换到分支：
git checkout new-branch
一步创建并切换：
git checkout -b new-branch
合并分支：
git checkout main
git merge new-branch
删除分支：
git branch -d new-branch
使用远程存储库
添加遥控器：
git remote add origin https://github.com/username/repo.git
推送更改：
git push -u origin branch-name
拉取变更：
git pull origin branch-name
撤消更改
取消暂存文件：
git reset filename
撤消上次提交（保留更改）：
git reset --soft HEAD~1
放弃所有本地更改：
git checkout -- .
使用 .gitignore
创建一个.gitignore文件以将文件/文件夹排除在版本控制之外：

node_modules/
.env
dist/
*.log
高级 Git 命令
储藏变化：
git stash
应用隐藏的更改：
git stash apply
重新定基：
git rebase branch-name
挑选一个提交：
git cherry-pick commit-id
Git GUI 工具
GitHub 桌面
Sourcetree
GitKraken
VS Code 源代码控制面板
