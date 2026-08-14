class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")
            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":

                if stack:
                    result[stack[-1]] += timestamp - prev_time

                stack.append(function_id)
                prev_time = timestamp

            else:

                result[stack[-1]] += timestamp - prev_time + 1

                stack.pop()
                prev_time = timestamp + 1

        return result