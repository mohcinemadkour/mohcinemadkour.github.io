Title: Data science in 2 minutes
Date: 2017-04-09 10:00
Category: Data science Learning
Tags: Data science
Slug: data science in 2 minutes
Author: Mohcine madkour
Illustration: datasciencejpg.jpg


# Data-Science-in-Two-Minutes
This repository contains short, concise descriptions and explanations on numerous data science topics. The main purpose is to aggregate the huge multi-verse of data science into something digestible that can be read and understood in under two minutes. These summarizations are not meant to replace more thorough rigorous material but to act more as an index for someone wanting to examine the vast array of possibilities under the data science umbrella.

Data Science Topics:
# Probability
# Statistics
### P-value
Value determined before a test that determines the probability that the null hypothesis will be rejected. If the test statistic produces a p-value in the rejection range and the null hypothesis is indeed correct then a type I error has been committed.

### MoM vs MLE vs MAP
MoM - Method of moments is a simple ways to estimate population parameters by using the moments of the observations. You set up a system of equations and solve for the parameters


One Form of the Method
The basic idea behind this form of the method is to:
(1) Equate the first sample moment about the origin M1=1/n∑Xi=Xbar to the first theoretical moment E(X).
(2) Equate the second sample moment about the origin M2=1n∑i=1nX2i to the second theoretical moment E(X2).
(3) Continue equating sample moments about the origin, Mk, with the corresponding theoretical moments E(Xk), k = 3, 4, ... until you have as many equations as you have parameters.
(4) Solve for the parameters.

Links
https://onlinecourses.science.psu.edu/stat414/node/193

### Moment Generating Function
Method to easily find moments of a probability distribution. M(t) = . It doesn’t always exist for all probability functions, though characteristic function always exists 
Taking the nth derivative of M evaluated at 0 yields the nth moment. 
The mgf uniquely characterizes a distribution so if two mgfs are equal then the pdfs are equivalent

### Unbalanced Classes SVM
You can assign weights to each class to more heavily weigh the unbalanced class, but even without weighting SVM’s do well.


### Covariance Matrix
Cov(X, Y) = Σ ( Xi - Xbar ) ( Yi - Ybar ) / N = Σ xiyi / N

To calculate this with a feature matrix.
Step 1: set x = X - Xbar
Step 2: Cov = x * x’/n

Diagonal elements will be variance

#Machine Learning
When presented a set of inputs, a machine can learn some thing about those inputs for some purpose.

##Types of Machine Learning
Machine learning can be divided into three broad learning types  
* Supervised - All inputs correspond with an output. The machine can be trained to predict future outputs.  
* Unsupervised - Only inputs are given. Machine can learn different structures within the input data.  
* Reinforcement - After a certain set of actions are performed some feedback on performance is returned which is used by the machine to learn.  

###Supervised Machine Learning Output
* Regression - Continuous real valued response.
* Classification - Each output is a particular class. **Nominal** classes have no particular natural ordering. **Ordinal** classes have a particular order (for example: Good, Average, Bad)


#Supervised Machine Learning

###Model
A simplistic representation of the world. Does not capture everything.

###Flexible vs Inflexible Models
* Flexible - Model has more knobs to tune and fit more wiggly (non-linear data). More prone to overfitting.
* Inflexible - Less knobs to tune. More rigid and usually more assumptions and easier to interpret.

###Parametric vs Non-Parametric Model
* Parametric - the form of the model is known before hand. Finite number of parameters. Machine learns the coefficients/parameters of the model. More rigid but simpler to learn and interpret. Examples are linear, logistic regression and linear support vector machines.
* Non-Parametric - Does not mean no parameters. The functional form of the model is not set before hand. Potentially infinite number of parameters. K-nearest neighbors, decision trees, RBF kernel Support Vector Machines  

[Blog Post][para vs non blog]  
[Quora Thread][quora para vs non]  

###The many synonymous names for input and output variables
* Input variables - predictor, covariates, feature, independent, explanatory, controlled, regressor, X
* Output variable - response, dependent, target, Y

##Linear Regression
A very simple regression model that models the response as a linear combination of the predictor variables.

