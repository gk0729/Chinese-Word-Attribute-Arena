"""
中文字詞屬性知識競技場核心模塊
"""
from .player import AIPlayer
from .judge import RefereeAI
from .game_engine import ArenaGame
from .player_factory import PlayerFactory, initialize_player_factory

__all__ = [
    "AIPlayer",
    "RefereeAI",
    "ArenaGame",
    "PlayerFactory",
    "initialize_player_factory"
]
