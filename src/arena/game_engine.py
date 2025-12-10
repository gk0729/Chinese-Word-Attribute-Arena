"""
ArenaGame 遊戲引擎
管理遊戲流程和玩家對戰
"""
from typing import List, Dict, Any
import logging
from datetime import datetime
from tqdm import tqdm

from .player import AIPlayer
from .judge import RefereeAI

logger = logging.getLogger(__name__)


class ArenaGame:
    """競技場遊戲引擎"""
    
    def __init__(self, players: List[AIPlayer], referee: RefereeAI):
        """
        初始化遊戲
        
        Args:
            players: 玩家列表
            referee: 裁判實例
        """
        self.players = players
        self.referee = referee
        self.game_history = []
        self.current_round = 0
        
        logger.info(f"遊戲初始化完成，{len(players)} 位玩家參賽")
    
    def run_single_round(
        self, 
        word: str, 
        attributes: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        運行單輪遊戲
        
        Args:
            word: 測試詞語
            attributes: 屬性列表，每個屬性包含 name 和 description
            
        Returns:
            Dict: 本輪遊戲結果
        """
        self.current_round += 1
        round_results = {
            "round": self.current_round,
            "word": word,
            "timestamp": datetime.now().isoformat(),
            "player_results": []
        }
        
        logger.info(f"第 {self.current_round} 輪開始: {word}")
        
        # 每個玩家回答基礎屬性問題
        for player in self.players:
            player_result = {
                "player_name": player.name,
                "boolean_answers": [],
                "custom_attributes": [],
                "round_score": 0
            }
            
            # 回答基礎屬性問題
            for attr in attributes:
                attr_name = attr["name"]
                attr_desc = attr["description"]
                
                try:
                    # 玩家回答
                    answer = player.answer_boolean_question(word, attr_desc)
                    
                    # 裁判評判
                    judgment = self.referee.judge_boolean_question(
                        word, attr_name, answer
                    )
                    
                    # 記錄結果
                    player_result["boolean_answers"].append({
                        "attribute": attr_name,
                        "answer": answer,
                        "correct": judgment["correct"],
                        "score": judgment["score"]
                    })
                    
                    # 更新玩家狀態
                    player.record_answer(judgment["correct"])
                    player.update_score(judgment["score"])
                    player_result["round_score"] += judgment["score"]
                    
                except Exception as e:
                    logger.error(f"{player.name} 回答 {attr_name} 時出錯: {e}")
                    player_result["boolean_answers"].append({
                        "attribute": attr_name,
                        "error": str(e)
                    })
            
            # 玩家提出自定義屬性
            try:
                custom_attrs = player.propose_custom_attributes(word, num_slots=8)
                
                for custom_attr in custom_attrs:
                    # 評估自定義屬性
                    evaluation = self.referee.evaluate_custom_attribute(word, custom_attr)
                    
                    player_result["custom_attributes"].append({
                        "attribute": custom_attr,
                        "score": evaluation["score"]
                    })
                    
                    player.update_score(evaluation["score"])
                    player_result["round_score"] += evaluation["score"]
                    
            except Exception as e:
                logger.error(f"{player.name} 提出自定義屬性時出錯: {e}")
                player_result["custom_attributes_error"] = str(e)
            
            round_results["player_results"].append(player_result)
            logger.info(f"{player.name} 本輪得分: {player_result['round_score']}")
        
        self.game_history.append(round_results)
        return round_results
    
    def run_batch(
        self, 
        words: List[str], 
        attributes: List[Dict[str, str]], 
        num_rounds: int = None
    ) -> Dict[str, Any]:
        """
        運行多輪遊戲
        
        Args:
            words: 詞語列表
            attributes: 屬性列表
            num_rounds: 運行輪數（None 表示使用所有詞語）
            
        Returns:
            Dict: 遊戲總結果
        """
        if num_rounds is None:
            num_rounds = len(words)
        else:
            num_rounds = min(num_rounds, len(words))
        
        logger.info(f"開始批量遊戲: {num_rounds} 輪")
        
        # 使用進度條
        for i in tqdm(range(num_rounds), desc="遊戲進度"):
            word = words[i]
            self.run_single_round(word, attributes)
        
        # 生成最終結果
        final_results = self.get_final_results()
        return final_results
    
    def get_final_results(self) -> Dict[str, Any]:
        """獲取最終遊戲結果"""
        leaderboard = sorted(
            [player.get_stats() for player in self.players],
            key=lambda x: x["score"],
            reverse=True
        )
        
        results = {
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "total_rounds": self.current_round,
                "total_players": len(self.players)
            },
            "leaderboard": leaderboard,
            "game_history": self.game_history
        }
        
        logger.info("遊戲結束，生成最終結果")
        return results
    
    def print_leaderboard(self):
        """打印排行榜"""
        stats = sorted(
            [player.get_stats() for player in self.players],
            key=lambda x: x["score"],
            reverse=True
        )
        
        print("\n" + "=" * 60)
        print("最終排行榜".center(60))
        print("=" * 60)
        print(f"{'排名':<6} {'玩家':<15} {'模型':<20} {'分數':<8} {'準確率':<10}")
        print("-" * 60)
        
        for i, stat in enumerate(stats, 1):
            print(f"{i:<6} {stat['name']:<15} {stat['model']:<20} "
                  f"{stat['score']:<8} {stat['accuracy']:.2%}")
        
        print("=" * 60 + "\n")
