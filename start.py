import pygame
from sett import Settings
from ship import Ship
import functions as f
from pygame.sprite import Group
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard
def run():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(game_settings, screen, "Play")
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()
    f.create_fleet(game_settings, screen, ship, aliens)
    while True:
        f.check_events(game_settings, screen, stats, sb, play_button, ship,
                       aliens, bullets)
        if stats.game_active:
            ship.update()
            f.update_bullets(game_settings, screen, stats, sb, play_button,
                             ship, aliens, bullets)
            f.update_aliens(game_settings, stats, sb, screen, ship, aliens,
                            bullets)

        f.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button)

        
run()
