## The fraud supply chain

I recently wrote a [tweetstorm](https://twitter.com/patio11/status/1465718782781911040) that touched on the supply chain for credit card fraud, and many people said they were surprised by it, so I thought I’d delve into that topic in a little more depth.

The business of fraud is almost as diverse as the business of... business. And it really is a business. Organized fraud has many of the accoutrements of professionalized systems with differentiated labor, like finance itself has. There are HR departments, professional fora, certifications, headhunters, and the like.

This is a surprising fact about the world, and not at all obvious. The mental model most have for crime is that it is largely committed by impulsive, not-terribly-well-organized individuals or small groups. That happens in finance, too, but the bulk of the work is done by professionals.

## Different classifications of payments fraud

One could write several books about fraud without scratching the surface of the topic, and unfortunately the margins of this newsletter contain too little space for them. (The best I have ever read, by far, is [Lying about Money](https://www.amazon.com/Lying-Money-Legendary-Frauds-Workings-ebook/dp/B078WFT5JV) by [Dan Davies](https://twitter.com/dsquareddigest).) So I’ll take the liberty of focusing on payments fraud, which is near and dear to my heart.

Obligatory disclaimer: I work professionally adjacent to this for the last few years at Stripe, and got my start in fraud at a previous employer doing anti-spam research (where the adversary has a truly surprising amount of overlap with payments fraud). The following represents only my own views.

Payments fraud misappropriates money from someone in the legitimate economy by convincing an actor in the legitimate economy to transfer it to someone it does not belong to. There are a million varieties of it; it happens on every conceivable payments rail. Almost anyone in the supply chain of legitimate payments could be targeted by it.

In the industry, we sometimes find it clarifying to bucket fraud by a matrix of intent on the part of the current holder of payment credentials and the intent of the business those credentials are being used at. The ill-intent/ill-intent quadrant is the one most people think of when they think of e.g. credit card fraud, but fraud occurs in the other quadrants ill-intent quadrants, too. Still, this is the easiest to think about: someone steals e.g. a credit card number and wants to turn it into money. How does that happen?

## Stealing credentials wholesale

Some credit card numbers are stolen by individuals. One could pickpocket a wallet, memorize the number of a patron at the restaurant one works at, or sweet talk someone over the telephone into giving it to you by misrepresenting your identity.

But this is not the dominant way cards (or other payment credentials) are stolen.

Amateurs talk strategy or tactics. Professionals talk logistics. Most misappropriation of payment credentials happens at an industrial scale. The industry is often referred to as “carding”, though every method to transfer value is vulnerable to something in this vein, not just credit cards.

Sometimes this happens via security research against firms that see lots of credentials legitimately. A famous example was the Target hack, where approximately 70 million credentials were compromised by malicious software running on legitimate point-of-sale hardware that routinely interacted with physical cards. The software was injected by hacking the network using [credentials misappropriated from an HVAC vendor](https://krebsonsecurity.com/2015/09/inside-target-corp-days-after-2013-breach/), which had itself ultimately been compromised because someone clicked on a link in email that installed malware on their machine.

There are multiple overlapping ecosystems of evil implicated here, and often they form supply chains, where one firm’s outputs are another’s inputs. For example, there is specialization of skill implied in sending malicious email at scale, in compromising the machines of a wide variety of small businesses, in exploiting those machines to e.g. become cloud infrastructure for bad actors or purloin credentials from them, in conducting offensive network security research, in developing malicious point-of-sale software, and in operating said software to steal the cards.

That’s all theoretically within the reach of a single dedicated individual, in the same way that building a software company is within the reach of a single dedicated individual, but most software is not written by individuals acting alone and in isolation. Trust this multi-time solo founder: it’s a heck of a lot of work for one person.

There are other ways to steal cards. You could, for example, send spam email to hundreds of millions of people offering desirable goods at unbelievable (or believable) prices, send them to fake e-commerce sites you control hosted on cloud infrastructure, and get their credit card numbers that way.

Notice that this re-uses a few intermediate outputs from the above example. It’s inefficient for every firm to implement their toolchain from scratch every time they try to do something, which is fundamentally why the economy has firms specialize and buy tooling and services from each other.

Lists of known email accounts, themselves often put together by specialist market research firms (but evil) consuming the work of data scientists (but evil) consuming the work of web application pentesters (but evil), are definitely a product that can be bought. “Ratware” to automate the sending of email such that it ends up in inboxes, like a mail services provider (but evil), is a thing you can buy off-the-shelf or commission from boutique consulting shops (but evil).

This economic activity is coordinated in ways not dissimilar to legitimate commerce. Much of it happens over industry forums (but evil), but there are also marketplace sites (but evil) which have customer service teams (but evil) to administer reputation systems (but evil) so that unsuspecting customers (but evil) don’t get frauded by fraudsters while frauding the fraud they fraud professionally.

And that’s just to get the cards!

## Turning purloined credentials into money

Suppose you have a small amount of text which doesn’t belong to you. You can’t eat text, pay your employees in text, live in text, drive your children to school in text, etc. You want to turn that text into money.

You will turn to the services of a “casher”, or in the alternative you will put your valuable text (payment credentials) for sale such that cashers can purchase it, for example at the above-mentioned fraud marketplaces.

The term Dark Web gets thrown around quite a bit at this point, because it is very evocative, but a lot of this actually happens on the same networks that everything else happens on rather than e.g. on sites which are accessible only over [Tor](https://en.wikipedia.org/wiki/Tor_\(network\)). (Tor is open source security technology developed by the U.S. government originally. Not everything in the supply chain of Evil Inc. is intrinsically bad! Most of it is browsers, programming languages, operating systems, etc etc etc, that are the same as the ones you use.)

Why have the operational split between carders and cashers? The reasons are similar for specialization within firms and professionals engaged in carding, with an additional wrinkle, which is risk. Just like the legitimate finance industry has extremely developed systems to price risk and transfer it to people who want certain slices of the exposure in exchange for certain return profiles, Evil Inc. has relatively safer professional specializations and relatively riskier professional specializations, and having them occur by different people, perhaps in different firms, perhaps in different countries both decreases the total amount of risk in the system and helps allocate it efficiently.

In traditional finance, most risk is denominated in money. In fraud, risk is sometimes denominated in risk of law enforcement action against you and sometimes denominated in adversarial action by fellow criminals. And sure, money, too.

There are as many ways to be a casher as there are to be a carder, and (much like one could be a carder just by stealing a wallet or memorizing a number) one could get in on the ground floor of cashing by acquiring a single credential. You could, perhaps, take that one credential to any e-commerce store you like, buy a thing, have it shipped to you, and then re-sell it for money or enjoy it for your personal use. Casual fraud is very much a thing, and (speaking generally) the targets of it are often the same sort of businesses that struggle with casual shoplifting. (Shoplifting is also sometimes an organized business, as many American cities are currently realizing to their discontent, but that is another newsletter entirely.)

When the legitimate holder of the card finds out that this happened, they’re likely going to call their bank to complain. The bank will reverse the transaction, and the e-commerce store will have to return the funds. They will also pay a fee to the financial system for mediating the dispute, which is designed to encourage companies to contribute their time and talent to zealously protecting the ecosystem.

But back to the bad guys. Notice that taking physical receipt of goods involves some amount of risk, in that it leaves records in the legitimate economy about a physical location which may be tied closely to you personally. If you do this once, you’re abundantly unlikely to come to the attention of law enforcement. But if you make a habit of it, you’re… still, unfortunately, unlikely to come to the attention of law enforcement, but quite likely to come to the attention of fraud departments, which will attempt to shut you down.

So cashers will do other things, both to achieve operational scale and to reduce their risk profile. One example is triangular e-commerce fraud, which (like much fraud) is so brilliant that if it weren’t absurdly evil you’d almost have to admire the folks who thought it up.

The basic mechanic is: open an account on a legitimate e-commerce platform. You operate like a real business, selling valuable things to people for money. You acquire customers by running ads or sending email or competing on SEO or pricing aggressively or what have you.

Then, when a customer orders something from you, you fulfill it at need by going to another e-commerce company (ideally, not on the platform that you transact on), signing up as a new customer, and ordering the thing your customer bought _with delivery to your customer_. You pay with a stolen credit card.

This is really hard for the e-commerce platform to detect, because _you look an awful lot like a legitimate business_! You will have many satisfied customers who legitimately paid you money and legitimately received exactly the product they expected to receive! Very few will notice who sent it, and if they do, they are probably the sort of weirdos who care about e-commerce business models and know that [dropshipping](https://en.wikipedia.org/wiki/Drop_shipping) is a thing that legitimate firms also do.

A funny aside: I first learned the word dropshipping in high school, at my first job, working for a publicly traded U.S. office supplies retailer in their order entry department. During the interview, the rep I was speaking started to explain how to input a dropshipped order in their system, realized she had used jargon, and started to explain it.

I said “I understand the term; that’s when you buy something after the customer orders it and ship it directly from your supplier rather than from your own warehouse. Your free shipping offer doesn’t apply and the customer needs to have an elevator up to the floor the delivery happens on or it will be an additional $75.”

She asked how I, a high school student, knew that.

I said “It’s in your catalog, in the fine print after the order form.” She asked why I had a copy of an office supplies catalog, I replied “I made it my business to know your business.”, and that, reader, is the smartest thing that I will ever do in a job interview.

Other variants on cashing involve money laundering in the legitimate financial ecosystem, often using purloined credentials to buy things-that-aren’t-quite-money then reselling those things for actual money. For example, gift cards are very money-adjacent, and there are thriving businesses that buy and sell them online. Much use of them is perfectly legitimate. Carders could either use purloined credentials to purchase gift cards from an original issuer then resell them for value or use purloined credentials to purchase gift cards from a gift card marketplace. (Entrepreneurs who run gift card marketplaces either go out of business or become the payment industry’s most ruthlessly effective fraud busters.)

## Turning deposits into value close to you

Suppose you have an account at a legitimate e-commerce platform, gift card provider, or similar. You want to accept payouts from it, but may not physically live where they support users or you may just not want to connect your (extremely surveilled) banking information with the nexus of your criminal activity.

You might hire the services of a so-called “money mule.” That person will use an identity, very often their own or that of a person in their family, to receive your funds. They will then move them around in the financial ecosystem the same way they generally move money in the financial ecosystem, send most to you, and keep something for their efforts.

Mules are the mugs of Evil Inc. Many of them don’t even realize they’re participating in a fraud. They’re recruited by advertisements pitching work-from-home opportunities in e.g. “being an accounts receivable clerk.” The basic job description is “We periodically email you descriptions of incoming payments to your bank account. You will forward those to us via a mechanism we specify, for example taking out cash and then sending it via a remittance service to our office abroad. Keep 10% as a commission.”

Money mules are very, very likely to come to the attention of fraud departments and (frequently) the authorities, but this is a very, very appealing pitch, and people fall for it (with varying levels of understanding that it is not legitimate) all the time. They’re difficult to exclude at scale from the financial ecosystem because they’re legitimate people with legitimate e.g. checking accounts. They pass KYC screens with ease; they legitimately are who they say they are and have the government-issued documentation to prove it.

An especially vexatious variant of money mule, from the perspective of the financial industry, is businesses operating as mules. Businesses have legitimate need for moving money around, sometimes in large quantities, at high velocity, in ways which look a little weird if you don't work in them but are probably legitimate. They also get extremely vexed if banks routinely ask them stupid questions about their internal operations. This tends to create a controls environment where business accounts are less surveilled than consumer accounts, though quantifying that is difficult.

My wife once remarked to me, as I was wrapping up one of my startups in Japan, that she had seen an ad for people buying closing companies to “recycle” them and that I could get ~$1,000. “Honey, that’s a crime and the person buying the business is a criminal.” “What, no. They just don’t want to go through all the rigamarole that you had to to open a company and then get a bank account for it.” “No no no, trust me on this, anyone with this pitch is overwhelmingly likely to be a criminal and when the police come looking for the stolen money the person whose name will be on the documents would be me.”

This doesn’t necessarily even require the business to fail and be sold. Sometimes the businesses are in on the scam, sometimes even simultaneously with using the opened accounts for their legitimate business. Sometimes they’re using the accounts simultaneously for legitimate purposes and don’t understand why the thing proposed by their new business partner / client / investor is in any way illegitimate.

## Fraud is an fascinating deep rabbit hole

If I hadn’t fallen backwards into entrepreneurship I think it is highly likely I would have ended up working in fraud full time (on the side of the good guys, to be clear). It is fractally interesting and involves a cat-and-mouse game between very, very talented people.

The financial industry invests a _staggering_ amount of effort into defeating fraud, but that isn’t the only priority. _The right amount of fraud is not zero_. We as a society care, for example, that consumers, even low-sophistication consumers, should be able to walk into any financial institution and walk out with a bank account. A lot of interventions against e.g. money mules would trade off with that societal goal.

If you’re interested in this subject, particularly as a technologist, [Krebs on Security](https://krebsonsecurity.com/) has a lot of great reads.

## Want more essays in your inbox?

I write about the intersection of tech and finance, approximately biweekly. It's free.