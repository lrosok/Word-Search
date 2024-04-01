This python script takes a text file and a list of search terms and detects how many lines each search term appears in and creates an output file containing these lines for each search term. 

First, several functions are created that 1) remove punctuation and 2) detect a search term from a line of text. A nested for loop is then used to create output files for each term, detect lines containing the term, write these lines to the output file, and create a dictionary containing the number of lines each term appears in.
