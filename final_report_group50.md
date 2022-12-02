# An Analysis of Heart Desease

### *Group memebers:*

- Colton Palfrey
- Justin Dilabio
- Mitchell Alexander

## **Introduction**

Because Heart disease is such a big problem in the United States, the data set we chose to analyze surrounds heart disease with data to calculate/analyze what factors in human health lead to an increased or decreased chance in heart disease. The data columns in our dataset include medical related tests such as high blood pressure and high cholesterol as well as data behind personal health choices such as smoker or non smoker and the patient's level of physical activity. This data set takes 22 columns of observations data into consideration and returns the tested results behind over 160 000 observations. These data are very well organized and will provide a great base for our project.

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

In my exploratory data analysis, I wanted to first get an idea of the range of this sample was. 

<img width="829" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc1.png">

The mean BMI value was 27.92, and most observations fell within plus/minus 5 of the mean. The distribution is also skewed to to the higher side. 

Next, I plotted the occurence frequency of stroke and heart attack/disease in the same plot. 

<img width="829" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc2.png">
From this plot, we can see that those most at risk of both events are those at very low BMI, around 10-18. From about 20, there seems to be a small but steady linear increase in rate. However stroke rates remain lower for BMI up to 30.

Finally, percentage rates of medical conditions were plotted as a function of BMI. 

<img width="829" alt="Screenshot 2022-12-01 at 2 14 53 PM" src="https://github.com/ubco-W2022T1-cosc301/project-group50/blob/main/images/sc3.png">

I can see from the plots, all explored occurences follow a similar pattern. They tend to increase sharply at very low bmi. Around BMI = 18 to BMI = 22, events are lowest and seem to gradually increase as BMI increases. However stroke rates remain low for BMI up to 30.

## How this EDA answers the research question
To begin, I plotted the BMI distribution of the population with which we are working. This revealed that in our sample, mos tof the individuals were within the 25-35 range, but a significant number of were above (see plot 1.1).

Next, to find who is most at risk of the recorded medical events int the dataset, I plotted the frequency of stroke and heart disease/attack (per 100 individuals) as a function of BMI. The shape of the plot revealed that those int the 10-17 range seemed to most frequently suffer from the medeical events. For Stroke, those between 20 and 30 were least at risk, and there was an linearly increasing risk as BMI increased. For heart attack/disease, those within the 20-25 range were the least at risk, and a linear increase was apparent beyond 25.

Finally, a similar process was done to explore who is most at risk of diabetes, high blood pressure and high cholesterol. Those in the 10-15 range tended to suffer significantly more than the average, but those on the higher side suffered of these at a higher frequency. The individuals least at risk were in the 18-22 range.

To answer my research question, from our data, those most at risk of medical events are the individuals in the 10-17 range, following by those with high BMI. Next, the people most at risk of the mentioned medical conditions were those with highest BMI, followed by those with very low BMI (10-15).

Putting everything in perspective, The association between BMI and health coditions is much higher than the association between BMI and health events(see figure 4.1). Both still have an apparent linear relationship.


## Analysis 3: Mitchell Alexander
 **Reasearch question:** What are the differences of health indicators between genders?


## **Conclusion**