###Assumptions
Linear regression makes many assumptions that make for a more rigid model though there are other techniques that can add flexibility to the model.
* Predictors are fixed constants
* Parameters are linear. Highly non-linear fits can still be made by transforming predictor variables. Only parameters need remain linear.
* Error variance is constant (Homoskedasticity). Plots of predicted value vs error are good to inspect whether this assumption is true. Non-constant variance can be a major problem with linear regression that can sometimes be alleviated by transforming the response variable.
* Errors are independent of one another. Knowing one error does not give information about another error as is the case with time series data.
* Errors are normally distributed with mean 0.
* No linear dependence (multicollinearity). No predictor variable can be a linear combination of all other predictors. Full rank matrix. 
* Linear specification is correct. The linear model accurately describes the true relationship between predictors and response.

[Linear Regression Assumption Blog post][regression assumptions]

###Fitting Linear Regression
Different algorithms and different metrics can be used to find the parameters of a linear regression model. Most popular is method of least squares which minimizes the squared error between the regression line and each point. Minimum absolute error and other loss functions can be used. 

Least squares equation below. 
![equation][least squares equation]

The model coefficients can also be estimated using [gradient descent][gd blog]. Which slowly moves in the direction of the gradient (found by taking the derivative of the least squares equation with respect to each parameter) to find the optimal parameters. The method of maximum likelihood can also be used whenever there is a parameterized probability distribution for the error terms. Procedure works by finding the likelihood function (multiplying all the probability of each point) and using calculus to maximize this product. 

###Multiple Regression
Simple linear regression is with one predictor variable. Multiple Linear regression is with two or more.

###Variable Transformations
Predictor variables can be transformed in any way imaginable as long as the input (design) matrix remains full rank. 

###Linear Regression Problems and how to Fix them
####[Outliers vs High Leverage Observations vs Influence][outlier vs leverage]
* Outliers are responses that are atypical and don't fit the natural trend of the data. 
* High leverage observations are unusual combinations of predictor variable values. Those observations that are furthest away from the mean of X. In simple linear regression, the observations at the end have the most leverage simply by being further away from the mean of the predictor variable.
* Influential Observations have drastic effects on model predictions, parameter estimates and hypothesis tests

####Detecting Outliers and Influential Observations
* How to discover outliers - plots of predicted value vs (studentized) residual. But this won't work when outlier pulls regression line close to it. Look at deleted studentized residuals
* [How to discover influential observations][influence link] - Cooks distance and DFFITS are good metrics. Both focus on how much a predicted value changes when one observation is left out.   
* Fix - Examine outliers/influential observations for data quality issues. Delete them only when you have a good reason. Use [Robust estimation][robust estimation] to downweight outliers.


####[Diagnostics and fixes for regression][diagnostics regression]
When the assumptions of the linear model are violated then the value of the model can decrease
* Non-linear fit: A plot of residuals vs predicted values. If there is any kind of trend that can be modeled with the residuals, the model is not correctly specified. Need to use interaction terms, polynomial features, a different model or a transformation to the responses to make linear.
* Correlated Errors - Diagnosed by plotting residuals over time (or by row). Some time-series analysis can be done to detect any dependence on previous residuals or previous response. Fix by adding lags of dependent and independent variable
* Non-constant Variance - Diagnosed by looking at studentized residuals. If they grow/shrink then there is a problem. Fix by taking log transform of response. Can use box-cox method to find more precise transformation.
* Non-normal errors - Normal errors are not a necessary assumption. Diagnose with qq-plot. Points should fall close to diagonal line. Can fix with methods for outliers above.
* Multicollinearity - When predictor variables are highly correlated with one another. Can lead to very unstable coefficients and poorly interpretted and fit models. Use correlation matrix and pair plot of all combinations of predictor variables to see most highly correlated predictors. Also can use Variance Inflation Factor which determines how predictable a predictor variable is when that predictor variable is used as the response variable. Can fix by selecting to keep just one of each highly correlated pair. Also by centering and scaling predictor values. Better to use penalized regression like ridge, lasso or elastic net.

