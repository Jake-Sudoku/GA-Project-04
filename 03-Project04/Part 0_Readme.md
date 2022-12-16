# Introduction

The year is 2013. There has been a recent epidemic of West Nile Virus (WNV) in the City of Chicago<a href="https://idph.illinois.gov/envhealth/wnvsurveillance12.htm" target="_blank"><sup>1</sup></a>. WNV is commonly transmitted to humans via the bite of an infected Culex mosquito. While most infected human cases report no symptoms, 1 in 5 patients develop symptoms ranging from a persistent fever, to inflammation of the brain or the spinal cord that can lead to paralysis and even, death. Those at highest risk of severe disease are older persons and those who are immunocompromised e.g going through chemotherapy. What exacerbates the situation are the lack of vaccine and specific therapy to treat West Nile disease<a href="https://www.cdc.gov/westnile/symptoms/index.html" target="_blank"><sup>2</sup></a>. The serious health implications and cost of seeking treatment presented a critical need for state intervention. 

The mosquito-borne virus was first detected among avian carcasses in the Windy City in 2001<a href="https://www.chicago.gov/content/dam/city/depts/cdph/statistics_and_reports/CDInfo_2013_JULY_WNV.pdf" target="_blank"><sup>3</sup></a>. As part of the state's efforts to manage WNV, the Chicago Department of Public Health (CDPH) has a two-pronged surveillance approach, namely <i>trap</i> and <i>spray</i>. Mosquito traps are set up around the city, and mosquitoes captured in these traps are then tested for the virus on a weekly basis from late spring through fall. Test results then inform the department of the next step of its control system; which is to emit airborne pesticides to control adult mosquito populations. However, it is clear that the current approach is not adequate, as it did not sufficiently detect the WNV-presence that led to the 2012 outbreak. Additionally, the current surveillance and control system imposes a large cost on the city, which can be chanelled to other important programmes. Hence, we need to look into the optimisation of the spray method to focus on areas with highest impact and spread which will help to alleviate the financial costs. 

Our job at the Disease And Treatment Agency, division of Societal Cures In Epidemiology and New Creative Engineering (DATA-SCIENCE) would thus be to interpret the historical data and find ways to optimise the current procedure. Our workflow is as follows: given weather and spray data as well as trap locations, develop a model with a recall score of at least 75%, which will accurately predict when and where WNV-infected mosquitos appear. 

A job well done will render critical assistance to the City of Chicago and the CDPH to work towards eradicating the potentially deadly virus, while allocating resources more efficiently.

# Model evaluation

Recall score is used as a measure of model performance in terms of correctly identifying the positive class out of all the actual positives. Recall is a more objective metric for imbalanced datasets and is also apt because of our greater interest in identifying true positives.Mathematically, Recall is the number of relevant documents retrieved by a search divided by the total number of existing relevant documents.

Optimizing for recall allows us to use the model to reduce the number of areas to spray while ensuring that we have a low miss rate on areas that actually have the West Nile Virus present. This is in line with the huge benefits that mosquito control has in terms of reducing various costs; from lost labor due to sick days up to massive medical costs and loss of life from potentially serious complications.

Random Forest emerged as the best model (Recall = 0.83) over the others in terms of test recall score. Random Forest cleared the benchmark KNN model (Recall = 0.25) by a large margin as well. While the other models built seemed to perform better in train and cross validation, their performance dips sorely on the test set, suggesting gross overfitting. These were hence not selected.


|Model|Train Recall|Test Recall|
|:---:|:---:|:---:|
|<font color="blue">Random Forest (tuned)</font>|<font color="blue">0.90</font>|<font color="blue">0.83</font>|
|||||||
|Logistic Regression (baseline)|0.82|0.68|
|||||||
|AdaBoost|0.88|0.76|
|||||||
|XGBoost|0.93|0.58|

# Cost Benefit Analysis

### Existing Efforts

The CDPH Environmental Health program has been performing targeted insecticide spraying of adult mosquitoes (adulticiding) from July through late August. The brand of adulticide used is Zenivex® and this is used at a rate of 1.5 fluid ounces per acre<a href="https://abc7chicago.com/archive/9206273/"><sup>4</sup></a>.

Our exploratory data analysis also suggest that spraying works to reduce incidence of WNV, likely through the mechanism of reducing the number of mosquitoes in an area.


### Implementation Costs
`Direct Cost: Cost of Adulticide` 

Zenivex costs \$299.80/gl.<a href="https://www.gfmosquito.com/wp-content/uploads/2017/07/2017-ND-Mosq.-Control-Quotes-Tabulation.pdf"><sup>5</sup></a> This translates to a cost of \$3.51 per acre, scaling up to **$526,851** if applied throughout Chicago (150,100 acres).

`Indirect Cost: Environmental Concerns`

While people may be concerned about the environmental and health impact of mosquito control, pesticides and their labeling are constantly under review and require approval from the US Environmental Protection Agency (USEPA) before use. This is done to protect public health and further ensures that application methods minimize the risk of human exposure as well as adverse environmental effects. In fact, there is generally no need to relocate during mosquito control fogging<a href="https://dph.illinois.gov/topics-services/environmental-health-protection/structural-pest-control/mosquito-spray-faqs.html"><sup>6</sup></a>. Potential health and environmental costs are as such minimal.

### Implementation Benefits
`Reduction in Medical Costs and Loss of Productivity`

