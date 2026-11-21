# Decryption

from .encryption import (
    S_BOX,
    bytes_to_state,
    state_to_bytes,
    gf_mul,
    add_round_key
)

# inverse s-box

INV_S_BOX = [0] * 256

for i in range(256):
    INV_S_BOX[S_BOX[i]] = i

# inverse sub bytes
def inv_sub_bytes(state):
    return [[INV_S_BOX[value] for value in row] for row in state]

# inverse shift rows
def inv_shift_rows(state):
    return [row[-r:] + row[:-r] if r else row[:] for r, row in enumerate(state)]