###Linear Regression Interpretation
If all the assumptions in the model hold and there are no interaction or polynomial terms then the coefficient of each predictor variable tells us the amount of increase in the response when that predictor variable is increased by one unit holding all other predictor variables constant.  

###Regression Output
* Coefficients and t-statistics - Each coefficient and its standard error is estimated from the data and is modeled by student-t distribution. A t-test is conducted to produce a p-value - a level of significance
* Confidence interval - Confidence intervals can exist for the coefficients, the value of the regression line and for the prediction of a single obervation. They are not probabilities. Given a significance level, say 95%, the statistic you are measuring will capture the true value 95% of the time. 
* F - test: Determines if at least one of the predictors is necessary for the model. Does not say which ones are significant. F-ratio = Explained variance / Unexplained Variance. F-Ratio equals 1 when the model explains nothing.

###Model Selection
Building a model with all predictor variables typically isn't best practice (unless using penalized regression). Normally we look for parsimonious models - the least number of predictors with the highest predictive power. There are several ways to do this.

####Stepwise Selection
* Forward Selection - Start with null model and add one variable at a time until some stopping criteria is met. Stop when AIC, BIC, Mallows CP, Adjusted R-squared stop improving
* Backward Selection - Start will full model and remove one variable at a time until stopping criteria is met.
* Forward and Backward selection - At each step, chose one variable to either add or remove from model
* Best subset - make all possible models (not possible if number of predictors is large) and choose best

####Selection Criteria
AIC, BIC, Mallows CP and adjusted R-squared are 'historical' metrics for penalizing linear models without splitting data and doing cross validation. These metrics are used because residual squared error will always improve when more variables are added to the model. These selection criteria penalize for more predictors. Cross validation is typically used in place of these criteria when there is enough data.

##Penalized Regression
Linear regression can be fit with numerous features and combinations/transformations of features with many of these features can be highly correlated to one another. As flexibility in the model increases, so does overfitting, building a model that fits the training set well but does not generalize well to unseen data. One of the best methods to combat overfitting is to penalize least squares by adding a term proportional to the size of the parameter. Ridge and Lasso regression are the most popular. Penalized regression does an excellent job at controlling overfitting. Can be used when number of parameters is greater than number of predictors. It is important to standardize predictors by subtracting mean and dividing by standard deviation since the size of the coefficient is directly related to the scale.

###Ridge Regression
A penalty proportional to the L2 norm is added to the least squares equation. A closed-form solution exists. As the penalty increases the coefficients in the model tend towards 0.

###Lasso Regression
The penalty is proportional to the L1 norm. Coefficients will become exactly 0 as the penalty increases and acts as a model selector unlike Ridge. Must be solved iteratively.

![Lasso and Ridge][Lasso Ridge]

###Elastic Net
Has both L1 and L2 penalty

###Principal Components Regression
Instead of fitting the dataset to all p predictors, use principal component analysis to find the first m < p principal components that explain most of the variance and use these m transformed predictors in least squares. Choose the number of principal components by cross-validation. Standardize variables first.

###Partial Least Squares
PLS is a supervised alternative to PCR. Standardize predictors and compute first component, Z as linear combination of each predictor, X, times its correlation coefficient to Y. Now use simple linear regression for all predictors onto Z and get residuals. Use these residuals to again find correlation coefficient to Y. Keep iterating until desired number of components is reached.

###Regression Splines
Linear regression in one variable does not work well when trying to fit through highly non-linear data. Polynomial features can be used but this can lead to unstable swings in the regression line. Piecewise regression can be used using to help avoid using high degree polynomial terms. Regression splines with knots can also work very well and are surprisingly easy to fit. A cubic regression spline is built with X, X^2, X^3 and a third degree term for each knot. Apply least squares and the magic spline will pop out that is continuous at each knot and have the same first and second derivatives and look very smooth to the human eye. A slight variation is a natural cubic spline which must be linear before and after the first and last knots.

###Smoothing Splines
Find a function that minimizes the squared loss but also is penalized proportional to its second derivative. If the second derivative is too high then the function will be very wiggly and overfit the data. This penalty ensures a smooth fit. It can be shown that a smoothing spline is a natural cubic spline with knots at every unique x value.

