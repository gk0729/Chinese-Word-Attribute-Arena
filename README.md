# 中文二字詞屬性對齋競技場

**Chinese Word Attribute Arena - v2.0**

一個創新的 AI 競技場系統，通過讓多個大語言模型相互競爭來標註中文二字詞的語言屬性。

## ✨ 核心特性

- 🎮 **多 AI 競技**：GPT-4、Claude-3、Gemini-Pro 等同台競技
- 📊 **12 個基礎屬性**：結構化的屬性標註系統
- 🚀 **自填補充屬性**：發現詞海未涵蓋的新維度（+2/-2 高分值鼓勵）
- 📈 **數據雙格式**：JSON（外部接口）+ TOON（內部優化）
- 🔍 **自動評分裁判**：標準化的屬性推導和評分邏輯
- 💾 **完整數據保存**：遊戲日誌、排行榜、統計分析

## 🎯 項目願景

通過遊戲化方式自動構建「中文詞語屬性本體庫」，最終為 NLP、認知科學和語言學研究提供高質量的標註數據。

## 🚀 快速開始

### 環境準備

```bash
# 1. 克隆倉庫
git clone https://github.com/yourusername/chinese-word-attribute-arena.git
cd chinese-word-attribute-arena

# 2. 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 配置 API 密鑰
# 編輯 src/config.py，填入您的 API keys
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"
export GOOGLE_API_KEY="your-key"
```

### 運行遊戲

```bash
# 基礎運行
python src/main.py

# 自定義參數
python src/main.py --rounds 500 --players gpt-4 claude-3 gemini-pro --judge standard

# 查看幫助
python src/main.py --help
```

### 查看結果

```bash
# 轉換為 JSON 格式
python scripts/json_to_toon.py data/game-logs/2025-12-31.json

# 分析結果
python scripts/analyze_results.py --input data/game-logs/2025-12-31.json

# 生成報告
python scripts/generate_report.py --output REPORT.md
```

## 📊 數據格式

### JSON 格式（外部接口）
```json
{
  "metadata": {
    "timestamp": "2025-12-31T23:59:59",
    "version": "2.0"
  },
  "final_leaderboard": {
    "1st": {
      "name": "GPT-4",
      "total_score": 6250,
      "accuracy_rate": 0.848
    }
  }
}
```

### TOON 格式（內部優化）
```toon
@start GAME_RESULTS
  LEADERBOARD {
    rank_1 = {
      name: GPT-4
      total_score: 6250
      accuracy_rate: 0.848
    }
  }
@end GAME_RESULTS
```

詳見 [FORMAT_GUIDE.md](docs/FORMAT_GUIDE.md)

## 🏗️ 系統架構

```
外部系統 (API)
    ↓ JSON
    ↓
main.py (入口)
    ↓
game_engine.py
├─ word-corpus.toon (快速讀取)
├─ judge_ai.py (推導屬性)
└─ ai_player.py (AI 回答)
    ↓
data_manager.py
├─ results.json (標準格式)
└─ results.toon (內部優化)
    ↓ JSON
    ↓
外部系統 (API)
```

詳見 [ARCHITECTURE.md](docs/ARCHITECTURE.md)

## 📚 文檔

- [快速開始指南](docs/SETUP_GUIDE.md)
- [系統架構說明](docs/ARCHITECTURE.md)
- [數據格式對比](docs/FORMAT_GUIDE.md)
- [API 參考](docs/API_REFERENCE.md)
- [數據模式定義](docs/DATA_SCHEMA.md)
- [使用示例](docs/EXAMPLES.md)

## 📈 項目進度

### v2.0 (當前)
- ✅ 12 個基礎屬性勾選
- ✅ 自填補充屬性系統
- ✅ JSON + TOON 雙格式支持
- ✅ 完整的評分機制
- ⏳ 自動化測試套件
- ⏳ GitHub Actions CI/CD

### 未來規劃
- 中文原生格式優化
- 屬性資源庫動態擴展
- Web 可視化界面
- 學術論文發布

## 🤝 貢獻

歡迎 PR 和 Issue！詳見 [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 引用

如果您在研究中使用本項目，請引用：

```bibtex
@software{chinese_word_attribute_arena_2025,
  title={Chinese Word Attribute Arena: A Competitive Framework for Language Model Evaluation},
  author={Your Name},
  year={2025},
  url={https://github.com/yourusername/chinese-word-attribute-arena}
}
```

## 📄 許可證

本項目採用 MIT 許可證。詳見 [LICENSE](LICENSE)

## 👤 作者

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 致謝

感謝 OpenAI、Anthropic、Google 提供的 API 支持。

---

## ❓ 常見問題

### Q: 為什麼要用 TOON 格式？
A: TOON 格式相比 JSON 體積更小、解析更快，特別適合內部運行。外部接口仍然使用通用的 JSON 格式。

### Q: 可以添加自己的 AI 模型嗎？
A: 完全可以！詳見 [examples/custom_ai_player.py](examples/custom_ai_player.py)

### Q: 遊戲數據在哪裡？
A: 所有遊戲結果存儲在 `data/game-logs/` 中，分別提供 JSON 和 TOON 格式。

---

**最後更新**：2025-12-09  
**項目狀態**：🟢 Active Development
