import sys

allow_spam = False
age_max = 65
count = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    stripped = line.strip()

    if not stripped or stripped[0] == '#':
        continue

    if stripped == 'ALLOW spam':
        allow_spam = True
        continue

    if stripped.startswith('AGE max='):
        n = int(stripped[len('AGE max='):])
        age_max = max(18, n)
        continue

    parts = stripped.split('|')
    age_str, label, score_str, country, is_premium_str, has_missing_str = parts

    age = int(age_str)
    label = label.strip()
    score_raw = score_str.strip()
    country = country.strip()
    is_premium = is_premium_str.strip().lower() == 'true'
    has_missing = has_missing_str.strip().lower() == 'true'

    if not (18 <= age <= age_max):
        continue

    if label == 'spam' and not allow_spam:
        continue

    if score_raw == '' or score_raw.upper() == 'NONE':
        continue
    if not (float(score_raw) >= 0.60):
        continue

    if not (country == 'LK' or is_premium):
        continue

    if has_missing:
        continue

    count += 1

print(count)