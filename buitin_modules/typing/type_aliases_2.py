from typing import List, Tuple, Dict

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: List[Server]) -> None:
    pass
