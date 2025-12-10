# 開發文檔索引 (Development Documentation Index)

歡迎！本文檔幫助您快速找到所需的開發資源。

## 📚 核心文檔

### 1. [README.md](../README.md)
**用途**: 項目概述和快速開始  
**適合**: 所有人，特別是新用戶  
**內容**:
- 項目介紹和特性
- 支持的 AI 模型
- 快速開始指南
- 使用示例

### 2. [CONTRIBUTING.md](../CONTRIBUTING.md) 
**用途**: 貢獻指南和規範  
**適合**: 準備貢獻代碼的開發者  
**內容**:
- 「先規劃，後編碼」理念
- 開發環境設置
- 提交規範和代碼風格
- Pull Request 流程
- Issue 提交規範

### 3. [DEVELOPMENT_WORKFLOW.md](../DEVELOPMENT_WORKFLOW.md)
**用途**: 詳細的開發工作流程  
**適合**: 開發新功能或修復 bug 的開發者  
**內容**:
- 為什麼要先規劃
- 7 個開發階段詳解：
  1. 需求分析
  2. 技術規劃
  3. 實現計劃
  4. 編碼實現
  5. 測試驗證
  6. 代碼評審
  7. 合併部署
- 每個階段的檢查清單
- 最佳實踐和常見問題

## 📝 模板文檔

### 4. [Feature Design Template](./feature_design_template.md)
**用途**: 功能設計文檔模板  
**適合**: 規劃新功能時使用  
**內容**:
- 14 個標準章節
- 從需求分析到批准記錄
- 完整的設計文檔結構

### 5. [Quick Reference](./QUICK_REFERENCE.md)
**用途**: 開發快速參考  
**適合**: 日常開發時快速查詢  
**內容**:
- 常用工作流程
- Commit 消息規範
- 常用命令
- 項目結構
- 開發原則

## 🎯 GitHub 模板

### 6. [Feature Planning Issue Template](../.github/ISSUE_TEMPLATE/feature_planning.md)
**用途**: 創建功能規劃 Issue  
**使用**: 在 GitHub 上創建新 Issue 時選擇此模板  
**內容**:
- 功能背景和動機
- 技術方案
- 實現計劃
- 風險評估
- 測試計劃

### 7. [Bug Report Issue Template](../.github/ISSUE_TEMPLATE/bug_report.md)
**用途**: 報告 Bug  
**使用**: 在 GitHub 上報告問題時選擇此模板  
**內容**:
- 問題描述
- 重現步驟
- 環境信息
- 預期和實際行為

### 8. [Pull Request Template](../.github/pull_request_template.md)
**用途**: 標準化的 PR 描述  
**使用**: 創建 Pull Request 時自動加載  
**內容**:
- PR 類型選擇
- 變更內容描述
- 測試說明
- 完整的檢查清單

## 🎓 學習路徑

### 新貢獻者
1. 閱讀 [README.md](../README.md) 了解項目
2. 閱讀 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解貢獻規範
3. 查看 [Quick Reference](./QUICK_REFERENCE.md) 了解常用操作
4. 開始貢獻！

### 開發新功能
1. 閱讀 [DEVELOPMENT_WORKFLOW.md](../DEVELOPMENT_WORKFLOW.md) 了解完整流程
2. 使用 [Feature Planning Template](../.github/ISSUE_TEMPLATE/feature_planning.md) 創建規劃 Issue
3. 使用 [Feature Design Template](./feature_design_template.md) 編寫設計文檔
4. 遵循工作流程實現功能
5. 使用 [Pull Request Template](../.github/pull_request_template.md) 提交 PR

### 修復 Bug
1. 使用 [Bug Report Template](../.github/ISSUE_TEMPLATE/bug_report.md) 報告問題
2. 參考 [Quick Reference](./QUICK_REFERENCE.md) 的 Bug 修復流程
3. 提交修復 PR

## 📋 文檔使用場景

| 場景 | 推薦文檔 |
|------|---------|
| 初次了解項目 | README.md |
| 準備開始貢獻 | CONTRIBUTING.md |
| 規劃新功能 | DEVELOPMENT_WORKFLOW.md + Feature Design Template |
| 日常開發查詢 | Quick Reference |
| 提交 Bug | Bug Report Template |
| 創建功能規劃 | Feature Planning Template |
| 提交代碼 | Pull Request Template |

## 🔍 快速查找

### 我想知道...

**如何設置開發環境？**  
→ [CONTRIBUTING.md](../CONTRIBUTING.md) 的「快速開始」章節

**Commit 消息怎麼寫？**  
→ [CONTRIBUTING.md](../CONTRIBUTING.md) 的「提交規範」章節  
→ [Quick Reference](./QUICK_REFERENCE.md) 的「Commit 消息規範」

**如何規劃一個新功能？**  
→ [DEVELOPMENT_WORKFLOW.md](../DEVELOPMENT_WORKFLOW.md) 的「階段 1-3」  
→ [Feature Design Template](./feature_design_template.md)

**代碼風格要求是什麼？**  
→ [CONTRIBUTING.md](../CONTRIBUTING.md) 的「代碼風格」章節

**如何提交 Pull Request？**  
→ [CONTRIBUTING.md](../CONTRIBUTING.md) 的「Pull Request 流程」  
→ [Pull Request Template](../.github/pull_request_template.md)

**開發流程是什麼？**  
→ [DEVELOPMENT_WORKFLOW.md](../DEVELOPMENT_WORKFLOW.md)

**常用 Git 命令有哪些？**  
→ [Quick Reference](./QUICK_REFERENCE.md) 的「常用命令」

## 💡 最佳實踐

1. **開始新任務前** - 先閱讀相關文檔
2. **規劃階段** - 使用提供的模板
3. **開發過程中** - 參考 Quick Reference
4. **提交前** - 檢查相關檢查清單

## 🔄 文檔更新

這些文檔會隨著項目發展持續更新。如果您發現：
- 文檔有錯誤
- 內容過時
- 需要補充

請：
1. 提交 Issue 說明問題
2. 或直接提交 PR 修正

## 📞 獲取幫助

如果文檔無法解答您的問題：

1. 查看 [GitHub Issues](https://github.com/gk0729/Chinese-Word-Attribute-Arena/issues)
2. 在 [GitHub Discussions](https://github.com/gk0729/Chinese-Word-Attribute-Arena/discussions) 提問
3. 提交新的 Issue

---

## 📊 文檔結構圖

```
中文字詞屬性知識競技場
│
├── README.md ─────────────────► 項目入口
│
├── 開發指南
│   ├── CONTRIBUTING.md ───────► 貢獻規範
│   ├── DEVELOPMENT_WORKFLOW.md ► 開發流程
│   └── Docs/templates/
│       ├── INDEX.md ──────────► 本文檔
│       ├── QUICK_REFERENCE.md ► 快速參考
│       └── feature_design_template.md ► 設計模板
│
└── GitHub 模板
    └── .github/
        ├── ISSUE_TEMPLATE/
        │   ├── feature_planning.md
        │   └── bug_report.md
        └── pull_request_template.md
```

## ⭐ 核心理念

> **先規劃，後編碼** (Plan First, Code Later)

在寫代碼前先思考：
- ✅ 減少返工
- ✅ 提高質量
- ✅ 促進協作
- ✅ 加速開發

---

**歡迎貢獻，共同建設更好的項目！**

**最後更新**: 2025-12-10
