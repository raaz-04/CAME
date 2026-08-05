drop_threshold = None
raw_scores = []

while True:
    try:
        line = input()
    except EOFError:
        break

    stripped = line.strip()

    if not stripped:
        continue

    if stripped[0] == '#':
        continue

    if stripped.startswith('DROP below='):
        try:
            drop_threshold = float(stripped[len('DROP below='):])
        except ValueError:
            pass
        continue

    try:
        val = float(stripped)
        if drop_threshold is None or val >= drop_threshold:
            raw_scores.append(val)
    except ValueError:
        print(f"Skipping invalid value: {line}")

scores = [value for value in raw_scores]

if not scores:
    print("No valid values")
else:
    print(scores)
    print(f'{sum(scores) / len(scores):.3f}')