"""Run a bounded local simulation of the KavunBet ways game."""

from .game_config import GameConfig
from .gamestate import GameState
from src.state.run_sims import create_books
from src.write_data.write_configs import generate_configs


def main() -> None:
    num_threads = 1
    batching_size = 5000
    compression = True
    profiling = False

    num_sim_args = {
        "base": 5000,
        "bonus": 5000,
    }

    config = GameConfig()
    gamestate = GameState(config)

    create_books(
        gamestate,
        config,
        num_sim_args,
        batching_size,
        num_threads,
        compression,
        profiling,
    )

    generate_configs(gamestate)


if __name__ == "__main__":
    main()
