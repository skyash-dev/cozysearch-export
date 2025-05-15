Alternative title: **The finance industry, mortgage-backed securities, bank bailouts, risk-weighted assets, and equity ratios: much more than you wanted to know.**

Also: you get to find out what I actually do for a living.

Epistemic status: I look forward to [learning a lot from the comments](https://meta.wikimedia.org/wiki/Cunningham%27s_Law).

Follow up post: [how finance improves and turkeys in the jungle](https://putanumonit.com/2019/01/01/finance-followups/).

## Galaxy Brain

13 billion years ago the first galaxies started forming, followed soon after by [the galaxy brain meme](https://knowyourmeme.com/memes/expanding-brain). Sometime in between, Scott Alexander wrote about the root of galaxy-brainism: the irresistible urge to signal intelligence by adopting [meta-contrarian positions](https://www.lesswrong.com/posts/9kcTNWopvXFncXgPy/intellectual-hipsters-and-meta-contrarianism). This urge is so strong that it is nearly impossible to find an issue where people up-and-down different levels of education and left-and-right on the political spectrum agree with each other. _Nearly_ impossible.

Dropout or Ph.D., Trumper or Berniebro, everyone seems to hate the financial industry. People signal intelligence or political affiliation not by having different attitudes towards finance, but by using different buzzwords to explain why bankers are evil and should be fired/jailed/ [eaten](https://tvtropes.org/pmwiki/pmwiki.php/Main/EatTheRich).

![bankers are bad](https://putanumonit.com/wp-content/uploads/2018/12/bankers-are-bad1.jpg?w=900)

To the consternation of all the brains pictured above, the only people who seem to respect finance are those with any real power. Tech companies have enough cash not to worry what bankers think of them, and yet it’s quite rare to hear a tech CEO criticize Wall Street. Voters on both sides of the spectrum hate bank bailouts, and yet presidents from both parties keep bailing banks out. Even Trump, who has appointed [criminals](https://www.politico.com/story/2018/09/19/michael-flynn-sentencing-mueller-830724) and [scammers](https://www.forbes.com/sites/dianahembree/2018/11/09/scam-company-advised-by-matthew-whitaker-threatened-victims-but-many-filed-complaints-anyway/#332359b41afa) to every post in the cabinet, was convinced to pick a moderate and well regarded professional to chair [the Federal Reserve](https://en.wikipedia.org/wiki/Jerome_Powell).

_“They’re all in the bankers’ pockets”_ lacks explanatory power. Rich and powerful people spend most of their energy fighting other rich and powerful people, not [altruistically conspiring with them](http://slatestarcodex.com/2014/09/14/does-class-warfare-have-a-free-rider-problem/). And the finance industry isn’t even that rich. Johnson & Johnson is bigger than any bank in the world, why aren’t the rich and powerful in the pocket of Big Band-Aid?

I have an alternative explanation: _Finance is the miracle glue that keeps our civilization intact. No one understands exactly how it works, so fucking with it in any way should be terrifying._ _People in power can see that._

I see scowling faces when I propose this explanation, or when I suggest that finance is important and bankers are doing useful work. The confidence with which people proclaim that finance is parasitic and worthless is [in direct proportion](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect) to their ignorance of any theory or facts pertaining to the financial industry.

There’s a lot I don’t know about finance. I don’t know which complex criticism of finance are correct, but I know which simple ones aren’t. I will list some basic facts, do some basic math, and present a basic model of what finance does. Any criticism of the finance industry should at least address these basics. A lot of them don’t, and that includes books written by economists, not just Twitter trolls.

The goal of this post is to push you up the Dunning-Kruger curve towards less ignorance about the finance, less reflexive hatred of it, less confidence that you know how to “fix” it.

Welcome to the galaxy brain.

![cosmic suit banker](https://putanumonit.com/wp-content/uploads/2018/12/cosmic-suit-banker.png?w=900)

## The Parable of Banksy

Imagine a world made up of two villages, a week’s ride apart. Maysville, where corn is grown and eaten, and Cottonton, which produces cotton. The resident of both villages work diligently, but their lives aren’t great. The Maysians eat well but have nothing to wear but tunics stitched of corn leaves; the Cottonites have good fabric but meager lunches.

There’s one Maysvillian, [Banksy](https://hanguppictures.com/artists/banksy/banksy-signed-prints/festival-destroy-capitalism), who just sucks at growing corn. At harvest, he barely has enough cobs to fill a single cart. But then Banksy has an idea. He takes the cart and rides out of Maysville, returning after a fortnight with a cart full of t-shirts, jeans, and underwear. The Maysians are happy to trade huge amounts of the corn they don’t need for a pair of MeUndies. After a few trips, Banksy has as much corn as the best farmers in town.

Some of the older farmers sneer at the young entrepreneur. “In my day, to get a silo full of grain you had to pull it out of the ground yourself”, they mutter. “What did _you_ do to deserve your riches?”

“I took on price risk and foreign exchange risk in connecting our village to geographically diverse markets”, replies Banksy.

“Sounds like a scam”, say the elders.

A while later, two women named Tori and Tilly are walking around Maysville telling everyone about a new idea they came up with. Instead of eating the corn raw, they could dry and mill it into flour, then bake it in flat circles. They named it after themselves: a tortilla. Unfortunately, the tortillas so far are hypothetical: Tori and Tilly don’t have enough corn to pay builders to construct a corn mill, and no one in Maysville is willing to work for free.

Banksy comes with a proposition: he will lend the two women 10 bushels to pay the laborers, and they pay him back 20 bushels when their tortillery is set up. Tori and Tilly agree, and soon Maysville is booming with baked delicacies of every sort from nachos to cornbread. Unfortunately, Tori and Tilly go out of business after [an angry mob accuses them of cultural appropriation](https://www.huffingtonpost.com/entry/portland-burrito-cart-closes-after-owners-are-accused-of-cultural-appropriation_us_5926ef7ee4b062f96a348181).

Banksy is richer than ever, and the elders are angrier than ever. “You used to pull your cart, now you get rich just by sitting around!” they shout.

“I took on time risk and credit risk by allowing our village to trade not just across geographies, but also across time,” says Banksy. “We are 99%!” the elders keep screaming [as they slowly shrink and transform into corn cobs](https://twitter.com/dril/status/134787490526658561?lang=en).

This is ultimately what finance does. It’s the intermediary that allows people to trade across time and space, and the party that assumes many of the risks inherent in this trade.

## Finance is a Coordinating Intermediary

You may notice that it takes 1 intermediary to connect 2 villages, but 100 nodes [have 4950 potential connections](https://simple.wikipedia.org/wiki/Network_topology#Mesh). A billion people have half a quintillion potential connections. The more actors participate in the global economy, the more middlemen it takes to connect them. The value of making those connections increases as well, as does the risk. As the global economy becomes more integrated we should see three things happening, and they do:

1.  Finance, insurance and trading take up [a larger share of the global economy](https://blogs.wsj.com/economics/2011/12/10/number-of-the-week-finances-share-of-economy-continues-to-grow/).
2.  Finance becomes riskier, more lucrative, and more unequal with greater rewards going to the winners. [[1]](#foot1)
3.  [Everyone in the world gets more prosperous](https://ourworldindata.org/grapher/declining-global-poverty-share-1820-2015).

This is what financial institutions do and how they make money. Goldman Sachs doesn’t rob people at gunpoint, it gets paid by willing clients to provide a service. Finance create value by connecting people: companies to investors, depositors to lenders, [corn buyers today to corn sellers next year](https://www.cmegroup.com/trading/agricultural/grain-and-oilseed/corn.html). You can argue that risks are not worth the rewards or that inequality is not worth the prosperity, but that doesn’t erase the value that finance provides.

Take the most vilified financial innovation of the past few decades – the [mortgage-backed security](https://www.investopedia.com/terms/m/mbs.asp). It’s built on a simple idea: instead of making an all-or-nothing bet that a single family will pay off their house by issuing a single mortgage, a bank can package 10,000 mortgages together into an MBS and you buy a piece of that, equivalent to making a bet that at least X% of the mortgages will get paid.

This is a really good bet when X is 10% or 40% or even 80%. But if X is 95% and all you own are crappy MBS, [it takes just 5%](https://fred.stlouisfed.org/series/DRSFRMACBS) of American borrowers defaulting on their mortgages at once to blow your shit up. This is what happened to Lehman Brothers and AIG, and it’s how we got a financial crisis.

It’s very tempting to draw the lesson from this that MBS are useless and risky, or that they’re a scam invented by greedy bankers to steal money.

But we can look at MBS as a solution to a coordination problem. There are 10,000 families who want to move into a house today and pay for it over a couple of decades. There are 10,000 construction workers who want to build a house today and get paid for it today. There are 10,000 investors who want to invest some money today and get a return in the future.

Those 30,000 people don’t live in the same city, the same country, or even in the same decade. Even if we could magically teleport them to the same (very large) room, they would not be able to coordinate a solution. How would they trust each other to do their part? Who would track how much money needs to get paid to whom and at what time?

Mortgage-backed securities are the solution to this seemingly impossible coordination problem. Without MBS fewer people would live in the houses they want, fewer construction workers will have a job, and investors will get worse returns on their hard-earned savings. The banks who securitize mortgages are in competition with each other and as a result, they capture only a small part of the surplus MBS create for all involved.

Any deal like this carries inherent risk since any subset of the 30,000 can mess things up for everyone else. Investors may pull their money, construction companies may build the wrong houses in the wrong geographies, tenants may default on their mortgages. This risk is unavoidable, and it’s very hard to figure out exactly how much risk was involved, and where it was concentrated. In 2008, the answers turned out to be: “way more risk than we thought” and “concentrated in a few huge and interconnected institutions that may need a _bailout_ to survive”.

If the story so far has been relatively uncontroversial, the opposite is true when we get to the B-word. Fasten your seatbelts.

## What’s in a Bailout

The sanity of conversations about the bailout got off to bad start right away. As the [Emergency Economic Stabilization Act](https://en.wikipedia.org/wiki/Emergency_Economic_Stabilization_Act_of_2008) was debated in Congress, [Americans supported the bill by a 27% margin](https://en.wikipedia.org/wiki/Emergency_Economic_Stabilization_Act_of_2008#The_public) when it was presented as _“the government is potentially investing billions to try and keep financial institutions and markets secure”_ and **opposed the same exact bill by a 24% margin** when it was phrased as _“the government should use taxpayers’ dollars to rescue ailing private financial firms whose collapse could have adverse effects on the economy and market”_. Very few of the people expressing their opinion bothered to read the 451 pages of the law, and the same is true of many of the congresspeople who voted on it.

Where do I stand? [I stand with Socrates](https://en.wikipedia.org/wiki/I_know_that_I_know_nothing). The financial system is so complex and anti-inductive that predicting the effects of major interventions in it is beyond mortal comprehension. The political system is so complex and anti-inductive that predicting the effects of major interventions it enacts is beyond mortal comprehension. Bailouts are a major intervention in the financial system enacted by the political system. Predicting the effects… Ah hell, let’s at least try.

The argument in favor of financial bailouts is that the financial system relies on confidence, and confidence is a resource that can be cheaply manufactured by the government.

Banks are vulnerable to negative feedback loops where temporary setbacks cause permanent damage. If a few depositors lose faith in a bank and withdraw their deposits at once, the bank has less money available to pay other depositors, which in turn causes _them_ to lose faith and withdraw their funds, and so on until the bank collapses in a [bank run](https://en.wikipedia.org/wiki/Bank_run). The government can easily put a break on this process by promising depositors that they [will always get their money back](https://en.wikipedia.org/wiki/Federal_Deposit_Insurance_Corporation). Once depositors are sure they can withdraw their deposits, they don’t feel the need to.

A similar thing happens in [a liquidity crisis](https://en.wikipedia.org/wiki/Liquidity_crisis), such as the one in 2008. When banks lose access to loans they can’t finance their own lending in turn, and the market for credit can collapse in a runaway process. Again, the government can provide credibility and prevent the death spiral by being the lender of last resort. Confidence is created by credibility, and as long as the government is stable, solvent, and able to print money, it has the credibility to inject confidence into a panicky financial system without much cost to itself.

There are two main arguments against government bailouts of banks.

The first is [moral hazard](https://en.wikipedia.org/wiki/Moral_hazard): if banks are protected from the downsides of making bad investments by an implicit government guarantee, they will make dumber and riskier investments. Had banks known they wouldn’t be bailed out in 2008 they wouldn’t have kept stuffing their balance sheets with explosive subprime MBS. But they knew, so they did.

I think that the general version of this argument is certainly true. But the particular case of subprime mortgages that’s so often cited as an example of moral hazard probably has little to do with it.

The crash of subprime MBS seems obvious in hindsight, but at the time the number of [people making bets against these instruments](https://www.investopedia.com/articles/investing/020115/big-short-explained.asp) was very small. The most famous of those, [Michael Burry](https://en.wikipedia.org/wiki/Michael_Burry), couldn’t even convince his own investors that MBS are too risky and had to enforce a moratorium on withdrawals to keep his hedge fund solvent. The groupthink that gripped everyone else, from mortgage lenders to bank traders to rating agencies, was too pervasive to be overcome by institutional incentives.

_Never attribute to malice that which is adequately explained by stupidity_, [goes the saying](https://en.wikipedia.org/wiki/Hanlon%27s_razor). If scientists can’t avoid p-hacking their own clean and simple data, it’s too much to expect of bankers to decipher their doom in the entrails of MBS prospectuses.

Moral hazard is also an unavoidable result of the principal-agent problem. Banks exist for the benefit of their shareholders, and bank [shareholders lost more than 80%](https://www.tradingview.com/symbols/SP-SPF/) (!) between the peak of May 2007 and the nadir of February 2009. Why didn’t the shareholders make the banks figure out that MBS are too risky to invest in? Shareholders can only influence the board, which directs the CEO, who manages several layers of directors before getting to the risk analysts whose job it is to figure out MBS. If that person didn’t do their job in 2007, expectations of a bailout likely had little to do with it.

The second argument against bailouts is that they put Washington in bed with Wall Street. This is really a naive argument. Bailout or no bailout, government and finance aren’t just friends with benefits, they’re conjoined twins.

Most of what governments do is a financial coordination problem: taking money from some citizens and redistributing it or spending it on collective projects. For as long as banks have existed, governments used them for those purposes. In July 2015 the UK government [finally finished paying off](https://www.gov.uk/government/news/repayment-of-26-billion-historical-debt-to-be-completed-by-government) government liabilities arising from investments in the South Sea Company in 1720 and loans taken to finance wars in 1754.

As for banks, the government isn’t only their largest counterparty but also the provider of the legal system that underpins finance, the issuer of regulations, and the ones who actually print the money. There no finance that stands apart of politics, and no politics that is independent of finance.

So what to make of all this? Moral hazard and Washington-Wall Street incest exist with or without bailouts. Bailouts certainly don’t make these two issues better, but there’s value in the government providing the confidence that banking requires same as it provides any other vital infrastructure.

I think that some sort of government backing for the financial system is good in theory. In practice, since having a sane and informed national conversation on bailouts is impossible, we ended up with the worst of all worlds.

[What happened in 2008/09](https://www.rollingstone.com/politics/politics-news/secrets-and-lies-of-the-bailout-113270/) is that the actual bailout turned out to be an order of magnitude larger than the bill Congress voted on, it was lied about and covered up by both politicians and bankers, it made the too-big-to-fail even bigger and more failure prone while simultaneously undercutting more prudent competitors, and it destroyed public confidence in the financial system instead of reinforcing it.

I don’t think that anyone actually aimed for this outcome. Instead, in the absence of consensus or even dialogue, the politicians, bankers, and the Fed just followed their instincts and short-term interests. There are no guaranteed ways to succeed in finance, but gut-based short-termism is a guarantee of failure.

And yet, even after that fiasco, the financial system keeps chugging along. Houses get built, mortgages get paid, retirees retire. No matter how bad that bailout was, I’m still not sure the counterfactual is better.

## Experts and Equity

The financial system is not perfect but it’s not terrible either, and I don’t think we could redesign it from scratch to improve it without risk. If we have ideas on how to improve it, we should try them out carefully and incrementally.

But maybe I just don’t have enough degrees in economics to figure out a better system to coordinate money flows across continents and centuries. Quite a few people with the requisite number of degrees seem to think it’s easy.

Anat Admati and Martin Hellwig are professors of economics, and they wrote _[The Banker’s New Clothes](http://bankersnewclothes.com/)__,_ a book about what’s wrong with the banking system and how to fix it with “specific and highly beneficial steps that can be taken immediately”. John H. Cochrane is a professor of economics at Chicago, which is like being a professor of economics but more so. **[He wrote a review](https://johnhcochrane.blogspot.com/2013/03/the-bankers-new-clothes-review.html)** of the book that appeared in the Wall Street Journal and on my Facebook wall with a ringing endorsement.

> The central problem, at the core of Anat Admati and Martin Hellwig’s “The Bankers’ New Clothes,” is capital. In order to make $100 of loans, **a typical bank** borrows $97—from depositors, from money-market funds, from other banks, or from bondholders—and sells $3 of stock, its “capital.” So if only 4% of the bank’s loans fail, the shareholders are wiped out, and the bank cannot pay its debts. […]

Three eminent professors explain that the problem with banking is that the typical bank holds enough equity to cover only 3% of its assets and that this number is falling. As Cochrane was writing those words, in March 2013, the average equity ratio of US banks was 11.2%, up from 6% in the late 1980s.

![equity assets](https://putanumonit.com/wp-content/uploads/2018/12/equity-assets.png?w=900)

Let me repeat that: economics professors who wrote a book about how raising equity ratios will solve the problem of financial crises **got the actual equity ratio for banks,** a number that is publicly reported and easily googlable, **wrong by a factor of 4.** You can’t make this shit up.

Unless you’re an economics professor, in which case you can make up whatever you want:

> What about those “tough” new capital regulations that you keep reading about? They are not nearly as tough as you think. At best, the new Basel III international bank regulation agreement calls for a 7% ratio of capital to assets by a leisurely 2019 deadline. But that is the ratio of capital to “risk-weighted” assets. Risk-weighting is a complex system in which some assets count less against capital requirements than others. A dollar of mortgage assets might count as 50 cents, but it might count as 10 cents or less if it is a complex mortgage-backed security, and zero if it is government debt. When Ms. Admati and Mr. Hellwig unravel those “risk weights,” we’re still talking about 2% to 3% actual capital.

Do you keep reading about new capital regulations? I bet you don’t.

You know who else has not done any reading about the new capital regulations? John Cochrane.

How can I tell? Because every single number he quotes in that paragraph is wrong.

Why do I know that? Because my job since 2013 was turning the tough new capital regulations into software and helping banks implement them. If you want to do some reading about capital regulations they are [all listed on the Federal Register](https://www.ecfr.gov/cgi-bin/text-idx?SID=3707cc5281d649a29ed64ff333cf6156&mc=true&tpl=/ecfrbrowse/Title12/12cfr217_main_02.tpl). But you don’t have to, I have the entire thing memorized.

Let’s see if I can rewrite that paragraph:

> At worst, the Basel III agreement calls for an 8% ratio of capital to assets, while allowing national regulators to impose 2.5% on top of that. The 7% ratio is for a specific subset of capital, an extra requirement to provide extra security. This has been fully implemented in almost all major jurisdictions, including the US, between 2013-2018. Risk-weighting is a not-so-complex system, even Jacob could figure it out. A dollar of mortgage assets counts as 50 cents only if it adheres to strict prudent loan standards, it counts as a full dollar otherwise. If it is a complex mortgage-backed security it might count as much as $12.5 (a 1250% risk weight) unless it’s a very safe senior tranche.

In any case, the average ratio of capital to risk-weighted assets in the US is above 14%. This is true of all the “too big to fail banks” as well. You can find this number if you’re curious by looking at the [FR Y-9C report for each major institution](https://www.ffiec.gov/npw/Institution/TopHoldings) on schedule HC-R Part I line item 43.

![equity risk weighted assets](https://putanumonit.com/wp-content/uploads/2018/12/equity-risk-weighted-assets.png)

Cochrane concludes:

> This simple truth has been met by howls of protest and layers of obfuscation and derision by bankers, their consultants and many of their regulators. “Oh, you just don’t understand the complexities of banking” is the basic attitude.

I’m sure that professor Cochrane understands very well the _complexities_ of banking. I’m just afraid he doesn’t understand the _simplicities_, such as how to look up a bank’s capital ratio online.

Ok, so maybe Cochrane misrepresents the views of Admati and Hellwig, and maybe those have changed since early 2013. I was excited to find out that a few weeks ago [Dr. Admati went on EconTalk](http://www.econtalk.org/anat-admati-on-the-financial-crisis-of-2008/#audio-highlights) to chat with Russ Roberts, a careful thinker, skeptical interviewer, and, of course, a professor of economics.

> **Anat Admati:** But what I see, I see the symptom of heavy indebted and distressed: there’s no companies as indebted as banks. I mean, they have single-digit equity in a good day, relative to total assets.

I agree that 11.2% isn’t a _very_ double-digit number, but it’s still a double-digit number.

> **Anat Admati:** They will have the story, ‘Yeah, yeah, yeah–we didn’t have enough equity and we figured that out and now we have more.’ But, I mean, the ‘more’ is like the smallest tweaks–it means nothing. The ‘more’ is like in Martin Wolf’s world, tripling zero. Which is still zero.

In the space of 15 minutes, we went from “single-digit” to “basically zero”. I’m sure Russ will call her out on that.

> **Russ Roberts:** That, of course, encourages banks to be very leveraged, to have very little skin in the game; as you point out, to have, say 1% in equity and 99% borrowed.

![giphy](https://putanumonit.com/wp-content/uploads/2018/12/giphy.gif?w=900)

Maybe there’s an upside. If all those econ professors really think that banks have a 1% or 3% equity ratio then it’s sensible to say that raising that number to 7% or 10% will ameliorate a lot of risk in the banking system. Unfortunately, in contradiction to all logic, the lower someone thinks current ratios are they higher they think they should be. Admati and Hellwig propose 20%-30% and mention the good old days when banks had 50% equity. [Cochrane thinks](https://johnhcochrane.blogspot.com/2013/03/the-bankers-new-clothes-review.html) we should go to 50% or 100%. And Roberts:

> **Russ Roberts:** Right. Because we can’t just–it was too risky. So, that incentive is going to always be there when powerful people have a chance to be bailed out. They are going to get bailed out. So, it seems to me that those of us who understand those incentives should call out and say: ‘Well, given this reality, the only way to deal with this is to have very low levels of leverage; very high levels of equity.’ Which is what you’ve come out for.
> 
> **Anat Admati:** Yep.
> 
> **Russ Roberts:** Now, that, to me, you can debate–and I know you have–whether that’s got a cost or not. I don’t really care. The cost of it is small compared to the costs of the ongoing failures of the financial system that happen.

If I had to summarize the main lesson of 400 hours of EconTalk episodes in 4 words, they would be “everything is a trade-off”. When Roberts says “I don’t care about the costs” without thinking for even three seconds what those costs may be… there’s something about this topic that seems to incinerate the sanity of anyone who approaches it.

So what are the costs of making banks hold more capital? Let’s put a number on it.

Let’s start with a simple model: a bank has $10 of _equity,_ it borrows $90 of deposits (_liabilities_) at 2%, it and lends out $100 (_assets)_ at 5% for a 10% equity-to-assets ratio. You can review [the basic accounting equation](https://en.wikipedia.org/wiki/Accounting_equation) if you’re not familiar with the terminology. Let’s say that the bank has operational costs that are 1% of assets (the cost actually doing the work of taking deposits and making loans) and that 1% of the bank’s debtors don’t repay their loans.

We can calculate how much money the bank makes.

Costs: 1%\*$100 operational costs + 1%\*$100 borrower defaults + 2%\*$90 interest paid = 1 + 1 + 1.8 = $3.8.

Revenues: 5%\*$99 interest received = $4.95.

Total profit: 4.95 – 3.8 = $1.15 of profit on $10 of equity. That means that every dollar of bank equity earns 11.5% return each year, which is in line with most other industries.

What would happen if a bank had to hold $50 in equity and take only $50 in deposits to cover $100 in loans?

Costs: 1%\*$100 + 1%\*$100 + 2%\*$50 = 1 + 1 + 1 = $3.

Revenues: $4.95.

The bank made a profit of $1.95, but that profit is divided among a lot more shareholders. Each dollar of equity has earned only 1.95 / 50 = 3.9%. This is a measly return, 3 times less than what shareholders were earning with a 10% equity ratio.

Perhaps shareholders will take a slightly lower return in exchange for a safer investment, but they wouldn’t take one-third. To get back a reasonable return on equity, instead of borrowing at 2% and lending at 5% banks might have to borrow at 1% and lend at 8%. Of course, there are a lot fewer borrowers and lenders willing to make that deal. A lot of lending will not get done: companies won’t get started [[2]](#foot2), houses won’t get bought, investor cash will remain stuffed in mattresses.

In fact, that’s what _will_ happen if capital requirements are raised. Equity investors will pull their money out of banks and into more profitable enterprises like [apple polishing](https://putanumonit.com/2017/02/10/get-rich-slowly/). Most banks will shut down, and the remainder will serve the greatly reduced loan intermediation market. In the good ol’ days of 50% equity ratios, even white people had a tough time getting a mortgage.

The argument _for_ capital requirements is that banks holding too little equity impose a negative externality on everyone else in the form of systemic risk from banks blowing up. This argument [runs into the puzzle](https://www.sciencedirect.com/science/article/pii/S1572308917302632) of banks holding 6-7% more capital than is required of them, but it’s probably correct as a general principle.

Ideally, then, regulations should set capital requirement at the point they would be if that externality was entirely internalized by the banks. That’s what the 8% number is aiming to do. It’s physically impossible to make bankers have 100% skin in the game and still do banking, so the regulations aim to set limits that would make banks behave _as if_ that was the case.

Of course, everyone “knows” that regulations are a scam. Admati and Hellwig promulgate the idea that corrupt regulators go easy on banks in order to get a cushy job in the industry. From Cochrane’s review:

> And, in an all-too-short chapter on “The Politics of Banking,” they show us how politicians and regulators like the cozy cronyism of the current system. […] Regulators commonly become sympathetic to the interests of the industry they regulate, which advances their careers in government or back in industry.

Unfortunately for this story, research shows that _tougher_ regulators [have an easier time](https://academic.oup.com/qje/article-abstract/129/2/889/1867167) getting jobs in finance than regulators who go easy on banks. Think about it: if you’re a bank, would you hire the diligent and exacting Fed employees, or the lazy and careless?

On EconTalk, regulation is simply dismissed out of hand:

> **Anat Admati:** I think that Basel, the way it was coming into the crisis was a _spectacular_ failure. And I can just tell you how many things were wrong with it. And that what they called a ‘major revision’ was really just tightening a few screws. But it really didn’t improve it that much. And it remains this game of, you know, of playing around with the risk weights and finding ways to increase, you know, to kind of game it; and this whole thing; and putting it off balance sheet; and what’s called Regulatory Arbitrage–this cat-and-mouse game that continues to go.
> 
> […]
> 
> **Russ Roberts:** How much Triple A, and weights, and how much of each kind you can have. And that whole hierarchy of, that infrastructure of supervision, monitoring, regulation, and implicit promise seems to me to be an utter failure. There’s no reason to think that that’s a good system.

I know more about the hierarchy of supervision, monitoring, and regulation than all but perhaps a hundred people in the United States. Almost all of those people, including me, are making their money by helping banks comply with the rules in letter and in spirit rather than by helping them evade the rules and play games. The reason is simple: _there are too many goddamn rules to evade them all._

Aside from requirements on the amount of capital a bank must hold, here are just the regulations that I’ve dealt with in the last five years:

-   [Liquidity coverage ratios](https://www.ecfr.gov/cgi-bin/text-idx?SID=3707cc5281d649a29ed64ff333cf6156&mc=true&tpl=/ecfrbrowse/Title12/12cfr249_main_02.tpl), ensuring that banks have enough cash flow to pay their short-term debts even in a liquidity crunch.
-   [Single-counterparty credit limits](https://www.federalregister.gov/documents/2018/08/06/2018-16133/single-counterparty-credit-limits-for-bank-holding-companies-and-foreign-banking-organizations), ensuring that no bank is overly exposed to a single institution that will drag it down if it fails.
-   [FDIC 370](https://www.axiomsl.com/resource-center/inside-view/2017/09/12/are-you-ready-for-fdic-part-370/), ensuring that even if a depository institution fails it will repay all of its deposits immediately.
-   Net stable founding ratio, country exposure reporting, stress tests, special rules for insurance companies, for broker-dealers, for funds, for swaps, for qualified financial contracts…

The last thing I’m worried about is that I’ll be out of a job because regulators decide to give banks a break.

There is really just one glaring problem with government regulation of banks – it’s _too nice to the government_. The US government decreed that US treasuries have a risk-weight of 0%, that they’re considered a highly liquid asset on par with cash, that the government is exempt from single-counterparty limits, and so on and so forth. Every major European and Asian regulator does the same. The only way banks can comply with all the regulations is by being massively exposed to government debt in all its forms. Did I mention conjoined twins?

If nations and taxpayers bear the burden of bank risk, banks are no less exposed to government risk. Governments print the money, banks move it around, and if you find this arrangement distasteful consider that it has underpinned the global economy since long before the industrial revolution.

## Conclusion

To wrap up:

-   The financial industry moves money between those who have it to those who have a good use for it, which makes everything possible from tortillas to tortoise toys.
-   Moving around debts is risky if you can end up holding the wrong end of it, and it’s impossible to fully control or eliminate those risks.
-   Regulations do some of it, but they’ll never eliminate the possibility of crises.
-   Making banks hold 100% equity will eliminate the risk in the financial system by eliminating the financial system.
-   Governments and finance have been intertwined since both were born in their modern form. It’s hard to tell whether this is a feature, a bug, or a law of nature. I lean towards the latter.

If you think it’s easy to design an alternative financial system without banks or the governments by repeating the word “blockchain” a lot, [I have some Jacobcoin to sell you](https://putanumonit.com/2018/01/21/jacobcoin/). And if you think it’s easy to fix the system by replacing the carefully crafted system of financial regulation and oversight with a 50% capital requirement and a ban on bailouts, you’re almost certainly an economics professor, and you’re almost certainly wrong.

[1] The top earners in finance do make a lot of money, but the average “banker” doesn’t. Median hourly wage in the finance and insurance sector is [$25.10](https://www.bls.gov/oes/current/naics2_52.htm), compared to [$31.43](https://www.bls.gov/oes/current/naics2_54.htm) in “Professional, Scientific, and Technical Services” or [$29.51](https://www.bls.gov/oes/current/naics2_51.htm) in information and communications. The financial industry is made up of a lot of average people earning an average salary putting in honest effort into average spreadsheets.

[[Back]](#bfoot1)

[2] Early on in FedEx’s history, its founder needed $27,000 to fuel the planes and save the business from bankruptcy. After failing to get just one more bank loan, [he flew to Vegas with his last $5000](https://www.huffingtonpost.com/2012/10/15/fred-smith-blackjack-fedex_n_1966837.html) and miraculously made enough to save the company, pioneer overnight shipping, and make things like Amazon Prime possible for millions of people. Somewhere a great company is closing its doors because the bank that would give it the loan is running up against its capital limits.

[[Back]](#bfoot2)