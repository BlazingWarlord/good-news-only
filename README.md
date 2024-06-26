# GoodNewsOnly

News is something that we see everyday. Many times, it may be negative and disturbing. The GoodNewsOnly project was developed to find the headlines of the day, and provide only the positive or inspiring news headlines, providing a satisfying read for a user.

The app was built with Python, and hosted with Flask. The google-news-feed module was used to extract news headlines live, and the hugging-face transformers module's sentiment analysis pipeline was used to classify headlines on positivity and negativity level. There is also a second classification level which removes all headlines with a set of pre-defined negative words list, containing words that generally hint to negative news. 

Finally, Flask was used to host it with a basic html file to provide a frontend, connected to the app for the backend.


