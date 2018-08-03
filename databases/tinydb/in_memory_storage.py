from tinydb import TinyDB
from tinydb.storages import MemoryStorage

db = TinyDB(storage=MemoryStorage)

# and use same commands