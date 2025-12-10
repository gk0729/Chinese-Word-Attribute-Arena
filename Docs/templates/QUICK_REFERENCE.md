# 開發快速參考 (Quick Development Reference)

快速查找開發過程中需要的信息。

## 📚 文檔索引

| 文檔 | 用途 | 適用場景 |
|------|------|----------|
| [README.md](../README.md) | 項目概述和快速開始 | 初次了解項目 |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | 貢獻指南 | 準備貢獻代碼 |
| [DEVELOPMENT_WORKFLOW.md](../DEVELOPMENT_WORKFLOW.md) | 詳細開發流程 | 開發新功能或修復 bug |
| [Feature Design Template](./feature_design_template.md) | 功能設計模板 | 規劃新功能 |

## 🚀 常用工作流程

### 開發新功能

```bash
# 1. 創建規劃分支
git checkout -b design/feature-name

# 2. 複製模板創建設計文檔
cp Docs/templates/feature_design_template.md Docs/feature-name-design.md

# 3. 編寫設計文檔
# 編輯 Docs/feature-name-design.md

# 4. 提交設計 PR
git add Docs/feature-name-design.md
git commit -m "docs: 添加 [功能名稱] 設計文檔"
git push origin design/feature-name

# 5. 創建 PR，等待評審
# 訪問 GitHub 創建標題為 "[DESIGN] 功能名稱" 的 PR

# 6. 設計通過後，創建實現分支
git checkout main
git pull
git checkout -b feature/feature-name

# 7. 實現功能
# 編寫代碼...

# 8. 運行測試
pytest tests/

# 9. 提交實現 PR
git add .
git commit -m "feat: 實現 XXX 功能"
git push origin feature/feature-name
```

### 修復 Bug

```bash
# 1. 創建 bug 修復分支
git checkout -b fix/bug-description

# 2. 修復 bug
# 編輯代碼...

# 3. 添加測試
# 編寫測試確保 bug 被修復...

# 4. 運行測試
pytest tests/

# 5. 提交
git add .
git commit -m "fix: 修復 XXX 問題"
git push origin fix/bug-description
```

### 更新文檔

```bash
# 1. 創建文檔更新分支
git checkout -b docs/update-description

# 2. 更新文檔
# 編輯文檔...

# 3. 提交
git add docs/
git commit -m "docs: 更新 XXX 文檔"
git push origin docs/update-description
```

## 📝 Commit 消息規範

### 格式
```
<類型>: <簡短描述>

[可選的詳細描述]

[可選的 issue 引用]
```

### 類型

| 類型 | 說明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: 添加 Claude-3 玩家支持` |
| `fix` | Bug 修復 | `fix: 修復玩家初始化錯誤` |
| `docs` | 文檔更新 | `docs: 更新 API 文檔` |
| `style` | 代碼格式 | `style: 統一代碼縮進` |
| `refactor` | 重構 | `refactor: 重構玩家工廠邏輯` |
| `test` | 測試 | `test: 添加裁判系統測試` |
| `chore` | 構建/工具 | `chore: 更新依賴版本` |
| `perf` | 性能優化 | `perf: 優化屬性匹配算法` |

### 示例

```bash
# 好的 commit 消息
git commit -m "feat: 添加騰訊混元模型支持

- 實現 HunyuanPlayer 類
- 添加 API 配置
- 更新玩家工廠

Closes #123"

# 簡單的 commit
git commit -m "fix: 修復配置文件路徑錯誤"

# 不好的 commit 消息（避免）
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

## 🔧 常用命令

### 環境設置

```bash
# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 配置環境變量
cp .env.example .env
# 編輯 .env 文件
```

### 運行和測試

```bash
# 運行主程序
python src/main.py

# 使用特定配置
python src/main.py --config config/blood_awakening.yaml

# 運行測試（未來）
pytest
pytest tests/test_specific.py
pytest -v  # 詳細輸出
pytest --cov  # 帶覆蓋率

# 代碼格式化（未來）
black src/
flake8 src/
```

### Git 操作

```bash
# 查看狀態
git status

# 查看差異
git diff
git diff --staged

# 暫存變更
git add file.py
git add .

# 提交
git commit -m "type: message"

# 查看歷史
git log --oneline -10
git log --graph --oneline

# 同步遠程
git pull origin main
git push origin branch-name

# 分支操作
git branch                    # 查看分支
git checkout -b new-branch    # 創建並切換
git checkout branch-name      # 切換分支
git branch -d branch-name     # 刪除分支
```

## 🧪 測試清單

### 代碼提交前檢查

- [ ] 代碼遵循 PEP 8 規範
- [ ] 所有新函數都有文檔字符串
- [ ] 添加了必要的測試
- [ ] 所有測試通過
- [ ] 沒有遺留 debug 代碼
- [ ] 更新了相關文檔
- [ ] Commit 消息清晰

### PR 提交前檢查

- [ ] 所有 commits 都有意義
- [ ] PR 描述完整
- [ ] 關聯了相關 issue
- [ ] 填寫了 PR 模板
- [ ] 通過了自我代碼評審
- [ ] 沒有不相關的文件變更

## 📂 項目結構

```
Chinese-Word-Attribute-Arena/
├── .github/                    # GitHub 相關配置
│   ├── ISSUE_TEMPLATE/        # Issue 模板
│   └── pull_request_template.md
├── config/                     # 配置文件
│   ├── players.yaml
│   └── blood_awakening.yaml
├── data/                       # 數據文件
│   ├── test_words.txt
│   └── base_attributes.yaml
├── Docs/                       # 文檔
│   ├── templates/             # 文檔模板
│   └── [各種設計文檔]
├── src/                        # 源代碼
│   ├── arena/                 # 競技場核心
│   │   ├── players/          # 玩家實現
│   │   ├── game_engine.py
│   │   ├── judge.py
│   │   └── player_factory.py
│   └── main.py
├── tests/                      # 測試（未來）
├── results/                    # 遊戲結果
├── CONTRIBUTING.md            # 貢獻指南
├── DEVELOPMENT_WORKFLOW.md   # 開發流程
├── README.md                  # 項目說明
└── requirements.txt           # Python 依賴
```

## 🎯 開發原則

### 核心原則

1. **先規劃，後編碼** - 在寫代碼前先設計
2. **小步快跑** - 頻繁提交，增量開發
3. **測試驅動** - 先寫測試，再寫實現
4. **代碼質量** - 保持代碼整潔和可維護
5. **團隊協作** - 積極溝通，相互評審

### 代碼質量標準

- **可讀性** > 簡潔性 > 性能
- 函數長度 < 50 行
- 嵌套深度 < 4 層
- 每個函數只做一件事
- 使用有意義的命名

## 💬 獲取幫助

遇到問題時：

1. 📖 **查看文檔** - 先檢查相關文檔
2. 🔍 **搜索 Issues** - 看是否有類似問題
3. 💭 **提問** - 在 GitHub Discussions 提問
4. 🐛 **報告 Bug** - 使用 Bug Report 模板
5. 💡 **建議功能** - 使用 Feature Planning 模板

## 🔗 有用的鏈接

- [GitHub Repository](https://github.com/gk0729/Chinese-Word-Attribute-Arena)
- [Issues](https://github.com/gk0729/Chinese-Word-Attribute-Arena/issues)
- [Pull Requests](https://github.com/gk0729/Chinese-Word-Attribute-Arena/pulls)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

**快速提示**: 如果您是新貢獻者，建議從小的改進開始，比如：
- 修復文檔中的錯別字
- 改進代碼註釋
- 添加測試用例
- 優化錯誤消息

**最後更新**: 2025-12-10
