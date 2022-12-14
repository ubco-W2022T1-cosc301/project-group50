# An Analysis of Heart Disease

### *Group memebers:*

- Colton Palfrey
- Justin Dilabio
- Mitchell Alexander

## **Introduction**

Because Heart disease is such a big problem in the United States, the data set we chose to analyze surrounds heart disease with data to calculate/analyze what factors in human health lead to an increased or decreased chance in heart disease. The data columns in our dataset include medical related tests such as high blood pressure and high cholesterol as well as data behind personal health choices such as smoker or non smoker and the patient's level of physical activity. This data set takes 22 columns of observations data into consideration and returns the tested results behind over 250 000 observations. These data are very well organized and will provide a great base for our project.

## **Exploratory Data Analysis**

Having chose a very rich dataset with lots of possibility for reasearch questions we were left with a variety of information that could be obsereved for our EDA. We explored things such as the total number of people with heart problems, the mean BMI value, the total number of women and men, and the number of rows and columns we were dealing with along with the number of unique values in each row.  
<img width="786" alt="Screenshot 2022-12-01 at 1 42 10 PM" src="https://user-images.githubusercontent.com/101154480/205165083-0d3bcb0c-328a-49e3-981a-9dcf71f6e47e.png">
<img width="213" alt="Screenshot 2022-12-01 at 2 35 18 PM" src="https://user-images.githubusercontent.com/101154480/205173802-530d8ace-16d4-4c58-9f05-2fb2befce9de.png">

Going into our EDA we also looked into the specific questions thats were asked to survey recepients to get these results which were the following:
* **HeartDiseaseorAttack:** Adults who have have a heart disease or a heart attack at some point.
* **HighBP:** Adults who have been told they have high blood pressure by a doctor, nurse, or other health professional.
* **HighChol:** Adults who have been told they're Cholesterol is high by a doctor, nurse or other health professional.
* **CholCheck:** Adults who have had a Cholesterol check within past five years.
* **BMI:** Calulated Body Mass Index.
* **Smoker:** Adults who have smoked at least 100 cigarettes in their entire life.
* **Stroke:** Adults who have had a stroke.
* **Diabetes:** 0 = no diabetes, 1 = pre-diabetes, 2 = diabetes. (later filtered to diabetes or no diabetes on a 0-1 scale)
* **MentHlth:** On a scale of 0-30 answering how many days in the last 30 days the subject felt stress, depression, or problems with emotions.
* **PhysHlth:** Including physical illness and injury how many days in the last 30 days were recepients physical health not good.
* **Age:** On a scale of 1-13 with each integer representing a different age group as filtered below.
* **Fruits/Veggies:** Consumes fruits of veggies atleast once daily.
* **HvyAlcoholConsump:** Adult men having more than 14 drinks per week and adult women having more than 7 drinks per week.
* **DiffWalk:** Those who have serious difficulty walking or climbing stairs.
* **GenHlth:** Recepient rating their health a scale of 1-5.
* **AnyHealthcare:** Whether or not recepient has access to any form of health care.
* **NoDocbcCost:** Whether or not recepient has no doctor because of the high cost.

<img width="380" alt="Screenshot 2022-12-01 at 1 53 22 PM" src="https://user-images.githubusercontent.com/101154480/205167873-7d2aad36-cee1-4ca2-8664-15608bfc4bb7.png"><img width="387" alt="Screenshot 2022-12-01 at 2 45 11 PM" src="https://user-images.githubusercontent.com/101154480/205174941-f191597c-4c75-4b10-a97f-2cb4cb19f18f.png">

Conducting this analysis gave us alot more insight into how we were going to be able to work with our data as we now knew more about things like the frequency of health factors and how the data could be used.



## Analysis 1: Colton Palfrey
 **Reasearch question:** What health factors relate the most to Heart problem/heart attacks?

For my research question I wanted to be able to figure out which of the data columns in our dataset coincided with the highest number of heart problems/heart attacks. Before beggining my analyses I had high predictions that recepients who had heart issues would also have had a high chance of having other health isseus such a stroke, high Cholesterol, Diabetes, or even a lack of physical activity. With my analysis complete and my diagrams to prove so I learned that recepients with heart problems had almost no notable coralation to strokes or diabetes and Instead I was able to see that smoking, high colesterol, and High blood pressure have the largest effect on those with heart conditions. My data showed that almost every single recepient with heart related issues received fequent Colesterol checks with many of them often returning a high colesterol value.

**Diagram 1:** Observing the graph below it appears as though people that have high blood pressure, high collesterol, and that are smokers all place very high in heart desease victims. I found these factors to all make alot of sense as these are all contributing factors to having lower health.

<img width="754" alt="Screenshot 2022-12-01 at 2 14 21 PM" src="https://user-images.githubusercontent.com/101154480/205171363-aa2f50f3-baa6-43c3-9362-feb3f422b35e.png">

**Diagram 2:** Observations can be made off this next graph following the recepients who answered no as it appears as though most people with heart problems are not heavy drinkers and many have also never had a stroke or have diabetes. This is a telling factor that heart problems aren't highly related to the likelihood of someone having a stroke or being insulin dependent.

