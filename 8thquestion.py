#8. Question: You have two sets of data representing the incomes of two different professions 
#Profession A: [48, 52, 55, 60, 62]
#Profession B: [45, 50, 55, 52, 47] 
#Perform an F-test to determine if the variances of the two professions'  incomes are equal. What are your conclusions based on the F-test? 

#Task: Use Python to calculate the F-statistic and p-value for the given data.
#Objective: Gain experience in performing F-tests and interpreting the results in terms of variance comparison.

#To determine if the variances of two professions’ incomes are equal, we can conduct an F-test. The null hypothesis 𝐻0 states that the variances of the two populations are equal, while the alternative hypothesis 𝐻𝑎 asserts that they are not equal.
#Data
#Profession A: [48, 52, 55, 60, 62]
#Profession B: [45, 50, 55, 52, 47]

#Steps to Perform the F-Test
#1. Calculate Sample Variances: We first need to compute the sample means and variances for both groups.
#For Profession A:
#Mean (𝑥ˉ𝐴) = 48+52+55+60+62/5 = 53.4
#Variance (𝑠2A) = (48−53.4)^2 +(52−53.4)^2 +(55−53.4)^2 +(60−53.4)^2 +(62−53.4)^2 / 5-1 =37.7

#For Profession B:
#Mean (𝑥ˉ𝐵) = 45+50+55+52+47/5 = 49.8
#Variance (𝑠2B) = (45−49.8)^2 +(50−49.8)^2 +(55−49.8)^2 +(52−49.8)^2 +(47−49.8)^2 / 5-1 = 8.7

#Calculate the F-Statistic: The F-statistic is calculated as the ratio of the variances:
#𝐹 = 𝑠𝐴2 / 𝑠𝐵2 = 37.7/8.7 ≈ 4.33

#Determine Degrees of Freedom:
#Degrees of freedom for Profession A (𝑑𝑓𝐴) = 𝑛𝐴−1=5−1=4
#Degrees of freedom for Profession B (df B) = nB−1=5−1=4

#Find the Critical Value: Using an F-distribution table or calculator, find the critical value for 𝑑𝑓𝐴 = 4 and dfB=4 at a significance level of 0.05. The critical value is approximately 6.39.

#Decision Rule: If the calculated F-statistic is greater than the critical value, we reject the null hypothesis.

#Conclusion: Since 4.33 < 6.39, we fail to reject the null hypothesis. There is not enough evidence to conclude that the variances of the incomes in Profession A and Profession B are significantly different.

#Python code
import numpy as np
import scipy.stats as stats

# Data
profession_A = [48, 52, 55, 60, 62]
profession_B = [45, 50, 55, 52, 47]

# Calculate variances
var_A = np.var(profession_A, ddof=1)  # sample variance
var_B = np.var(profession_B, ddof=1)  # sample variance

# Calculate F-statistic
F = var_A / var_B

# Calculate p-value
df_A = len(profession_A) - 1  # degrees of freedom for A
df_B = len(profession_B) - 1  # degrees of freedom for B
p_value = 1 - stats.f.cdf(F, df_A, df_B)

# Results
print(f'F-statistic: {F}')
print(f'p-value: {p_value}')

# Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: Variances are significantly different.")
else:
    print("Fail to reject the null hypothesis: No significant difference in variances.")
