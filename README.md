# Transaction Database Assignment

## Code Execution Instructions

### Prerequisites

- Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/randolj/Transaction-DB-Assignment.git
   cd Transaction-DB-Assignment

### To run the code 
1. To select which commands will be run, simply edit the main.py main() function with all the commands you wish to run (It comes set with example functions that display error messages and showing all functions work).

2.  Execute the main.py script while in the file directory:

   ```bash
   python main.py
```

For functions that are meant to throw an error (i.e. when transaction not in progress, an exception class called DBException was created to handle and not crash the program. In these cases, the function should be formatted like this:

   ```python
    try:
        inmemoryDB.example_function()
    except DBException as e:
        print(e)
```
   

### Features
1. The following functions are included and can be called by using inmemoryDB. followed by the desired command.
- begin_transaction()
- put(key, value)
- get(key)
- commit()
- rollback()
2. Keys should be string and values should be integers.
3. put(key, val) will create a new key with the provided value if a key doesn’t exist. Otherwise it will update the value of an existing key.
4. get(key) will return the value associated with the key or null if the key doesn’t exist.
5. If put(key, val) is called when a transaction is not in progress throw an exception
6. get(key) can be called anytime even when a transaction is not in progress
7. begin_transaction() starts a new transaction.
8. At a time only a single transaction may exist.
9. Within a transaction you can make as many changes to as many keys as you like. However, they should not be “visible” to get(), until the transaction is committed.
10. A transaction ends when either commit() or rollback() is called
11. commit() applies changes made within the transaction to the main state. Allowing any future gets() to “see” the changes made within the transaction
12. rollback() should abort all the changes made within the transaction and everything should go back to the way it was before.

### To create an official assignment
1. Additional Functions: Consider adding functions that might enhance the database's functionality, such as a function to check if a key exists, retrieve a list of all keys, or perform conditional updates.
2. Testing Guidelines: Clearly define a set of test cases that should be used to assess the correctness of the implementation. Encourage students to write unit tests for their functions to ensure robustness.
3. Scalability Considerations: Discuss potential scalability issues and how the implementation might handle a large number of transactions or keys. Encourage students to think about optimizations and improvements for a real-world scenario.
4. Code Structure and Style: Specify guidelines on code structure, organization, and style. Encourage the use of best practices and design patterns. Emphasize modularity and extensibility in the codebase.
5. Peer Review Component: Introduce a peer review component where students review and provide feedback on each other's code. This fosters collaboration, exposes students to different coding styles, and promotes a culture of constructive criticism. Students could be grouped by language used.
