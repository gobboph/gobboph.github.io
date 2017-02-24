Title: What Happened There?
Date: 2017-02-15 14:00
Category: data
Tags: data
Slug: wht
Author: Roberto Gobbetti
Summary: Matching Wikipedia traffic spikes with breaking news.

Time series are omnipresent. If you were around in 2008, you probably have seen the graph of a financial index collapsing from one day to another. Alternatively you might check the temperature prediction for each hour of the day before leaving in the morning. A time series is nothing more than a set of values with a time stamp and represents how a certain quantity changes over time.

Time series often have very recognizable features (e.g. a big drop in the stock prices). The number of daily views of a Wikipedia webpage (its traffic) usually displays big spikes if people show particular interest in its main topic, but it can be hard to figure out why people were interested in a particular person or entity, especially time after the triggering event happened.

Here is where [WhatHappenedThere?](http://whathappenedthere.xyz/) enters the scene. Given a topic, the app downloads the time series of its associated Wikipedia page (if it exists) and automatically detects the spikes. It then queries a database storing all the New York Times articles since the earliest time in the Wikipedia time series (July 2015) and returns a list of most relevant articles according to a natural language processing (NLP) algorithm. I will use this post to flesh out some of the technical details behind the project.

A bit of context: I worked on this project during my fellowship at Insight Data Science and discussed the developments with the team at About.com. The development of the app took a couple of weeks from idea to completion and if it works well now, there are definitely directions where it could be improved. As will be clear by the end of this post, WhatHappenedThere? provides a proof of concept for the power of connecting a time series with a source of context to automatically provide insights. For even more details, all of this project is shared on [GitHub](https://github.com/gobboph/WhatHappenedThere).


As one inputs an entry on WhatHappenedThere?, the app looks for the associated Wikipedia page. If this exists, it then retrieve the daily view counts of the page, i.e. the time series (check out the [wiki](https://github.com/gobboph/WhatHappenedThere/blob/master/application/flasknews/wiki.py) module on GitHub). The app consists of 3 separate parts joined together:

* #### [Spike detection in Time Series](#spikes)
* #### [Database query](#search)
* #### [NLP on retrieved documents](#nlp)


### <a name="spikes">Spike detection</a>

The spike detection algorithm is coded up in the [anomalies](https://github.com/gobboph/WhatHappenedThere/blob/master/application/flasknews/anomalies.py) module you can see on GitHub. The algorithm keeps a window period (let's say 30 days) prior to the date I am interested in checking for a spike. It computes the mean and standard deviation and classifies the value as a spike (anomaly) if it falls outside the range of $avg \pm tolerance \times std$. Both the window period and the tolerance are parameters. Notice that thanks to the "-", the algorithm would in principle detect big drops as well, but this is not relevant in this particular case and I can not think of an event that would trigger a drop if not after a spike.

In the precise case of detecting spikes in webpage traffic, one must bear in mind that the daily distribution of visits has a [heavy tail](https://en.wikipedia.org/wiki/Heavy-tailed_distribution), hence the very large spikes we want to detect.  From this point of view, one might think that keeping track of the mean and standard deviation might not be a good approach since the assumption behind this approach is that the distribution of daily views is Gaussian. Still, for all practical purposes, this approach works well as long as the tolerance is kept very high. The app declares a spike when a value is more than 6 standard deviations away from the null hypothesis. For reference, 5 is enough to declare that the Higgs boson does indeed exist.

Maybe it could be better to treat the daily distribution as a Poissonian. This would not be a big modification: we just need to change the standard deviation to the mean. The net result is similar and again, the app does a posteriori find the peaks that are relevant. I have not thoroughly delved into autoregressive models as they would take longer and defeat the purpose of having a quick and responsive online app, but they are definitely a direction one should explore if interested in developing this further.

I also added an absolute threshold as a third parameter of the spike detection algorithm. This is useful for my particular application: if a Wikipedia page has 30 views on average and 200 one day, this might as well be a spike, but probably not one that made the news and should be disregarded.


### <a name="search">Database search</a>

The second source of data is a record of all the articles published by the New York Times since July 2015 (the earliest date in the Wikipedia time series). I downloaded the articles using the [NYT  Archive API](https://developer.nytimes.com/) and stored them with PostgresSQL. The data provided by the API is not complete, meaning the whole body of the article is not provided. Still, there is quite a bit of text in the headline, abstract and lead paragraph, and of course there are the publication dates.

The search is nothing more than a SQL query that looks for articles within a date bracket (the consecutive dates classified as a spike) and regarding a topic. It is coded up in the [nyt](https://github.com/gobboph/WhatHappenedThere/blob/master/application/flasknews/nyt.py) module. Although the coding part is in itself trivial, there is an interesting precision vs. recall problem here, *i.e.* how to maximize the number of articles that are relevant, while minimizing the number of irrelevant ones that get picked up anyway.

There is no perfect solution to this problem. Let me explain with an example: I had initially decided to search for each single word in the Wikipedia page name. The reason behind this was that the data for each article is limited and that the NLP part of the project would take care of giving more relevance to the topic I want over others. The drawback of this is clear: if you look for "David Bowie", the algorithm would pick any article referring to anyone called David.

Alternatively, I tried maximizing precision and searching for the full string. The app would pick up only specific articles, but at the expense of others. An article referring to "President Obama" would not appear, since the app would look for "Barack Obama" only as that is the name tag of the Wikipedia page. In some other case, all possible content might be lost. Looking for "Earthquakes in Italy" would return the Wikipedia page "List of earthquakes in Italy" and no article would have this precise string in it. The previous method would instead return the articles relative to last year's events.

I eventually settled for precision when I noticed friends were getting frustrated by getting wrong results more than getting no result at all. As of now, the algorithm queries for the full Wikipedia name or the full string inserted by the user. In this way, searching for "Obama" gives more results than searching for "Barack Obama", but you avoid learning about minor politicians when looking for "Michael Jordan".


### <a name="nlp">NLP</a>

The last piece of the picture is extracting meaningful information from the articles. Not having the whole body of the article might look like a problem, but in a sense it helps making things easier: you can think of it as if the New York Times did some part of the job already by weeding out the non essential information. The clear counterpart is that you do not get anything about people relevant enough to be in the news, but not as the main charater of the story.

An example: "Sergio Mattarella" is the president of Italy and has a big spike in december 2016, the weekend of an important referendum, but still gets no article. The articles that cite "Matteo Renzi" (Italy's prime minister, a more significant role) might cite Mattarella in the body, but he did not make the headline or lead paragraph.

However one wants to see it, the relatively small amount of data per article, together with the time constraint of computing things on the fly, calls for a fast approach. The app takes all the articles relative to a spike and computes the [tf-idf score](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) of each word ranking them from the most relevant to the least. This helps extracting concepts.

This helps us find the most relevant articles. In order to do that, we need to define a measure to compute *distance* between articles and then find which one has the lowest sum of distances, *i.e.* is most similar to most other articles.

We can treat each article as a vector in the space of all the words of the extracted corpus: it will have a 0 in the direction of a word that does not appear, 1 if the word appears once and so on. I used cosine similarity as a measure. This consists in taking the normalized dot product of two vectors A and B, which is the cosine of the angle between them: the highest this value (closest to 1) the more similar the vectors are. The app computes the cosine similarity between each pair of articles and sums the values for each article: the article that has the highest score is the one whose topics are most similar to most other articles in the batch.

Finally, the website prints an ordered list of the most relevant 10 articles per spike together with a nice word cloud. You can click on each headline and read the article.


### Conclusions

Perhaps the main drawback of the app is the limitation of the context data, *i.e.* the New York Times corpus. The New York Times is a biased source of context: it gives more relevance to American over international news and maybe to some topics over others, like politics. It is not the best publication to figure out what a certain actor or pop star has been up to for example (although "Beyonce" works pretty well). One can easily overcome this limitation with a more diversified dataset.

At high level, WhatHappenedThere? is a tool to automatically extract information by maintaing a connection between two datasets, a time series and a source of context. This allows to gain precise insights and fast. Of course, a similar tool could help analyze time series beyond Wikipedia traffic and the code is broken down to minimize dependencies and allow for easy adaptation into new projects.





