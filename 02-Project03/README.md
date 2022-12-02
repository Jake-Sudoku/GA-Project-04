# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Webscraping from Reddit : Depression vs Anxiety

## Project Description

The project was done as part of General Assembly's requirement to pass the course. The aim of this project is to identify and classify two different subreddit post using Natural Language Processing (NLP). To achieve it, I have to do webscraping, clean data and preprocess data, Exploratory Data Analysis (EDA) and training various model to predict and identify the subreddit post. A model accuracy of 82% was achieved for this project. 

---

## Table Content

- [Background](#Background)
- [Problem Statement](#Problem-Statement)
- [Assumptions](#Assumptions)
- [Import Libraries](#Import-Libraries)
- [Functions](#Functions)
- [Web Scraping](#Web-Scraping)
- [Data Cleaning and EDA](#Data-Cleaning-and-EDA)
- [Preprocessing & Modeling](#Preprocessing-&-Modeling)
- [Conclusions & Recommendations](#Conclusions-&-Recommendations)

---

## Background

According to Bachmann S. Epidemiology of Suicide and the Psychiatric Perspective, most suicides are related to psychiatric disease, with depression, substance use disorders and psychosis being the most relevant risk factors. In view of this statistic, a newly developed social media application, Chipper, has implemented a new feature where users are able to report other users' posts for suspected mental health issue so that they will be able to provide help to these users before it is too late. As a data scientist working in this company, I am tasked to train a classifier that will categorise posts that were reported for mental health issues into either Anxiety or Depression so that we are able to route these users to its appropriate helpline. To train the classifier, I will be using posts from Reddit's r/Anxiety and r/Depression subreddits as proxy data.
 
---

## Problem Statement

To correctly classify post from the correct subreddit for Chipper to route the users to its appropriate helpline.

---

## Assumptions

The following are the assumptions made:

- all data analysed are based on the time where the data was scrapped,
- the target audiences consist of a mix of technical and non-technical background,
- due to the time and hardware limitations, we are unable to perform a live data monitoring and analysis,
- photos, vidoes and emojis from the post are ignored and removed from our analysis,
- missing data are removed from our analysis.

---

## Import libraries

The libraries that I have import are for webscraping, data import, data cleaning, eda and modeling. 

---

## Functions

The functions that I have created are for webscraping and data cleaning. 

---

## Webscraping

For webscraping, it conconsist of the number of post that was scrapped, the time it took and the date where it was scrapped. It also consist of the location of the saved dataset.  

---

## Data Import & Cleaning

#### Datasets

There are 3 datasets are used. The below are the 3 datasets :

* [`depression_data.csv`](./00-datasets/depression_data.csv): Depression dataset that was scraped from reddit using PushShift.
* [`anxiety_data.csv`](./00-datasets/anxiety_data.csv): Anxiety dataset that was scraped from reddit using PushShift.
* [`combined_dataset.csv`](./00-datasets/combined_dataset.csv): Combined dataset from both depression and anxiety dataset.

The below are the steps that was done for data import and cleaning:
- create functions for cleaning;
- import libraries such as pandas, numpy, matplotlib.pyplot, shapy, sklearn , warnings, and seaborn;
- cleaning the data such as converting dictionary to dataframe, remove duplicates, check and remove missing values, convert values format into suitable format, remove missing values,lemmatize words,remove punctation ,rename headings and remove data not used for analysis;

#### Data dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**target**|int64|Depression and Anxiety|The target for the dataset where 0 is the depression dataset and 1 is the anxiety dataset. The purpose of this feature is for modeling the y variable.| 
|**title+selftext_n_stopwords**|object|Depression and Anxiety|The title and text with no stopwords. The purpose of this feature is for modeling the x variable compare which x variable gives a better accurate score.| 
|**title+selftext_lemmatizing**|object|Depression and Anxiety|The title and text that has been lemmantized. The purpose of this feature is for modeling the x variable compare which x variable gives a better accurate score.| 
|**title+selftext_all_clean**|object|Depression and Anxiety|The title and text that has been cleaned. The purpose of this feature is for modeling the x variable compare which x variable gives a better accurate score.| 
|**title_lemmatizing**|object|Depression and Anxiety|The title that has been lemmantized. The purpose of this feature is for modeling the x variable compare which x variable gives a better accurate score.| 
|**text_lemmatizing**|object|Depression and Anxiety|The text that has been lemmantized. The purpose of this feature is for modeling the x variable compare which x variable gives a better accurate score.| 

---

## Exploratory Data Analysis

From the Data Analysis, I have found out :
- both depression and anxiety plot is right-skewed distribution. It might be from the [start-up effects.](https://www.itl.nist.gov/div898/handbook/eda/section3/histogr6.htm)
- alot of depressed people wants to communicate on how they feel on the reddit. There is a possiblu that they want someone to have a [listening ear.](https://dailyburn.com/life/lifestyle/depression-awareness-month-help/)
- alot of anxious people wants to communicate on how they feel on the reddit. There is a possible that they want [to be heard.](https://www.healthline.com/health/high-functioning-anxiety-want-you-to-know#6.-I-just-want-to-be-heard.) It is slightly different from the depressed people where they want a listening ear.

---

## Data Visualization & Modeling

The following are the visualization done:
- Histogram
- Bar Chart
- Word Cloud
- ROC Curve

The follwing are the modeling done:
- Count Vectorizer : Naive Bayes Bernoulli , Multinomial Logistic, Random Forest, AdaBoost and Gradient Boosting
- Count Vector Ngram: Naive Bayes Bernoulli , Multinomial Logistic, Random Forest, AdaBoost and Gradient Boosting
- TF-IDF : Naive Bayes Bernoulli , Multinomial Logistic, Random Forest, AdaBoost and Gradient Boosting

---

## Conclusions & Recommendations

To conclude, my model can correctly classify post from the correct subreddit with a accuracy of around 82%. It means that for every 10 post, my model can correctly identify 8 correct posts.
The recommendations based on this results is to use this model to find list of post and route these users to its appropriate helpline.

---