---
layout: post
title:  "Git基础"
date:   2017-10-29 22:53:59
categories: Git
---

# Git

Git是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。Git与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

echo "# CDNredirectTest" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add origingit@github.com:yourname/CDNredirectTest.git

git push -u origin master

工作和学习中经常用到git命令行，所以总结了一些比较常用的git命令行。
![git](assets/image/git/gitcmd.jpeg)

## init project

Command line instructions


Git global setup

git config --global user.name "wenqi"
git config --global user.email "wenqi@qq.com"

Create a new repository

git clone https://code.in.qq.com/devops/web-frontend.git
cd web-frontend
touch README.md
git add README.md
git commit -m "add README"

Existing folder

cd existing_folder
git init
git remote add origin https://code.in.qq.com/devops/web-frontend.git
git add .
git commit -m "Initial commit"

Existing Git repository

cd existing_repo
git remote rename origin old-origin
git remote add origin https://code.in.qq.com/devops/web-frontend.git

## git分支管理

- master

所有提供给用户使用的正式版本，都在这个主分支上发布。

- 开发分支Develop  

主分支只用来分布重大版本，日常开发应该在另一条分支上完成。我们把开发用的分支，叫做Develop。

# commit message

类型说明
类型代表某次提交的类型，⽐如是修复⼀个 bug 还是增加⼀个新的 feature
所有的类型如下：
- feature：新增 feature
- task：完成任务
- bugfix：修复 bug
- docs：仅仅修改了⽂档，⽐如 README, CHANGELOG, CONTRIBUTE 等等
- style：仅仅修改了空格、格式缩进、换⾏等等，不改变代码逻辑
- refactor：代码重构，没有加新功能或者修复 bug
- performance：优化相关，⽐如提升性能、体验
- test：测试⽤例，包括单元测试、集成测试等
- chore：改变构建流程、或者增加依赖库、⼯具等
- revert：回滚到上⼀个版本

## 修改提交历史作者信息

```bash
git rebase -i 6d2009
pick ----> edit
git commit --amend --author="xxxx@qq.com"
git rebase --continue
...
git push origin master
```

## 修改Commit的用户名与邮箱

注意： 只建议修改未 push 的 commit。
因为修改 Commit 的用户名或邮箱会生成一个新的 commit 来替换之前的 commit 。如果在修改之前已经 push 到了远端，修改后再次 push 会出现冲突。 只能使用 push -f。 如果其他人已经拉取（ pull ）了旧 commit 会出现很多麻烦。
只修改最新的 commit

如果你只需要修改最新的 commit ，直接使用：
git commit --amend --author="Author Name <email@address.com>"

如果你已经修改了 git config 中的用户名和邮箱，也可以使用
git commit --amend --reset-author --no-edit

## 打tag

```
git tag -a tag_name -m "comment...."

git tag tag_name

git log --pretty=oneline
git tag -a tag_name commit_id

git push origin tag_name
git push origin --tags
```

删除标签

```
git tag -d tag_name
git push origin --delete tag_name
(git push origin :refs/tags/tag_name)
```


## 撤销

### 撤销单个文件的修改

```
git log file_name
git reset $commit_id file_name
git checkout file_name
git commit --amend
git push ...
```
