class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        month = {
            "Jan": '01', "Feb": '02', "Mar":'03', 
            "Apr": '04', "May": '05', "Jun":'06', 
            "Jul": '07', "Aug": '08', "Sep":'09', 
            "Oct": '10', "Nov": '11', "Dec": '12'
        }
        
        target = date.split()
        
        year = target[2]
        month = month[target[1]]

        date = numbers = re.findall(r'\d+', target[0])
        date = ''.join(date)
        if len(date) == 1:
            date = '0' + date

        time = [year, month, date]
        return '-'.join(time)