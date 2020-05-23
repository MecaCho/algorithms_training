


# git操作

## 

## 提交信息规范：

build: 影响构建系统或外部依赖关系的更改（示例范围：gulp，broccoli，npm）
ci: 更改我们的持续集成文件和脚本（示例范围：Travis，Circle，BrowserStack，SauceLabs）
docs: 仅文档更改
feat: 一个新功能
fix: 修复错误
perf: 改进性能的代码更改
refactor: 代码更改，既不修复错误也不添加功能
style: 不影响代码含义的变化（空白，格式化，缺少分号等）
test: 添加缺失测试或更正现有测试


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