###Locally Weighted Regression
At each unique x, a new low degree polynomial is fit. Each point is weighted by how far it is away from the current point being estimated.

###Generalized Additive Models
A method that can use many different linear models, such as splines or weighted regression or polynomial features as additive building blocks to build one big linear regression. Fit using backfitting.

###Multivariate Adaptive Splines (MARS)
MARS is a linear combination of multiple hinge functions. An example hinge (hockey stick) function is max(0, x - c) where c is a constant and a knot.  MARS is fit in an iterative, greedy fashion that adds two mirrored hinge functions to its model that have the greatest affect on lowering the squared error. After the addition of the pair of terms, pruning takes place where a term can be excluded from the model. 

###Prediction vs Inference
* Prediction - When given a set of inputs **X** and we are not necessarily concerned about interpreting the underlying target function *f* (could say its a black box) to predict **y**.
* Inference - We care about the meaning of the predictors, their relationships, and how are they related (linear, non-linear) 

##Logistic Regression
Simple model used for classification. Models the probability of a bernoulli distribution given input data. The output of logistic regression is the probability that an observation is in one of two classes. So even though technically logistic regression outputs a number between 0 and 1, it is used for classification.

###Logistic Model Specification
Logistic Regression uses the same (linear combination of predictors times a coefficient) as linear regression except that it takes the result of this combination and smashes it with the sigmoid function so that it's value is always between 0 and 1.

###Sigmoid Function
![sigmoid][sigmoid image]

###Model Interpretation
Some algebra with the sigmoid function will show that for every one unit increase in a predictor variable will result in a corresponding increase parameter value increase to the log odds. The log odds can be any real number.

### Generalized Linear Models
Not to be confused with General Linear Models (abbreviated GLM) which is the name for ordinary linear regression. Generalized Linear Models abbreviated GLIM but the trend is to use GLM specifically for Generalized Linear Models and have no abbreviation for General Linear Models (just call them linear models, ordinary linear regression, or simple linear regression).

GLMs offer more flexibility than ordinary linear regression by allowing a non-linear relationship to hold between the response and the predictors. The right hand side is still a linear combination of coefficients and covariates (**XB** in matrix notation) but the response variable **Y** is transformed by a *link* function *g* which transformed values are then assumed to have a linear relationship with the covariates.

The response variable does not have the constraint that it is continuous, normally distributed with constant variance. The classic case is a binomial (0/1) response which clearly doesn't follow linear regression assumptions. The outcome (0/1) is not directly modeled in this case, just the log-odds using the logit link function. Poisson and negative binomial regression can be used to model discrete counts. The distribution of **Y** is different than the link function. For instance, with binomial data, Y is distributed as a binomial distribution and uses the logit link. In ordinary linear regression, **Y** is normally distributed with the identity link function.

The response variable must still be independent and the covariates can be transformed as in linear regression.

No closed form solution. Use maximum likelihood with newton rapson or gradient descent.

##Linear Discriminant Analysis
LDA is a machine learning method that can be used to classify two or more classes. LDA works by first assuming all predictor variables follow a normal distribution.  A multivariate normal distribution is estimated for each predictor for each different class. So, if there are three classes, 3 separate multivariate normal (with common covariance matrix and class specific mean) distributions will arise. A prior distribution of the classes is created based directly on the proportion of each class in the training data. Using bayes theorem, prediction can be made given a new observation.

##Quadratic Disriminant Analysis
Same as LDA except that there will be a separate covariance matrix for each class. This give it more flexibility than LDA.




### SVM vs Logistic Regression
If there is a separating hyperplane there is no guarantee logistic regression will be able to find the best one. It just guarantees the probability will be 0 or 1. This is more so for unregularized LR. SVMs might not do as well if there are random points close to the hyperplane

links
http://www.quora.com/Support-Vector-Machines/What-is-the-difference-between-Linear-SVMs-and-Logistic-Regression




