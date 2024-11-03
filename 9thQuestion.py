#9. Question: Conduct a one-way ANOVA to test whether there are any statistically significant differences in  average heights between three different regions with the following data1 
#Region A: [160, 162, 165, 158, 164] 
#Region B: [172, 175, 170, 168, 174] 
#Region C: [180, 182, 179, 185, 183] 

#Task: Write Python code to perform the one-way ANOVA and interpret the results.
#Objective: Learn how to perform one-way ANOVA using Python and interpret F-statistic and p-value.

#To test whether there are statistically significant differences in average heights between three different regions, we can conduct a One-Way ANOVA. The regions and their heights are as follows:
#Region A: [160, 162, 165, 158, 164]
#Region B: [172, 175, 170, 168, 174]
#Region C: [180, 182, 179, 185, 183]

#Steps to Perform One-Way ANOVA
#State the Hypotheses:
#Null Hypothesis (H0): All group means are equal (μA = μB = μC).
#Alternative Hypothesis (Ha): At least one group mean is different.

#Calculate Group Means:
#Mean for Region A (xˉA) = 160+162+165+158+164 / 5= 161.8
#Mean for Region B (xˉB) = 172+175+170+168+174 / 5= 171.8
#Mean for Region C (xˉC) = 180+182+179+185+183 / 5= 181.8

#Calculate the Overall Mean:
#𝑥ˉoverall = xˉA + xˉB + xˉC/ 3 = 161.8 + 171.8 + 181.8 / 3 ≈ 171.8

#Calculate Sums of Squares:
#Total Sum of Squares (SST): SST = n∑i=1(xi - 𝑥ˉoverall)^2
#Between-Group Sum of Squares (SSB): SSB = nA(xˉA​ − xˉoverall)2 + nB(xˉB − xˉoverall)2 + nC(xˉC​ − xˉoverall)2
#Within-Group Sum of Squares (SSW): SSW = ∑(xij − xˉj​)2
 
#Calculate Mean Squares:
#Mean Square Between (MSB) = SSB / k−1, where k is the number of groups.
#Mean Square Within (MSW) = SSW / N−k, where N is the total number of observations.

# Calculate the F-Statistic:
#𝐹 =MSW / MSB

#Interpret Results: Compare the calculated F-statistic to the critical value from the F-distribution table with k−1 and N−k degrees of freedom at a significance level of 0.05.

#Python Code 

import numpy as np
import scipy.stats as stats

# Data
region_A = [160, 162, 165, 158, 164]
region_B = [172, 175, 170, 168, 174]
region_C = [180, 182, 179, 185, 183]

# Combine data into a single array
data = [region_A, region_B, region_C]

# Perform One-Way ANOVA
F_statistic, p_value = stats.f_oneway(*data)

# Results
print(f'F-statistic: {F_statistic}')
print(f'p-value: {p_value}')

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: At least one group mean is significantly different.")
else:
    print("Fail to reject the null hypothesis: No significant differences in means.")