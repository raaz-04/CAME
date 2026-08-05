import sys

fold_case = False
bind_name = None
labels = []

for line in sys.stdin:
    line = line.rstrip('\n')
    stripped = line.strip()

    if not stripped or stripped[0] == '#':
        continue

    if stripped == 'FOLD case':
        fold_case = True
        continue

    if stripped.startswith('BIND duplicate '):
        bind_name = stripped[len('BIND duplicate '):]
        continue

    labels.append(stripped)

def normalize(s):
    return s.casefold() if fold_case else s

normalized_labels = [normalize(lbl) for lbl in labels]

if bind_name is not None:
    bind_key = normalize(bind_name)
    bind_count = 0
    for lbl in normalized_labels:
        if lbl == bind_key:
            bind_count += 1

    if bind_count >= 2:
        print("unique=1")
        print("has_duplicates=yes")
    else:
        bind_name = None

if bind_name is None:
    freq = {}
    for lbl in normalized_labels:
        if lbl in freq:
            freq[lbl] += 1
        else:
            freq[lbl] = 1

    unique_count = len(freq)

    has_dup = False
    for lbl in freq:
        if freq[lbl] > 1:
            has_dup = True
            break

    print(f"unique={unique_count}")
    print(f"has_duplicates={'yes' if has_dup else 'no'}")