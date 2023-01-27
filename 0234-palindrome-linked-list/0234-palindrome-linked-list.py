class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
            
        # check for palindrome
        if ls == ls[::-1]:
            return True
        else: 
            return False
        
        