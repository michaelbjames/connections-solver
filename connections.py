import dataclasses as dc
from typing import List

@dc.dataclass
class Connection:
    level: str
    connection: str
    words: List[str]

@dc.dataclass
class ConnectionDay:
    date: str
    iteration: int
    connections: List[Connection]

    def words(self):
        return [word for connection in self.connections for word in connection.words]