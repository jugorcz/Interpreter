

class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.memory = {}

    def hasKey(self, name):  # variable name
        return name in self.memory

    def getFromMemory(self, name):         # gets from memory current value of variable <name>
        return self.memory.get(name)

    def putIntoMemory(self, name, value):  # puts into memory current value of variable <name>
        self.memory[name] = value

class MemoryStack:
                                                                             
    def __init__(self, memory=None): # initialize memory stack with memory <memory>
            if memory is not None:
                self.stack = [memory] 
            else:
                self.stack = [Memory("global")]

    def getVariableValue(self, name):             # gets from memory stack current value of variable <name>
        for memory in reversed(self.stack):
            if memory.hasKey(name):
                return memory.getFromMemory(name)
        return None

    def insertVariable(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stackTop().putIntoMemory(name,value)

    def setVariableValue(self, name, value): # sets variable <name> to value <value>
        for memory in reversed(self.stack):
            if memory.hasKey(name):
                memory.putIntoMemory(name, value)
                return
        self.stackTop().putIntoMemory(name, value)


    def pushMemory(self, memory): # pushes memory <memory> onto the stack
        if memory is None:
            memory = Memory(str(len(self.stack) + 1))
        self.stack.append(memory)

    def popMemory(self):          # pops the top memory from the stack
        return self.stack.pop()

    def stackTop(self):
        return self.stack[-1]


