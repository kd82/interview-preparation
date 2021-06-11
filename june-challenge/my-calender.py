def __init__(self):
        self.meetings = []

def book(self, start: int, end: int) -> bool:
        for s, e in self.meetings:
            if s < end and start < e:
                return False
        self.meetings.append([start, end])
        return True