### Recurrent Neural Net
The units form a directed cycle and thus can keep an internal state where they have different gates that determine whether
Best use case: unsegmented Hand-written digits
LSTM - long-short term memory doesn’t have vanishing gradient problem
BPTT - trained through backpropagation through time

There are different gates - input gates, forget gates of previous input, output gates
Essentially the current input and the previous input are passed to different gates. Each has different weights. They are aggregated then squashed via an activation function and finally passed to an output layer where process begins again.


links
https://s3.amazonaws.com/piazza-resources/i48o74a0lqu0/i6ys94c8na8i2/RNN.pdf?AWSAccessKeyId=AKIAJKOQYKAYOBKKVTKQ&Expires=1438359044&Signature=bks5t9RHMGBKnu2X15JWE75Hcio%3D


### Convolutional Neural Nets
Neurons are tiled in such a manner to represent overlapping visual fields.
There can be pooling layers which combine outputs from previous layers.
Can be fully connected layers.
Drop out layers reduce overfitting. Individual neurons drop out with some predefined probability

Max-Pooling: After each convolutional layer, there may be a pooling layer. The pooling layer takes small rectangular blocks from the convolutional layer and subsamples it to produce a single output from that block. There are several ways to do this pooling, such as taking the average or the maximum, or a learned linear combination of the neurons in the block. Our pooling layers will always be max-pooling layers; that is, they take the maximum of the block they are pooling.



### Generative vs Discriminative Models

Generative models give a way to generate data given a particular model. They model the joint probability distribution p(x,y) and use this to calculate the posterior probability p(y|x). They model the distribution of classes p(x|y). 
Can generate sample points. For example - first pick y (say a topic) and then pick x (say a word in that topic)

p(y|x) = p(x, y) / p(x) = p(x|y)p(y)/p(x)

Generative models make assumption about distribution - as for example in Naive Bayes we assume independence of all features which can over-count evidence such as the word “Hong Kong”
Better for outlier detection and non-stationary models (dynamic data where test set is different that training)
Can be interpreted as probabilistic graphical model with a more rich interpretation of the model.
Gives you a way to generate data with p(y) and p(x|y)
Generative models assumptions don’t allow it to capture all the dependencies that are possible.
Generative models can do very well if structure is applied correctly.
Can work better with less data. 
Tend not to overfit because of restrictive assumptions

Discriminative classifiers model the posterior p(y|x) directly. They model the boundary between classes. Provide classification splits though not necessarily in a probabilistic manner, so you don’t actually need the underlying distribution

Can capture dependencies better because doesn’t have strict assumptions on distribution.
No attempt to model underlying probability distribution.


Links
http://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf
http://stats.stackexchange.com/questions/12421/generative-vs-discriminative
http://www.cedar.buffalo.edu/~srihari/CSE574/Discriminative-Generative.pdf


### Parametric vs Non-Parametric Modeling
**Parametric** - The shape of the target function *f* is assumed. The most common is linear model f(X) = β0 + β1X1 + β2X2 + ... + βpXp. With model chosen parameters are estimated from historical data. If model assumptions are wrong then a poor fit could occur. Can choose more flexible models but those are prone to overfitting.

**Non-Parametric** - No explicit assumptions about *f*. Can fit a wide variety of shapes. Since problem is not reduced to estimating parameters, much more data is needed for better fit. Hyperparameters are used instead to instruct fit.

https://www.quora.com/What-is-the-difference-between-the-parametric-model-and-the-non-parametric-model


### PCA
Many uses and abuses of PCA

When there are a large number of covariates and potentially many of them are correlated with each other, PCA can greatly reduce the number of covariates and the multicollinearity between them

A principal component is the direction of the data that explains the most variance. One that captures the most spread in the data. Take a look at the images below. If were to only examine the points where the arrows touch the line, it would be clear to see that the points on the line in the left image vary greater than those on the right. The line on the right is the line that produces the maximum variance and thus would be the first principal component. 


Each line (or hyperplane) created has a direction and variance associated with it. In PCA the direction is the eigenvector and the variance is the eigenvalue. The eigenvector with the highest eigenvalue is the principal component. This line (hyperplane) also minimizes the squared distance from the points to the line. This is not to be confused with linear regression which minimizes the squared error (given an x).

