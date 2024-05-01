# https://www.gymlibrary.dev/environments/toy_text/frozen_lake/
FROZEN_LAKE_ENV = {
    "name": "FrozenLake-v1",
    "observation_dim": 16,
    # Массив действий в соответствии с документацией
    "actions_variants": [0, 1, 2, 3],
}

# https://www.gymlibrary.dev/environments/toy_text/frozen_lake/
CLIFF_WALKING_ENV = {
    "name": "CliffWalking-v0",
    "observation_dim": 48,
    # Массив действий в соответствии с документацией
    "actions_variants": [0, 1, 2, 3],
}
