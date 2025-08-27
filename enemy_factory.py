import pygame
from enemy import Enemy
import random

class EnemyFactory:
    enemy_images = {}
    enemykind = ["-0", "-1", "-2", "-3", "-4"]

    @staticmethod
    def load_images(random_index):
        EnemyFactory.enemy_images = {
            "enemy1-0": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy0{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-1": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy1{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-2": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy2{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-3": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy3{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-4": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy4{i}.png"), (35, 55)) for i in range(5)],
            "police": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemyP{i}.png"), (60, 120)) for i in range(5)],
            "enemy2": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy2/2walkers{i}.png"), (35, 70)) for i in range(0, 20, 2)],
            
            "mileage": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/lamp0.png"), (1, 1))],
            
            }
        '''
            "enemy1": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy{int(i/5)}{i}.png"), (60, 120)) for i in range(5)],
                '''
          
          
                

    @staticmethod
    def create(enemy_type, x, y, bullet_group):
        #EnemyFactory.enemykind = random.randint(0,4)
        if enemy_type == "enemy1":
            return Enemy(x, y, animation=EnemyFactory.enemy_images[enemy_type + random.choice(EnemyFactory.enemykind)], 
                         bullet_group=bullet_group, bullet_type=enemy_type, value=100, speedy_range=(2, 3))
        elif enemy_type == "police":
            return Enemy(x, y, animation=EnemyFactory.enemy_images[enemy_type], 
                         bullet_group=bullet_group, bullet_type=enemy_type, value=100, speedy_range=(2, 3))
        
        elif enemy_type == "enemy2":
            return Enemy(x, y, animation=EnemyFactory.enemy_images[enemy_type], 
                         bullet_group=bullet_group, bullet_type=enemy_type, value=200, speedy_range=(8, 9))
        elif enemy_type == "mileage":
            return Enemy(x, y, animation=EnemyFactory.enemy_images[enemy_type], 
                         bullet_group=bullet_group, bullet_type=enemy_type, value=200, speedx_range=(0,0), speedy_range=(10, 10))