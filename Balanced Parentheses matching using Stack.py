def pairs(open,close):
    if open=="[" and close=="]":
        return True
    if open=="(" and close==")":
        return True
    if open=="{" and close=="}":
        return True

def balanced(string):
    stack=[]
    for i in range(len(string)):
        if string[i]=="[" or string[i]=="{" or string[i]=="(":
            stack.append(string[i])
        elif string[i]=="]" or string[i]=="}" or string[i]==")":
            if pairs(stack[-1],string[i] or len(stack)!=0):
                stack.pop()
            else:
                break
    if len(stack)==0:
        print("Balanced")
    else:
        print("Not Balanced")

string=input("Enter the string:")
print(balanced(string))
