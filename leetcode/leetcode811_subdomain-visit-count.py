'''
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

'''
class Solution(object):
            
            
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        def getStringArr(dic):
            """
            input: {'mail.com': 901, 'yahoo.com': 50, 'google.mail.com': 900, 'wiki.org': 5, 'org': 5, 'intel.mail.com': 1, 'com': 951}
            output ["901 mail.com", "50 yahoo.com","900 google.mail.com", "5 wiki.org" ... ...]
            """
            res = []
            for key, val in dic.items():
                tmp_str = str(val) + " " + key
                res.append(tmp_str)
            return res

        def getSubDomains(domain):
            """
            input: "google.mail.com"
              [["google", "mail", "com"]["mail", "com"]["com"]]
            output: ["google.mail.com", "mail.com", "com"]
            return subdomains of a given domain
            """
            res = []
            tmp_separate_domain_items = domain.split(".")
            num = len(tmp_separate_domain_items)
            for i in range(num):
                separate_domains = tmp_separate_domain_items[i:]
                tmp_domain = ""
                for dom in separate_domains:
                    if dom == separate_domains[-1]:
                        tmp_domain += dom 
                    else:
                        tmp_domain += dom + "."
                res.append(tmp_domain)
            return res

        dic = {}
        for item in cpdomains:
            num =item.split(" ")[0]
            subdomains = getSubDomains(item.split(" ")[1])
            for domain in subdomains:
                if domain in dic:
                    dic[domain] += int(num)
                else:
                    dic[domain] = int(num)
        res_final = getStringArr(dic)
        return res_final
            
s = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print s.subdomainVisits(cpdomains)
        
        
                    