#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys
import numpy as np
import pandas as pd 
import nltk
import string


# In[2]:


text_files = [f for f in os.listdir("C:/Users/Abhi/Desktop/stats and ml/scraped100") if f.endswith(".txt")]


# In[3]:


os.getcwd()


# In[4]:


text_files


# In[5]:


from nltk.tokenize import sent_tokenize, word_tokenize


# In[6]:


word_tokenize(text_files[99])


# In[7]:


folder_path = "C:/Users/Abhi/Desktop/stats and ml/scraped100"

# Create an empty dictionary to store the tokenized data
tokenized_data = {}

# Loop through each file in the folder
for file in os.listdir(folder_path):
    if file.endswith('.txt'):
        # Read in the file and tokenize the text into sentences
        with open(os.path.join(folder_path, file), 'r') as f:
            text = f.read()
            sentences = nltk.sent_tokenize(text)
        # Save the tokenized sentences in the dictionary
        tokenized_data[file] = sentences

# Print the tokenized data
print(tokenized_data)


# In[8]:


newtokenized= tokenized_data


# In[9]:


def word_tokenize_whitespace(text):
    return text.split()

word_tokenized_data = {}
# Loop through the files in the dictionary
for file_name, sentences in newtokenized.items():
    # Create an empty list to store the word-tokenized sentences
    word_tokenized_sentences = []

    # Loop through the sentences in the file
    for sentence in sentences:
        # Tokenize the sentence into words
        words =[word.strip(string.punctuation) for word in word_tokenize_whitespace(sentence) if word]
        words = [word for word in words if word]
        # Add the word-tokenized sentence to the list
        word_tokenized_sentences.append(words)

    # Add the list of word-tokenized sentences to the dictionary
    word_tokenized_data[file_name] =[sentence for sentence in word_tokenized_sentences if sentence]

# The dictionary now contains word-tokenized data
print(word_tokenized_data)


# ## 7. Personal Pronouns

# In[10]:


import re


# Regular expression pattern for personal pronouns
pattern = r'\b(I|you|he|she|they|we|my|us|ours)\b'

# Create a dictionary of flattened lists for each key
flattened_dict = {key: ' '.join(' '.join(sublist) for sublist in value) for key, value in word_tokenized_data.items()}

# Concatenate the flattened lists into a single list
flattened_list = ' '.join(flattened_dict.values())

# Use dictionary comprehension to find the count of personal pronouns for each key
result = {key: len(re.findall(pattern, flattened_dict[key])) for key in word_tokenized_data.keys()}

# Print the result dictionary to check the counts
print("Result dictionary:", result)


# In[11]:


new_word_token = word_tokenized_data
new_word_token


# # 1. SENTIMENTAL  ANALYSIS :-

# ### 1.1) cleaning tokenized words using stopwords

# In[12]:


stopwords = set()
stopwords_folder = "C:/Users/Abhi/Desktop/stats and ml/data set-20230603T103433Z-001/StopWords-20240323T133504Z-001/StopWords"
for file in os.listdir(stopwords_folder):
    if file.endswith('.txt'): 
        with open(os.path.join(stopwords_folder, file), 'r') as f:
            for line in f:
                stopwords.add(line.strip().lower())


# In[13]:


stopwords


# In[14]:


len(stopwords)


# In[15]:


print(type(new_word_token))
print(type(stopwords))


# In[16]:


#stopwords{}
for key, value in new_word_token.items():
    new_word_token[key] = [list(filter(lambda x: x not in stopwords, inner_list)) for inner_list in value]
print(new_word_token)


# ### 1.2) creating dictionary of positive and negative words
# 

# In[17]:


# Define the dictionary
positive= [] 
negative = [] 

# Define the paths to the text files
pos_file = 'C:/Users/Abhi/Desktop/stats and ml/data set-20230603T103433Z-001/MasterDictionary-20240323T133516Z-001/MasterDictionary/positive-words.txt'
neg_file = 'C:/Users/Abhi/Desktop/stats and ml/data set-20230603T103433Z-001/MasterDictionary-20240323T133516Z-001/MasterDictionary/negative-words.txt'

# Check if the files exist
if os.path.isfile(pos_file) and os.path.isfile(neg_file):
    # Open the files and read the contents
    with open(pos_file, 'r') as f:
        pos_words = f.read().strip().split('\n')

    with open(neg_file, 'r') as f:
        neg_words = f.read().strip().split('\n')
positive = list(set(pos_words))
negative = list(set(neg_words))

# Print the dictionary
print(positive)
print("----" *30, sep = ' ')
print(negative)


# ### 1.3) extracting derived variables- positive score, negative score, polarity score, subjectivity score

# In[18]:


positive_score = []
negative_score = []
polarity_score = []
subjectivity_score = []


# In[19]:


new_wtoken = {key: [item for sublist in value for item in sublist] for key, value in new_word_token.items()}
print(new_wtoken)


# In[20]:


# Initialize the count variable and the new_list

positive_score = []
# Iterate over each key-value pair in the new_wtoken dictionary
for key, value in new_wtoken.items():
    # Initialize a temporary list to store the common words
    common_words = []
    count = 0
    # Iterate over each word in the value list
    for word in value:
        # Check if the word is in the positive dictionary
        if word in positive:
                # If it is, add it to the common_words list

            common_words.append(word)
            print(f"Common word found in {key}: {word}")
            print(word)
    # After checking all the words in the value list, update the count variable and append it to the new_list
    count += len(common_words)
    positive_score.append(count)

