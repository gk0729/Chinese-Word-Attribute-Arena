"""
QwenPlayer 實現
使用阿里雲 Qwen API (DashScope SDK)
"""
from typing import List
import os
import logging

try:
    import dashscope
    from dashscope import Generation
    DASHSCOPE_AVAILABLE = True
except ImportError:
    DASHSCOPE_AVAILABLE = False
    logger = logging.getLogger(__name__)
    logger.warning("dashscope 模塊未安裝，QwenPlayer 將無法使用")

from ..player import AIPlayer

logger = logging.getLogger(__name__)


class QwenPlayer(AIPlayer):
    """通義千問 AI 玩家"""
    
    def __init__(self, name: str = "Qwen", model: str = "qwen-max"):
        """
        初始化 Qwen 玩家
        
        Args:
            name: 玩家名稱
            model: 模型名稱 (qwen-max, qwen-plus, qwen-turbo 等)
        """
        super().__init__(name, model)
        
        if not DASHSCOPE_AVAILABLE:
            raise ImportError("dashscope 模塊未安裝，請運行: pip install dashscope")
        
        # 設置 API Key
        api_key = self._get_api_key()
        dashscope.api_key = api_key
        
        logger.info(f"Qwen 玩家初始化完成: {name}")
    
    def _get_api_key(self) -> str:
        """
        獲取 DashScope API 密鑰
        
        Returns:
            str: API 密鑰
            
        Raises:
            ValueError: 如果環境變量未設置
        """
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            raise ValueError("DASHSCOPE_API_KEY 環境變量未設置")
        return api_key
    
    def answer_boolean_question(self, word: str, attribute: str) -> bool:
        """
        使用 Qwen 回答布林問題
        
        Args:
            word: 中文詞語
            attribute: 屬性描述
            
        Returns:
            bool: True 或 False
        """
        try:
            # 構造提示詞
            prompt = f"""請判斷中文詞語「{word}」是否具有以下屬性：

屬性：{attribute}

請只回答「是」或「否」，不要有其他內容。"""
            
            # 調用 API
            messages = [
                {"role": "system", "content": "你是一位中文語言學專家，擅長分析中文詞語的語言學屬性。"},
                {"role": "user", "content": prompt}
            ]
            
            response = Generation.call(
                model=self.model,
                messages=messages,
                result_format='message',
                temperature=0.3,
                max_tokens=10
            )
            
            # 檢查響應
            if response.status_code == 200:
                answer_text = response.output.choices[0].message.content.strip()
                
                # 判斷回答
                if "是" in answer_text or "yes" in answer_text.lower():
                    return True
                else:
                    return False
            else:
                logger.error(f"Qwen API 調用失敗: {response.message}")
                return False
                
        except Exception as e:
            logger.error(f"Qwen API 調用失敗: {e}")
            # 默認返回 False
            return False
    
    def propose_custom_attributes(self, word: str, num_slots: int = 8) -> List[str]:
        """
        使用 Qwen 提出自定義屬性
        
        Args:
            word: 中文詞語
            num_slots: 屬性數量
            
        Returns:
            List[str]: 屬性列表
        """
        try:
            # 構造提示詞
            prompt = f"""請為中文詞語「{word}」提出 {num_slots} 個有意義的語言學屬性。

要求：
1. 每個屬性應該是有價值的語言學特徵
2. 屬性應該具體、明確
3. 每行一個屬性，不要編號
4. 屬性名稱應包含「屬性」二字

示例格式：
音韻屬性_平仄特徵
構詞屬性_詞根來源
"""
            
            # 調用 API
            messages = [
                {"role": "system", "content": "你是一位中文語言學專家，擅長發現詞語的深層語言學屬性。"},
                {"role": "user", "content": prompt}
            ]
            
            response = Generation.call(
                model=self.model,
                messages=messages,
                result_format='message',
                temperature=0.7,
                max_tokens=500
            )
            
            # 檢查響應
            if response.status_code == 200:
                answer_text = response.output.choices[0].message.content.strip()
                
                # 提取屬性列表
                attributes = []
                for line in answer_text.split('\n'):
                    line = line.strip()
                    # 移除編號
                    if line and not line[0].isdigit():
                        attributes.append(line)
                    elif '.' in line or '、' in line:
                        # 移除數字編號
                        parts = line.split('.', 1) if '.' in line else line.split('、', 1)
                        if len(parts) > 1:
                            attributes.append(parts[1].strip())
                
                # 確保返回正確數量
                return attributes[:num_slots]
            else:
                logger.error(f"Qwen API 調用失敗: {response.message}")
                return []
            
        except Exception as e:
            logger.error(f"Qwen API 調用失敗: {e}")
            # 返回空列表
            return []
