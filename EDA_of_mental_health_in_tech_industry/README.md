# DS.v3.2.1.5


## Technical Instructions
For detailed technical instructions on how to run the project, refer to the [SETUP.md](SETUP.md) file.


## Findings
**Key Results:** The analysis revealed some insights of significance into the mental health of tech industry professionals. A notable percentage of respondents reported experiencing mental health issues (total prevalence rate of the sample is **~37%** for Mood Disorders, Anxiety Disorders, and ADHD) that were associated more closely to their gender, family illness history, country freedom level rather than workplace environment.

**Patterns and Trends:**
- A large number of participants are from the USA, with responses evenly distributed across different states.

- The 2016 survey is particularly significant, as it was the only survey year to include specific 'diagnosis' questions, making it a focal point for analysis.

**Possible contributors to the rise in mental health disorders:**

- Genetic Factors: The proportion of mental health disorders is higher among respondents with a family history of mental illness.

- Discrimination:
    - Sociocultural Gender Pressures: Cisgender females and non-binary/transgender individuals report higher rates of mental health disorders. It’s possible that men may under-report or remain undiagnosed due to societal expectations or perceived stigma (further data would be needed to confirm this); however, this alone likely doesn’t account for the strong association.
    
    - Sociocultural Pressures Related to Country Freedom Levels: Higher rates of mental disorders are observed in countries with greater freedom levels. While additional analysis is needed, it is likely that mental health issues in moderate- to low-freedom countries are more stigmatized, making them less likely to be reported or diagnosed. Economic pressures may also play a role in diagnosis rates in these regions.

- Common themes included openness to discussing mental health, workplace attitudes toward mental health, and the impact of disclosing mental health concerns. However, these factors did not show a significant direct impact on mental health outcomes or vice versa. It may be beneficial to explore questions related to these themes individually (during this analysis they were combined) in future analyses.

## Conclusion
**Summary:** The analysis indicates that genetic factors, gender, and sociocultural influences (such as country freedom levels) are significant in shaping mental health outcomes and less workplace environment.

**Implications:**

- Cultural Stigma: Differences in mental health disorder rates across countries with varying freedom levels underscore the role of local stigma.

- Gender-Specific Needs: Higher rates of mental health disorders among cis-females, non-binary, transgender individuals highlight the need for targeted, inclusive support.

- Workplace Support: Creating supportive environments may be insufficient without accessible, actionable mental health resources.

**Recommendations:**

- Normalize Mental Health: Reduce stigma, particularly in lower-freedom regions, through public awareness campaigns and culturally sensitive workplace initiatives.

- Targeted Support for Vulnerable Groups: When ethical, prioritize tailored support for cisgender females, non-binary, and transgender individuals.
    Additionally, governments could increase awareness about heightened mental health risks for individuals with a family history of mental illness (private information that could/must not be accessed by workplace).


## Data Description
**Source:** The dataset was sourced from the Kaggle dataset "Mental Health in the Tech Industry".

**Time Period:** The data covers surveys conducted from 2014 to 2019 (analyzed 2016). 

**Variables:** Key variables include age, gender, country, position, employees count, self-employment status, working remotely, diagnosis, family illness history, willingness to share mental health issues, workplace attitude, and mental health disclosure impact.

**Preprocessing:** Data cleaning involved handling missing values, standardizing and grouping entries for most of features.


## Methodology
**Variables:** All variables included in the analysis were categorical.

**Confidence Intervals:** Calculated using the Wilson Score Interval, preferred for categorical data and provides better interval estimates for proportions.

**Statistical Tests:** Cramér's V test was used to assess associations between categorical variables. This method is suitable for larger sample sizes and remains sensitive to smaller groups within the data.

**Visualizations:**
- Bar plots for univariate visualizations.

- Mosaic plots to illustrate relationships between categorical variables.

- Heatmaps to display the strength of associations (Cramér's V test) across variable pairs.
