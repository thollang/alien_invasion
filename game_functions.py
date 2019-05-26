import sys

import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship, pikachu):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pikachu.blitme()

    pygame.display.flip()
