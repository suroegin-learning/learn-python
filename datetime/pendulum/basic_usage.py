### Datetime

import pendulum

now = pendulum.now('Europe/Moscow')
two_days_later = now.add(days=2)

print(now)
print(two_days_later)

### Duration

dur = pendulum.duration(days=15)

print(dur.weeks)
print(dur.hours)

print(dur.in_hours())

print(dur.in_words())