"""
Implement a MyCalendar class to store your events.
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book,
return true if the event can be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this:
MyCalendar cal = new MyCalendar();
MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

Hide Hint #1
Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.
"""


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.starts)):
            if self.starts[i] <= start < self.ends[i]:
                return False
            if self.starts[i] < end <= self.ends[i]:
                return False
            if start < self.starts[i] and end > self.ends[i]:
                return False
        self.starts.append(start)
        self.ends.append(end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
if __name__ == '__main__':
    my_calendar = MyCalendar()
    books = [[97, 100], [33, 51], [89, 100], [83, 100], [75, 92], [76, 95], [19, 30], [53, 63], [8, 23], [18, 37],
             [87, 100], [83, 100], [54, 67], [35, 48], [58, 75], [70, 89], [13, 32], [44, 63], [51, 62], [2, 15]]
    expected = [True, True, False, False, True, False, True, True, False, False, False, False, False, False, False,
                False, False, False, False, True]

    ans = []
    for i in range(len(books)):
        ans.append(my_calendar.book(books[i][0], books[i][1]))
        print(i, ans[i] == expected[i])
    print(expected)
    print(ans)
