a = []
a.append(10)
a.append(20)
a.append(30)
b = a.pop()
print(b)

# TO CHECK THE LIST IS EMPTY OR NOT
bb = []
## Type 1
if not bb:
    print("The list is empty")
else:
    print("The list is not empty")

## Type 2
if len(bb) == 0:
    print("The list is empty")
else:
    print("The list is not empty")


# STACK BY BBUILT IN MMODULE
print("STACK BY BUILT IN MMODULE")
import queue
q = queue.LifoQueue()
q.put(10)
q.put(20)
q.put(30)
print(q.get())