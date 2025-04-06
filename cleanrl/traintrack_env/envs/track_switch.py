from random import randint
from random import choice

from model import track_switch_block_count

def random_locomotive_position() -> dict[str, int]:
    locomotive_block_1 = randint(0, track_switch_block_count)
    locomotive_block_2 = choice([i for i in range(0, track_switch_block_count) if i != locomotive_block_1])
    return {"lok1": locomotive_block_1, "lok2": locomotive_block_2}