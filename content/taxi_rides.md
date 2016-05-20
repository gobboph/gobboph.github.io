Title: Taxi Ride Value
Date: 2016-05-20 22:30
Category: data
Tags: data, social
Slug: taxi_rides
Author: Roberto Gobbetti
Summary: Where should I drive my cab to make more money?

Like many others this past year, I stumbled on the impressive set of [TLC Trip Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) and could not resist taking my turn at seeing where the NYC cabs like to hang out. I worked to find where are the best spots for cabs to pick people up at different times of the day in orer to maximize their hourly income. You can find code and more images in my [github repo](https://github.com/gobboph/nycabs).

The data are a lot. They encompass all the taxi rides from Jan 2009 to Dec 2015. For each month there are about O(10^7) rides for wihch is given pickup coordinates and datetime, dropoff coordinates and datetime, trip distance, passenger count, total amount paid split in categories, payment method. The files' size oscillates between 1.8-2.2 Gb per month.

First thing first, I downloaded Jan 2015 (literally the first file you see on the website) and here is a pretty map of New York drown by plotting pickup locations (in red) and dropoff location (green) for the whole month.

<center><img src="images/green.png" alt="NYC by cabs" style="width: 400px;"/></center>