The number of eigenvectors (principal components) is equivalent to the number of dimensions of the data. Each successive eigenvector is orthogonal to the previous one. Using eigenvectors transforms your data from one space to another. These new directions are more intuitive and show more information. The image below shows this transformation



We can go a step further and reduce dimensionality by choosing to keep those eigenvectors with eigenvalues above a certain threshold.


We want lots of spread between covariates - maximum variance
To get PCA
Step 1: Get covariance matrix
Step 2: get eigenvalues of covariance matrix (do Singular value decomposition)
Step 3: normalize eigenvalues to 0 - 1. These eigenvalues represent the amount of variation retained for each variable
Step 4: USV from singular value decomposition U is new space (eigenvectors), S contains eigenvalues

The first principal component has the largest variance of the combination of covariates. It finds the direction of maximum variance and projects it on a smaller subspace. Eigenvectors point in this direction and corresponding eigenvalue gives variance in that direction
Second PC is largest variance of combination of covariates that are orthogonal to first PC

PCA: PCA sidesteps the problem of M not being diagonalizable by working directly with the n×n "covariance matrix" MTM.  Because MTM is symmetric it is guaranteed to be diagonalizable.  So PCA works by finding the eigenvectors of the covariance matrix and ranking them by their respective eigenvalues.  The eigenvectors with the greatest eigenvalues are the Principal Components of the data matrix.

Now, a little bit of matrix algebra can be done to show that the Principal Components of a PCA diagonalization of the covariance matrix MTM are the same left-singular vectors that are found through SVD (i.e. the columns of matrix V) - the same as the principal components found through PCA:

When PCA is not useful:
When doing predictive modeling, you are trying to explain the variation in the response, not the variation in the features. There is no reason to believe that cramming as much of the feature variation into a single new feature will capture a large amount of the predictive power of the features as a whole

When PCA may not be useful - for example when using random forests. The splits may happen in the last features that explain the least amount of variance among the features
The first principal component is a linear combination of all your features. The fact that it explains almost all the variability just means that most of the coefficients of the variables in the first principal component are significant.
Now the classification trees you generate are a bit of a different animal too. They do binary splits on continuous variables that best separate the categories you want to classify. That is not exactly the same as finding orthogonal linear combinations of continuous variables that give the direction of greatest variance. In fact we have recently discussed a paper on CV where PCA was used for cluster analysis and the author(s) found that there are situations where best separation is found not in the 1st few principal components but rather in the last ones.


links
https://georgemdallas.wordpress.com/2013/10/30/principal-component-analysis-4-dummies-eigenvectors-eigenvalues-and-dimension-reduction/
http://www.stats.uwo.ca/faculty/braun/ss3850/notes/sas10.pdf
http://www.councilofdata.com/algorithms/principal-component-analysis-pca-part-1/

### Latent Dirichlet Allocation
Step 1 - Choose number of topics by eyeballing, using prior info or max likelihood
Step 2 - randomly assign each word a topic
This gives each document and word to a distribution of topics
Say Doc1 is (30, 32, 38) for the three topics and 
Word1 in Doc1 is (60, 30, 10) for the three topics
Step 3 - Iterate through each word and randomly assign it to the topic given two components.

Component 1 - prevalence of topics in that specific document p(topic|document)
Component 2 - prevalence of word across topic p(word | topic)


Say word ‘ted’ represents 20% of the words in cat1 and 40% in cat2 across all documents and we want to reassign ‘ted’ in the first document. The first document is 85% cat1 and 15% cat2. So we can weigh these probabilities and come up with a 17:6 ratio of cat1:cat2 and randomly choose how to assign the word ‘ted’

This uses bayes theorem to generate the “prior” probabilities of each word (component 1).  What is the current composition of the document. This probability will add up to 1 and then updated by the likelihood - probability word is generated from that prior.
p(topic) * p(word | topic) for each topic and then randomly select from those numbers

To initiate generative process
Initially choose topics via dirichlet distribution. This assumes a prior for the topics
And then choose words from another dirichlet distribution

Dirichlet is a continuous multivariate distribution

