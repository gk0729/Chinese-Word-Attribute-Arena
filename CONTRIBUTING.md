# 貢獻指南 (Contributing Guide)

感謝您對「中文字詞屬性知識競技場」項目的關注！本項目遵循「先規劃，後編碼」的開發理念。

## 📋 開發理念

### 先規劃，後編碼 (Plan First, Code Later)

在開始編寫任何代碼之前，我們強烈建議：

1. **充分理解問題**：確保完全理解要解決的問題或要實現的功能
2. **設計方案**：在文檔中詳細描述技術方案和實現思路
3. **評審討論**：與團隊成員討論方案的可行性
4. **開始編碼**：只有在方案得到確認後才開始編碼

這種方式可以：
- ✅ 避免不必要的重構
- ✅ 提高代碼質量
- ✅ 促進團隊協作
- ✅ 減少開發時間浪費

詳細的規劃流程請參考 [DEVELOPMENT_WORKFLOW.md](./DEVELOPMENT_WORKFLOW.md)

## 🚀 快速開始

### 1. Fork 並克隆倉庫

```bash
git clone https://github.com/YOUR_USERNAME/Chinese-Word-Attribute-Arena.git
cd Chinese-Word-Attribute-Arena
```

### 2. 設置開發環境

```bash
# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 配置環境變量
cp .env.example .env
# 編輯 .env 文件，填入您的 API keys
```

### 3. 創建功能分支

```bash
git checkout -b feature/your-feature-name
```

## 📝 提交規範

### Commit 消息格式

使用清晰的 commit 消息：

```
<類型>: <簡短描述>

<詳細描述（可選）>

<相關 issue（可選）>
```

**類型**：
- `feat`: 新功能
- `fix`: 修復 bug
- `docs`: 文檔更新
- `style`: 代碼格式調整（不影響功能）
- `refactor`: 重構代碼
- `test`: 添加或修改測試
- `chore`: 構建過程或輔助工具的變動

**示例**：
```
feat: 添加 Claude-3 玩家支持

- 實現 Claude3Player 類
- 添加 API 配置
- 更新玩家工廠

Closes #123
```

## 🔧 開發流程

### 1. 創建規劃文檔

在 `Docs/` 目錄下創建詳細的設計文檔：

```markdown
# 功能名稱

## 背景
描述為什麼需要這個功能

## 目標
明確要達成的目標

## 技術方案
詳細的實現方案

## 測試計劃
如何驗證功能正常工作

## 時間估算
預計開發時間
```

### 2. 提交規劃 PR

- 創建一個 PR，只包含規劃文檔
- 標題前綴使用 `[PLAN]`
- 在 PR 中邀請團隊成員評審

### 3. 實現功能

規劃通過後，開始編碼：

- 遵循現有代碼風格
- 添加必要的註釋
- 編寫單元測試
- 更新相關文檔

### 4. 提交實現 PR

- 創建新的 PR 包含代碼實現
- 引用之前的規劃 PR
- 確保所有測試通過

## 🧪 測試

### 運行測試

```bash
# 運行所有測試（當測試套件完成後）
pytest

# 運行特定測試
pytest tests/test_specific.py
```

### 手動測試

```bash
# 運行遊戲進行手動測試
python src/main.py
```

## 📚 代碼風格

### Python 風格指南

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 規範
- 使用有意義的變量名和函數名
- 為複雜邏輯添加註釋
- 保持函數簡潔（建議不超過 50 行）

### 文檔字符串

為所有公共函數和類添加文檔字符串：

```python
def process_word_attributes(word: str, attributes: list) -> dict:
    """
    處理詞語屬性
    
    Args:
        word: 要處理的詞語
        attributes: 屬性列表
        
    Returns:
        包含處理結果的字典
        
    Raises:
        ValueError: 當詞語為空時
    """
    pass
```

## 🤝 Pull Request 流程

1. **創建 PR**：
   - 使用清晰的標題
   - 填寫完整的描述
   - 關聯相關 issue

2. **代碼評審**：
   - 至少需要一位維護者批准
   - 解決所有評審意見
   - 確保 CI 通過

3. **合併**：
   - 維護者會在評審通過後合併 PR
   - 使用 squash merge 保持提交歷史清晰

## 📋 Issue 規範

### 提交 Bug 報告

```markdown
**問題描述**
清晰描述遇到的問題

**重現步驟**
1. 執行 xxx
2. 輸入 xxx
3. 出現錯誤

**預期行為**
應該發生什麼

**實際行為**
實際發生了什麼

**環境信息**
- OS: Ubuntu 20.04
- Python: 3.9
- 版本: v2.0
```

### 提交功能請求

```markdown
**功能描述**
簡短描述想要的功能

**使用場景**
為什麼需要這個功能

**建議方案**
如果有想法，可以描述實現方式

**替代方案**
還考慮了哪些其他方案
```

## 🎯 優先級項目

當前項目的優先級開發任務：

1. **自動化測試套件** (高優先級)
2. **更多 AI 模型支持** (中優先級)
3. **Web 可視化界面** (中優先級)
4. **性能優化** (低優先級)

## 📞 聯繫方式

- 提交 Issue：[GitHub Issues](https://github.com/gk0729/Chinese-Word-Attribute-Arena/issues)
- 討論：[GitHub Discussions](https://github.com/gk0729/Chinese-Word-Attribute-Arena/discussions)

## 📜 行為準則

- 尊重所有貢獻者
- 保持友善和專業
- 歡迎建設性的批評
- 專注於問題本身，不要針對個人

## 🙏 致謝

感謝每一位貢獻者的付出！您的每一個 PR、Issue 和建議都讓這個項目變得更好。

---

**最後更新**：2025-12-10
