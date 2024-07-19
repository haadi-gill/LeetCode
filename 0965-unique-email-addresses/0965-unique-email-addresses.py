class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actual = set()

        for e in emails:
            s = e.split('@')
            actual.add(s[0].split('+')[0].replace('.','')+'@'+s[1])

        print(actual)
        
        return len(actual)