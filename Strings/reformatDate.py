class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan" :"01", "Feb":"02", "Mar":"03", "Apr": "04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        day, month, year = date.split(' ')
        day = list(day)
        for i in range(len(day)-1,-1,-1):
            if day[i].isalpha():
                day.pop(i)
        stringDay = ''.join(day)
        if len(stringDay) == 1:
            stringDay = '0'+stringDay
        stringValMonth = months[month]
        formattedString = year + '-' + stringValMonth + '-'+stringDay
        return formattedString