import tomllib
from random import choice
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='cake-game.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger.info('Started')


def load_settings(filename):
    with open(filename, 'rb') as f:
        settings = tomllib.load(f)
    with open('pyproject.toml', 'rb') as f:
        settings["poetry"] = tomllib.load(f)
    return settings


class GameState:
    def __init__(self, settings_path='settings.toml'):

        self.settings = load_settings(settings_path)
        self.poetry = self.settings.get('poetry', {})
        self.version = self.poetry.get('tool').get('poetry').get('version')
        self.characters = self.settings.get('characters', [])
        self.name = self.settings.get('poetry').get('tool').get('poetry').get('name')

    def initialize_characters(self):
        logger.info('Initializing characters')
        for character in self.characters:
            print(f"{character} initialized!")
        print(f"Total characters: {len(self.characters)}")
        guilty_character = choice(list(self.characters))
        print(f"The {guilty_character} is guilty!")


    def game_loop(self):
        self.start_game()
        self.initialize_characters()
        self.game_over()


    def start_game(self):
        logger.info('Starting game')
        print(f"Welcome to {self.name}!")
        print(f"Version {self.version}")
        self.initialize_characters()
        print("Game started!")
        print("Good luck!")
        print("")


