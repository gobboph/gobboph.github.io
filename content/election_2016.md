Title: Don't shoot the messenger!
Date: 2016-11-12 18:30
Category: data, politics
Tags: data, social
Slug: election_2016
Author: Roberto Gobbetti
Summary: Spare thoughts about slamming the predictive models for the 2016 election.


Despite living in the States on and off for seven years and witnessing the 2012 presidential election, this year I got caught into the campaign madness. I felt the stakes were higher than usual: I had moved back to New York City with the prospect of building a family here but, most importantly, the circus around the election and its rules are truly entertaining for an outsider.

I am a data geek, and like many of my kind, I became addicted to following how the election predictive models developed throughout the past few months. That is why I am so appalled by the anger so many people seem to direct towards the modelers now that the election is over.

Articles have been published, even [in the New York Times](http://www.nytimes.com/2016/11/10/technology/the-data-said-clinton-would-win-why-you-shouldnt-have-believed-it.html), blasting the models and their makers for not correctly predicting the outcome of the election. These voices seem to confuse a risk model for a deterministic one. The former is what we saw on sites like FiveThirtyEight or even the Times itself, while the second would always give the same outcome given the same initial conditions.

Let me make this clear with an example. Let’s suppose I play a game of Russian roulette with one bullet, then my probability of survival is about 83%. This is based on the assumption that there are 6 equally probable scenarios and only one kills me. From a frequentist perspective, this means that if 100 people were to play the same game of Russian roulette, around 17 of them would die. If I play it only once and I kill myself, it would be foolish to say that the probability computation was wrong: I was just one of those 17 out of 100.

This is to say two things: first that it is hard to judge the quality of a model on a single experiment (and we have just one election in 2016). Second, that if someone gives an 80% chance to an event and you take the event for granted, you are making a mistake, not the modeler.

One sees now that the wild criticism certain models have received might be misplaced. Nate Silver’s FiveThirtyEight model gave something around 70% chance to a Clinton win, with a sizable probability (~12%) of her winning the popular vote despite losing the electoral college. These probabilities are far from being inconceivable.

If one wants to judge the goodness of FiveThirtyEight’s model, then perhaps they should look at how it did state by state: it predicted most of the swing states within a reasonable error (which was admittedly large this year). Moreover, it predicted Clinton would win the popular vote by ~3%, which turned out to be pretty close to reality.

I did not look as deeply into the details of the Times’ model, but in the days before the election, it gave Clinton a winning probability of 85%, so we are back to the Russian roulette. Other models gave her a 99% chance: they seem a bit off in retrospect, but one should check how they did state by state and how unlikely they concluded the actual outcome to be.

Once anyone cooks up any risk model that spits out a probability for a given event, the work is not done yet. The interpretation of the outcome depends on how risky the situation is, and this could be somehow subjective. For example, I would advise against playing Russian roulette with one bullet, but I don’t mind leaving the house without the umbrella if there is a 17% chance of rain. Given the stakes in this election, I personally was freaking out when FiveThirtyEight gave Clinton less than a 70% chance of winning a few days before the election.

To conclude, it is frustrating to see serious newspapers seemingly struggling to understand the statistical nature of a risk assessment. If all the polls were perfectly conducted (which they were not) and all the modelers had all the right assumptions (which seems unlikely), and we were told that Clinton had 90% chance of winning, this still would imply that there is a scenario in 10 that makes her lose. It is up to us then to decide if we are happy living with that or not.

PS: for a more in depth analysis, checkout the latest article on [FiveThirtyEight](http://fivethirtyeight.com/features/why-fivethirtyeight-gave-trump-a-better-chance-than-almost-anyone-else/).

