import sys

if len(sys.argv) != 2:
    print('Nao implementado')
    quit()
    
arg = sys.argv[1]

if arg.find('.') == -1:
    print('Nao implementado')
    quit()
    
moduleName = arg[0:arg.find('.')]
functionName = arg[arg.find('.')+1:]

namespaceControl = __import__('p23control.'+moduleName)

callFunction = namespaceControl.__getattribute__(moduleName).__getattribute__(functionName)

namespaceTest = __import__('p18test.'+moduleName)

testFunction = namespaceTest.__getattribute__(moduleName).__getattribute__(functionName)
argFunction = testFunction[0]

callFunction(**argFunction)
