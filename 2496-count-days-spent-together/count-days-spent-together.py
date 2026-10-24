class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def get_day(date):
            month, day = map(int, date.split("-"))

            total = 0

            for i in range(month - 1):
                total += days[i]

            return total + day

        a1 = get_day(arriveAlice)
        a2 = get_day(leaveAlice)

        b1 = get_day(arriveBob)
        b2 = get_day(leaveBob)

        start = max(a1, b1)
        end = min(a2, b2)

        if start > end:
            return 0

        return end - start + 1