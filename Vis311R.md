Title: An interactive visual of Houston 311 calls 
Date: 2017-04-08 10:00
Category: R, Data Visualization
Tags: Data Visualization, R, Houston, 311 calls
Slug: Vis311R 
Author: Mohcine madkour
Illustration: background.jpg

#An interactive visual of Houston 311 calls 

**Background**

Houston receives 311 calls for non-emergency services from it's residents, businesses and visitors. The response time for these calls is longer than those for emergency (911) calls. Accordingly the resources allocated to these services may not be as highly funded, resourced and/or prioritized as the emergency services. It is why the Houston authorities need to optimize the use and allocation of the resources available to service these calls.

Help Houston city to optimize the use and allocation of the resources available to service 311 calls.

Objective

The goal of this visual analysis is to aid the NYC authorities in optimizing the use of the limited resources available to service 311 calls/requests. There are 3 dimensions chosen along which this optimization can be done, time, location and skill type.



#barplot() 

        pol = read.csv("http://www.calvin.edu/~stob/data/csbv.csv")
        barplot(table(pol$Political04), main="Political Leanings, Calvin Freshman 2004")
        barplot(table(pol$Political04), horiz=T)
        barplot(table(pol$Political04),col=c("red","green","blue","orange"))
        barplot(table(pol$Political04),col=c("red","green","blue","orange"),names=c("Conservative","Far Right","Liberal","Centrist))

![image](/images/barplot.png)

       barplot(xtabs(~sex + Political04, data=pol), legend=c("Female","Male"), beside=T)

![image](/images/barplotNB.png)

#boxplot()

    data(iris)
    boxplot(iris$Sepal.Length)
    boxplot(iris$Sepal.Length, col="yellow")
    boxplot(Sepal.Length ~ Species, data=iris)
    boxplot(Sepal.Length ~ Species, data=iris, col="yellow", ylab="Sepal length",main="Iris Sepal Length by Species") 

![image](/images/boxplot.png)

#plot()

    data(faithful)
    plot(waiting~eruptions,data=faithful)
    plot(waiting~eruptions,data=faithful,cex=.5)
    plot(waiting~eruptions,data=faithful,pch=6)
    plot(waiting~eruptions,data=faithful,pch=19)
    plot(waiting~eruptions,data=faithful,cex=.5,pch=19,col="blue")
    plot(waiting~eruptions, data=faithful, cex=.5, pch=19, col="blue", main="Old    Faithful Eruptions",
    ylab="Wait time between eruptions", xlab="Duration of eruption")

![image](/images/plot.PNG)