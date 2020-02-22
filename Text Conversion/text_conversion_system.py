# imports
import pandas as pd
import string as str
import time
import gensim
#nltk imports
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
#gensim imports

#-----------------------------------------------------------------
# start the clock
start = time.time()

# reading in the data
data_1 = pd.read_csv('example_text.csv')

# mask the example data
data = data_1['Student Responses']
codes = data_1['FinalCode']
#-----------------------------------------------------------------
# prepping the data for the model

# function to remove stopwords
stop_words = stopwords.words('english')
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

# splitting the text into sentences
student_responses = []
data_length = len(data)
for i in range(data_length):
    student_responses.append(sent_tokenize(data[i]))

clean_student_responses = []
for i in student_responses:
    # remove punctuations and numbers
    resp = pd.Series(i).str.replace("[^a-zA-Z]", " ")
    # make alphabets lowercase
    resp = [s.lower() for s in resp]
    #remove stopwords
    resp = [remove_stopwords(r.split()) for r in resp]
    # append responses to larger list
    clean_student_responses.append(resp)

clean_student_responses = pd.DataFrame(clean_student_responses)
print(clean_student_responses)
#-----------------------------------------------------------------
# end the clock
end = time.time()
print('Total time:',end - start)
#-----------------------------------------------------------------
# Sources

# https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com
# http://kavita-ganesan.com/gensim-word2vec-tutorial-starter-code/
# https://stackoverflow.com/questions/10121926/initialise-numpy-array-of-unknown-length
# https://kanoki.org/2019/03/07/sentence-similarity-in-python-using-doc2vec/
