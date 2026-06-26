def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dict_list = []
    
    def make_words(current):
        if len(current) == 6:
            return
        
        dict_list.append(current)
        
        for v in vowels:
            make_words(current + v)
    
    for v in vowels:
        make_words(v)
    
    return dict_list.index(word) + 1