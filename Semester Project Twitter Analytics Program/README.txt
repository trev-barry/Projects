ABOUT

This code was developed as an end of the semester project for one of my intro level python courses. This code utilizes a a linear regression model to predict the number of likes on a tweet and was run against my own twitter data from 2014 to 2018. This data includes information such as number of likes, use of media, number of characters, number of retweets, and if the post used tagging or not. I then used this model to predict the number of likes I would receive on a future tweet and the model was accurate to within 7%.
----------------------------------------------------------------------------------------------------
ABOUT THE CODE

This code uses scipy to fit a curve to my linear regression model. The model takes in four variables, number of retweets, media usage, tweet length, and use of tagging to predict the number of likes on any tweet. I chose to run this regression model because I was personally curious to see if there were any characteristics of the tweets that I produce that influence my followers to like a tweet or not. I found that number of retweets poetically impacted likes where tagging negatively influenced likes to the same degree as number of retweets.
----------------------------------------------------------------------------------------------------
LIBRARIES USED

IPython
matplotlib
numpy
pandas
scipy