The median medical cost for a patient with WNV non-neuroinvasive disease (vanilla WNV disease) was \\$4,467 while the median cost for a patient with acute flaccid paralysis (serious complication) was \$20,774<a href="https://www.ajtmh.org/view/journals/tpmd/90/3/article-p402.xml"><sup>7</sup></a> in the United States. Majority of the total costs were incurred as hospital charges.

On a larger scale, extrapolated findings of a study on 2003 WNV data estimates that hospitalized cases of WNV disease have an **annual burden of \$56 million** in the United States<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3945683/"><sup>8</sup></a>. Long-term direct and indirect medical costs after the initial illness can be extremely costly, depending on the severity of the illness and complications. While only a small subset of patients do end up with serious conditions, ranging from meningitis to acute flaccid paralysis, the costs to these individuals can easily runup to an amount much larger than the initial illness and hospitalization<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3945683/"><sup>9</sup></a>.

This also draws down on available healthcare resources and is not an ideal situation to be in for an entire 5-month season.

`Preventing Proliferation of Disease Vectors`

While Culex mosquitoes are unable to fly far and only 5.2% of populations actually carry WNV, letting them breed and feed freely during the peak season is a dangerous game to play. Most mosquito-borne diseases proliferate with increased mosquito count and host-vector contact, which implies exponentiation of WNV presence with increased host & vector density. Keeping mosquito populations low, especially in dense and urbanized areas is also an effective way to prevent further spread and maintenance of disease hotspots.


### Analysis

Taking into consideration the various costs and benefits of an effective spraying plan, the direct net benefits alone appear to amount in the millions. Additionally, indirect benefits such as peace of mind are hard to quantify but equally important. Constantly getting bitten by mosquitoes over 5 months isn't the most enjoyable experience either.

`Further Cost Savings`

In its current iteration, the seasonal mosquito spraying program in Chicago is already highly beneficial, particularly when compared to its cost. However, spraying efforts can be further streamlined to reduce direct costs.

Rather than the current spray and pray method, using our model as a guide to decide on spraying areas on demand can help to reduce costs by preventing overspraying. A Recall score of 0.83 implies that the model is quite capable in ensuring that areas with WNV are not missed. While the model isn't particularly high on precision, the extra cost of a false positive (extra spraying) is much lower than that of a false negative.

# Recommendations

1. Identify more precisely when mosquito season is about to pick up in Q3 of each year and remind citizens to keep up with their protective/preventive strategies.


2. Enhance on the ground surveillance for mosquito breeding grounds. As recommended to all states by the CDC, Chicago should also employ professionals to conduct inspections for mosquito breeding areas during the high season. This will help supplement adulticiding efforts.


3. Use the model as a preliminary guide in deciding spray areas. The model can be used to predict the possible presence of WNV based on weather and trap related observations to be collected by the surveillance team. This would guide efforts in identifying hotspots by narrowing down the search area

# Conclusions
### Summary
To recap our problem statement, as part of DATA-SCIENCE we are aiming to develop a model that can accurately predict the presence of WNV based on weather and temporal features to help Chicago and the CDPH more efficiently allocate resources to effectively prevent transmission of this harmful virus.

Key insights:

1. In general, the plots for 2007 and 2013 showed more sharp peaks and decline because WNV was more prevalent in these years as seen from the bar plot at the beginning of our analysis.

2. Temperature seems to play an important factor in the proliferation of WNV. Higher temperatures (>60 degrees fahrenheit) would contributes to higher prevalence of WNV and number of mosquitoes with WNV.

3. Lower average and resultant wind speed (<10 mph) contributes to higher number of mosquitoes and the prevalence of WNV.

4. Lower total precipitation (<1.0 inch) contributes to higher prevalence of WNV and number of mosquitoes with WNV.

5. Most importantly, areas around traps that were sprayed had lower incidence of WNV and number of mosquitoes.

Following exploratory data analysis, we proceeded to engineer some relevant features and built several models. Our Random Forest Classifier model was ultimately evaluated as the best performing for our purpose and was hence selected as the production model since it fulfilled both criteria outlined in the problem statement (Recall > 0.75 & better performance than baseline model). This selected model achieved a recall score of 0.80 on the hold-out test set with minimal data pre-processing and feature engineering required. 

Through a cost benefit analysis, we were able to deduce that the overall benefit brought through the implementation of a spray-based mosquito control program outweighs its costs by a large margin. The model we built is also able to help streamline these efforts by providing some guidance on potential hotspots and allowing for more precise prediction on the start of mosquito season. 

The project can be considered a success since the aims outlined at the start were achieved. We hope that our work will be used to inform important mosquito-control-related decisions and help the CDPH more efficiently allocate resources to effectively prevent transmission of this potentially deadly virus. Stay safe, Chicago.

### Future Directions
1. Projected costs of WNV prevention may differ for different years. This means that the cost benefit analysis should be reviewed from time to time.


2. The current dataset used in analysis and model building only focuses on weather features and trap-based data. Additional data might be useful in increasing the predictive ability of the model. One such example would be observations regarding reports on dead birds since WNV incubates in birds.


3. Some of the findings in our project can be included in educational materials to help the general public understand conditions favourable to culex mosquito breeding and hence WNV propagation.


4. This project is explicitly focused on spraying programs. Research into other mosquito-control methods can be done to supplement these efforts.
