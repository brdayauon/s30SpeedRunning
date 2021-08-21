class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog = []
        digitLog = []
        
        for log in logs:
            l = log.split(" ")
            uid, words = l[0], ''.join(l[1::])
            if words.isdigit():
                digitLog.append(log)
            else:
                letterLog.append(log)
        #sort identifiers first   
        letterLog.sort(key=lambda x: x[:x.index(' ')])
        #sort on contents
        letterLog.sort(key=lambda x: x[x.index(' '):])

        return letterLog + digitLog
         