# Now, the new_list contains the total number of common words for each key's value list
print(positive_score)# Output: [1, 2, 3]


# In[21]:


len(positive_score)


# In[22]:



# Initialize the count variable and the new_list

negative_score = []

# Iterate over each key-value pair in the new_wtoken dictionary
for key, value in new_wtoken.items():
    # Initialize a temporary list to store the common words
    common_words_n = []
    ncount = 0
    
    # Iterate over each word in the value list
    for word in value:
        # Check if the word is in the positive dictionary
        if word in negative:
            # If it is, add it to the common_words list
            common_words_n.append(word)
            
    # After checking all the words in the value list, update the count variable and append it to the new_list
    ncount += len(common_words_n)
    negative_score.append(ncount)

# Now, the new_list contains the total number of common words for each key's value list
print(negative_score)  # Output: [1, 2, 3]


# In[23]:


print(len(negative_score))


# In[24]:


polarity_score = []
# calculating polarity score
polarity_score = [(pos - neg) / ((pos + neg) + 0.000001) for pos, neg in zip(positive_score, negative_score)]
print(polarity_score)


# In[25]:




# Initialize a dictionary to store the word count for each key
total_clean_word = []

# Iterate through each key in the dictionary
for key in new_wtoken:
    # Initialize the word count for the current key to 0
    count = 0
    # Iterate through each word in the list for the current key
    for word in new_wtoken[key]:
        # Increment the word count by 1
        count += 1
    # Add the word count for the current key to the word_count dictionary
    total_clean_word.append(count)

# Print the word count for each key
print(total_clean_word)


# In[26]:


subjectivity_score = []
for i in range(len(positive_score)):
    sub_score = (positive_score[i] + negative_score[i])/(total_clean_word[i]+ 0.000001)
    subjectivity_score.append(sub_score)
print(subjectivity_score)  


# ## 2. ANALYSIS OF READABILITY

# In[27]:


nwt = new_word_token
average_sentence_length = [] # initialize an empty list to store the average sentence length for each key

# iterate over each key in the dictionary
z = 0
for key in nwt:
    #words = sum(nwt[key], []) # flatten the lists of words for this key into a single list
    #num_words = sum(len(word) for word in words) # calculate the total number of words for this key
    num_sentences = len(nwt[key]) # calculate the total number of sentences for this key
    asl = total_clean_word[z] / num_sentences if num_sentences != 0 else 0 # calculate the average sentence length for this key
    average_sentence_length.append(asl) # append the average sentence length to the list
    z +=1
print(average_sentence_length)
print(total_clean_word[99])


# In[28]:



def syllable_count(word):
    #word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"): #or word.endswith("es"):
        count -= 1
    if count == 0:
        count += 1
    return count

def complex_word_count(nwt):
    """Returns the count of complex words in the nwt dictionary."""
    complex_word = []
    for key in nwt:
        num_complex_words = 0
        for sentence in nwt[key]:
            for word in sentence:
                if syllable_count(word) > 2 and (not word.endswith("es") and not word.endswith("ed")):
                    num_complex_words += 1
        complex_word.append(num_complex_words)
    return complex_word


# In[29]:


complex_word = complex_word_count(nwt)
print(complex_word)


# In[30]:


# percentage of complex words as per your formula
per_complex_word = [] 
for c in range(len(complex_word)):
    pcw = (complex_word[c]/total_clean_word[c]) if total_clean_word[c]!=0 else 0
    per_complex_word.append(pcw)
print(per_complex_word)
#print(num_of_word[99])


# In[31]:


# fog index
fog_index = []
for f in range(len(per_complex_word)):
    foi = 0.4*(average_sentence_length[f] + per_complex_word[f])
    fog_index.append(foi)
print(fog_index)    


# ## 3. Average Number Of Words Per Sentence
# 

# In[32]:


avg_words_per_sent = average_sentence_length
avg_words_per_sent


# ## 4. complex word count

# In[33]:


complex_word


# ## 5. Word Count

# In[34]:


total_clean_word # in this variable we have store word count of each key after performing stopwords list on it


# ## 6. Syllable Count Per Word

# In[35]:


'''
directory = 'C:/Users/Abhi/Desktop/stats and ml'
def syllable_count(nwt, directory):
    for word, definition in nwt.items():
        s_count = syllable_count(nwt, directory)
        file_name = f"{word}_syllable_count.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as file:
            file.write(str(s_count))
            '''


# In[36]:


#syllable_count(nwt,directory)


# ## 8. Average Word Length
# 

# In[37]:


sum_total_char_each_word = []
avg_word_length = []
for key in nwt:
    words = sum(nwt[key], [])
    num_words = sum(len(word) for word in words)
    sum_total_char_each_word.append(num_words) 
for b in range(len(total_clean_word)):
    avg = (sum_total_char_each_word[b]/total_clean_word[b]) if total_clean_word[b]!=0 else 0
    avg_word_length.append(avg)
print(avg_word_length)
print('\n')
print(sum_total_char_each_word)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




