

'''
Write a function balancedBrackets that receives a string of opening and closing brackets and determines whether or not the string's openers and closers are properly nested.

The possible opening brackets are [, {, and (. The corresponding closers are ], }, and ).

Examples:

balancedBrackets('[]{}()');   // should return true
balancedBrackets('[{[()]}]');   // should return true
balancedBrackets('[({}}]');   // should return false

'''


print('hello')

# fifo -> stack, recurcursion or stack data struct

def balancedBrackets(brackets):
    print(list(brackets))
    brackets_splited = list(brackets) #.split(',')[0]
    #return brackets
    brac_type = {'[': ']', '{': '}', '(':')'}
    #brac_type_c = {']', '}', ')'}
    # while brackets has values
    stack = []
    print('before', brackets_splited, stack)

    while(len(brackets_splited)):
        brac = brackets_splited.pop(0)
        print(brac)
        stack.append(brac)
    # if opener stack will push brac_types opener index
    # check against closing bracket
    #return True

print(balancedBrackets('[]{}()'))
#print(balancedBrackets('[,],{,},(,)')) #true
#print(balancedBrackets('[,{,[,(,),],},]')) #true
#print(balancedBrackets('[({}}]')) #false
