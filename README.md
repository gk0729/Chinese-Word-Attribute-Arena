＃中文字詞屬性知識競技場

**Chinese Word Attribute Arena**

一個創新的 AI 競技場系統，通過讓多個大語言模型相互競爭來標註中文字詞的語言屬性。

## ✨ 核心特性

- 🎮 **多 AI 競技**：DeepSeek、Qwen、GPT-4、Claude-3、Gemini-Pro 等同台競技
- 📊 **12 個基礎屬性**：結構化的屬性標註系統
- 🚀 **自填補充屬性**：發現詞海未涵蓋的新維度（+2/-2 高分值鼓勵）
- 📈 **數據雙格式**：JSON（外部接口）+ TOON（內部優化）
- 🔍 **自動評分裁判**：標準化的屬性推導和評分邏輯
- 💾 **完整數據保存**：遊戲日誌、排行榜、統計分析
- 🇨🇳 **中文優化**：默認使用 DeepSeek 和 Qwen，專為中文優化的模型

## 🎯 項目願景

通過遊戲化方式自動構建「中文詞語屬性本體庫」，最終為 NLP、認知科學和語言學研究提供高質量的標註數據。

## 🤖 支持的 AI 模型

### 默認中文團隊（推薦）

#### DeepSeek
- **模型**：deepseek-chat
- **優勢**：性價比極高，中文理解能力強，API 響應快
- **費用**：輸入 $0.14/M tokens，輸出 $0.28/M tokens
- **註冊**：[DeepSeek Platform](https://platform.deepseek.com/)
- **環境變量**：`DEEPSEEK_API_KEY`

#### 通義千問 (Qwen)
- **模型**：qwen-max, qwen-plus
- **優勢**：阿里雲開發，中文原生支持，語言學準確度高
- **費用**：qwen-max $2.00/M tokens，qwen-plus $0.50/M tokens
- **註冊**：[阿里雲 DashScope](https://dashscope.aliyun.com/)
- **環境變量**：`DASHSCOPE_API_KEY`

### 國際模型（可選）

#### GPT-4
- **模型**：gpt-4-turbo-preview
- **優勢**：綜合能力強，推理能力優秀
- **費用**：輸入 $10/M tokens，輸出 $30/M tokens
- **註冊**：[OpenAI Platform](https://platform.openai.com/)
- **環境變量**：`OPENAI_API_KEY`

### 成本估算

| 模型 | 20詞遊戲 | 100詞遊戲 | 1000詞遊戲 |
|------|---------|----------|-----------|
| DeepSeek | ~$0.01 | ~$0.05 | ~$0.50 |
| Qwen-Plus | ~$0.02 | ~$0.10 | ~$1.00 |
| Qwen-Max | ~$0.08 | ~$0.40 | ~$4.00 |
| GPT-4 | ~$0.40 | ~$2.00 | ~$20.00 |

*注：估算基於每詞約12個屬性判斷 + 8個自定義屬性提案*

## 🚀 快速開始

### 環境準備

```bash
# 1. 克隆倉庫
git clone https://github.com/gk0729/Chinese-Word-Attribute-Arena.git
cd Chinese-Word-Attribute-Arena

# 2. 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 配置 API 密鑰
# 複製環境變量模板
cp .env.example .env

# 編輯 .env 文件，填入您的 API keys
# 至少需要配置以下其中一個：
# - DEEPSEEK_API_KEY (推薦，性價比高)
# - DASHSCOPE_API_KEY (Qwen API，中文表現優秀)
# - OPENAI_API_KEY (可選)
```

### 運行遊戲

```bash
# 基礎運行（使用默認的 DeepSeek + Qwen 團隊）
python src/main.py

# 查看結果
cat results/game_results_*.json
```

## 📊 遊戲規則

### 基礎屬性問答（12個屬性）
- 每個詞語需要回答 12 個基礎屬性問題
- 正確回答得 1 分，錯誤回答得 0 分

### 自定義屬性提案（8個槽位）
- 每個詞語可以提出最多 8 個自定義屬性
- 有價值的新屬性可獲得額外分數
- 鼓勵發現詞典未涵蓋的語言學特徵

## 📊 數據格式

### JSON 格式（遊戲結果）
```json
{
  "metadata": {
    "timestamp": "2025-12-10T10:30:00",
    "total_rounds": 20,
    "total_players": 2
  },
  "leaderboard": [
    {
      "name": "DeepSeek",
      "model": "deepseek-chat",
      "score": 156,
      "accuracy": 0.85
    }
  ]
}
```

## 🏗️ 系統架構

```
Chinese-Word-Attribute-Arena/
├── src/
│   ├── arena/
│   │   ├── __init__.py
│   │   ├── player.py           # AI玩家基類
│   │   ├── judge.py            # 裁判系統
│   │   ├── game_engine.py      # 遊戲引擎
│   │   ├── player_factory.py   # 玩家工廠
│   │   └── players/
│   │       ├── deepseek_player.py
│   │       ├── qwen_player.py
│   │       └── gpt4_player.py
│   └── main.py                 # 主程序入口
├── config/
│   └── players.yaml            # 玩家配置
├── data/
│   ├── test_words.txt          # 測試詞表
│   └── base_attributes.yaml    # 基礎屬性
└── results/
    └── game_results_*.json     # 遊戲結果
```

## 📈 項目進度

### v2.0 (當前)
- ✅ 12 個基礎屬性勾選
- ✅ 自填補充屬性系統
- ✅ 完整的評分機制
- ✅ DeepSeek 玩家支持
- ✅ Qwen 玩家支持
- ✅ GPT-4 玩家支持
- ✅ 玩家工廠系統
- ✅ 遊戲引擎和裁判系統
- ⏳ 自動化測試套件
- ⏳ GitHub Actions CI/CD

### 未來規劃
- Web 可視化界面
- 更多 AI 模型支持（Claude、Gemini 等）
- 屬性知識庫優化
- 學術論文發布

## 🤝 貢獻

歡迎提交 Pull Request 和 Issue！

## ❓ 常見問題

### Q: 為什麼推薦使用 DeepSeek 和 Qwen？
A: 這兩個模型都是專為中文優化的，在中文語言學任務上表現優秀，且成本遠低於 GPT-4。DeepSeek 性價比極高，Qwen 由阿里雲開發，對中文理解深刻。

### Q: 可以添加自己的 AI 模型嗎？
A: 完全可以！繼承 `AIPlayer` 基類並實現相應方法即可。參考 `src/arena/players/` 中的實現。

### Q: 遊戲數據在哪裡？
A: 所有遊戲結果存儲在 `results/` 目錄中，使用 JSON 格式保存。

### Q: API 調用失敗怎麼辦？
A: 檢查以下幾點：
1. 確認 API Key 已正確配置在 `.env` 文件中
2. 確認 API 餘額充足
3. 檢查網絡連接是否正常
4. 查看日誌文件了解具體錯誤信息

## 📝 引用

如果您在研究中使用本項目，請引用：

```bibtex
@software{chinese_word_attribute_arena_2025,
  title={Chinese Word Attribute Arena: A Competitive Framework for Language Model Evaluation},
  author={gk0729},
  year={2025},
  url={https://github.com/gk0729/Chinese-Word-Attribute-Arena}
}
```

## 📄 許可證

本項目採用 MIT 許可證。詳見 [LICENSE](LICENSE)

## 👤 作者

**gk0729**
- GitHub: [@gk0729](https://gk0729)
- Email: your.email@example.com

## 🙏 致謝

感謝 DeepSeek、阿里雲（Qwen）、OpenAI 等提供的優秀 API 支持。

---

**最後更新**：2025-12-10  
**項目狀態**：🟢 Active Development
