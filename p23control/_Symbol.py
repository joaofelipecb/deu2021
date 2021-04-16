def resolve(path, namespace=None):
    parts = path.split('.')
    if namespace == None:
        if parts[0] in ['p17data','p18test','p23control','p24command']:
            symbolName = parts.pop()
        else:
            symbolName = parts[-1]
    if namespace is None:
        pointer = __import__(str.join('.',parts))
    else:
        pointer = namespace[parts[0]]
    parts.pop(0)
    for part in parts:
        pointer = pointer.__getattribute__(part)
    if namespace == None:
        return pointer.__getattribute__(symbolName)
    else:
        return pointer
