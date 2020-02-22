ABOUT

This code was created to aid me in a section of my research where I analyze and categorize student responses for an intro level physics course. Each student would be asked to fill out multiple choice responses and then provide a few sentences explanation for their choice. This code takes student responses and preps them to be input into a natural language processing program to help me categorize student responses faster.

Edit
This project has been put on hold for the time being.
----------------------------------------------------------------------------------------
ABOUT THIS CODE

This code takes in a csv file containing student responses and "cleans" the data to make it easier for the NLP program to categorize the responses. This is done by first removing all stop words from each response and splits the texts back into sentences. Next the responses have punctuation and numbers removed as well as making all letters lowercase. This breaks down each response to a very basic, albeit grammatically incorrect, form of English that a NLP can understand.