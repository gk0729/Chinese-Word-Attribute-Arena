"""
AIPlayer 抽象基類
定義所有 AI 玩家的通用接口
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import os
import logging

logger = logging.getLogger(__name__)


class AIPlayer(ABC):
    """AI 玩家抽象基類"""
    
    def __init__(self, name: str, model: str):
        """
        初始化 AI 玩家
        
        Args:
            name: 玩家名稱
            model: 使用的模型名稱
        """
        self.name = name
        self.model = model
        self.score = 0
        self.correct_answers = 0
        self.total_answers = 0
        logger.info(f"初始化玩家: {name} (模型: {model})")
    
    @abstractmethod
    def answer_boolean_question(self, word: str, attribute: str) -> bool:
        """
        回答布林型問題（對錯題）
        
        Args:
            word: 中文詞語
            attribute: 屬性描述
            
        Returns:
            bool: True 表示該詞語具有該屬性，False 表示不具有
        """
        pass
    
    @abstractmethod
    def propose_custom_attributes(self, word: str, num_slots: int = 8) -> List[str]:
        """
        提出自定義屬性
        
        Args:
            word: 中文詞語
            num_slots: 可提出的屬性數量
            
        Returns:
            List[str]: 屬性列表
        """
        pass
    
    @abstractmethod
    def _get_api_key(self) -> str:
        """
        獲取 API 密鑰（從環境變量）
        
        Returns:
            str: API 密鑰
            
        Raises:
            ValueError: 如果 API 密鑰未設置
        """
        pass
    
    def update_score(self, points: int):
        """更新分數"""
        self.score += points
        logger.debug(f"{self.name} 得分 {points}，總分: {self.score}")
    
    def record_answer(self, is_correct: bool):
        """記錄答題結果"""
        self.total_answers += 1
        if is_correct:
            self.correct_answers += 1
    
    def get_accuracy(self) -> float:
        """計算準確率"""
        if self.total_answers == 0:
            return 0.0
        return self.correct_answers / self.total_answers
    
    def get_stats(self) -> Dict[str, Any]:
        """獲取玩家統計信息"""
        return {
            "name": self.name,
            "model": self.model,
            "score": self.score,
            "correct_answers": self.correct_answers,
            "total_answers": self.total_answers,
            "accuracy": self.get_accuracy()
        }
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, model={self.model}, score={self.score})"
