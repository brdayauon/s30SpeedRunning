class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest_key = 'a'
        longest_duration = 0
        n = len(keysPressed)

        for i in range(n):
              pressedTime = releaseTimes[i - 1] if i > 0 else 0
              duration = releaseTimes[i] - pressedTime
              if duration == longest_duration:
                  slowest_key = max(slowest_key, keysPressed[i])
              elif duration > longest_duration:
                  slowest_key = keysPressed[i]
                  longest_duration = duration

        return slowest_key