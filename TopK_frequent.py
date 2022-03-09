        word_list={}
        for word in words:
            if word in word_list:
                word_list[word]+=1
            else:
                word_list[word]=1
        sorted_list = sorted(word_list.items(),key=lambda x:(-x[1],x[0]))
        # print sorted_list
        final_list= [h for h,v in sorted_list[:k]]
        # print final_list
        print final_list
        
