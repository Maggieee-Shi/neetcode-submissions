class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        dic=defaultdict(list)
        for string in strs:
            s=[0]*26
            for letter in string:
                s[ord(letter)-ord("a")]+=1
            dic[tuple(s)].append(string)
        return [v for k,v in dic.items()]
        #create a dic to hold a key to identify anagram
        #build the list of 26 chars
        #make the list as key and string as value
        #append each as our result

            