Latent variable is one that we infer and not directly observed

links
http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/

Go through each document, and randomly assign each word in the document to one of the K topics.
Notice that this random assignment already gives you both topic representations of all the documents and word distributions of all the topics (albeit not very good ones).
So to improve on them, for each document d…
Go through each word w in d…
And for each topic t, compute two things: 1) p(topic t | document d) = the proportion of words in document d that are currently assigned to topic t, and 2) p(word w | topic t) = the proportion of assignments to topic t over all documents that come from this word w. Reassign w a new topic, where we choose topic t with probability p(topic t | document d) * p(word w | topic t) (according to our generative model, this is essentially the probability that topic t generated word w, so it makes sense that we resample the current word’s topic with this probability). (Also, I’m glossing over a couple of things here, in particular the use of priors/pseudocounts in these probabilities.)
In other words, in this step, we’re assuming that all topic assignments except for the current word in question are correct, and then updating the assignment of the current word using our model of how documents are generated.
After repeating the previous step a large number of times, you’ll eventually reach a roughly steady state where your assignments are pretty good. So use these assignments to estimate the topic mixtures of each document (by counting the proportion of words assigned to each topic within that document) and the words associated to each topic (by counting the proportion of words assigned to each topic overall).

### NMF
Brute force matrix decomposition method factoring matrix C (DxW) into A (DxT) and matrix B (TxW). AxB approximately equals C. The non-negative part is useful in applications where non-negativity is a must. It can also make it easier to inspect. Smaller dimensions make it easier to store

In topic modeling
D - number of Documents
W - number of words
T - number of topics

So matrix A can be interpreted as the mixture of topics that for each document (row)
and matrix B can be interpreted as the mixture of words in that topic.

These can be converted to probabilities to form a generative model where documents are formed

Used to discover latent features
Algorithm uses ||C - AB||^2 and iterates to minimize this
Gibbs Sampling
A way to randomly sample from a complex multivariate joint probability distribution.

Step 1: pick out random feasible values of each variable
Step 2: condition on all the random variables except one. 
Step 3: Now you can use a simple uniform random variable to get a random value using the marginal distribution.
Step 4: repeat for other random variables in the joint. Once all variables have a value you have your ‘random’ point.

There is a burn-in required to get more feasible random values. Once you have sampled enough random values you can then choose from these sampled values to get more truly random values


### Expectation Maximization
Form of soft clustering where each point can be part of multiple clusters with different probabilities. We usually assume a gaussian or multinomial distribution and want to find the optimal parameters (mean, covariance) of the distribution

Begin algorithm by picking number of clusters
Pick random (smart) gaussians (multinomial) distributions that are feasible
Go through each point and do a soft clustering - assign a probability that it arose from each gaussian P(cluster 1 | x1) and so on. Use bayes rule here and just assume equal priors - all classes are equally likely
Once it has these assignments (probabilities of being in each cluster) it readjusts the parameters of the gaussians to fit points better
Find new mean by doing a weighted average of the points. So points that are 99% in one class will have more weight than points that are 20% of that class
Calculate new variance in the same way. Find a weighted average of the squared difference between the point and the old mean.
Repeat until distributions aren’t moving
Exellent Video: https://www.youtube.com/watch?v=REypj2sy_5U
http://stats.stackexchange.com/questions/72774/numerical-example-to-understand-expectation-maximization

#Evaluation

### ROC Curve

A graphical plot that plots False positive rate vs True positive rate by varying the threshold of a binary classifier. 

False positive rate(x) vs True positive rate(y)
False positive rate - out of all the samples that were actually negative, the percentage that was actually guessed positive - FP / Real Negatives

True Positive - sensitivity - recall - out of all the samples that were actually positive how many were actually guessed positive. TP / Real Positives



For example, we want to minimize false positives on spam so we set the threshold at .95. The false positive rate might be very low (.02) but the true positive rate might also be very low (.15) since the model needs to be very sure to guess spam. If we move the threshold to .5 - FPR will increase to say and TPR might be .8

Area on the curve is a good measure

