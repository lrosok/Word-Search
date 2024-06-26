import string


# create function that removes punctuation
def clean_punc(source_str):
    lower_source = source_str.lower().split()
    list_nopunc = []
    for one_word in lower_source:
        one_word = one_word.strip(string.punctuation)
        list_nopunc.append(one_word)
    return list_nopunc


# create function that detects if a specific word (argument 2) is in a string (argument 1)
def detect_word(source_str, word_to_detect):
    lower_sourcestr = source_str.lower()
    lower_word = word_to_detect.lower()
    lower_source_no_punc = clean_punc(lower_sourcestr)
    if lower_word in lower_source_no_punc:
        return True
    else:
        return False


# open and read text file of interest
my_file = open('ThreeYearsinEurope.txt', 'rt', encoding='utf-8')
read_file = my_file.readlines()
# designate the terms you'd like to check for in the text file
search_terms = ['oxford', 'paris', 'london', 'quantum']
count = {}
# loop over each term and create an output file for each term
for term in search_terms:
    filename = term + '-results.txt'
    outfile = open(filename, 'wt', encoding='utf-8')
    if term not in count:
        count[term] = 0
# loop over each line in the text file and use detect_word() to find how many lines contain the term
# write lines containing the term onto its own text file and count the number of lines the term is in
    for line in read_file:
        if detect_word(line, term):
            outfile.write(line + '\n')
            if term not in count:
                count[term] = 1
            else:
                count[term] += 1
    outfile.close()
my_file.close()
print(count)
