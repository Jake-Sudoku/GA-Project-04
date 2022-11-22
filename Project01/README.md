# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Can Standardized Test Be Used As The Only Way To Reduce Drop Out?

## Project Description

The project was built as part of General Assembly's requirement to pass the course. This project showcase if the standardized test score can be used as the only way to reduce the number of drop out in university. The purpose of doing so is to uncover the relationship between these variables and to inform the university admissioners that the standardized test is not the only way to reduce the number of drop outs in university. Prior to the analysis, different datasets are carefully collected, cleaned and compared. Thereafter, I analyze and uncover the relationships between these few datasets. 
The insights of the project is that test scores and dropout rate are related to a certain extend and it can be used as a rough estimate to gauge how likely the students will drop out. There are also various factors that are more likely to affect the number of dropouts and it is not included due to the complexity of the issue.
The challenges that occur in this project are time constraint and the lack of background data on the students who dropped out.
In the future, I hope that I can implement features such as forecasting dropouts of student using of machine learning. 

---

## Table Content

- [Background](#Background)
- [Assumptions](#Assumptions)
- [Data Import & Cleaning](#Data-Import-&-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Visualization](#Data-Visualization)
- [Conclusions & Recommendations](#Conclusions-&-Recommendations)

---

## Background

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

These measures have also been used to measure the retention rate in students in university ([*source*](https://satsuite.collegeboard.org/media/pdf/national-sat-validity-study-overview-admissions-enrollment-leaders.pdf)). With student's tution fee as one of the university's source of revenue, higher retention rate in students means that university will have a more stable source of reveune. ([*source*](https://www.statista.com/statistics/240889/revenue-sources-of-us-higher-education-insitutions/)) 

Therefore, the target audience will be the finance administrators in the university to decide if the standardized test is the only way for predicting and reducing the number of dropouts.

---

## Problem Statement

To determine if standardized test is the only way for admissions process for predicting and reducing the number of dropouts.

---

## Assumptions

The assumptions made for this analysis are the following:
- Students have enough money to study for the entire university.
- Students who dropout are due to only acdamic reasons.
- Students always put in their best effort in each exam/tests.
- Since [SAT and ACT test are highly correlated](https://www.hartlandschools.us/documents/curriculum/PLAN-PSAT-ACT-SAT%20Assessment%20Correlations%20-%20Washtenaw%20ISD%202015.pdf) , either SAT or ACT scores will produce the similar results. For this analysis, SAT scores will be used.
- Dropout rates throughout the years are almost the same. ([*source*](https://educationdata.org/college-dropout-rates))

---

## Data Import & Cleaning

#### Datasets

There are 4 datasets are used. The below are the 4 datasets :

* [`Dropout_rates`](https://educationdata.org/college-dropout-rates): Dropout rates by State
* [`sat_2019.csv`](./data/sat_2019.csv): 2019 SAT Scores by State
* [`sat_2020.csv`](./data/sat_2020.csv): 2020 SAT Scores by State
* [`sat_2021.csv`](./data/sat_2021.csv): 2021 SAT Scores by State

The below are the steps that was done for data import and cleaning:
- create functions for cleaning;
- import libraries such as pandas, numpy, matplotlib.pyplot, scipy and seaborn;
- cleaning the data such as converting dictionary to dataframe, remove duplicates, check and remove missing values, convert values format into suitable format,rename headings and remove data not used for analysis;
- merge all 4 datasets into a file and saved it as csv format

#### Data dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**state**|object|SAT 2019|The state of United States.| 
|**p_rate_19**|float64|SAT 2019|The participation rate of the state for the SAT score(units percent to two decimal places 0.07 means 7%).| 
|**total_19**|int64|SAT 2019|The total SAT score of the state which consist of Math and Evidence-Based Reading and Writing (EBRW).| 
|**p_rate_20**|float64|SAT 2020|The participation rate of the state for the SAT score(units percent to two decimal places 0.07 means 7%).| 
|**total_20**|int64|SAT 2020|The total SAT score of the state which consist of Math and Evidence-Based Reading and Writing (EBRW).| 
|**p_rate_21**|float64|SAT 2021|The participation rate of the state for the SAT score(units percent to two decimal places 0.07 means 7%).| 
|**total_21**|int64|SAT 2021|The total SAT score of the state which consist of Math and Evidence-Based Reading and Writing (EBRW).| 
|**dropout_rate**|float64|[Source](https://educationdata.org/college-dropout-rates)|The drop out rate from university of the state (units percent to three decimal places 0.248 means 24.8%).| 

---

## Exploratory Data Analysis

This analysis consist of the following:
- Summary Stats
- States that have the highest and lowest participation rates for the 2019/2020/2021 SAT
- States that have the highest and lowest total scores for the 2019/2020/2021 SAT
- States that shows >50% participation on 2019/2020/2021 test
- States that have the highest and lowest dropout rate

---

## Data Visualization

The following are the visualization done:
- Triangle Heatmap
- Triangle Pair Gird
- Scattered Joint Plots
- Density Plot

---

## Conclusions & Recommendations

The key takeaway is that there is correlation between dropout with the total SAT scores by the students by a certain extent. This means that there are other highly more correlated factors that causes the dropout of university and further research is required.

Therefore, standardized test can only be **one of the ways** to predict and reducing the number of dropouts and it should be combined with other correlated factors for more accuracy.

In the future, I hope that I can implement features such as forcasting dropouts of student using of machine learning.

---