Why the diagonal line with slope of 1? 
Let’s say there is 100 observations and 20 are actually positive.
And now I am given the chance to have 70% false positive rate (thats 56 positives out of 80 negatives wrong). Meaning by random if I am given 56 positives, just by random chance I should get at least 70% TPR. Let’s say I actually guess 5 / 20 right for TP and guess 56 positive wrong out of the 80 negative. I could simply reverse my decision and get 15 right for .75 TPR and only 24 wrong for .3 FPR. This is opposite (.25 TPR and .7 FPR)


###L1 vs L2
Penalizing extreme parameter values
L1 - L1 norm, diamond shaped. Easier to think of this regularization as a condition sum(abs(parameters)) < C

L1 better at sparse data. Incorrectly used on non-sparse data could yield large error.
L2 better at prediction since both highly correlated variables stay in the model.
L2 is like diversifying your portfolio. If one variable is corrupted can use other variable. L1 is more aggressive.

[para vs non blog]: http://machinelearningmastery.com/parametric-and-nonparametric-machine-learning-algorithms/
[quora para vs non]: https://www.quora.com/Do-Support-Vector-Machines-come-under-parametric-or-non-parametric-models-and-why
[regression assumptions]: https://economictheoryblog.com/2015/04/01/ols_assumptions/
[least squares equation]: https://wikimedia.org/api/rest_v1/media/math/render/svg/917759911692e98ba477c3d669356525a84aace6
[gd blog]: https://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
[influence link]: http://onlinestatbook.com/2/regression/influential.html
[outlier vs leverage]: https://onlinecourses.science.psu.edu/stat501/node/337
[robust estimation]: https://onlinecourses.science.psu.edu/stat501/node/353
[diagnostics regression]: http://people.duke.edu/~rnau/testing.htm
[sigmoid image]: https://wikimedia.org/api/rest_v1/media/math/render/svg/a26a3fa3cbb41a3abfe4c7ff88d47f0181489d13
[Lasso Ridge]: http://gerardnico.com/wiki/_media/data_mining/lasso_vs_ridge_regression.png?w=800&tok=f55022

#Databases
#Data Science Interview Questions
What is wrong with memorizing data?

How would you describe a clock (in ML lingo) that is always two hours behind?

##Statistics
When is an F-test used and what are its limitation?

Why does the sum of squares regression (SSR) have only one degree of freedom?


##Generic Questions
What do you think a data scientist does?

What do you think are the most important skills for a data scientist to have?

What is a project you would want to work on at our company?

What unique skills do you think you could bring to the team?

What is an example of your experience working with real, dirty data?

What makes data dirty?


### What is the difference between reducible and irreducible error?

### What is the difference between a machine learning model and a machine learning algorithm?
Many times these words are used interchangeably but generally they have different meanings
A model (or method or technique) can be a general idea of how to interpret 
An algorithm instructs the user of the model of precisely how to execute computational steps
Examples: Linear regression is a model and least squares (or maximum likelihood) is the algorithm used to find the parameters in the model.
Neural Networks are a model with backpropagation

# Resources

### Good Data Science Blogs
blog.kaggle.com (Very useful for reading how winners of kaggle competitions win. Its usually 1. Feature Selection. 2. Gradient Boosted Trees or Deep Learning)  
http://www.kdnuggets.com/websites/blogs.html  

All of data science
http://www.datascienceontology.com/

Great quora thread on how to learn machine learning - https://www.quora.com/How-do-I-learn-machine-learning-1  

### Books

## Free Books
- **Intro to Statistical Learning** Excellent introduction to most common ml algos. Only need basic stat/prob as a prereq. http://www-bcf.usc.edu/~gareth/ISL/
- **Elements of Statistical Learning** Same authors as above but much more rigorous - http://statweb.stanford.edu/~tibs/ElemStatLearn/
- **Bayesian Reasoning and Machine Learning** http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage
- **Information Theory, Pattern Recognition and Neural Networks** http://www.inference.phy.cam.ac.uk/itprnn/
- **Mining of Massive Datasets** http://www.mmds.org/
- **Deep Learning** - Still in production but nearly finished. http://www.deeplearningbook.org/


