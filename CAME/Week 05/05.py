import sys

class Model:
    framework = 'CAME-ML'

    def __init__(self, name):
        self.name = name

for line in sys.stdin:
    line = line.rstrip('\n')
    stripped = line.strip()

    if not stripped or stripped[0] == '#':
        continue

    if stripped.startswith('FRAMEWORK '):
        Model.framework = stripped[len('FRAMEWORK '):]
        continue

    model_01 = Model(stripped)
    print(f"{model_01.name}|{Model.framework}")