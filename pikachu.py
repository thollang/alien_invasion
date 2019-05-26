import pygame


class Pikachu():

    def __init__(self, screen):
        """初始化pikachu并设置其初始位置"""
        self.screen = screen

        # 加载pikachu图像并获取其外接矩形
        self.image = pygame.image.load('images/pikachu.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
