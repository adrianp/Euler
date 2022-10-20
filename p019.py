import sys

from datetime import datetime, timedelta


def naive():
    start = "1901-01-01"
    end = "2000-12-31"

    start = datetime.fromisoformat(start)
    end = datetime.fromisoformat(end)

    sundays = 0

    while start <= end:
        if start.weekday() == 6 and start.day == 1:
            sundays += 1
        start += timedelta(days=1)

    print(sundays)


if __name__ == "__main__":
    sys.exit(naive())
