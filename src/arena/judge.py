"""
RefereeAI 裁判類
負責評判玩家答案的正確性
"""
from typing import Dict, Any
import logging
import random

logger = logging.getLogger(__name__)


class RefereeAI:
    """裁判 AI，負責評判玩家答案"""
    
    def __init__(self, dictionary_path: str = None):
        """
        初始化裁判
        
        Args:
            dictionary_path: 詞典路徑（可選，暫未使用）
        """
        self.dictionary_path = dictionary_path
        logger.info("初始化裁判系統")
        
        # 簡化版：使用預定義的正確答案（實際應用中可以用更複雜的邏輯）
        self._initialize_knowledge_base()
    
    def _initialize_knowledge_base(self):
        """初始化知識庫（簡化版）"""
        # 這裡使用簡化的規則，實際應用中應該有更完善的知識庫
        # 為了演示，我們使用隨機判定加上一些基本規則
        self.knowledge_base = {}
        logger.debug("知識庫已初始化")
    
    def judge_boolean_question(
        self, 
        word: str, 
        attribute: str, 
        player_answer: bool
    ) -> Dict[str, Any]:
        """
        評判布林問題的答案
        
        Args:
            word: 中文詞語
            attribute: 屬性名稱
            player_answer: 玩家的答案
            
        Returns:
            Dict: 包含 correct (bool), score (int), reasoning (str)
        """
        # 簡化版評判邏輯
        # 實際應用中應該有更複雜的推理系統
        
        # 使用啟發式規則進行判斷
        correct_answer = self._evaluate_attribute(word, attribute)
        is_correct = (player_answer == correct_answer)
        
        # 評分規則
        score = 1 if is_correct else 0
        
        reasoning = self._generate_reasoning(word, attribute, correct_answer)
        
        result = {
            "correct": is_correct,
            "score": score,
            "reasoning": reasoning,
            "expected_answer": correct_answer
        }
        
        logger.debug(f"評判結果: {word} - {attribute} = {is_correct}")
        return result
    
    def _evaluate_attribute(self, word: str, attribute: str) -> bool:
        """
        評估詞語是否具有某個屬性（簡化版）
        
        實際應用中應該使用：
        1. 詞典查詢
        2. 語言學規則
        3. AI 模型推理
        4. 專家標註數據
        
        這裡使用簡化的啟發式規則
        """
        # 結構屬性判斷
        if "並列結構" in attribute:
            # 並列結構：如 "美醜"、"高低" 等對立詞
            parallel_words = ["快樂", "痛苦", "美麗", "醜陋", "高山", "平原", "時間", "空間", "知識", "智慧", "勇氣", "懦弱"]
            return word in parallel_words
        
        if "偏正結構" in attribute:
            # 偏正結構：如 "老師"、"醫生" 等
            modifier_words = ["老師", "醫生", "火焰", "水流", "星空", "大地"]
            return word in modifier_words
        
        # 語義屬性判斷
        if "具體性" in attribute:
            concrete_words = ["老師", "醫生", "火焰", "水流", "高山", "平原", "星空", "大地"]
            return word in concrete_words
        
        if "抽象性" in attribute:
            abstract_words = ["邏輯", "思想", "快樂", "痛苦", "美麗", "醜陋", "時間", "空間", "知識", "智慧", "勇氣", "懦弱"]
            return word in abstract_words
        
        # 語用屬性判斷
        if "正式度" in attribute:
            formal_words = ["老師", "醫生", "邏輯", "思想", "知識", "智慧"]
            return word in formal_words
        
        if "口語化" in attribute:
            colloquial_words = ["快樂", "痛苦", "美麗", "醜陋"]
            return word in colloquial_words
        
        # 情感屬性判斷
        if "褒義" in attribute:
            positive_words = ["老師", "醫生", "快樂", "美麗", "智慧", "勇氣"]
            return word in positive_words
        
        if "貶義" in attribute:
            negative_words = ["痛苦", "醜陋", "懦弱"]
            return word in negative_words
        
        # 認知屬性判斷
        if "高頻詞" in attribute:
            common_words = ["老師", "醫生", "快樂", "痛苦", "美麗", "時間", "空間", "知識"]
            return word in common_words
        
        if "專業詞" in attribute:
            professional_words = ["邏輯", "思想"]
            return word in professional_words
        
        # 文化屬性判斷
        if "象徵義" in attribute:
            symbolic_words = ["火焰", "水流", "高山", "星空", "大地"]
            return word in symbolic_words
        
        # 時態屬性判斷
        if "時代性" in attribute:
            # 大部分詞都沒有明顯時代特徵
            return False
        
        # 默認返回 False
        return False
    
    def _generate_reasoning(self, word: str, attribute: str, correct_answer: bool) -> str:
        """生成評判理由"""
        if correct_answer:
            return f"詞語「{word}」具有屬性「{attribute}」"
        else:
            return f"詞語「{word}」不具有屬性「{attribute}」"
    
    def evaluate_custom_attribute(self, word: str, attribute: str) -> Dict[str, Any]:
        """
        評估自定義屬性的質量
        
        Args:
            word: 中文詞語
            attribute: 自定義屬性
            
        Returns:
            Dict: 包含 score (int), feedback (str)
        """
        # 簡化版：根據屬性的新穎性和合理性評分
        # 實際應用中應該有更複雜的評估邏輯
        
        # 基礎分數
        score = 1
        
        # 檢查是否為有意義的屬性
        if len(attribute) > 3 and "屬性" in attribute:
            score += 1
        
        feedback = f"自定義屬性「{attribute}」評分: {score}"
        
        return {
            "score": score,
            "feedback": feedback
        }
