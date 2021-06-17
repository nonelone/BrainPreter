import sys

#define variables:
tape = [0]
pointer = 0
todo = ""
insNum = 0

#all instruction's commands:
def inc():
    global todo
    tape[pointer] = tape[pointer] + 1
    return todo[1:]

def dec():
    global todo
    tape[pointer] = tape[pointer] - 1
    return todo[1:]

def bck():
    global todo
    global pointer
    try: 
        pointer = pointer - 1
        exceptor = tape[pointer]
        return todo[1:]
    except:
        print("Interpretation ERROR: index out of range {}".format(pointer - 1))

def fwd():
    global todo
    global pointer
    pointer = pointer + 1
    try:
        exceptor = tape[pointer]
    except:
        tape.append(0)

    return todo[1:]

def prt():
    global todo
    print(tape[pointer])
    return todo[1:]

def inp():
    global todo
    global pointer
    tape[pointer] = input(">>> ")
    return todo[1:]

def bgn():
    global todo
    endIndex = todo.find("]")
    currentTodo = todo[insNum + 1:]
    print(currentTodo)
    index = currentTodo.find("]")
    currentTodo = currentTodo[:index]
    condition = tape[pointer]
    conPointer = pointer
    print(currentTodo)
       
    while condition > 0:
        for i in currentTodo:
            instructions[i]()
        condition = tape[conPointer]
        
    todo = todo[endIndex:]
    return todo

#list of all instructions:
instructions = {
       "+" : inc,
       "-" : dec,
       "<" : bck,
       ">" : fwd,
       "." : prt,
       "," : inp,
       "[" : bgn
}

#main function:
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if ".bf" in sys.argv[1]:
            with open(sys.argv[1], "r") as f:  todo =  f.read()
            todo = todo.replace("\n", "")
        else:
            todo = sys.argv[1]

        while todo != "":
            todo = instructions[todo[0]]()
            insNum = insNum + 1

    else: print("Bad usage! You should use BrainPreter.py [path to .bf file / list of commands]")
