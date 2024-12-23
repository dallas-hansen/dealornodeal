import json
import random
from classes.case import Case

def load_settings(file_path='settings.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

settings = load_settings()

def create_cases(settings):
    num_cases = settings['game_structure']['num_cases']
    max_prize = settings['game_structure']['max_prize']
    min_prize = settings['game_structure']['min_prize']
    
    prizes = [random.randint(min_prize, max_prize) for _ in range(num_cases)]
    random.shuffle(prizes)
    
    return [Case(i + 1, prize) for i, prize in enumerate(prizes)]
