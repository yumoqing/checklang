---
name: checklang-repo
version: 1.0.0
description: checklang
trigger_conditions:
  - 需要理解、修改或排障 checklang 的代码
  - 在 checklang 里定位入口、数据表、对外契约或构建方式
---

# checklang 仓库技能

> 由仓库实际内容生成的骨架（README/目录/模型定义/契约/构建脚本逐项取证）。新增判断与坑位请直接在下面对应小节补充。

## 定位

**checklang**

- 远端：`https://github.com/yumoqing/checklang.git`
- 默认分支：`main`（共 6 个提交）
- 最近提交：2026-11-03 `2bd7f3c` chore: 忽略 init/logs 等生成物
- 规模：15 个文件；Python 3，Shell 1，JSON 1

## 目录结构

- `i18n/` — 多语言（`msg.txt` 逐行 `key: value` + `i18n.json`）（4 个文件）
- `checklang/` — Python 包源码（模块本体）（3 个文件）
- `app/` — 应用级初始化 / 菜单与页面装配（1 个文件）
- `conf/` — 配置（`config.json`；密码为 AES 密文）（1 个文件）
- `wwwroot/` — 前端页面与 `.dspy` 契约（服务端渲染入口）（1 个文件）
- 根文件：`.gitignore`、`MANIFEST.in`、`README.md`、`install.sh`、`pyproject.toml`

## 注册入口

- `checklang/init.py` → `load_checklang()`

## 代码入口（顶层 Python）

- `checklang/init.py` — 获取地球上主要人类语言列表

## 构建与运行

- `pyproject.toml`：`checklang` v0.1.0，依赖 4 项
- Python 包 `checklang/`：`__init__.py`、`init.py`

## README 要点与注意（摘自 `README.md`）

- 章节：Usage、Dependents

## 建议阅读顺序

1. `README.md`
2. `checklang/init.py`
3. `wwwroot/`

