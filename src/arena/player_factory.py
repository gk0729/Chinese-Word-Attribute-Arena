"""
PlayerFactory 玩家工廠類
負責根據配置創建玩家實例
"""
from typing import List, Dict, Any
import logging

from .player import AIPlayer

logger = logging.getLogger(__name__)


class PlayerFactory:
    """玩家工廠，負責創建和管理玩家實例"""
    
    # 可用玩家類型映射
    AVAILABLE_PLAYERS = {}
    
    @classmethod
    def register_player(cls, player_type: str, player_class: type):
        """
        註冊玩家類型
        
        Args:
            player_type: 玩家類型標識
            player_class: 玩家類
        """
        cls.AVAILABLE_PLAYERS[player_type] = player_class
        logger.debug(f"註冊玩家類型: {player_type}")
    
    @classmethod
    def create_players(cls, player_configs: List[Dict[str, Any]]) -> List[AIPlayer]:
        """
        根據配置創建玩家列表
        
        Args:
            player_configs: 玩家配置列表，每個配置包含：
                - name: 玩家名稱
                - type: 玩家類型
                - model: 模型名稱
                - enabled: 是否啟用
                
        Returns:
            List[AIPlayer]: 玩家實例列表
        """
        players = []
        
        for config in player_configs:
            # 檢查是否啟用
            if not config.get("enabled", True):
                logger.info(f"跳過未啟用的玩家: {config.get('name')}")
                continue
            
            player_type = config.get("type")
            player_name = config.get("name")
            model = config.get("model")
            
            # 檢查玩家類型是否支持
            if player_type not in cls.AVAILABLE_PLAYERS:
                logger.warning(f"不支持的玩家類型: {player_type}，跳過")
                continue
            
            try:
                # 創建玩家實例
                player_class = cls.AVAILABLE_PLAYERS[player_type]
                player = player_class(name=player_name, model=model)
                players.append(player)
                logger.info(f"成功創建玩家: {player_name} ({player_type})")
            except Exception as e:
                logger.error(f"創建玩家 {player_name} 失敗: {e}")
        
        return players
    
    @classmethod
    def create_default_chinese_team(cls) -> List[AIPlayer]:
        """
        創建默認中文團隊（DeepSeek + Qwen）
        
        Returns:
            List[AIPlayer]: 默認玩家列表
        """
        default_configs = [
            {
                "name": "DeepSeek",
                "type": "deepseek",
                "model": "deepseek-chat",
                "enabled": True
            },
            {
                "name": "Qwen",
                "type": "qwen",
                "model": "qwen-max",
                "enabled": True
            }
        ]
        
        logger.info("創建默認中文團隊")
        return cls.create_players(default_configs)


    @classmethod
    def create_blood_awakening_team(cls) -> List[AIPlayer]:
        """
        創建血脈覺醒陣容（純中文原生模型）
        
        Returns:
            List[AIPlayer]: 血脈覺醒陣容玩家列表
        """
        blood_awakening_configs = [
            {
                "name": "DeepSeek-V3 🔥",
                "type": "deepseek",
                "model": "deepseek-chat",
                "enabled": True
            },
            {
                "name": "Hunyuan-Turbo 🔥",
                "type": "hunyuan",
                "model": "hunyuan-turbo",
                "enabled": True
            },
            {
                "name": "GLM-4-Plus 🔥",
                "type": "glm",
                "model": "glm-4-plus",
                "enabled": True
            }
        ]
        
        logger.info("創建血脈覺醒陣容")
        return cls.create_players(blood_awakening_configs)


def initialize_player_factory():
    """初始化玩家工廠，註冊所有可用的玩家類型"""
    try:
        from .players.deepseek_player import DeepSeekPlayer
        PlayerFactory.register_player("deepseek", DeepSeekPlayer)
    except ImportError as e:
        logger.warning(f"無法導入 DeepSeekPlayer: {e}")
    
    try:
        from .players.qwen_player import QwenPlayer
        PlayerFactory.register_player("qwen", QwenPlayer)
    except ImportError as e:
        logger.warning(f"無法導入 QwenPlayer: {e}")
    
    try:
        from .players.gpt4_player import GPT4Player
        PlayerFactory.register_player("gpt4", GPT4Player)
    except ImportError as e:
        logger.warning(f"無法導入 GPT4Player: {e}")
    
    try:
        from .players.hunyuan_player import HunyuanPlayer
        PlayerFactory.register_player("hunyuan", HunyuanPlayer)
    except ImportError as e:
        logger.warning(f"無法導入 HunyuanPlayer: {e}")
    
    try:
        from .players.glm_player import GLMPlayer
        PlayerFactory.register_player("glm", GLMPlayer)
    except ImportError as e:
        logger.warning(f"無法導入 GLMPlayer: {e}")
    
    logger.info(f"玩家工廠初始化完成，已註冊 {len(PlayerFactory.AVAILABLE_PLAYERS)} 種玩家類型")
