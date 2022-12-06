class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion'''
    
    def __init__(self):
        '''Инициализирует статические настройки игры.'''
        #Параметры игры
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2.5
        self.ship_limit = 3
        '''Параметры снаряда'''
        self.bullet_speed = 25
        self.bullet_width = 10
        self.bullet_height = 35
        self.bullet_color = (60, 60, 60)
        
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        
        '''Темп ускорения игры'''
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1