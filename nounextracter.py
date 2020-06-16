import nltk
import docx

try:
    #reading document filr
    doc = docx.Document('./try.docx')
    fullText = []
    #Extracting text from file and storing them in one string varibale
    for para in doc.paragraphs:
        fullText.append(para.text)

    fullText = ''.join(fullText)

    #Removing unwanted characters from documents
    char_to_remove = '!,()[]@$%^*.;:=><-'

    for char in char_to_remove:
        fullText = fullText.replace(char," ")

    #lambda function to check if the worrd is noun
    is_noun = lambda x: x[:2] == 'NN'

    #tokeninzing the string for analysis
    tokenized = nltk.word_tokenize(fullText)

    nouns = [word for (word,x) in nltk.pos_tag(tokenized) if is_noun(x)]

    print(nouns)
    ##Exporting the nouns in text file
    with open('./output.txt','w') as fp:
        for noun in nouns:
            fp.write("%s\n" % noun)
except e:
    print(e)

#print(fullText)