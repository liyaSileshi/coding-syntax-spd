#4, Given a string of text and a number k,
# find the k words in the given text that 
# appear most frequently. Return the words 
# in a new array sorted in decreasing order.


#input: text=  ‘one fish two fish blue fish red fish’ k=2
#find the k(2) most frequent words that are in the text

#histogram of all the words
#sort a dict by the value



def hist_text(text, k):
    text_hist = {} #make a histogarm out of the text
    text_arr = text.split(' ')
    for i in text_arr:
        # if i is in the hist
        # increment by 1
        if i in text_hist:
            text_hist[i] += 1
        # if not make a key and assign it to 1
        else:
            text_hist[i] = 1
 
    text_hist = sorted(text_hist.items(), key= lambda x: x[1], reverse=True)
    
    sub_text = text_hist[:k]
    return sub_text

text=  "one fish two fish blue fish red fish red"
print(hist_text(text, 2))