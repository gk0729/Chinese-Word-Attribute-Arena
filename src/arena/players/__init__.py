"""
玩家實現模塊
"""
# Import players with error handling for missing dependencies
__all__ = []

try:
    from .deepseek_player import DeepSeekPlayer
    __all__.append("DeepSeekPlayer")
except ImportError:
    pass

try:
    from .qwen_player import QwenPlayer
    __all__.append("QwenPlayer")
except ImportError:
    pass

try:
    from .gpt4_player import GPT4Player
    __all__.append("GPT4Player")
except ImportError:
    pass

try:
    from .hunyuan_player import HunyuanPlayer
    __all__.append("HunyuanPlayer")
except ImportError:
    pass

try:
    from .glm_player import GLMPlayer
    __all__.append("GLMPlayer")
except ImportError:
    pass