<img width="829" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://user-images.githubusercontent.com/101154480/205171347-0473739e-88ce-4451-abdd-f2f08e263f9e.png">

**Wanting to see more on analysis 1?**
[find the full analysis notebook here, including the code and the data here!](https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/notebooks/analysis1.ipynb)

## Analysis 2: Justin Dilabio


 **Reasearch question:** At which BMI are people most most at risk of medical events and conditions?
 
---
For this portion of our analysis, I looked into the relationship between medical coditions and events and BMI, to answer the question above.
### events/conditions iclude:
- stroke
- heart disease/heart attack
- high cholesterol
- diabetes 

To begin, I plotted the BMI distribution of the population with which we are working. This revealed that in our sample, mos tof the individuals were within the 25-35 range, but a significant number of were below (see plot 1.1).

<img width="720" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc1.png">



Next, to find who is most at risk of the recorded medical events int the dataset, I plotted the frequency of stroke and heart disease/attack (per 100 individuals) as a function of BMI. The shape of the plot revealed that those int the 10-17 range seemed to most frequently suffer from the medical events. For Stroke, those between 20 and 30 were least at risk, and there was an linearly increasing risk as BMI increased. For heart attack/disease, those within the 20-25 range were the least at risk, and a linear increase was apparent beyond 25.

<img width="720" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc2.png">


Finally, a similar process was done to explore who is most at risk of diabetes, high blood pressure and high cholesterol. Those in the 10-15 range tended to suffer significantly more than the average, but those on the higher side suffered of these at a higher frequency. The individuals least at risk were in the 18-22 range.

<img width="720" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc3.png">


To answer my research question, from our dataset, those most at risk of medical events are the individuals in the 10-17 range, followed by those with high BMI. Next, the people most at risk of the mentioned medical conditions were those with highest BMI, followed by those with very low BMI (10-15).

Putting everything in perspective, The association between BMI and health coditions is much higher than the association between BMI and health events. Both still have an apparent linear relationship.
Click [here](https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/notebooks/analysis2.ipynb) to view the techniques and code used to conduct my EDA.

## Analysis 3: Mitchell Alexander
 **Reasearch question:** What are the differences of health indicators between genders, and which gender is on average more unhealthy?

Before conducting my research analysis I was curious about the differences in health indicators between men and women. I decided to focus my analysis on the columns which showed a binary 1 (yes) and 0 (no) for having the specified health issue. The columns of focus for my data analysis were HeartDiseaseorAttack, HighBP(High Blood Pressure), HighChol (High Cholesterol), Stroke, Diabetes, and DiffWalk (Difficuly Walking up Stairs). Therefore the other collumns were filtered out.
I wanted the data to look more presentable so I changed the column names to be more understandible, and changed the values of gender from 0 to 'Women' and 1 to 'Men'. I also changed the values of the health indicators from 0 to 'No' and 1 to 'Yes'. I wanted to see how many people were in each gender so I created two subsets of the original csv file 

<img width="588" alt="2022-12-02 (2)" src="https://user-images.githubusercontent.com/114033686/205422134-bbc45a4e-865c-41c2-b78e-a647ec7b10e9.png">

<img width="624" alt="2022-12-02 (3)" src="https://user-images.githubusercontent.com/114033686/205422140-4e49510c-0b77-4214-80b7-f7fd38ad42f7.png">


This helped me gain an understanding that there where in fact more women then men which was important to take in account going forward with the analysis

![M Wdifference](https://user-images.githubusercontent.com/114033686/205422214-a2d8e83e-87a1-4e1f-a885-c3161b440f2d.png)



I then plotted the distribution of people who did and did not have each specific health issues in both genders. To avoid an ecsessive anpount of images I've added a link where you can see these plots in my data analisis in [my notebook here](https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/notebooks/analysis3.ipynb)

It was hard to notice at first but with taking in account the difference in the amount of people in each gender, it became apparent that the ratio of men who had health issues versus those who didnt was greater than that of women. this was true for almost every column other than DifficultyWalkingUpStairs which seemed equally porportional to each other.

Therefore I was able to conclude my research question and determine that men had on average more health issues than women.

## **Conclusion**

This project had 3 research questions:
 1. What health factors relate the most to Heart problem/heart attacks?
 1. At which BMI are people most most at risk of medical events and conditions?
 1. What are the differences of health indicators between genders?
 
To answer the first question, Colton plotted some determinants of health against the number of people with heart problems as well as the same determinants, against the count of those who have no had heart problems. From his EDA, Colton was able to conclude that smokers, those with high cholesterol and those with high blood pressure all appeared to have an increased risk of heart disease. Those who have not had a stroke, do not have diabetes, and those who are no heavy drinkers are less likely to experience heart problems. 

To answer Question 2, Justin Plotted rates of stroke, heart attack/disease, diabetes, high blood pressure and high cholesterol against BMI. He was able to pull from his EDA that those at risk of all of these are thos at very low BMI, and those at very high. 

To asnwer the third question, Mitchell plotted the count of those with health issues grouped by gender. From his analysis, he was able to determine that for almost every negative health indicator, men represented a higher percentage of occurences.
