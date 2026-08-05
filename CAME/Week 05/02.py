import sys

watchlist = set()
results = []

for line in sys.stdin:
    line = line.rstrip('\n')
    stripped = line.strip()

    if not stripped or stripped[0] == '#':
        continue

    if stripped.startswith("WATCHLIST "):
        labels_part = stripped[len("WATCHLIST "):]
        watchlist = set(lbl.strip() for lbl in labels_part.split(','))
        continue

    comma_idx = stripped.rfind(',')
    label_raw = stripped[:comma_idx]
    conf_raw = stripped[comma_idx + 1:]

    label = label_raw.strip().lower()

    try:
        confidence = float(conf_raw.strip())
    except ValueError:
        continue

    if label in watchlist:
        priority = "HIGH"
    elif confidence < 0.50 or label == 'unknown':
        priority = "HIGH"
    elif 0.50 <= confidence < 0.80:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    results.append(priority)

for r in results:
    print(r)