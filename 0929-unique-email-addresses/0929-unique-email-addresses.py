class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            # '+' 뒤의 부분 제거
            local = local.split('+')[0]
            # '.' 제거
            local = local.replace('.', '')
            # 최종 이메일 생성
            simplified_email = local + '@' + domain
            unique_emails.add(simplified_email)
    
        return len(unique_emails)