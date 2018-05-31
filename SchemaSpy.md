Title: SchemaSpy: a Java-based tool that analyzes the metadata of a schema in a database and generates a visual representation of it in a browser-displayable format.
Date: 2018-01-07 17:46
Category: Data Science
Tags: Data science, Artificial intellignce
Slug: SchemaSpy: a Java-based tool that analyzes the metadata of a schema in a database and generates a visual representation of it in a browser-displayable format.
Author: Mohcine Madkour
Illustration: data-lake-background.png

# Univariate Analysis

## Explaining Odds Ratios

### What is an odds ratio?

An odds ratio (OR) is a measure of association between an exposure and an outcome. The OR represents the odds that an outcome will occur given a particular exposure, compared to the odds of the outcome occurring in the absence of that exposure. Odds ratios are most commonly used in case-control studies, however they can also be used in cross-sectional and cohort study designs as well (with some modifications and/or assumptions).

### When is it used?

Odds ratios are used to compare the relative odds of the occurrence of the outcome of interest (e.g. disease or disorder), given exposure to the variable of interest (e.g. health characteristic, aspect of medical history). The odds ratio can also be used to determine whether a particular exposure is a risk factor for a particular outcome, and to compare the magnitude of various risk factors for that outcome.

    OR=1 Exposure does not affect odds of outcome
    OR>1 Exposure associated with higher odds of outcome
    OR<1 Exposure associated with lower odds of outcome

### What about confidence intervals?

The 95% confidence interval (CI) is used to estimate the precision of the OR. A large CI indicates a low level of precision of the OR, whereas a small CI indicates a higher precision of the OR. It is important to note however, that unlike the p value, the 95% CI does not report a measure’s statistical significance. In practice, the 95% CI is often used as a proxy for the presence of statistical significance if it does not overlap the null value (e.g. OR=1). Nevertheless, it would be inappropriate to interpret an OR with 95% CI that spans the null value as indicating evidence for lack of association between the exposure and outcome.

* Worked Example


In 1950, the Medical Research Council conducted a case-control study of smoking and lung cancer (Doll and Hill 1950). 649 male cancer patients were included (the cases), 647 of whom were reported to be smokers. 649 men without cancer were also included (controls), 622 of whom were reported to be smokers. The odds ratio of lung cancer for smokers compared with non-smokers can be calculated as (647*27)/(2*622) = 14.04, i.e., the odds of lung cancer in smokers is estimated to be 14 times the odds of lung cancer in non-smokers. We would like to know how reliable this estimate is? The 95% confidence interval for this odds ratio is between 3.33 and 59.3. The interval is rather wide because the numbers of non-smokers, particularly for lung cancer cases, are very small. Increasing the confidence level to 99% this interval would increase to between 2.11 and 93.25.
