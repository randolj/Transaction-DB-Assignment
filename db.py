from collections import defaultdict


class DBException(Exception):
    """Custom exception class for database-related errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InMemoryDB:
    def __init__(self) -> None:
        self.in_transaction = False
        self.memory = defaultdict(
            lambda: [None, None]
        )  # store (committed value, intermediate value)
        self.modified_keys = set()

    def begin_transaction(self):
        if self.in_transaction:
            raise DBException("Already in transaction.")
        self.in_transaction = True

    def put(self, key, value):
        if not self.in_transaction:
            raise DBException("Must begin transaction.")
        self.memory_last = self.memory[key][1]
        self.memory[key][1] = value  # set intermediate value
        self.modified_keys.add(key)

    def get(self, key):
        return self.memory[key][0]

    def commit(self):
        if not self.in_transaction:
            raise DBException("Must begin transaction.")
        for key in self.modified_keys:
            self.memory[key][0] = self.memory[key][1]  # move intermediate values into committed values
        self.modified_keys.clear()
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise DBException("Must begin transaction.")
        for key in self.modified_keys:
            self.memory[key][1] = None  # remove all intermediate values
        self.modified_keys.clear()
        self.in_transaction = False
