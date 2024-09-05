class Solution(object):
    def defangIPaddr(self, address):
        newAddress = list(map(str, address.split('.')))
        return '[.]'.join(newAddress)