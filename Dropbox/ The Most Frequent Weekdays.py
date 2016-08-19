# coding: utf8

import calendar
from collections import Counter


def most_frequent_days(year):

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    counter_dict = Counter()
    a = calendar.Calendar().yeardatescalendar(year)

    for q in a:
        for w in q:
            for e in w:
                for r in e:
                    if r.year == year:
                        counter_dict[weekdays[r.weekday()]] += 1

    b = [day for day in counter_dict.keys() if counter_dict[day] == max(counter_dict.values())]
    return [day for day in weekdays if day in b]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
