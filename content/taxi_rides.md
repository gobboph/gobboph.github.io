Title: Taxi Ride Value
Date: 2016-05-20 22:30
Category: data
Tags: data, social
Slug: taxi_rides
Author: Roberto Gobbetti
Summary: Where should I drive my cab to make more money?

Like many others this past year, I stumbled on the impressive set of [TLC Trip Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) and could not resist taking my turn at seeing where the NYC cabs like to hang out. I planned to find where are the best spots for cabs to pick people up at different times of the day in orer to maximize their hourly income. I will explain here how and show you some plots, you can find code and more images in my [github repo](https://github.com/gobboph/nycabs).

There is a lot of data. They encompass all the taxi rides from Jan 2009 to Dec 2015. For each month there are O(10^7) rides for wihch is given pickup coordinates and datetime, dropoff coordinates and datetime, trip distance, passenger count, total amount paid split in categories, payment method. The files' size oscillates between 1.8-2.2 Gb per month.

First thing first, I downloaded Jan 2015 (literally the first file you see on the website) and here is a cool map of New York City drown by scatter plotting pickup (in red) and dropoff (green) locations for the whole month.

<center><img src="../../images/green.png" alt="NYC by cabs" style="width: 600px;"/></center>

If you played with this dataset (or with any dataset at all) you know that it needs some cleaning. There appear to be a staggering number of cabs picking people up at the North Pole or traveling at over 1000 miles/h on average. Some even arrive before they leaving.

These are easily taken care of, but what surprised me was that lots of people do not seem to tip: have I been an idiot all this time? The set of customer is divided clearly in tippers and non-tippers, which correspond almost 1 to 1 to card payers and cash payers. I am guessing that inserting the tip in the records when paid in cash is an extra mile that cab drivers are not willing to go for the sake of data collecting.

I populated the tip column with a linear model based on the card payers and the data was pretty much good to go for further analysis.

Now, how to assign value to a cab ride? Easiest answer: (totale fare) / (ride duration). The problem with this first approximation is that it does not take into account the time that cabs spend finding new customers, i.e. not making money. Still I could not track every single cab. Luckily some [old data](http://www.andresmh.com/nyctaxitrips/) has the info needed. I dowloaded the first set that is there, i.e. Jan 2013, and that is the base for all that follows.

After combining and cleaneing this dataset as well, I computed the wait between two clients, here as average for hour of the day. Notice the gigantic variance even after I took care of cabs out of service.

<center><img src="../../images/taxi_2013/wait_jan2013.png" alt="Cabs wait" style="width: 600px;"/></center>

Going on, I defined the trip value as:

**trip value = (total fare) / (time waited + trip duration)**

and plotted it as a function of the hour of the day and day of the month (in red weekends and holidays).

<center><img src="../../images/taxi_2013/valueperhour_jan2013.png" alt="value per hour" style="width: 600px;"/></center>

<center><img src="../../images/taxi_2013/valueperday_jan2013.png" alt="value per day" style="width: 600px;"/></center>

The few cabs out at 5am are doing well (maybe because no one else is around) and then there is a peak after work. From the day of the month barplot we can easily infer that drunk folks like to take cabs after new year's eve celebration. Also, the drivers seem to make increasingly more $/h as the week progresses.

Finally, here are a few more maps (you might want to enlarge it, but a blownup example is under it). For each hour of the day the data is pixeled and the maps are colored according to the average trip value in each pixel. Pixels with too few cab pickups are discarded: there might be some very valuable trip, but still it is not adviseble to drive a particular area if there is just a couple of pickups a month.

<center><img src="../../images/taxi_2013/panel_jan2013.png" alt="value panel" style="width: 800px;"/></center>



