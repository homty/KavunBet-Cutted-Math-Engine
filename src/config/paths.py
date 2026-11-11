"""Define paths used by the local math engine."""

import os
from pathlib import Path

PROJECT_PATH = os.path.abspath(Path(__file__).resolve().parent.parent.parent)
PATH_TO_ENGINE = PROJECT_PATH
PATH_TO_GAMES = os.path.join(PROJECT_PATH, "games")
