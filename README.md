This repo contains all algorithms I'm learning and practising.
# Data structure
## Basic data types in python
- Integer
- String
- Boolean
- Float
## Types of data structures
Builtin | User defined 1 | USer defined 2 
:---:|:---:|:-----:
List | Linked list | Queue
Tuple | Tree | 
Set | Graph | 
Dictionary | Stack 

## Stack
- LIFO - Last in First Out
- push and pop
- Used in undo and redo operations

```python
a = []
a.append(10)
a.append(20)
a.append(30)

# User pop to access last entered value
b = a.pop()
print(b)
```

## Queue
- FIFO - First in First Out
- Adding elements is called enqueue.
- Removing elements is called dequeue.
- Used in linear operations
	- Uploading images
	- Printing documents