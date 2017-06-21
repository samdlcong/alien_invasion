import os

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始话统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于活动状态
        self.game_active = False
        #在任何情况下都不应重置最高得分
        self.filename = 'data.dat'
        if os.path.exists(self.filename):
            self.read_high_score()
        else:
            self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open(self.filename, 'w') as file_object:
            file_object.write(str(self.high_score))

    def read_high_score(self):
        with open(self.filename, 'r') as file_object:
            self.high_score = int(file_object.readline())

        