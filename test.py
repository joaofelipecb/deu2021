import sys
import p23control._Condition
import p23control._Symbol

if len(sys.argv) != 2:
    print('Nao implementado')
    quit()
    
arg = sys.argv[1]

if arg.find('.') == -1:
    print('Nao implementado')
    quit()
    
callFunction = p23control._Symbol.resolve('p23control.'+arg)
testFunction = p23control._Symbol.resolve('p18test.'+arg)

if len(testFunction) != 2:
    print('Nao implementado')
    quit()

argsFunction = testFunction[0]
argsFunctionParsed = {}
for argName, argValue in argsFunction.items():
    if not isinstance(argValue,dict) or (isinstance(argValue,dict) and not '_type' in argValue):
        argsFunctionParsed[argName] = argValue
    else:
        symbol = p23control._Symbol.resolve(argValue['_type'])
        del argValue['_type']
        argsFunctionParsed[argName] = symbol(**argValue)
    
finalFunction = testFunction[1]
if not '_condition' in finalFunction:
    print('Nao implementado')
    quit()

result = callFunction(**argsFunctionParsed)

condition = p23control._Condition.parse(finalFunction['_condition'])
print(p23control._Condition.verify(condition,argsFunctionParsed))

