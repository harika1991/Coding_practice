class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        words_1={}
        words_2={}
        counter=0
        words_final=[]
        word_list={}
        for word in words1:
            if word in words_1:
                words_1[word]+=1
            else:
                words_1[word]=1
        for x in words_1:
            if words_1[x]==1:
                words_final.append(x)
        
        for word in words2:
            if word in words_2:
                words_2[word]+=1
            else:
                words_2[word]=1
        for x in words_2:
            if words_2[x]==1:
                words_final.append(x)
        
        #print words_final
        for word in words_final:
            if word in word_list:
                word_list[word]+=1
            else:
                word_list[word]=1
        for word in word_list:
            if word_list[word]==2:
                counter+=1
        # print final_list
        return counter
        
