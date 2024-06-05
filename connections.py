import dataclasses as dc
from typing import List

@dc.dataclass
class Connection:
    level: str
    connection: str
    words: List[str]

    def level_number(self):
        if self.level == "🟡":
            return 1
        elif self.level == "🟢":
            return 2
        elif self.level == "🔵":
            return 3
        elif self.level == "🟣":
            return 4
        return -1


@dc.dataclass
class ConnectionDay:
    date: str
    iteration: int
    connections: List[Connection]

    def words(self):
        return [word for connection in self.connections for word in connection.words]