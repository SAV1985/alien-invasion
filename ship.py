import pygame

class Ship():
    '''Класс для управления кораблем'''
    def __init__(self, ai_game):
        '''Инициализирует корабль и задает его начальную позицию'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        
        '''Загружает изображение корабля и получает прямоугольник'''
        self.image = pygame.image.load('game/ship.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.x = ai_game.settings.screen_width / 2
        '''Каждый новый корабль появляется у нижнего края экрана'''
        self.rect.midbottom = self.screen_rect.midbottom        
        '''Флаг перемещения'''
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        self.rect.x = self.x
    
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)
        
        
    def center_ship(self):
        '''Размещение корабля в центре нижней стороны'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)