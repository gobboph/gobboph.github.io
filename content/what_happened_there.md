Title: What Happened There?
Date: 2017-02-15 14:00
Category: data
Tags: data
Slug: wht
Author: Roberto Gobbetti
Summary: Matching Wikipedia traffic spikes with breaking news.

Time series plot are omnipresent. If you were around in 2008, you probably have seen the graph of a financial index collapsing from one day to another. Alternatively you might check the temperature prediction for each hour of the day before leaving in the morning. A time series is nothing more than a set of values with a time stamp and represents how a certain quantity changes over time.

Time series often have very recognizable features (e.g. a big drop in the stock prices). The number of daily views of a Wikipedia webpage (its traffic) usually displays big spikes if people show particular interest in their main topic, but it can be hard to figure out why people were interested in a particular person or entity, especially time after the triggering event happened.

Here is where [WhatHappenedThere?](http://whathappenedthere.xyz/) enters the scene. Given a topic, the app downloads the time series of its associated Wikipedia page (if it exists) and automatically detects the spikes. It then queries a database storing all the New York Times articles since the earliest time in the Wikipedia time series (July 2015) and returns a list of most relevant articles according to my natural language processing (NLP) algorithm. I will use this blog post to get into the details of what goes on behind the curtains.

A bit of context: I worked on this project during my fellowship at Insight Data Science and discussed the developments with the team at About.com.