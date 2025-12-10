"""
HunyuanPlayer 實現
使用騰訊雲混元大模型 API
"""
from typing import List
import os
import logging

from ..player import AIPlayer

logger = logging.getLogger(__name__)

try:
    from tencentcloud.common import credential
    from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
    HUNYUAN_AVAILABLE = True
except ImportError:
    HUNYUAN_AVAILABLE = False
    logger.warning("tencentcloud-sdk-python-hunyuan 模塊未安裝，HunyuanPlayer 將無法使用")


class HunyuanPlayer(AIPlayer):
    """騰訊混元 AI 玩家"""
    
    def __init__(self, name: str = "Hunyuan", model: str = "hunyuan-turbo"):
        """
        初始化 Hunyuan 玩家
        
        Args:
            name: 玩家名稱
            model: 模型名稱 (hunyuan-turbo, hunyuan-lite 等)
        """
        super().__init__(name, model)
        
        if not HUNYUAN_AVAILABLE:
            raise ImportError("tencentcloud-sdk-python-hunyuan 模塊未安裝，請運行: pip install tencentcloud-sdk-python-hunyuan")
        
        # 獲取 API 認證信息
        secret_id, secret_key = self._get_api_key()
        
        # 初始化騰訊雲客戶端
        cred = credential.Credential(secret_id, secret_key)
        region = os.getenv("HUNYUAN_REGION", "ap-guangzhou")
        self.client = hunyuan_client.HunyuanClient(cred, region)
        
        logger.info(f"Hunyuan 玩家初始化完成: {name} (region: {region})")
    
    def _get_api_key(self) -> tuple:
        """
        獲取騰訊雲 API 認證信息
        
        Returns:
            tuple: (secret_id, secret_key)
            
        Raises:
            ValueError: 如果環境變量未設置
        """
        secret_id = os.getenv("HUNYUAN_SECRET_ID")
        secret_key = os.getenv("HUNYUAN_SECRET_KEY")
        
        if not secret_id:
            raise ValueError("HUNYUAN_SECRET_ID 環境變量未設置")
        if not secret_key:
            raise ValueError("HUNYUAN_SECRET_KEY 環境變量未設置")
        
        return secret_id, secret_key
    
    def answer_boolean_question(self, word: str, attribute: str) -> bool:
        """
        使用 Hunyuan 回答布林問題
        
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
            
            # 構造請求
            req = models.ChatCompletionsRequest()
            req.Model = self.model
            req.Messages = [
                {"Role": "system", "Content": "你是一位中文語言學專家，擅長分析中文詞語的語言學屬性。"},
                {"Role": "user", "Content": prompt}
            ]
            req.TopP = 0.8
            req.Temperature = 0.3
            
            # 調用 API
            resp = self.client.ChatCompletions(req)
            
            # 解析回答
            if resp.Choices and len(resp.Choices) > 0:
                answer_text = resp.Choices[0].Message.Content.strip()
                
                # 判斷回答
                if "是" in answer_text or "yes" in answer_text.lower():
                    return True
                else:
                    return False
            else:
                logger.error("Hunyuan API 返回空響應")
                return False
                
        except Exception as e:
            logger.error(f"Hunyuan API 調用失敗: {e}")
            # 默認返回 False
            return False
    
    def propose_custom_attributes(self, word: str, num_slots: int = 8) -> List[str]:
        """
        使用 Hunyuan 提出自定義屬性
        
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
            
            # 構造請求
            req = models.ChatCompletionsRequest()
            req.Model = self.model
            req.Messages = [
                {"Role": "system", "Content": "你是一位中文語言學專家，擅長發現詞語的深層語言學屬性。"},
                {"Role": "user", "Content": prompt}
            ]
            req.TopP = 0.8
            req.Temperature = 0.7
            
            # 調用 API
            resp = self.client.ChatCompletions(req)
            
            # 解析回答
            if resp.Choices and len(resp.Choices) > 0:
                answer_text = resp.Choices[0].Message.Content.strip()
                
                # 提取屬性列表
                attributes = []
                for line in answer_text.split('\n'):
                    line = line.strip()
                    if not line:
                        continue
                    # 移除編號
                    if len(line) > 0 and not line[0].isdigit():
                        attributes.append(line)
                    elif '.' in line or '、' in line:
                        # 移除數字編號
                        parts = line.split('.', 1) if '.' in line else line.split('、', 1)
                        if len(parts) > 1:
                            attributes.append(parts[1].strip())
                
                # 確保返回正確數量
                return attributes[:num_slots]
            else:
                logger.error("Hunyuan API 返回空響應")
                return []
            
        except Exception as e:
            logger.error(f"Hunyuan API 調用失敗: {e}")
            # 返回空列表
            return []
