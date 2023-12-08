from db import InMemoryDB, DBException


def main():
    inmemoryDB = InMemoryDB()

    # should return null, because A doesn’t exist in the DB yet
    print(inmemoryDB.get("A"))

    # should throw an error because a transaction is not in progress
    try:
        inmemoryDB.put("A", 5)
    except DBException as e:
        print(e)

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # set’s value of A to 5, but its not committed yet
    inmemoryDB.put("A", 5)

    # should return null, because updates to A are not committed yet
    print(inmemoryDB.get("A"))

    # update A’s value to 6 within the transaction
    inmemoryDB.put("A", 6)

    # commits the open transaction
    inmemoryDB.commit()

    # should return 6, that was the last value of A to be committed
    print(inmemoryDB.get("A"))

    # throws an error, because there is no open transaction
    try:
        inmemoryDB.commit()
    except DBException as e:
        print(e)

    # throws an error because there is no ongoing transaction
    try:
        inmemoryDB.rollback()
    except DBException as e:
        print(e)

    # should return null because B does not exist in the database
    print(inmemoryDB.get("B"))

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # Set key B’s value to 10 within the transaction
    inmemoryDB.put("B", 10)

    # Rollback the transaction - revert any changes made to B
    inmemoryDB.rollback()

    # Should return null because changes to B were rolled back
    print(inmemoryDB.get("B"))


if __name__ == "__main__":
    main()
