class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hm = {}
        count = 0
        for i in range(len(time)):
            if 60-(time[i]%60) == 60:
                check = 0
            else:
                check = 60-(time[i]%60)
                
            if check in hm:
                #print(check, hm[check], i)
                count += hm[check]
                #print(count)
            #incase future number needs it
            if (time[i]%60) in hm:
                hm[time[i]%60] += 1
            else:
                hm[time[i]%60] = 1
            print(hm)
        return count