try:
    with open("sample.txt", "r", encoding="utf-8")  as file:
        text = file.read()
    words = text.split()

    word_count = {}     #empty dictionary bnaya h
    for word in words:    #iska kaamhar word ko count krna h
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    #print(word_count)      #dictionary print krta h

                                               #key = get_count bhi kr skte h
                                               #sorting kis basis pr krni h
    sorted_words = sorted(word_count.items(), key = lambda x: x[1], reverse = True)      #sorted() build in function h
                           #.items() - keys or values dono deta h        descending order me sort krna
    print("\nMost Common Words\n")
    for word, count in sorted_words:
        print(f"{word} : {count}")
             # word me word store hota h or count me frequency
except FilenotFoundError:
    print("Error: sample.txt didn't found the file")