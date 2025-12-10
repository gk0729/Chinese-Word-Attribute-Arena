"""
中文字詞屬性知識競技場 - 主程序
"""
import os
import sys
import json
import yaml
import logging
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# 添加 src 目錄到 Python 路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from arena import (
    RefereeAI,
    ArenaGame,
    PlayerFactory,
    initialize_player_factory
)

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_config(config_path: str) -> dict:
    """載入配置文件"""
    logger.info(f"載入配置: {config_path}")
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_words(words_path: str) -> list:
    """載入測試詞表"""
    logger.info(f"載入詞表: {words_path}")
    with open(words_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
    logger.info(f"載入了 {len(words)} 個詞語")
    return words


def save_results(results: dict, output_path: str):
    """保存遊戲結果"""
    logger.info(f"保存結果: {output_path}")
    
    # 確保輸出目錄存在
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    logger.info("結果保存成功")


def main():
    """主程序"""
    logger.info("=" * 60)
    logger.info("中文字詞屬性知識競技場".center(60))
    logger.info("=" * 60)
    
    # 載入環境變量
    load_dotenv()
    logger.info("環境變量已載入")
    
    # 獲取項目根目錄
    project_root = Path(__file__).parent.parent
    
    # 定義文件路徑
    config_path = project_root / "config" / "players.yaml"
    words_path = project_root / "data" / "test_words.txt"
    attributes_path = project_root / "data" / "base_attributes.yaml"
    
    # 載入配置
    try:
        players_config = load_config(config_path)
        attributes_config = load_config(attributes_path)
        words = load_words(words_path)
    except FileNotFoundError as e:
        logger.error(f"配置文件不存在: {e}")
        return
    except Exception as e:
        logger.error(f"載入配置失敗: {e}")
        return
    
    # 初始化玩家工廠
    initialize_player_factory()
    
    # 創建玩家
    try:
        players = PlayerFactory.create_players(players_config["players"])
        
        if not players:
            logger.warning("未能創建任何玩家，嘗試創建默認團隊")
            players = PlayerFactory.create_default_chinese_team()
        
        if not players:
            logger.error("無法創建玩家，請檢查 API 密鑰配置")
            return
            
        logger.info(f"成功創建 {len(players)} 位玩家")
        
    except Exception as e:
        logger.error(f"創建玩家失敗: {e}")
        logger.info("嘗試繼續運行，但可能無法正常工作")
        return
    
    # 創建裁判
    referee = RefereeAI()
    
    # 創建遊戲
    game = ArenaGame(players=players, referee=referee)
    
    # 運行遊戲
    logger.info("\n開始遊戲！\n")
    
    try:
        results = game.run_batch(
            words=words,
            attributes=attributes_config["base_attributes"],
            num_rounds=len(words)
        )
        
        # 打印排行榜
        game.print_leaderboard()
        
        # 保存結果
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = project_root / "results"
        output_path = output_dir / f"game_results_{timestamp}.json"
        
        save_results(results, str(output_path))
        
        logger.info("=" * 60)
        logger.info("遊戲結束！".center(60))
        logger.info(f"結果已保存至: {output_path}")
        logger.info("=" * 60)
        
    except KeyboardInterrupt:
        logger.info("\n遊戲被用戶中斷")
    except Exception as e:
        logger.error(f"遊戲運行出錯: {e}", exc_info=True)


if __name__ == "__main__":
    main()
