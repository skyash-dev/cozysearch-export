The development of vaccines for Covid-19 was a world historical success. The rollout of the vaccines in the United States was plagued with logistical and communication issues.

In January 2021, a ragtag group of technologists spun up a volunteer effort to fix some of these issues with the rollout, beginning with the State of California’s lack of a website listing where one could get vaccinated. Within months they created and operated the shadow data infrastructure for the US vaccination effort. This infrastructure quietly bridged public and private sector response efforts, made the vaccine Googleable, and directly enabled healthcare providers to save many thousands of lives.

This is our story. It’s a window into an undercovered facet of the overall pandemic response effort. It’s a tale of startup-infused derring-do and frequent institutional failure. I hope that we as a society can learn from it to inform our rapid-response efforts in the future.

All the opinions I express below are in my personal capacity and do not necessarily reflect the views of Call the Shots, Inc., other members of the team, volunteers, funders, partners, or any other organization I may be affiliated with.

_Editor’s note: This is a very long essay, but we promise it’s worth it._

## January 2021

Operation Warp Speed, one of the most effective research projects in history (well chronicled, warts and all, in [_A Shot to Save the World_](https://www.amazon.com/Shot-Save-World-Life-Death/dp/059342039X)), had successfully delivered multiple vaccines that were effective against the then-dominant variant of Covid-19 (alpha). After bureaucratic dithering, the Pfizer-Biontech and Moderna vaccines were given emergency-use authorization on 11th and 18th December 2020.

While Warp Speed was immensely successful in the face of substantial technical risk, balls were being dropped throughout the public health establishment. Everyone thought someone else was going to solve the vaccine distribution problem. This resulted in a patchwork, poorly coordinated constellation of distribution policies from the US federal government, national healthcare providers, state governments, county- and city-level public health departments, and a diverse list of vaccine providers ranging from pharmacies to fire departments to jails to individual doctors.

The system confronting the public in early January 2021 would be fairly described as chaotic. This was not the only chaos in early January, and unfortunately the political ramifications of the events of 6th January colored the response efforts of many actors, frequently decreasing their effectiveness. We’ll get back to that later.

## The logistical problem that wasn’t

It was [widely believed](https://www.npr.org/sections/health-shots/2020/11/17/935563377/why-does-pfizers-covid-19-vaccine-need-to-be-kept-colder-than-antarctica) by the professional commentariat and in the public health field, at least early in the rollout, that shipping and storing the Covid-19 vaccines would require unprecedented feats of infrastructure. This was untrue. The Pfizer vaccine [keeps](https://www.cdc.gov/vaccines/covid-19/info-by-product/pfizer/downloads/storage-summary.pdf) for ten weeks when transported or stored unopened between two degrees Celsius and eight degrees Celsius (36°F and 46°F), which is the [_exact_ same range as the flu vaccine](https://www.cdc.gov/h1n1flu/vaccination/storage_handling_qa.htm) and overlaps that of _milk_. It is then viable for 12 hours at temperatures between 8°C and 25°C (46°F to 77°F). That is... room temperature. Moderna’s version is [only slightly](https://www.cdc.gov/vaccines/covid-19/info-by-product/moderna/downloads/storage-summary.pdf) more difficult to work with.

Transportation was easily achievable via [cold-chain logistics](https://www.trade.gov/cold-chain-services), abundantly commercially available in the US and already [used pervasively in the pharmaceutical industry](https://blog.vrr.aero/the-role-of-cold-chain-logistics-in-the-pharmaceutical-industry/). If administering the vaccine in adverse environments, like a parking lot on a hot day, you can keep it adequately cool with portable dry ice packs. They are available at noted high-tech medical infrastructure provider Walmart.

If an actor wanted to store it _for a year_, they did need a specialized freezer. Perhaps they could have cooled it with their hearts, because there was overwhelming need for the vaccine as quickly as it could be manufactured.

The product rollout for the vaccine should have been approximately as logistically straightforward as any product rollout in the United States. It was not, principally because it did not use the US’s formidable advantages in coordinating product rollouts.

## Hyperlocal market clearing

You need four things to administer the vaccine: a patient, a healthcare provider, a space with some air that will accommodate approximately 30 minutes of dwell time, and a vial of the vaccine. Critically, they must all be in the exact same location at the exact same time for at least one minute.

The single greatest solvable strategic issue facing the US vaccination effort early on was that we had overwhelming demand for the vaccine, limited supply of vials, and no ability to direct the demand to go where the vials actually existed.

This was directly caused by decisions in how to distribute the vials. They were directed into multiple parallel and overlapping supply chains that had extremely imperfect knowledge of one another. We’ll get to that, but for now let’s oversimplify: Vials were allocated by the federal government to states, which allocated them to counties, which allocated them to healthcare providers and community groups. The allocators of vials within each supply chain had sharply limited ability to see true systemic supply levels. The recipients of the vials in many cases had limited organizational ability to communicate to potential patients that they actually had them available.

Patients then asked the federal government, states, counties, healthcare providers and community groups, ‘Do you have the vaccine?’ And in most cases the only answer available to the person who picked up the phone was ‘ _I_ don’t have it. I don’t know if _we_ have it. Plausibly _someone_ has it. Maybe you should call someone else.’ Technologists will see the analogy to a distributed denial of service incident, and as if the overwhelming demand was not enough of a problem, the rerouting of calls between institutions _amplified_ the burden on the healthcare system. Vaccine seekers were routinely making _dozens of calls_.

This caused a standing wave of inquiries to hit all levels of US healthcare infrastructure in the early months of the vaccination effort. Very few of those inquiries went well for any party. It is widely believed, and was widely believed at the time, that this was primarily because supply was lacking, but it was often the case that supply was frequently _not being used as quickly as it was produced_ because demand _could not find it_.

## Perhaps California has someone who could make a website

There were widespread media reports in early January of patients only finding the vaccine after making dozens of phone calls in California. The numbers were even more brutal than the anecdotes. California had to report to the feds the number of vaccines they had injected against the number they had been shipped. Their [reported efficiency](https://www.vox.com/future-perfect/2021/1/15/22231241/california-coronavirus-vaccine-availability-moderna-pfizer) at getting shots in arms placed them 49th in the nation in mid-January; they told the feds they had administered 27 percent of delivered shots and, by implication, 73 percent of them were still in the freezer.

This seemed _bonkers_ to me.

I’m an American technologist who has lived my entire adult life in Japan. The beating heart of the tech industry, a rich and well-educated part of a rich and well-educated nation, _clearly_ had better options than ‘have _every_ resident call _every_ doctor to look for where the vaccine is.’

So I [tweeted](https://twitter.com/patio11/status/1349577791537250310) a suggestion that someone undertake a civtech (civic technology) project:

![](https://wip.gatspress.com/wp-content/uploads/2023/02/tweet-that-started-things-1024x691.png)

Image

Patrick McKenzie. @patio11 on Twitter, January 14, 2021.

I then offered to fund server costs, so that no one would be intimidated by the prospect of succeeding. I thought a working prototype could be ready in hours and immediately useful to patients.

Karl Yang [took up the gauntlet](https://twitter.com/chiefofstuffs/status/1349584512859074565). Unbeknownst to me at the time, he was working from Indonesia during my afternoon in Japan. This was late in the evening in California. (For convenience, all further mentions of time will be the time in California.) Karl quickly set up a server on Discord, a program mostly used for coordinating play of video games, and invited several friends he knew from the tech industry.

I ducked into the Discord. I thought I would be there for a few minutes to explain to the team how call centers work, which would shortly become extremely relevant to their interests. Then my plan was to tweet about their launch in the morning and go back to my usual life of working for the internet. Little did I know.

A core group of approximately ten coordinators worked through the night. They’d end up forming the nucleus of our operations for the first few weeks, and many of them stayed on for the duration, but we never could have done it without many other volunteers writing code and making phone calls. We had about 70 people pitching in that first night. Most of them were the colleagues, friends, and professional acquaintances of the first people Karl thought of after reading my tweet, who got a text or Slack message after dinner that rhymed with, ‘Hey, are you free? I am working on the pandemic.’

The tech industry, like California, is both very diverse and has some identifiable cultural leanings. This also describes our team. Many of us are, well, Berkeley liberals. One team member was even a political appointee in the Obama White House. I, by contrast, got the franchise just in time for Obama’s Senate race and therefore have a coveted perfect record of picking the loser in every election he was ever in.

We didn’t spend our time pointing fingers; fingers are better used banging out code, googling for lists of healthcare providers, or making calls to pharmacists. I suspect that many team members would disagree strongly with what I came to believe about the causes of the dysfunction we were seeing. We were absolutely united in not accepting that dysfunction.

We had technical work to do: sourcing lists of Californian healthcare providers, creating a spreadsheet, building a website backed by the spreadsheet, and the like. We had some uncertainty as to whether we’d be able to get useful information for the spreadsheet without having a privileged vantage point within the US healthcare system.

I resolved this ambiguity in a very startup-y way: I googled for the phone number of the Walgreens at Fourth and Townsend in San Francisco. I have been to San Francisco on business before; that Walgreens is right next to the city’s main Caltrain station. (Like everyone living in Japan, I assume that a city is centered not at its geographical midpoint but at the train station. A human is a heart or a brain or a soul, depending on your desired level of poetry, and in Japan at least a city’s beating heart is the train station that bears its name.) I called at 9:30am and asked to speak to the pharmacist. Without identifying myself or giving any preamble I asked, ‘Could a 65 year old get the Covid vaccine, and, if so, how?’ The pharmacist told me that they didn’t have it but to check back in two weeks.

I reported to the team that the US healthcare system would happily give vaccine inventory information to literally anyone calling. We immediately started calling the healthcare providers in the spreadsheets we had compiled overnight.

Over 70 volunteers placed about 125 calls on Thursday, successfully finding 24 sites with available vaccines. We put the reports on our site as soon as we had them and tweeted to get the word out. Our entire plan, at this point, was to scale up this operation.

## On being legally forbidden to administer lifesaving healthcare

It is legal by default to save a life, unless it is through healthcare, in which case it is illegal by default to save a life, unless one has a license to practice healthcare, in which case it is legal by default to save a life, unless it is early 2021 and your intervention of choice is a Covid vaccine, in which case it is illegal by default to save a life and _don’t you forget it_.

It is a biological fact about Covid that some people are vastly more at risk from it than others. In particular, [risk of death goes up with age](https://www.cdc.gov/coronavirus/2019-ncov/covid-data/investigations-discovery/hospitalization-death-by-age.html). The magnitude of this effect is so large that it breaks many people’s intuitions about risk, including those of whom work in public health and in medicine. You know how smoking causes lung cancer? The [relative risk](https://www.cdc.gov/cancer/lung/basic_info/risk_factors.htm) of a smoker developing lung cancer is about 25 times that of a nonsmoker. The relative risk of death for a 55-year-old from Covid compared to an 18-year-old is... roughly the same, 25 times. The relative risk of an 85-year-old compared to an 18-year-old is... roughly _350 times_. These are _staggering_ disparities compared to most risk factors in healthcare, _including_ other commonly identified risk factors for Covid. This was _extremely_ well understood scientifically by early 2021.

It was a logistical fact about the Covid vaccines that we had far fewer doses than people living in America in early 2021.

The United States government decided to resolve this temporary-but-undeniable shortage by instituting a prioritization system, leaving the exact contours of that prioritization to its political subdivisions. In broad strokes it expected that the vaccine would first be administered to healthcare providers, so-called essential workers, the elderly, and people with conditions that would pose an increased risk of severe outcomes. The plan was always to vaccinate everyone who wanted a vaccine, at the public’s expense, _eventually_.

Political subdivisions of the United States then conducted politics briskly, and made choices about who would benefit from lifesaving medical care under conditions of extreme scarcity and who would not (yet).

Sometimes these decisions were based on medical reality. Sometimes they were based on political expediency. Very rarely were they effectively administered.

A key consideration for us, from the first day of the effort, was recording not just which pharmacist had vials but _who they thought they could provide care to_. This was dependent on prevailing regulations in their state and county, interpretations of those regulations by the pharmacy chain, and (frequently!) ad hoc decision-making by individual medical providers. Individual providers routinely made decisions that the relevant policy makers did not agree comported with their understanding of the rules.

VaccinateCA saw the policy sausage made in real time in California while keeping an eye on it nationwide. It continues to give me nightmares.

California, not to mince words, prioritized the appearance of equity over saving lives, over and over and over again, as part of an explicitly documented strategy, at all levels of the government. You can read the sanitized version of the rationale, by putative medical ethics experts, in [numerous official documents](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Allocation-Guidelines-COVID-19-Vaccine-Phase-1A.aspx). The less sanitized version came out frequently in meetings.

This was the _official_ strategy.

The unofficial strategy, the result the system actually obtained, was that early access to the vaccine was preferentially awarded based on proximity to power and to the professional-managerial class.

The [California prioritization tiering list](https://www.sandiegocounty.gov/content/dam/sdc/hhsa/programs/phs/Epidemiology/covid19/vaccines/Know%20Your%20Vaccination%20Phase_ENG.pdf) is abundantly available on the historical record, though it doesn’t record a hundredth of the horse-trading that was involved in writing and implementing it. (As a note to the reader, your state or county may have used different labels or used the same labels but had them mean different things, or changed the meaning of the labels on a weekly basis. Public communication regarding prioritization was a confused mess.)

Consider ‘essential workers’, a concept that predated the availability of the vaccines. If you weren’t on the [Essential Critical Infrastructure Workers list](https://covid19.ca.gov/essential-workforce/), you were at risk of being locked indoors and suffering economic damage, to say nothing of being deprioritized for the vaccine, and so _clearly_ your lobbyists were very bad at their jobs. You should have had better lobbyists. The essential workers list heavily informed the vaccination prioritization schedule. Lobbyists used it as procedural leverage to prioritize their clients for vaccines. The veterinary lobby was unusually candid, [in writing](https://media.kalzumeus.com/vaccinateca-wip/Vaccine-Status-Update-1-8-2021-1.pdf), about how it achieved maximum priority (1A) for veterinarians due to them being ‘healthcare workers’.

Teachers’ unions worked tirelessly and landed teachers a 1B. They were ahead of 1C, which included (among others) non-elderly people for whom preexisting severe disability meant that ‘a covid-19 infection is likely to result in severe life-threatening illness or death’. The public rationale was that teachers were at elevated risk of exposure through their occupation. Schools were, of course, mostly _closed_ at the time, and teachers were Zooming along with the rest of the professional-managerial class, but teachers’ unions _have power_ and so 1B it was. Young, healthy teachers quarantining at home were offered the vaccine before people _who doctors thought would probably die if they caught Covid_.

Now repeat this exercise up and down the social structure and economy of the United States.

There were literal and metaphorical passwords to get priority access to the vaccine. Non-intended use of them was rampant. Stories, often told in whispers, of widespread corruption in administration of the vaccines (‘Donate $10,000 to a nonprofit hospital and get scheduled for a shot immediately’, ‘Learn a password from your brother in the FBI and...’ ‘Be a friend of the governor and...’ etc) led to crackdowns. Elected officials held press conferences to promise that unauthorized healthcare was public enemy number one.

This led to the worst of all possible worlds.

Healthcare providers were [fired](https://www.nytimes.com/2021/02/10/us/houston-doctor-fired-covid-vaccine.html) for administering doses that were destined to expire uselessly. The public health sector devoted substantial attention to the problem of _vaccinating too many people during a pandemic_. Administration of the formal spoils system became farcically complicated and frequently outcompeted administration of the vaccine as a goal.

The process of registering for the vaccine inherited the complexity of the negotiation over the prioritization, and so vulnerable people were asked to parse rules that routinely befuddled healthy professional software engineers and healthcare administrators – the state of New York [subjected](https://twitter.com/polly/status/1348464494108954626?s=20&t=089XTa7069Rs4Ft0pA4CkQ) senior citizens to a ‘51 step online questionnaire that include[d] uploading multiple attachments’!

That _isn’t hyperbole_! New York _meant_ to do that! On purpose!

_Lives were sacrificed by the thousands and tens of thousands for political reasons._ Many more were lost because institutions failed to execute with the competence and vigor the United States is abundantly capable of.

## The Department of Public Works adopts good intentions as a road surface

VaccinateCA was told, more than a few times, that merely listing the availability of the vaccine and eligibility requirements on a publicly accessible website compromised the desire of some group or another to earmark ‘their’ doses for ‘their’ clients.

We had a golden rule here: We’d obey instructions from medical providers regarding their operations. If a pharmacist wanted to be delisted, for any reason, we’d do it. Everyone else in society was welcome to their opinion. If a politician or civil servant complained that listing doses available in their district complicated their ability to reward favored constituencies, they were welcome to tell us so. It’s a free country. Did I personally have to take immediate action to _implement_ their opinion? It’s a free country.

Why did California go head over heels for equity? Aside from the political valence of it and the point at which American society was less than a year after George Floyd’s death, it is classic [bikeshedding](https://en.wiktionary.org/wiki/bikeshedding). Most people in civil society cannot develop, manufacture, distribute, or administer a vaccine. Decrying systemic racism, on the other hand, is quite accessible. We exhaustively train the entire professional-managerial class in doing it. Accordingly, official discussions of strategy for the vaccination effort quickly bent toward systemic racism. Lacking any ability to contribute regarding one pressing problem, many individuals of good will focused on the other.

I believe this routinely was counterproductive for _both_ goals. I feel it necessary to acknowledge that this sounds like the rantings of an unhinged mind and, my mind being hinged, to acknowledge that I know what it sounds like.

It is a true historical fact that government officials embraced an explicit policy of prioritizing lives in the present pandemic to atone for historical inequities. Sometimes, and frequently in California, they had a level of discretion about writing down the rationale, intent, and planned mechanisms of their policies. Vermont [eschewed all euphemisms](https://khn.org/news/article/vermont-gives-blacks-and-other-minority-residents-vaccine-priority/).

Efforts here were directly counterproductive _according to their own terms_, including on occasions that I directly witnessed and ones where I have credible reports from people I worked with. A full accounting of them would shock the conscience of a democratic society that considers itself a nation of laws.

Perhaps private experiences would be considered insufficient evidence of extraordinary claims. Let us proceed, then, to the written record.

## In which California institutes a policy of redlining for justice

The State of California instituted a policy of redlining in the provision of medical care in a pandemic to thunderous applause from its activist class and medical ethics experts. They called it ‘residency restrictions’, except that one time Governor Gavin Newsom called it ‘geofencing’ during a [press conference](https://www.youtube.com/watch?v=HtYxQoMecUM).

> [We have] one site in Northern California, Oakland Coliseum, focused exclusively on the issue of equity, geofencing the geographic areas in and around [it] to make sure that underserved and underrepresented communities are getting their fair access to the vaccines.

Since the tech industry uses ‘geofencing’ to mean figuring out whether your phone is in a particular area to, e.g., target ads for the local burger joint or say, ‘Welcome to the airport, would you like to take a rideshare?’ and not to mean denying people healthcare based on where they live, I will use ‘residency restrictions’ for what California did.

Residency restrictions were pervasively enforced at the county level and frequently finer-grained than that. A pop-up clinic, for example, might have been restricted to residents of a single zip code or small group of zip codes.

All people are equal in the eyes of the law in California, but some people are... let’s politely say ‘administratively disfavored’.

The theory was, and you could write down this part of it, disfavored potential patients might use social advantages like better access to information and transportation to present themselves for treatment at locations that had doses allocated for _favored_ potential patients. This part of the theory was extremely well-founded. Many people were willing to drive the length and breadth of California for their dose _and did so_.

What many wanted to do, and this is the part that they _couldn’t_ write down, is deny healthcare to disfavored patients. Since healthcare providers are [public accommodations](https://calcivilrights.ca.gov/unruh/) in the state of California, they are legally forbidden from discriminating on the basis of characteristics that some people wanted to discriminate on. So that was laundered through residency restrictions.

Unfortunately for this plan, another advantage disfavored patients have is ability to _prove their residency to a bureaucratic process_. They are more likely to have a government-issued ID with their current address. They easily sailed through approved secondary checks, like ‘Show us a piece of paper mail addressed to you’, because, e.g., banks knew where they lived and sent them credit card offers frequently. Disfavored patients were far less likely to have informal or frequently changing living arrangements. For more on those mechanisms, see literally anything ever written about voting rights.

And so government actors, in their majestic embrace of public health equity, [allocated doses preferentially](https://www.healthyplacesindex.org/post/hpi-north-star) (fully twice as many, on a per-eligible-potential-patient basis) to providers in neighborhoods low on the [Healthy Places Index](https://www.healthyplacesindex.org/). That wasn’t illegal. Who could not be in favor of providing more healthcare in on-average unhealthy places?

They did this out of explicit intent to give care to, and this per the explanation of the director of the Office of Health Equity, ‘people who would not otherwise have been prioritized early on’ had the allocation been prioritized according to medical necessity. We were willing _to spend more lives in total_ in the cause of reducing disparity in death _rates_ along axes that are politically salient in California, by allocating resources in a manner _we knew_ to be inefficient.

Did we execute _competently_ on this plan? No.

When the residents of those neighborhoods dear to the state showed up to receive healthcare, they had to hope that the person providing it knew that the residency restriction was only supposed to apply if you were a disfavored patient. But that policy _could not be written down_, and the _actual written policy_ said that the rules applied to everyone. And the rule was frequently that you could not get treatment without proving residence.

Remember, the state was extremely adamant that they would terminate the license (and thus career) of any healthcare provider who ignored instructions during the pandemic. And so many healthcare providers _did what the state told them to do_ and enforced the residency restrictions _to deny healthcare to the people the residency restrictions were instituted to benefit_, including in the places where they _factually lived_.

When residency restrictions were implemented in neighborhoods that generally have _excellent_ access to healthcare, they were frequently executed with _enthusiasm and ruthless efficiency_. For more on this topic, see anything ever written about residency restrictions in public schools. ‘Oh, I’m sorry, dear, but my hands are tied. The state says I cannot give you medical care if you cannot prove to me that you live here. No, just living here is not good enough, I need to see the proof. Lower your voice, sir, this is a hospital. I am sorry you feel that way, but if you do not leave, I will call the police.’

The state and counties spent tens of millions of dollars to get consultancies to build them software to _scalably_ _enforce the denial of healthcare via residency restrictions_. The web applications would block you from registering for an appointment if you could not _demonstrate to a computer_ that you were eligible. (We were frequently told _by pharmacists_ that patients should lie to the web application so that they could get an appointment, and then the pharmacist would look the other way, because _damn the rules I swore an Oath._)

Organizations throughout the United States devoted a huge portion of their efforts early in the vaccine rollout to make sure they were reserving ‘their’ doses for ‘their’ people. It was ludicrous to spend effort hoarding property rights to doses in a freezer during a pandemic. There are merely _the people’s doses_ which should be accelerated into _the people’s arms_, arms being _the only places they do any good_.

How did patients experience hitting a residency restriction? Like so:

Say you _were eligible_ for a dose. The medical experts and the tiering list and the state and the county frequently all agreed you needed _a_ dose, today. You _had waited_ for your turn. And if you were the right sort of person, you could have had _this_ dose, this dose sitting in the freezer, this dose that no actual patient has spoken for yet. But you were _not_ the right sort of person for _this_ dose. We have better plans for _this_ dose than treating _you_. Not medically better plans, no, we agree that the tiering list says what it says, and we must pretend that that is our best understanding of medical reality, and based on that tiering list it is your turn. No, we mean better plans for a _different_ reason, which we feel absolutely no need to explain to you.

Where was _your_ dose? Answering that question was not the system’s problem and, honestly, the system was probably offended that you displayed such _entitlement_ to the care that the system agrees you were immediately eligible for. Now stop wasting the system’s time, because the system has important work to do delivering healthcare to important patients.

Our society stranded doses in freezers, for justice. We instituted and enforced policies to deny healthcare during a pandemic. We called men with guns into places healthcare is delivered, to throw out people whose crime was seeking healthcare. And we now sleep the sleep of the righteous.

Meanwhile, pharmacies across California had doses _sitting in the freezer_. Again, in mid-January, California told the feds that they were only injecting about a quarter of shipped doses. There was a lot of energy put into deciding who would get the _one dose_ the system was capable of competently administering; there was grossly insufficient effort, at the time, put into pointing eagerly waiting patients toward the _three doses_ the system was not.

VaccinateCA effectively became an outsourced marketing team for doses allocated to pharmacies. Why did the most anticipated product launch in history need a marketing team? We’ll return to that in a moment.

## Building the world’s least impressive inventory-tracking system

In the US healthcare system, a pharmacist is reachable by telephone (to receive new prescriptions from healthcare providers and answer questions from patients), individually responsible for managing supplies within their pharmacy (with their technicians), and legally allowed to administer vaccines. This trifecta gives pharmacists oracular insight as to whether their pharmacy can currently vaccinate a patient and under what circumstances.

As I repeated ad nauseam to people for the next several months: If The System disagrees with a pharmacist as to whether that pharmacist can inject you right now, the pharmacist _is always right_. No database and no policy mattered in the face of the medical provider who individually could administer the vaccine and knew how many doses they had remaining.

We called that the ‘ground truth’ and optimized _maniacally_ for getting it. Happily, pharmacists knew the ground truth. And indeed, within days of our calling campaign starting, pharmacists started to tell our (oft anonymous!) callers, ‘I don’t have the vaccine but you should go to Vaccinate C A dot com. They know who has it.’

## Clearly this was not the United States of America’s actual plan

The incoming administration complained furiously to the press early in 2021 that they had been left no plan for distribution from the outgoing administration. It was necessary for the success of our operation that we be scrupulously politically neutral. I will observe that various groups, including many levels of government, had been planning for the distribution effort since early 2020.

The State of California, for example, commissioned a statewide website for finding the vaccine and getting an appointment for it. My Turn was commissioned from Accenture, which the state had tapped to lead contact tracing software development in [May 2020](https://files.covid19.ca.gov/pdf/Accenture-LLP-CDPH.pdf) and its vaccine distribution systems in [December 2020](https://files.covid19.ca.gov/pdf/Accenture-LLP-CDPH-2.pdf). My Turn was rolled out in late January 2021 to help coordinate [more than 60 distribution systems](https://techblog.cdt.ca.gov/2021/04/myturn-working-for-california/).

I must neutrally observe that My Turn was delivered almost a year into the pandemic, that the gap between the delivery of the first vaccine to California and the availability of the first appointment through My Turn is substantial, and that My Turn was of limited utility at launch. It was not able to actually show appointment availability until early March. It would not let you ‘get in line’ without immediate appointment availability for you. My Turn, during the early months of the vaccination campaign, could not direct Californians to most supply present in California. It _still cannot_, though abundance means that is less of a problem.

Abundance is the only cure for scarcity, ever. Everything else merely _allocates_ scarcity. Institutional competence would minimize the depth of that scarcity. Unfortunately, our institutions underperformed their capabilities, and scarcity _was worse_ as a consequence.

All software problems are people problems. For example:

Several California counties had independently commissioned consultancies to write their own vaccination registration portals and refused to use My Turn (or make ‘their’ doses available through it). They had not asked their consultancies to include compatibility with My Turn when they asked them for bids on pandemic software projects, and accordingly their consultancies had not delivered interoperability. The counties had budgetary and political reasons for not approving a change order. The state had budgetary and political reasons for not forcing them to.

My Turn also did not surface doses available to Californians that were not ‘California’s’ doses. Unfortunately, California only administered about half of the doses available to Californians. We’ll return to the other half in a moment.

As a result of being late, breaking frequently in the early weeks, not being easy for most Californians to use, and lacking supply that factually existed, My Turn’s impact on the experience of Californians was perhaps less extensive than one would model the officially instituted Californian one-stop shop for the vaccine. _CalMatters_ reported that, by April, My Turn was responsible for [about a quarter](https://calmatters.org/health/coronavirus/2021/04/myturn-vaccine-appointments-problems/) of new daily appointments, based on data from the Department of Public Health.

There was the usual amount of government-contracting tomfoolery. Governments purchase processes, not outcomes. Contractors sell them _exactly_ the thing they say they are buying, not the thing they will say that they want.

The State of California and Accenture consider My Turn a great success. VaccinateCA was institutionally in favor of every effort to get more shots into arms faster.

## The System does not know where the vaccine is

We found it surprising that The System did not know where the vaccine was and that this fact persisted. The System allocates and ships the vaccine, after all. Devolution to various layers of government, community groups, and healthcare providers; pervasive inability to connect IT systems; and unwillingness to correct this problem meant that people in positions of authority considered the ground truth _beyond the abilities of their institutions to discern_.

It is not harder to track a shipment of vaccine than it is to track a package from Amazon. Full stop. We are a nation that is _extremely skilled_ at logistics, including healthcare logistics. A pharmacy chain can calculate, within a matter of minutes, the number of bottles of aspirin it owns, broken down by address. That count will be _shockingly_ close to physical reality. Capitalism, ho!

We chose, as a nation, that knowing the location of the vaccine was... just not a top priority.

As an example of places where the data chain of custody broke down, consider the (true) case where a government actor directs some vials that it controls into the University of California at XYZ hospital system. (I will elide naming the specific hospital system, but for people not familiar with California, note that there are many different academic institutions called the University of California and their names are distinguished by the city they are primarily located in.) That hospital system has one address, according to a shipping spreadsheet.

That hospital system routinely _centrally_ receives, records, allocates, and reships all the medical supplies needed to keep a hospital system running, from saline to radiomedicine to scalpels. Then it parcels them out to the locations it provides healthcare at. Which it has _more than one of_ and which are _not a short walk from one another_. I invite you to take a look at the [locations list for the University of California at San Diego hospital system](https://health.ucsd.edu/locations/Pages/default.aspx).

We surprised the government by telling them that the vaccine was present where they believed it was absent. After delivery was taken at the central receiving facility, the vaccine was moved to individual locations where healthcare was conducted within the area of interest.

The pharmacist whose hand is physically on a vial of vaccine is right that she has it. The spreadsheet that says she cannot possibly have it because they haven’t shipped it to her because it doesn’t have her address listed _is mistaken_.

If you are a little perplexed as to why a software engineer needs to tell public health officials that university hospital systems frequently have more than one physical location, know that I was perplexed by it too.

The federal government, the states, the counties, and even some private actors routinely didn’t know where ‘their’ vaccine was.

Note that if you don’t know where it is you _don’t know where it isn’t_, either, and shipments meant to alleviate scarcity sometimes ran into responses like, ‘Why are you shipping me this? Doesn’t anyone need it more? I already received doses this week.’

Who else was shipping doses? The Veterans Administration was one prominent example, and their supply chain was almost entirely opaque to state planners. There were other ones too. My hometown of Chicago got a direct allocation from the feds rather than through Illinois or Cook County, for reasons I never had time to investigate.

Those doses were critically needed _elsewhere_ that same day, but allocators were too frequently doing instrument-only navigation when their instruments were lying to them, resulting in the logistical equivalent of controlled flight into terrain. This was _not_ a tiny little spreadsheet issue during a busy time; people _died_ because their shot was delayed by inability of governmental organizations and their IT systems to present allocators with sufficient information to make optimal decisions.

Who is to blame for this? Blame is an irrelevant concept; only our actions and results matter. Our actions created an internal command economy; our results were consistent with those usually experienced by command economies.

You can’t point patients at ‘your’ vaccine, or try to sensibly balance supply levels across locations, if you _don’t know where it is_.

## The vaccination effort as a grocery store

Imagine you want to check out at a grocery store during a busy time. Pretend you could not see the lines at each register. You just have to pick a line and hope it is short.

You intuitively understand that this cannot possibly be as fast as when you see all the lines, right? While you personally may not have a PhD in operations research, being able to pick the really short line is clearly better than ending up at the end of the really long line. Right?

Now let’s turn our attention away from you, toward someone much more unfortunate. We should care a bit about the unluckiest person in the grocery store, the last person checking out of the last register to empty their line. Call him Bad Luck Bob. Would Bob have benefitted if everyone, including Bob, could see the lines? Clearly yes. Some people in front of Bob would have picked other lines, not the longest line, and so Bob’s line would have been shorter. Bob gets out of the grocery store faster if the lines are visible, even though Bob is _always_ the last person out of the grocery store, because by definition _every grocery store must produce a Bob_.

This is an extremely simple result in [queuing theory](https://en.m.wikipedia.org/wiki/Queueing_theory). People directing patients (health departments, medical providers, friends and family, and patients themselves) who couldn’t see the length of the lines (supply/demand situation in an area) directed them less efficiently than if they had been able to see the lines. _Every patient was harmed by this._

Another simple result from queuing theory: Not letting people change lines is _guaranteed_ to lengthen the time it takes Bad Luck Bob to check out. People changing lanes is an important mechanism for keeping all cashiers active, which maximizes the throughput of the store _as a unit_. That seems like a result people interested in equity should pay more attention to.

What if only half of people can switch lanes? What if switching lanes requires _privilege_? Then you _definitely_ want that half to move out from in front of less privileged people in the slow lanes and into the lanes that have less waiting people! It will get those people with less privilege checked out sooner! That is your real goal, right, not simply avoiding line switching for its own sake?

Residency restrictions are _policy_ _bans on switching lanes._ They resulted in obviously inefficient and inequitable results like one county having locally raced through phase 1B to 1C while 1B patients distinguished only by living on the other side of the county line could not access locally abundant doses. This was _pervasive_ until perception of improved supply caused political subdivisions to abandon their residency restrictions, which was frequently substantially after the state declared that all adult Californians were now immediately eligible.

## The politics of public health and the tech industry

Here be dragons.

What if the State of California had an alternative to engaging consultancies to deliver information systems months late and half functional? What if it, for example, had the world’s leading tech industry, which is abundantly capable of shipping and operating websites? What if that industry was also extremely experienced at solving scaled logistical challenges, including ‘atoms, not bits’ logistical challenges, including via the employment of tens of thousands of call center workers?

Throughout the pandemic, as part of the ongoing estrangement between the tech industry and other corridors of power, there was [unwillingness in the political class](https://www.theatlantic.com/magazine/archive/2020/07/big-tech-pandemic-power-grab/612238/) to work directly with the tech industry. You can write the tweet yourself, right? ‘Government tells Big Tech to ask millions of vulnerable Americans about their medical conditions. So they can do what, sell their data to advertisers?’ It certainly did not help matters that various people in positions of power assumed tech was complicit in serial prevarication being heard from _elsewhere_ in the public sector, including about, e.g., [Covid testing](https://www.vox.com/recode/2020/3/15/21180518/coronavirus-google-verily-website-testing-trump).

This rift deepened _sharply_ in the immediate wake of 6th January, which many important people [laid at the door](https://www.wsj.com/articles/capitol-riot-puts-more-scrutiny-on-big-tech-11610372968) of tech. Damn techies trying to Ctrl-Alt-Delete constitutional democracy; _they will pay_.

Actors within tech can _also_ read the newspaper, watch their political leaders make speeches, and understand that they need to take immediate action to preserve their literal and figurative licenses to stay in business. Government relations and PR teams at AppAmaGooBookSoft told everyone that the marching orders were Keep Your Heads Down and Avoid Media Coverage during early 2021. This _directly interfered_ with the efforts that public health teams at AppAmaGooBookSoft were making contemporaneously. (It probably surprises many people outside the tech industry that AppAmaGooBookSoft have teams dedicated to public health. AppAmaGooBookSoft are increasingly the operating system for the world, whether one desires that to be true or not. _Of course_ their operations touch healthcare, governments, and government departments responsible for healthcare.)

In deference to the professional reputations of people who worked with VaccinateCA, I will not at length transcribe the internal decision-making of our partners, either at AppAmaGooBookSoft or in government. Ask them for their stories, hopefully over a _very_ stiff drink.

An observation from Joel Spolsky bent the course of my life: In his (Jewish) faith tradition, those given gifts must use them on behalf of society, and I (specifically) was at risk of squandering my gifts by being content to be the world’s leading expert in [bingo card typesetting](https://www.kalzumeus.com/2016/08/26/kalzumeus-podcast-episode-13-selling-online-businesses-with-thomas-smale/). Luke 12:48 expresses a similar sentiment. So does Spider-Man.

I keenly believe that the tech industry underperformed in proportion to our capabilities and responsibility to society during the pandemic. We had great power, less than some but more than many, and we did not wield it to the absolute limits of our capabilities in the service of humanity.

## Skepticism of technological solutionism in government

Members of our team attempted to do due diligence via conversations with public health officials in the earliest days of VaccinateCA.

An official working on vaccine distribution had limited enthusiasm for prioritizing a searchable map of vaccine availability:

> It would probably help with public communication to have a map like the one you describe, and we could probably build (and verify) in less time than you would expect, especially given what I read as your sometimes-correct view of the glacial pace of government. However, it comes with a lot of ancillary considerations. For example, it would be very bad to send people to a location for a vaccine only to be turned away because a website was wrong, especially if those people are seniors, or front-line workers who only get limited time off of work. It also doesn’t help folks who don’t have smartphones or lack the technical savvy to understand this kind of information, who, demographically speaking, are more likely to be the ones who need the early vaccine doses anyway.

I replied that this was a persuasive argument against shipping a map _which was wrong_. Not being able to help _everyone_ is not a persuasive reason to not do things that help at the margin though. We instead intended to ship a map that would improve over time, beginning _immediately_, versus waiting for a theoretically perfect veto-proof proposal.

We eventually impressed many people in government, including that correspondent, who wrote (five _days_ later):

> Wow!... I’m genuinely impressed – I know the tech community can be fast, but it’s rare to be a) this fast, and b) this willing to do the hard work of calling places like this. Let me know if there’s any way I can help. I’ll be passing this around in my organization.

The perfect should not be the enemy of the good!

## Localizing vaccine information into ten languages

I was informed that technologists didn’t understand the fascinating and rich culture of the state of California, including that _English is not the only language spoken there_. そうですか。

I will admit to being absolutely wrong on an early decision. I have substantial professional experience in software localization. It had never, not once in my career, been an easy project.

Our team wanted localization almost immediately after launching. I said we had a choice between spending time getting good data in week two or spending time doing localization. Given that localization of fragmentary and dubious data would serve no one’s interest and that English-only access to better data would serve everyone’s interest, including the interests of people less comfortable with English, I put my foot down. I understood the moral, pragmatic, and political concerns, but we were making hard choices under scarcity. We could not afford multiple team members tied up in that project for multiple weeks (my best estimate), not yet, not when there were so many _other_ things to do.

I told the team that we would revisit localization in two weeks and not work on it until then. A team of volunteers, led by [Philip James](https://twitter.com/phildini), ignored me and had a proof of concept ready _overnight_. (Localization technology has gotten surprisingly less awful in the decades I have been in the industry, as the tech industry has become less US-centric and more routinely began to consider the needs of its global users early in development cycles. A specific example of this is that all commonly used programming frameworks have a way to decouple words presented to users from computer code, so that you can have words written or translated by people who are not capable of editing computer code.)

With the engineering completed there was clearly no reason to not have the site translated and that translation checked for accuracy, since that could now be done without slowing work on data collection. We shipped Spanish and simplified Chinese support on Day 18 and would go on to support the top ten languages spoken in California.

## Beginning to work with California and its counties

To various actors’ credit, after glowing press and some hard work in the trenches, we started getting more cooperation from various parts of the government.

At the beginning, this was mostly informal and ad hoc.

_The institution that is the government_ didn’t trust _our organization._ The government has _rules_ for that sort of thing, and according to the rules we were a nonentity, very literally so in the early days – we hadn’t incorporated anything! _People working in the government_ might have known some _people working for VaccinateCA_. They were willing to have some informal off-the-record conversations. And of course the government is willing to receive emails from members of the general public. Sometimes the general public sends in a useful email. Sometimes government employees forward emails to one another. Sometimes emails inspire action.

Very soon after that, we got a [Bat-Phone](https://en.wikipedia.org/wiki/Bat_phone) to the State of California. It was explained, deadpan, that the State of California had absolutely no obligation to pick up the Bat-Phone, no obligation to have a state employee immediately address any issue spoken into the Bat-Phone, no intention of telling us what state employees spent their day doing before or after hypothetically answering the Bat-Phone, and that the Bat-Phone would stop working if we were indiscreet about the existence of the Bat-Phone. This is the social contract for Bat-Phones everywhere.

The Office of the Governor had a [Covid volunteering program](https://www.californiavolunteers.ca.gov/get-involved/covid-19/). Californian do-gooders were cooped up at home and aching to help with pandemic response. It is extremely difficult to have shovel-ready projects to take volunteers who have wildly varying professional specialties, skill levels, physical locations, and abilities to leave the house. (A shovel-ready project is capable of immediately productively absorbing labor given the decision to do so, versus, e.g., a project that needs a few more months of planning and approvals to start work.) The Office of the Governor was thrilled to send volunteers to a project which could onboard almost anyone and _immediately_ actually start getting value for Californians from their work. The most important thing was shots in arms, but I am happy many of us felt like we had renewed _agency_.

That is what informal cooperation with California and its counties looked like, before we had more formal cooperation. We’ll return to that later.

Meanwhile, in Washington:

## America deputizes pharmacy chains to deliver half our doses

The feds made a decision with a host of consequences, some positive and some negative: They bet big on pharmacy chains for national distribution. Pharmacies had great geographic distribution, an in-place workforce who were legally empowered to administer the vaccine, and competent logistics operations.

This was called the [Federal Retail Pharmacy Program](https://www.cdc.gov/vaccines/covid-19/retail-pharmacy-program/index.html) (FRPP) and it [debuted](https://www.whitehouse.gov/briefing-room/statements-releases/2021/02/02/fact-sheet-president-biden-announces-increased-vaccine-supply-initial-launch-of-the-federal-retail-pharmacy-program-and-expansion-of-fema-reimbursement-to-states/) on 2nd February.

The FRPP was allocated approximately half of all doses, though the percentage varied week to week. It was the formalization of preexisting plans to use pharmacies as a primary vaccination channel. I have no desire to referee claims made by competing administrations, but I know when Inauguration Day is (a week into our existence), and I know what we [spent it](https://twitter.com/patio11/status/1351940599469928449) doing: calling pharmacies almost exclusively.

Why did we end up calling mostly pharmacies before the FRPP? They seemed to be much more likely than other medical providers to have the vaccine available. They were also much more discoverable; we collected hundreds of locations on Day 0 via scraping online lists versus having to more laboriously find every individual doctor’s office. They are also structurally more efficient to call; pharmacists are quickly findable at every pharmacy but the individual responsible for vaccine stock levels in a large hospital is very opaque from outside of it.

Naive approaches to finding the vaccine (‘Ask your doctor.’) were overwhelmingly likely to fail. We knew because we had tried them and taken notes. Doctors had _no earthly clue_ about vaccination policy and were, in the majority of cases, not planned to ever be allocated a dose of the vaccine. There was no institutional route from the federal government to them.

Meanwhile, pharmacists had 100 percent reliable knowledge on whether they had a vial and who they could administer the vaccine to.

This knowledge did not always mirror official government policy. For one thing, the government had many policies simultaneously, which often failed to agree with one another. Some people who read this assume I mean that different levels of the government disagreed. That happened _pervasively_ but, reader, that is _not the only thing I mean_. Pharmacists frequently learned of policy changes days or weeks after the government believed it had made them. Some pharmacists felt strongly that if folks at the county wanted to make medical decisions then they were welcome to go to medical school.

When we discovered instances of this, we optimized for accelerating shots in arms. This generally took the form of reporting ground truth versus reporting official policy. We considered deviations from policy an important issue to address only if they blocked shots from going into arms, such as if a pharmacist had missed the memo of not inquiring about immigration status, perhaps because they had relied on a state webpage whose author had missed the same memo.

We quickly began learning how pharmacies operate. This research was conducted mostly by calling their pharmacists to ask about the Covid vaccine, but we also took obvious steps like ‘walk down to the local pharmacy and ask nicely’, ‘google it’, ‘read a book about pharmacy management’, etc. A pharmacist could clearly develop a pretty high-fidelity model of how tech companies work if they wanted to. It takes effort, but it doesn’t take effort like med school takes effort.

An interesting operational wrinkle we discovered on Day 4 was that Safeway, a grocery chain, has a wildly competent logistical operation in their pharmacy department, to a degree that remained notably above peers for the duration. When we discovered that a streak of Safeways we called had received the vaccine, we guessed that plausibly _the Safeway logistical network_ had received the vaccine and was distributing it to stores. We immediately prioritized calling all the Safeways. (It took us another several hours to learn that Safeway is but one chain owned by a [corporate parent](https://www.albertsonscompanies.com/home/default.aspx). We correctly guessed many of their corporate siblings were hooked into the same logistical network. We immediately expanded to calling them, with generally similar results.)

We made extensive use of this tight feedback loop between callers, operations managers, and software engineers for most of our run, as we were heavily constrained by our call capacity.

A less fun operational wrinkle of using pharmacies to enact healthcare policy: The pharmacies were not necessarily thrilled to be doing it. The reimbursement the pharmacies got for administering the vaccine (approximately [$40 a shot](https://www.cms.gov/medicare/covid-19/medicare-covid-19-vaccine-shot-payment)) is not a lot of money to a pharmacy. They did not optimize their operations to capture it. (A maximally charitable view of this is: ‘Look, we’re in charge of almost all routine drug delivery in the United States and, in aggregate, that is staggeringly more important than one drug for one disease. _Of course_ we shouldn’t drop what we’re doing to optimize for it. Do you have _any idea_ how important the day-to-day work of pharmacies is and how many lives hang in the balance?’) Particularly early in the vaccination effort, the amount of pharmacist time that was spent fielding calls from the general public was substantial. The Covid vaccine was a distraction from the business of running a well-managed pharmacy and _was institutionally treated as such_.

So the chains made some choices. One was to lie to patients about vaccine availability.

That sounds like a shocking allegation, and it is so gobsmacking that we had to train our callers about it. ‘When you call XYZ Pharmacy, you will get a chain-wide recording that says that the pharmacist has no additional information about the Covid vaccine and that you should visit their website instead. Their website has no useful information. The recording is lying. Ignore it and press 4 to speak to the pharmacist, then continue to ask your scripted questions as normal.’

Useful information here might include: ‘I have the vaccine and can administer it immediately. Would you like to make an appointment?’; ‘I have a wait list here for end-of-day shots. Would you like to get on it?’; and ‘I do not have the vaccine, but this is a small town and I am socially acquainted with the folks at city hall who _do_ have the vaccine. Would you like their number?’

We always, always wanted their number.

A pharmacy telling you, via recorded message, that the pharmacist had no information about the Covid vaccine might have been unable to integrate their automated phone system and their inventory system. Or maybe they wanted to maximize the return on expensive staff time. Or maybe they wanted to protect pharmacists’ attention and devote it to direct patient care. Regardless, the result is the same: Pharmacies failed to tell the truth (and said some things that were the opposite of the truth) about the availability of the vaccine to patients, pervasively.

The pharmacist was frequently the _only person alive_ who knew whether their pharmacy had the vaccine, and _it would have stayed that way_, had we not ignored the lie and asked the pharmacist anyway. Individual pharmacists would often happily tell the truth about the healthcare they offered and we would publish the truth.

An important nonobvious detail about the FRPP: If you were a pharmacist administering an FRPP dose, the people you could administer it to were determined by your state and county, not by the feds. Remember, the US had _delegated_ the specifics of prioritization. This allowed states and counties to control the administration of individual FRPP doses that they could not find on a map or did not know existed. This sounds a bit counterintuitive but is the nature of all regulation ever. The regulator establishes rules but does not personally see every work site, every customer, and every transaction every day.

## A quick aside about end-of-day shots

Let me quickly explain what an end-of-day shot was: By manufacturers’ instructions, the vaccines were viable for 12 hours after being taken out of storage. They could not be recooled after the seal was punctured; once you had decided to dose a patient from a vial, all of the doses in the vial (five or ten, depending on which vial you were issued) were going into an arm or the trash can that same day.

Israel had a [very sensible policy](https://www.cnbc.com/2021/01/07/israels-covid-vaccine-rollout-is-the-fastest-in-the-world.html): At the end of the day, _give literally anyone_ leftover shots. Run into the street and ask passersby if they’d like the vaccine if you have to. The best-managed pharmacy chains in the United States, and some savvy individual pharmacists, adopted systems like a paper list next to the phone where they would take down numbers and at end-of-day call the ones at the top of the queue and say, ‘Can you get here in the next 15 minutes?’

But, discouragingly, many doses went into the trash can. Administering the end-of-day list took work at a busy point of the day when everyone wanted to just go home. Not to keep banging this drum but it is an important one: We fired and stripped licenses from professionals who gave away end-of-day shots to disfavored potential patients, including in several well-publicized cases. In some cases, healthcare providers adopted policies to prohibit end-of-day shots because their lawyers told them that if they violated the tier list then the state would revoke the pharmacy’s permission to do business _at all_. I wonder where they got that cockamamie notion.

I do not believe that end-of-day waste of the vaccine was a substantial contributor to the supply issues. I know _precisely_ how many lives were saved by administering scarce, lifesaving healthcare to trash cans. Any conceivable variant of the Israeli method works better. We should have never fired anyone for injecting an end-of-day shot, even if we thought their method for choosing the recipient was _maximally_ morally odious. That shot got many innocent people one shot closer to _their_ shots. Keep the line moving.

## Pharmacy website awfulness was a rationing mechanism

Another somewhat desultory consequence of using the pharmacies as distribution partners was that this exposed many patients to their systems for scheduling appointments. These systems were some of the most important software written in 2021 and they were _broken by design_.

Why? Because there was a true systemic supply/demand mismatch early in the vaccination effort. If, e.g., BigCo had allowed one to easily sign up for an appointment, BigCo would quickly become known to vaccine seekers and the media as the place to get an appointment. BigCo would tell the overwhelming majority of appointment seekers that there was no appointment available. BigCo would then take a hit in the press and plausibly get called into Congress to answer for why they had no appointments despite being part of the FRPP. BigCo’s competitors would _not have this problem_ because their websites were falling over during crushing demand.

A website that falls over doesn’t disappoint millions of people daily, not for long anyway. Those people will go to BigCo, which they saw on Facebook or the nightly news as having a website that actually worked, and _further increase the relative imbalance_ of seekers versus doses for BigCo.

So instead BigCo sometimes intentionally and sometimes through considered inaction engages in _rationing through mediocrity_. BigCo has good vaccination scheduling systems in 2022, and BigCo could have shipped them in early 2021, but BigCo chose not to. They slow-rolled their development and kept decision-making several layers from the top of the company, deep in their technical orgs, where no one who mattered would ever be called in front of Congress.

Then, when their systems went down, when sessions reset randomly in the middle of the search flow, when servers were routinely overloaded, etc., some discouraged vaccine seekers _did not keep trying_. (Many, of course, hit refresh quite a bit every day.) Media articles of breakages in vaccination appointment systems were legion but _mostly did not single individual chains out, despite them actually having the vials_.

Was this strategy successful? Well, do you remember the time their CEOs were called before Congress to account for their performance during the pandemic? \* _crickets chirp_ \*

We as a society accepted _so much mediocrity_ during the pandemic, and we do to this day.

Speaking of BigCo: the largest pharmacy chains in the United States spend an absolutely gobsmacking amount of money so that you remember their name and choose to fill your prescriptions at them. These chains suffered the worst imbalance in seekers versus doses, directly as a result of being good at marketing their standing ability to provide healthcare.

Mid-tier chains, the sort that do not _immediately_ spring to mind when you think _pharmacy_, frequently had imbalances in seekers versus doses in the other direction: They were granted a lot of doses but had little public mindshare as the _first_ place you’d call.

Many, many people gave up after the first no, assuming someone would tell them when the answer changed, not realizing that there could simultaneously be a yes across the street. This is an extremely understandable reaction from a seeker of healthcare. The _county health department_ could understand there to be no untapped vaccine supply when there was a yes at the pharmacy across the street _from their own office_.

Vaccine seeker discouragement likely disproportionately impacted elderly patients and those in vulnerable populations. If you grew up believing that a doctor would either a) obviously immediately give you the right answer about your healthcare, or b) ignore you again in 2021 like they had ignored you your entire life, you had a rough go during the pandemic. If you were a member of the professional-managerial class used to navigating complex systems and skilled at sifting through information, it was _much_ easier.

When we realized that the mid-tier chains were frequently underutilized, we started telling everyone we could reach about it, including in press interviews and similar.

You, an individual with no tool other than a telephone, could greatly increase your ability to access the vaccine simply by _adopting a better strategy for finding it_. Many people did this! There was a thriving community on Facebook and other places where ‘vaccine seeker’ groups arranged care for themselves, their loved ones, and members of their communities. They swapped tips about finding the vaccine and frequently set up appointments on behalf of patients who couldn’t manage it themselves. We met a vaccine seeker who had personally coordinated appointments for more than 70 people. She, a lawyer, got appointments for most friends and family (using us as a data source) and then volunteered to call pharmacies to help people she _didn’t_ know. There are [credible media reports](https://calmatters.org/health/coronavirus/2021/04/myturn-vaccine-appointments-problems/) of individuals who made several hundred appointments.

These individuals succeeded in part because they _had a strategy_. They also succeeded because they were overwhelmingly using skills and other advantages inherent to being members of the professional-managerial class. To our class, finding the vaccine was just another day at the office.

Back to mid-tier pharmacies. Once I had data suggesting they were gold mines of underutilized vaccines, I assumed that this was likely true across the country, and I immediately called my father. Mom and Dad live in Illinois and were, by state policy, immediately eligible for doses based on their age. Dad is retired, worked in real estate for most of his career (including finding locations for new pharmacies), and had not found the vaccine despite hours of trying. I told him to call the third-largest chain in Chicago, not the first or second but the third. He found himself and Mom appointments _within minutes_ of receiving that advice.

This is a more subtle variation of the pathology we’ve already mentioned: Your access to healthcare was determined not by the state’s tiering logic but, frequently, by how socially close you were to someone who was good at working the healthcare system. And one of the defining features of classes is that their members _cluster_. If you wanted the vaccine, life was much easier if you clustered in the class that includes everyone who writes think pieces about healthcare equity, everyone who writes vaccination policy, and everyone who navigates the healthcare system because it is their job.

Plausibly some readers will wonder if I had ethical conundrums about accelerating my parents’ access to the vaccine using superior knowledge of the healthcare system. I ask those readers whether they would have ethical conundrums about leaving doses unused at the third-largest pharmacy chain in Chicago.

## Messaging to the public about acting virtuously was confused

There was never any virtue in delaying shots.

The messaging, at all levels of civil society, from the jump, should have been ‘Take the first shot offered to you. Keep the line moving.’ People, including nonspecialists, including the general public, can follow rules if you keep them very simple and repeat them constantly. Don’t believe it? Do you work in aviation safety, by any chance? No? Okay, complete this sentence: ‘Put on your own oxygen mask before...’ Wow, you had an important fact about what to do in a midair emergency memorized.

It was extremely frustrating to read about hospitals that could not give away the shots _to their own staff_ because their staff thought they could virtuously decline the shot and have it given to someone more vulnerable instead. That is a reasonable moral intuition, like prioritizing your child over yourself in an aerial emergency seems like a reasonable moral intuition. That is why we tell people to _ignore_ that intuition and instead do the thing which will save lives.

Declining that shot extremely frequently resulted in it being either unused in the freezer or _thrown away_. It did not result in America’s vaccine czar giving it to a sympathetic patient with a high risk of death if they caught Covid. America had no vaccine czar.

Why not reallocate doses refused by virtuous healthcare workers? One compelling reason: A doctor who did it would swiftly lose their license, to protect the integrity of the state’s tiering system.

You might think I am confabulating about this. Perhaps I misunderstood a statement made by a tired junior staffer. But clearly that was not carefully considered and promulgated official policy, right?

Governor Newsom, at a [news conference](https://www.rev.com/blog/transcripts/california-gov-gavin-newsom-covid-19-press-conference-transcript-december-28) on 28th December 2020:

> I just want to make this crystal clear. If you skip the line or you intend to skip the line, you will be sanctioned, you will lose your license. You will not only lose your license. We will be very aggressive in terms of highlighting the reputational impacts as well. We are going to be aggressive here.

To add the tiniest possible bit of commentary to that crystal clear statement, in context, ‘skip the line’ meant ‘administer shots to line skippers’, because anyone capable of legally administering a shot was first in line.

This policy is not only counterproductive in its own terms. It exerted a chilling effect on _things the state wanted to encourage_, like doctors using their medical judgment, avoiding waste, and promoting equity. Doctors heard from the governor’s own lips, from their medical association, and from their employers’ counsel that policy was being made and enforced by a system that bragged about its intention _to aggressively strip licenses from doctors in a pandemic_ if they provided healthcare out of order.

Would you gamble your entire career on a system this perverse backing your decisions? Would you risk your community losing a critically needed doctor during a pandemic? Would you trust the system to take into account your local knowledge of conditions and considered evaluation of the patient in front of you? Many were unwilling to take that gamble!

Some were willing but instructed by their employers not to. Their lawyers had patiently explained that if staff exercised moral courage it would not merely cost staff their licenses but could cost the employers _their permission to stay in business in California_. And if you work in a pharmacy _you work in a panopticon_. Smile, you’re on camera, and _everything is audited_.

This is not an academic concern. We heard many variants of: ‘Yes, I have doses, and yes, nobody is coming in to get them, but no, I cannot yet give them to patients with preexisting conditions [of the sort which would mean a Covid infection would likely mean severe injury or death]. That is phase 1C. The county says we are still on phase 1B. I absolutely must not move to 1C until I get word from corporate. I want to help, but I need my job.’

If you worked in a regulated industry, or you were a lawyer working in a regulated industry who had spent their entire career minimizing risks: Would you trust that the system that embraced this policy then quietly put out the word, ‘Ah hah, JK JK, clearly we did not mean that’, was _now making a truthful and durable commitment about its future actions_?

There exists a narrative that engineers love technological solutionism too much, believing complex societal problems could be solved if we just had software that worked. This critique is accurate sometimes. But it did not describe the dynamics _this_ time.

Against my prior expectations, governments wanted magical IT systems that would paper over their bureaucratic divisions. We technologists were willing to ship low-tech approaches that actually worked.

The core unique insight VaccinateCA had was that America has access to a reliable technology for getting information from the healthcare system. It is called a telephone.

You do not need to convince every healthcare provider to have every IT department simultaneously agree on a data format and transfer protocol to update a central system with daily inventory levels and then fan out information from that central source of truth to every possible user of it, including the general public. The government really _wanted_ to do that, and made multiple independent attempts, the results of which speak for themselves.

You only need to realize that there are approximately 6,000 pharmacies in California, their phone numbers are in the phone book (or at least more accessible than a locked filing cabinet stuck in a disused lavatory with a sign on the door saying ‘ [Beware of Leopard](https://www.goodreads.com/quotes/40705-but-the-plans-were-on-display-on-display-i-eventually) ’), and a call center employee can talk to approximately 100 pharmacists a day. Then you choose what freshness level you want for vaccine information.

Let me give you an oversimplified view of the freshness-versus-staffing tradeoff. If you want to call every pharmacy every day, that will take 60 agents. Simple division. Your data will be, at any moment, on average about a half-day old. If you are okay with results that are on average a day and a half old, you need to call all the pharmacies every three days; that only will take 20 agents. Call centers are actually _much_ more sophisticated in how they think about call queueing and frequency than this sketch, but napkin math is frequently good enough for a first pass at capacity planning. The call center will happily accommodate you adding more agents if you need them, at additional cost and requiring a slight delay to train them up.

These are, by industry standards, small call center contracts! Some call centers will decline to work with you if you only need 20 agents because your needs are just _too small to service economically_ given how they run their particular operations.

In our case, to kickstart our operations, build intuitions about relevant parts of the problem, and gain leverage throughout the project, we had a team of unpaid volunteers using their personal cell phones before (and then in addition to) a professional, physical call center. I considered our volunteers to be very similar to a distributed call center. Most of our team members whose hands were not physically on a phone were building tools for that call center or managing it.

For various institutional reasons, the federal-, state-, and county-level public health officials did not choose to use large teams of callers to collect data.

One reason was that, while governmental actors could collaborate with volunteer-based organizations, they could not use the work of volunteers directly, due to a raft of considerations. One mentioned to me was union-negotiated labor rules. There is no one employed by the government whose job is calling pharmacists to get this information, true, but if that person hypothetically existed they would be a union member, which means that a volunteer doing that job is nonunion labor competing with them. Unions are _extremely predictable_ in what they think of their employers using nonunion labor.

That constraint I understand, even though I doubt that anyone truly believes labor rules are more important than lives at the margin. (Economists would call this a revealed preference of the US.) What I understand less is why no government actor decided to implement our model with a contracted call center so that they could have a single source of truth about vaccine availability, public or otherwise, without needing to boil the ocean that is government IT systems.

We have a titanic gap in state capacity: The largest and most well-resourced organizations in the world did not conceive of, approve, and immediately execute an obvious and largely successful operational plan that nonspecialists were able to draw up on Discord _in a matter of hours_.

## The fateful first weeks of VaccinateCA

Back to our gang on Discord. We had thrown together a website, whose name we changed shortly to VaccinateCA because we couldn’t even remember it ourselves (covid19vaccineca.com just rolled off the tongue, didn’t it). We were making hundreds of calls a day to pharmacies.

Word got out very quickly, which is a very _passive_ way to say, ‘We ran the social media and PR playbook that a start-up would use for a launch’.

The first patients who we positively _know_ got vaccinated as a result of our effort, on Day 6, were booked an appointment by their adult child, who [found out about us](https://twitter.com/Mallrat9000/status/1349933326543454209) from tech-journalist-turned-VC [Kim-Mai Cutler on Day 1](https://twitter.com/kimmaicutler/status/1349860673564536833).

![](https://wip.gatspress.com/wp-content/uploads/2023/02/raj-discord-quote-and-father-photo.jpg)

From the VaccinateCA Discord, posted with Raj’s permission. Note that Raj is not @Mallrat9000.

Image

Image by Patrick McKenzie.

We had an internal culture of counting the passage of time from Day 0, the day (in California) we started working on the project. We made the first calls and published our first vaccine availability on Day 1. I instituted this little meme mostly to keep up the perception of urgency among everyone.

We repeated a mantra: Every day matters. Every dose matters.

Where other orgs would say, ‘Yeah I think we can have a meeting about that this coming Monday,’ I would say, ‘It is Day 4. On what day do you expect this to ship?’ and if told you would have your first meeting on Day 8, would ask, ‘Is there a reason that meeting could not be on Day 4 so that this could ship no later than Day 5?’

I started every meeting and status report to the team by reminding them what Day it was. Our internal stats dashboard had a counter of what Day it was. I had a whiteboard in my apartment showing what Day it was. I wrote that every morning as soon as I woke up, and updated the other two numbers right before I went to sleep. Those were: the number of locations we had published to Californians where they could currently get the vaccine, and the number we knew about elsewhere across the United States with the vaccine.

The latter was zero at this point, of course. I brushed my teeth, wrote my emails, ate my meals, did media interviews, called my family, negotiated with funders, and said my prayers with the zero where I could see it.

![](https://wip.gatspress.com/wp-content/uploads/2023/02/on-wall-dashboard-1024x768.jpg)

A photo of the non-computer version of VaccinateCA’s dashboard, taken on Day 39. It shows VaccinateCA’s then-current understanding of where to find the vaccine: 1,025 sites in California and 0 sites outside of California.

Image

Image by Patrick McKenzie.

We received overwhelmingly positive coverage in [_Vox_](https://www.vox.com/future-perfect/2021/1/15/22231241/california-coronavirus-vaccine-availability-moderna-pfizer), [ABC](https://abc7.com/covid-vaccine-registration-california-rollout-vaccinate-ca-pfizer/10069613/), [NBC](https://www.nbcnews.com/tech/tech-news/california-technologists-create-website-track-vaccinations-n1255381), [NPR](https://www.npr.org/2021/01/26/960855949/with-few-details-from-health-officials-volunteers-create-covid-19-vaccine-databa), [The Wall Street Journal](https://www.wsj.com/articles/covid-19-vaccine-confusion-leads-volunteers-to-create-online-guides-11612002601), local San Francisco and California outlets, etc. I cautioned the team that we were getting a credibility advance on our future accomplishments. There was an incredible _need_ for what we offered, as demonstrated by tens of thousands of people searching with us daily. We were a bunch of nobodies with a site that worked but had relatively little data on it. We had barely made a dent in the problem yet, but we were _an appealing story_.

That outpouring of positive PR was partially organic. Reporters wanted good news angles and were happy to highlight a group of concerned individuals who seemed to have something interesting and do-goodery in motion.

That outpouring of positive PR was also carefully coordinated. Three members of the team, including two board members, were PR professionals working in tech. We had a rotation of briefed spokespeople, carefully groomed to avoid seeming too much like tech workers. We had written talking points and briefing documents (which included recent work from the scheduled reporter, themes they frequently hit upon, and so on). We exercised tight message discipline.

For example, we were always asked in interviews why we could do the thing the state government wasn’t doing. I practiced my prepared answer in the mirror and can recite it by heart: It is just team humanity versus team virus. The vaccine being available is one of the greatest achievements in the history of science. The rollout has some hitches. We are thrilled to be able to do our small part in supporting the rest of civil society in quickly resolving those hitches.

We did this for two reasons. There was a sentiment among some coordinators early, before we had spoken to many government officials, that we might be officially asked to cease operations. I did not believe this was likely, but the team agreed that if ordered to we would stand down. The more compelling reason to court respectability in the eyes of the public health establishment was to engineer our invitation into the formal effort, because we thought that would maximize our ability to get shots in arms.

But first we needed something that could be invited.

## An OSS project turns into a nonprofit

VaccinateCA had started with the feel of an open-source software (OSS) project. We were ten part-time coordinators, all with day jobs, none with a scintilla of formal expertise on healthcare policy. Things quickly spiraled beyond that.

I had started chatting with the other organizers with the intention of giving them some quick advice and a tweet of support. I did a full Day 1 of work in Japan for my actual employer and then a full night for VaccinateCA. I took Day 2 off to focus on the project. On Day 3, over the weekend, I emailed my manager and CEO, told them we had accidentally incubated core public health infrastructure, and asked to be allowed to pursue it full-time for the foreseeable future. They graciously came to an arrangement with me.

I work for the internet at [Stripe](https://stripe.com/), a company that builds payments infrastructure. I have a job that is fairly illegible outside of tech circles, but it certainly does not suggest ‘would be a great CEO for a healthcare nonprofit’. For flavor, my scheduled work for the week was editing a blog post about load-testing infrastructure that ensures credit card transactions don’t fail during the holiday season peaks.

On Day 6, I drafted a memo about the future and started one-on-one conversations with most of the other coordinators. We were a team of peers who were all grabbing tasks as they came up. We had no structure, legal or otherwise. We had created something that was valuable, important, and _extremely fragile_.

We were inevitably going to have volunteers burn out and stop calling pharmacies, likely early in the coming workweek. We were taking on legal liability with no shields for ourselves and our families. We had no committed funding outside of our own pockets. We worried that we were building a time bomb adjacent to patient care, because we all knew the sort of work reliable systems take at scale and we were sure we could not sustain it on the current trajectory.

The point about value is a nuanced one: It was absolutely clear to me that one potential structure for VaccinateCA would have been as a for-profit entity. I didn’t think any of the organizers wanted that. But, as someone who has been in tech for his entire career, I knew that the team had created something that sophisticated investors would immediately assign at least $20 million in value to. I wanted to convince the team to _waive their legal rights to an equal share of that_, and I wanted them to _understand they were doing that_.

I told everyone that we could certainly write OSS but that we could not continue as an informal project, because that would compromise mission success. We needed an organization, with employees and funding, and some sort of management structure. I suggested, lacking any other great alternatives, that our partnership of equals nominate me as CEO.

There was unanimity about broad concerns.

Some coordinators had joined for a quick sprint but needed to get back to their jobs and families; others were ready to put life aside for the duration of the pandemic, if necessary. On Day 8, the team unanimously agreed to make me CEO and charged me to do what needed to be done.

I shot the team a video message, which was the first time any of them had seen my face, to accept the mandate from them. I thanked them profusely for incredible work in the first week.

The plan from the memo: Find us a few million dollars in funding. Offer full-time employment to anyone who needed it. Get a nonprofit entity established and quickly legally recognized. And then we would become the shadow vaccination information infrastructure provider for the United States of America.

Then I closed Discord, kissed my wife and children goodbye, and booked a one-way ticket from Japan to San Francisco. I told my wife I would be back in two weeks if we failed and much, much later if we succeeded.

By the time I got to the US, we had a Delaware C corporation up and running: Call the Shots, Inc. Jesse Vincent, one of the other organizers, came on as chief operating officer. Zoelle Egner, another organizer, came on as our chief communications officer and third board member.

## The daily grind

So what did a typical day early in the life of VaccinateCA look like? It was largely organized around the morning call-a-thon.

We quickly learned the rhythms of pharmacy operations in California. Most are first ready to take calls at 9:30am, but some before that; we eventually distinguished between the two.

VaccinateCA had a public-facing website with a map on it, but the main technical product in the early days was jury-rigged infrastructure to facilitate the callers extracting as much useful information from as many pharmacists as possible in however many calls they’d choose to do. Technologists might say we were low code; we had Discord as our main organizing technology and Airtable as our database and primary software platform. The website started as a static site with all the vaccine locations for the state of California in a (single) frozen JSON document. It was updated every few minutes with the latest data.

That allowed vaccine seekers to access search results like the below, which concisely conveyed vaccine availability, presently enforced eligibility criteria, location information, and an indication of how fresh (and therefore reliable) our understanding was. This design went through many iterations to make it more useful for users.

![](https://wip.gatspress.com/wp-content/uploads/2023/02/early-search-result-mockup-1024x308.png)

An early design of a search result for VaccinateCA, showing vaccines available for patients 75 and older at a drive-through clinic in San Francisco. The patient is told to make an appointment through their website. The address of the location is provided.

Image

Image by VaccinateCA.

VaccinateCA never had load problems, at least not on our website. Technologists will understand that this is not particularly praiseworthy. Simple websites are easy to keep running these days, assuming competence. We picked one of many plausible technical options for a scrappy, competent team.

Since in those first weeks we were doing only volunteer-delivered calls, we had a sharply limited (and unknown to us every morning!) amount of call capacity, and had to prioritize ruthlessly. This meant, basically, trying to optimize calls for getting new information. We wanted to avoid futile calls (which would never result in ‘Yes, I have the vaccine; here’s how to get it’) and we also wanted to avoid calls where we learned little at the margin useful to patients (for example, by repeatedly spending all calls in one geographic area).

One method of avoiding futile calls became project oral lore: Sometimes we would call a location that would never have the vaccines. Internally, this was coded as sir\_this\_is\_an\_arbys, after an internet meme. We would not call back locations we’d learned to be Arby’s. You would be surprised how many organizations in California have a name that accurately suggests that they are a hospital but somehow omits the tiny detail that their only patients are horses.

Horse hospitals were a nuanced case of being an Arby’s. Prior to being coded as one, we’d ask them if they had or expected to receive the Covid vaccine. Some horse hospitals might have received allocations. Because people who send a box of Covid vaccine to a horse hospital did not always make optimal decisions, this could have resulted in the hospitals having extra doses where no patient would think to look for them.

(I regret that after Dunkin’ Donuts’s PR dollars started funding vaccine logistics, which was absolutely [a thing that happened](https://www.wpri.com/health/coronavirus/we-are-heading-in-the-right-direction-dunkin-donuts-center-celebrates-100k-doses-administered/), I didn’t have time to convince _literal_ Arby’s to do a creative branding campaign by opening a pop-up clinic. It would have gone viral.)

We had one tactic that copied from a progressive advocacy organization (which an early volunteer had worked at, and, notably, from which she sourced many other volunteers): call captains. Each day we assigned a call captain who was in charge of both rallying the troops (convincing volunteers to stay on just a few more minutes to make just a few more calls every day saved lives at the margin) and keeping tabs on the incoming results. We posted call results in real time into Discord.

While vaccine supply was extremely scarce, we learned that we could motivate callers a lot more successfully when we found a win early in the day. There were days when finding the first new dose of the vaccine in California took us almost an hour. You could cut the despair with a knife. On days where we booked a win early, or where our gongbot was repeatedly spamming the channel with the vaccine emoji, we all felt better and our volunteers called more.

We had an extremely rapid feedback loop between engineers, operations staff, and callers, and indeed many people were wearing all of the hats. If you noticed a bug while on a call, mentioning it in Discord would have an engineer start working on it immediately. If you noticed a pattern in a few calls and told the call captain, they could have our queue reconfigured to take advantage of your finding within minutes. This is _not_ the level of autonomy and agility call centers typically expect to deliver.

An aside about the utility of volunteers: That autonomy and agility made volunteers crucial for us even when, later, we were able to afford professional call centers. I viewed volunteers like scouts for an army, nimbly perceiving reality and reacting to it so that we could mass some divisions and go Waterloo on the virus. I view our tiny project like that too, as part of the much larger response effort of all of society. Watch out, logistical issues; if you’re spotted by that little unassuming squad they will radio your position to California, Google, and the United States federal government, which control metaphorical heavy artillery. And also, come to think of it, literal heavy artillery. But I am getting ahead of myself.

VaccinateCA operated on trust in the early days. We were getting Californians access to the vaccine, a goal that some people oppose (including violently!), and we were worried about both accuracy and resistance to internal sabotage. So we recruited most volunteers early from our own networks, and as a result they skewed heavily in the beginning days to tech professionals.

Most of the vaccines we found early were from engineers talking on the phone to pharmacists and then entering the data manually into a spreadsheet. Within a minute, new entries were available on our website, directing vulnerable Californians to available doses.

This was described by the media early on as crowdsourcing and I worked _extremely hard_ to shake that branding. I emphasized to government partners that we were not merely aggregating untrusted opinions about vaccine availability. We were not Yelp for vaccines. We did not trade in rumors. We were _professionals_ who had built a reliable system to _talk to healthcare professionals_ and then _accurately report what they had told us_ about healthcare that they would offer _with their own hands_.

This was our mantra on accuracy, and we repeated it to healthcare providers, the government, funders, and publishers. We _felt_ like imposters, but when we needed it, I used every trick I knew to present as the CEO of an officially recognized healthcare nonprofit and elide the fact that my sole prior leadership experience had been running a _World of Warcraft_ guild.

After the workday was over and pharmacies stopped answering their phones, the workday began again _immediately_, as much of our engineering team turned off their day job computers and logged on to Discord to digest what we had learned. We worked into the night, and not infrequently through it, to be ready for 9:30am the next morning.

It was often a brutal crunch. I told the team to take care of themselves and keep an eye on one another. The mission wouldn’t be served by anyone ending up in the hospital. But subject to that constraint, we worked like men and women possessed, because people were dying.

We created the best data source available in the state of California within approximately five days. That sounded like a bold claim when it was made to me, but if you can’t trust the government, who can you trust?

Then we started making it better.

## Optimizing call capacity

After the heady first days of enthusiasm, the willingness of engineers we knew from work and Twitter to continue making dozens of calls to pharmacies to perhaps find one with doses of the vaccine began to wane. We had, thankfully, seen that coming. Political campaigns can count on enthusiasm and shared purpose to get large volunteer call centers to work for them for a few weeks every election cycle. Basically every other initiative under the sun that needs to make calls at scale for extended periods of time pays dedicated professional callers to do what is (frequently) a thankless job.

In the earliest days of VaccinateCA, we had thought that our project might inspire peer projects in other states. We hoped our open-source software and methods might accelerate their ability to fix local problems. We opened a channel on our Discord (#other-states) to host organizers from across America and the world, and collaborated where we could without spending too much time.

We saw peer projects sprout up in many states, with varying levels of effort and success. Many credited us as an inspiration. One peer project was ILVaccine.org, a project of [Eli Coustan](https://www.chicagotribune.com/coronavirus/vaccine/ct-life-eli-coustan-vaccination-help-tt-0401-20210401-42cyywdfw5gyrbopfx73lolvj4-story.html). We were working with him for a while before I learned he was in middle school. When I later blanked on his name and asked someone about the public health infrastructure coordinator who was a middle school student I was _asked to be more specific_.

I quickly became convinced that unofficial projects would be forced to do one of two things. They would either focus on automatically aggregating information from official websites, in which case they would only ever be as accurate as those existing websites, which had (as of January) extremely limited information and were routinely inaccurate with what they had. Or they would hire a call center, which would likely be a six-figure proposition. It did not seem viable to me for initiatives to make hundreds of calls per day, every day, for the duration, using only volunteers. Navigating extremely limited resources and volunteer burnout features prominently in the experience of peer projects, such as [VaccinateNJ](https://leonwu.tech/posts/vaccinate_nj).

Anyhow, finding a call center is not particularly difficult. They’re in the phone book. Finding a call center that would immediately greenlight a project with a nascent team with no budget and limited expertise as a client was slightly trickier.

I started working my phone to every tech CEO who I thought might immediately donate the use of their call centers. In addition to being free, an important consideration because we had almost no money, this would allow us to start calling quickly rather than waste time negotiating contracts and setting up infrastructure. We could piggyback on the infrastructure already used daily by Capitalism, Inc.

I had a commitment on a handshake within hours.

We obtained a few weeks of free use of a team at a call center (which happened to be in Guadalajara, Mexico) on Day 8. They broke land speed records for a new calling program (which requires script writing, mutual agreement on procedures, a meeting of the minds on data formats and transfer methods, and holding trainings for callers). We started calls there on Day 12.

Call centers were dealing with many, many problems of their own, such as the difficulties with having people report to a densely populated office and speak ceaselessly during a pandemic caused by a virus spread through the air. Even so, several layers of managers and workers dropped what they were doing to help out people throughout California. Sure, they got paid as usual, but nobody told them they had to work nights and the weekend getting this spun up. They told us they did that out of humanitarian impulse. _Dios se lo pague._

This is as good a point as any to say that Californians and Americans owe an immense debt to our friends around the globe. In addition to the team in Mexico, we had volunteers worldwide, including our two coordinators in Asia. One of many memorable moments was someone reading about us on Twitter while getting the vaccine in Israel, waiting the prescribed 20 minutes to check for side effects, then immediately returning home to call pharmacies in California on the behalf of Californians. I believe the term is _mensch_.

Working with the call center forced us to up our game a bit with respect to scripts and data collection. We had provided callers with scripts since Day 1, but relied on them using their professional backgrounds (and, unfortunately but accurately, observable socioeconomic position) to finesse conversations with pharmacists. Call center workers and software engineers do not pull from the same distributions in terms of skills or socioeconomic background. They are not equivalently socialized in how to deal with professionals like pharmacists.

There is a lot of art in the science of call center management and scriptwriting. Happily, many team members had up-close-and-personal experience with it. We were aware of how this works in, among other places, sophisticated tech company call centers. They, for example, employ an operations manager whose job is to manage the managers of the call center. We swiftly hired [Kim Dietz Vandiver](https://www.linkedin.com/in/kim-dietz-vandiver-412bb55/), a force of nature who had wandered onto Discord to volunteer and just so happened to have previously been VP of operations at a healthcare–facing technology company.

We fleshed out decision trees for the calls and scripted language for the callers. Hit 4 to speak to the pharmacist. If someone answers who is not the pharmacist, ask to speak to the pharmacist on duty; if they are not available, note this fact in Miscellaneous Notes then proceed with the below questions. First question: Could a 65-year-old patient get a Covid vaccine at your pharmacy? If yes, record as Yes and proceed to questions about getting an appointment. If no, proceed to follow-up questions about known timelines and known availability.

You may be asked for information and you should answer honestly. Are you calling on behalf of yourself or a family member? No, I am seeking general information. Who are you? I’m Insert Name Here calling on behalf of VaccinateCA, a nonprofit helping Californians find the Covid vaccine. What are you going to do with that information? We will publish it to our website, vaccinateCA.com, for free so that vaccine seekers can find who has the vaccine and how to get it. I would prefer you stop calling me. Absolutely, I will make a note of that fact and we will never call you again. Have a nice day. (Virtually no healthcare workers asked us to not call back. Many more asked us to call again.)

In the second week, we were struggling to get enough volunteer time to make low hundreds of calls a day. Bringing five agents at the call center online immediately got us to over 500 calls a day. We had a clear line of sight to an ongoing census of availability at all pharmacies in California. Again, I hate to keep beating this drum, but there are only a few thousand pharmacies, calling them takes perhaps five minutes on average, and after that this is _strictly a math problem_.

But 500 calls is still less than 6,000 pharmacies, and we wanted our data to be fresh. I also told the team that they should consider California’s pharmacies the proof of concept for calling healthcare providers across the US, which I ballparked at 50,000 locations. We’d clearly need to scale our capacity by more than an order of magnitude.

The team juggled this knowledge against the knowledge that our donated call center would un-donate itself in a few weeks.

That’s life in a start-up: trying to create enough impact _very quickly_ to convince people to give you more resources, while understanding that the default case is running out of resources, and, by the way, everything is broken all the time.

Speaking of impact.

## Inspecting the operation of a system changes it in real time

Heisenberg’s uncertainty principle states that attempting to measure physical reality changes it. Engineers have similar dicta about inspecting the insides of complex systems.

You cannot make a large number of calls into the healthcare system without changing it. Happily, you can change it _for the_ _better_.

An example: Our scripts instructed callers to take down notes from pharmacists as to how to get an appointment for doses they had, when they had them. A Rite Aid pharmacy in San Bernardino asked our caller to sign up for an appointment at the county health department’s website. Our caller, who had been calling into San Bernardino frequently and had seen that website frequently, remarked that he had seen no Rite Aid listed as a possible vaccination location.

The pharmacist then swore into the telephone, hung up, and immediately called the county health department.

I want you to visualize the operations of county health offices during the middle of the pandemic. A stressed staff are busy coordinating a logistical challenge larger than any they’ve faced in their careers. Their phones are ringing off the hook. The consultancy that won the bid finally delivered the freaking appointment website, thank god. It is crappy and barely works but at least it is finally here. You just have to download all of the email attachments from the pharmacy chain corporate offices, maybe fix a few in Excel because those jokers can’t read clear instructions, then upload them into the administrative side of the portal, and _finally_ people can register for appointments to get the doses sitting in pharmacy freezers.

Rite Aid’s data never made it into the system. Maybe Rite Aid forgot to send it and nobody followed up. Maybe it got eaten by the county’s spam filter. Maybe a public health worker with a million things to do did 999,999.

There were 13 Rite-Aids in San Bernardino county. None of them, despite being in possession of the most desirable object in the world, had received a single appointment. No pharmacist, with years of training in healthcare, noticed this before we told them.

Why would they? Every pharmacy has _lots_ of tiny glass vials and bottles of pills and satchels of powder. Patients were coming in and getting healthcare. It was _no one’s job_ to check that any _particular_ vials got distributed quickly. Pharmacists are not pharmaceutical sales representatives; they _do not generate demand_. Pharmacists service appointments and prescriptions, deliver healthcare, and go on to the next patient. If you walked up to the counter or called in and asked about Covid appointments, they’d tell you to book one with the county and move on to the next customer. Just another day at the pharmacy.

You might object and say that it _must_ have been _someone’s_ job to actually get those doses injected. Someone who worked... at the White House? Okay, no, but at the CDC? Okay, no, but at the California Office of the Governor? Okay, no, but at the county health department? Okay, no, county health departments do not track individual SKU inventory levels at individual pharmacies, that’s actually not a thing. OK, then, Rite Aid – some logistics manager at Rite Aid should have opened a spreadsheet, seen an SKU like #DJFKJDF3285325 with 50 doses available out of 50 shipped at a location in San Bernardino, and immediately said, ‘Oh, #$\*#(%. That drug being _in supply_ is equivalent to a life-threatening medical emergency. I will now get out my emergency procedures binder.’ Nope, that is also not a reasonable expectation.

Each of these organizations wants someone else to be responsible for catching errors like this, and they want them to be effective at doing so. They want, and the nation wants, an organization to be _accountable_ for delivering the vaccine.

VaccinateCA considered this bug, and anything else that kept vaccines in freezers while patients were still waiting, to be _our_ problem.

This problem was fixed because a caller from VaccinateCA thought to say, ‘Wait, I notice that I am confused’. It was fixed within about half an hour of being noticed. We estimate more than 500 doses were quickly taken out of freezers, thawed, and injected into waiting arms. Those arms were often attached to people who had been refreshing the county website every few minutes hoping new appointments would finally open up.

This was early and dramatic evidence to me that California was benefiting from having an organization that felt itself accountable for delivering the vaccine.

We kept looking for logistical bugs like this and fixing them for our entire run. I hoped we’d find examples this dramatic at scale; we didn’t. Instead, our largest impact was likely through leveraging the largest organizations in the world.

## Working with the world’s largest publishers

Suppose you are an unfathomably well-resourced entity that has discovered, while running the world, that you would really benefit from knowing where Covid vaccines are. You have a team of policy experts who are aware of the broad distribution strategy, the layers of government which determine allocations, and the fact that the vaccine is administered at thousands of locations within California. How would you use your massive power to put pins on a map, annotated with instructions on eligibility and access, while making sure your understanding was as accurate as possible?

I am speaking, of course, of the problem facing Google.

Google exists to organize the world’s information, and a bit of information that many individuals in the US were acutely interested in was ‘Where do I find the Covid vaccine?’

Google attempted to negotiate data-sharing agreements with various parties that they reasonably believed would know where the vaccine was. These sort of agreements are routine for Google. Long gone are the days where their only method of organizing the world’s data was to send their spiders into the internet to crawl it. Google has a variety of internal processes and controls around these agreements.

One question kept tripping up various potential counterparties for vaccine information: that of on-the-ground accuracy. Almost no one had any clue of where the vaccine was, at all. Those who did have some notion had unsatisfactory answers regarding comprehensiveness, freshness, and accuracy of their information.

How do you know that a fact in a database is, in fact, true? There is a Walgreens at Fourth and Townsend in San Francisco. That fact is in many databases, but _is it true_? How do you _know_? What evidence would change your mind? Is it, in fact, a probability distribution? Do you just accept that over all the locations in the world you’re probably right about most but wrong about some but extremely unlikely to be wrong given that this specific location purports to be a Walgreens in San Francisco?

These sorts of questions keep the Google Maps team up at night, and they have far more prior art on answering them than I’d ever be able to recount here, even if I knew it all.

Many of our coordinators and volunteers had day jobs. One coordinator, [Manish Goregaokar](https://twitter.com/manishearth), happens to work at Google. He navigated the internal mailing lists and found the people who were in charge of Google having a responsive answer to queries like [Covid vaccine near me].

We then bizdeved the bizdev. _Business development_, or bizdev, in tech parlance, is the skill of developing interesting arrangements between companies that are more complicated than simply purchasing their services and less expensive than buying them outright. Bizdev professionals are often written off in tech as bozos who have no real job and exist mostly to mooch off of the industry. If you believe this to be true, you have never met a good one.

Our process involved explaining at length to various Googlers what our strategy was, our trajectory with how many pharmacies we could reach a day, how we prioritized calls, what our flows were for taking correction requests from medical providers (trust!) and the general public (verify!), and our policies and procedures for cross-checking data. It helped that we had nascent cooperation with various government efforts in California, that back-channel checks on us reported, ‘Yep, definitely the good guys, despite being techies’, and that there was a public record of positive press. Google was institutionally terrified of negative news stories and government ire in the wake of 6th January.

Google, for its part, was comparing both our methods and our results to those of other participants in the vaccine data ecosystem. Those participants include healthcare providers, community-oriented organizations, and one large entity that owns both Covid vaccines and nuclear weapons. In Google’s considered opinion, we were far and away the best option for trustworthy vaccine location data in California.

We had a public API (a way to consume our data with computer programs without needing permission or individualized cooperation from us) since Day 1. We worked with Google to interoperate with their systems, which are the same combination of engineering marvel and terrible jank that civilization itself is. We talked at length with their teams around data refresh cadence, bilateral workflows for corrections, and similar. (Some of those conversations went better than others. Google, like all organizations, has its faults.)

On Day 47 (2nd March), Google began using our data to direct vaccine seekers to the vaccine throughout California. For example, here is what I saw when searching for [Covid vaccine near me].

![](https://wip.gatspress.com/wp-content/uploads/2023/02/vaccinateca-on-google-maps-1024x535.png)

Image

Image from Google.

Google graciously gave us a quote to prod some money out of potential funders:

> The uplift from VaxCA is ~5,000 sites (up from 127 [that Google otherwise had reliable information on]). For all intents and purposes, VaxCA is enabling our launch in California, and we greatly appreciate the partnership... VaxCA listings are now live on Local Search and Maps.

Google has _many_ users. Our website was peaking at tens of thousands of users a day. Although Google is reluctant to publish how many people found the vaccine on Google through data we sourced, at Google scale, millions of users is a small number.

There is a sardonic saying in tech to the effect of ‘the best minds of my generation are working to maximize the number of clicks on web pages’. What is the actual human impact of getting one vaccine searcher a useful result? Early in the vaccination effort, a reasonable approximation was that accelerating a dose by one day saves 0.0001 lives in expectation or, equivalently, that 10,000 dose-days saves a life. There are more formal efforts to quantify this [in the literature](https://www.nber.org/digest/202205/estimating-lives-saved-covid-vaccines), but that estimate, the sheer _moral weight_ of it, compelled me to take drastic action once I saw our stats on _Day 3_ and extrapolated.

One million dose-days? One hundred lives.

I believe our partnership with Google accelerated delivery of the vaccines by _many millions_ of dose-days.

Every day matters. Every dose matters.

## Paying for it all

As CEO, I tried to influence strategy for the team, including beating the drum for national expansion when that sounded delusionally ambitious. I dealt with most of the paperwork burden of setting up a nonprofit, hiring employees and filing reports with various states about that fact, getting our team healthcare, and cutting checks. I was a public face to the media or partners when required. I negotiated deals with players like Google. And so on and so forth.

VaccinateCA had an _extremely_ effective team, as good as any I have ever had the privilege of working with. They were instrumental in almost everything I did and probably could have done almost all of it without me. The main thing I uniquely brought to the table, and spent a lot of my cycles on, was finding the money.

Our earliest funding source was a prepaid debit card I spun up and posted in our public Discord, with $20,000 of my own savings on it. That would cover servers and software and similar for a while. That was not going to be sufficient to get a proper nonprofit with a paid staff off the ground, and I knew we would both need that and need to be _read as_ that to get cooperation from some quarters.

I called in favors and plead our case up and down the tech industry, and scraped together about $1.2 million in funding.

This was below what I initially thought I could reasonably raise, and below what I thought we likely needed. For better or worse, it would have been a lot easier if I had pitched it as: ‘Just make a small angel investment in a promising technology company whose CEO thinks his job is burning through investor dollars as quickly as possible while driving the total addressable market to zero. You won’t make any money on it, but think of the _story_.’

But while that tech company would probably have been well funded, it would have smelled like a tech company to potential partners. To accelerate shots in arms we urgently needed the cooperation of people who, if confronted with the proposition ‘Big Tech is bringing about the end of constitutional democracy so that it can gather more of your data to sell’, would like that tweet from their iPhone. I have a different point of view, but debating would not have put shots in arms.

We were approximately the most privileged nascent nonprofit imaginable in terms of access to funding, and given that it directly unlocked our ability to help people find the vaccine, I don’t want to complain too much about the process of getting it. I will record, for the benefit of future charitable founders, that probably half of my time from Day 8 to Day 160 was spent chasing funding, dealing with funders and the nonprofit industrial complex, pitching (and pitching and pitching and pitching) large pots of tech money earmarked for pandemic response, filing required reports with funders and the government, and diligently accounting for every penny spent.

It was a bit of a culture shock coming from the technology industry. Tech isn’t exactly _profligate_, but it certainly empowers twentysomething engineers to spend thousands of dollars by typing a command into their terminals. An engineer who fumble-fingers a command and spends ten times what they expected to is told to type more carefully next time.

The IRS wanted documentation on our foreign operations. Why? Because a US-registered charity had spent precisely 90 cents of tax-advantaged money abroad and _the law demands an accounting_. It also demands a documented basis for knowing that the recipient of those funds, a permanent resident of Japan who clearly needs to negotiate his CEO salary better, is not a terrorist. If you think I’m joking, our official basis for knowing I am not a terrorist is (as required by law) part of the public record; see our [Form 1023, Section IV, Question 10](https://media.kalzumeus.com/call-the-shots-documents/patio11-is-not-a-terrorist-well-probably-anyway.png).

The IRS sometimes catches flak for administering laws that the American public has voted for, through its elected representatives. I’d like to balance this by praising them for quickly processing our 501(c)(3) nonprofit application. These applications are the gold standard for charities in the US, and various institutions will, both informally and structurally, default to trusting them. The 501(c)(3) approval process takes three to six months normally in the best of times and the pandemic is [not the best of times](https://www.irs.gov/charities-non-profits/charitable-organizations/wheres-my-application-for-tax-exempt-status). I mailed a request to expedite and they got it done in just over three weeks.

Part of entrepreneurship is having a vision of something that is possible and figuring out what is necessary to bring it into the world. A cynic would say that the world has a secret: Building things is not actually possible, because different organizations have different timelines allowing access to different resources, and it is impossible to correctly sequence things to satisfy all the requirements in order to build anything. An entrepreneur would tell the cynic a secret in return: You can carefully titrate the amount of truth to various parties to dissolve these deadlocks.

Your donor-advised fund won’t let you donate unless we’re a 501(c)(3)? Well, you’d donate if we _were_ a 501(c)(3), right? Great. We’re applying for approval as a 501(c)(3) from the IRS. Can I put you down for $25,000? [Dear IRS examiners](https://media.kalzumeus.com/call-the-shots-documents/8-expedited-processing-request-redacted.pdf): I have a written commitment from a charitable allocator for a $25,000 donation contingent on 501(c)(3) status. As you are aware, IRS [procedure](https://www.irs.gov/charities-non-profits/applying-for-exemption-expediting-application-processing) says that this qualifies for expedited processing. Oh, yes, government actor whose cooperation we need, we’re a nonprofit. Look at this official paperwork from Delaware. It says that the State of Delaware is officially aware that I say we’re a nonprofit. Not good enough? Our 501(c)(3) status? The IRS is busy approving it, on an expedited basis.

Some potential funders were in after an emailed discussion that could fit in a tweet. Some were in after a single call.

Some potential funders had expectations that were misaligned with us. VaccinateCA was always designed as a rapid-response project that would spin up, cover for an urgent gap in US infrastructure, and then spin down once the work was done. We explained this at length while emphasizing that we wanted to work with funders who could reach a decision _quickly._ Every day mattered. Every dose matters.

We had some interactions where we were put through weeks or months of grant writing, which sounds like ‘turn in a paper and wait for it to be graded’ and is more ‘schedule sufficient meetings with sufficient backing documentation to buy a company for $20 million’. The funder eventually passed on us, saying they worried we would create no institution with enduring value after the pandemic.

I don’t begrudge anyone’s choices of how to spend their money, particularly charitably earmarked money. I will point out that the gap in expectations between a grant-reviewing team keen on institution building and a nonprofit with an urgent unmet need is a very, very common story in nonprofit fundraising.

Many pots of money have preferences with regard to how they allocate, and those preferences change with the seasons. Have I mentioned that health equity was all the rage in California in 2021? I put on my best face to funders, explained that the system of siloing vaccine information benefited only people who were professionally competent at navigating the American healthcare bureaucracy. I suggested that publishing vaccine locations to a website and Google and every other place we could think of was an improvement over that status quo. I didn’t engage with debates about how, and this was made _absolutely explicit_ in some conversations – perhaps saving lives but failing to save lives in preferred demographic ratios would be considered worse than not engaging in the project at all.

The experience gave me some compassion for grant writers who need to stick semi-relevant barnacles onto their program proposals to match the keywords that the funding ecosystem is looking for.

What did the $1.2 million go to? Fun fact: The Form 990 (tax return) of all 501(c)(3) charities must be made publicly available [by law](https://www.law.cornell.edu/cfr/text/26/301.6104\(d\)-1). But to save you that _scintillating_ reading, in broad strokes about half went to employing professionals to work full-time on the project and about half was paying for commercial call centers.

We employed about ten people. We had about ten volunteers doing engineering or operations work substantially full-time, some after their day jobs and some with their day jobs’ blessing during the workday. (I called a few CEOs and asked if they could please, please keep a senior engineer employed but release them from job duties for a few months.) We had variable interest in volunteering to do calls but probably a few hundred people doing one or more in any given month, plus between 5 and 25 call contractors and contracted call center workers.

Is $1.2 million a lot of money for the US to spend remediating its vaccine information infrastructure challenges in the midst of a pandemic? To put that number in perspective, Warp Speed’s initial budget was $10 billion. My Turn [cost more than $50 million for 2021, including an $18 million initial check to Accenture](https://calmatters.org/economy/2021/11/california-coronavirus-technology/).

Should we regret any of those expenditures? Oh heck no. I consider it a severe failing of our political system that we didn’t spend a hundred times as much on pandemic IT _and end up with a system that functioned wonderfully_. That would have been _obviously cheap at the cost_. We should regret our manifest failure to achieve what we were capable of and the lives that were lost as a result.

It is also a severe failing of our political system that the president didn’t have the switchboard connect him to the CEOs of Google, Amazon, etc. and say something like:

> The United States of America has made incredible progress against the pandemic. We have the vaccines. We have the doctors. We have the science. We have FedEx and dry ice. We need someone to make sure every doctor has patients ready to receive the drugs _immediately_ after FedEx shows up, every time. We also need an effective nationwide advertising campaign for the vaccines. And I want any decision maker in public health to be able to see the entire situation on an iPad app.
> 
> You seem to employ many of America’s best experts in software, logistics, and marketing. I think it would be salutary if you put your very best people on solving this problem for America, immediately. I think you can probably have an initial proposal ready by tomorrow. If you think you will need to demonstrate moral authority or gain cooperation from any arm of government, you can put your project leader in a US Army colonel’s uniform and give them a piece of paper saying Do It Because the President Says So. Well, you can’t do that, but [I _absolutely_ can](https://www.law.cornell.edu/uscode/text/10/603), and will. Does this sound reasonable to you?

The United States of America can be that decisive and effective. It _knows_ this. It teaches case studies about its ability to be decisive and effective in its history classes. The _existence of history classes_ is itself evidence of decisive, effective action! Not action in the distant past! Action every Monday through Friday from September through May!

It _chose_ not to be decisive and effective, because it _believes_ itself incapable of simple things.

## The United States of America does not believe it can build websites

The Biden administration identified the lack of a nationwide site for finding the vaccine as a problem early, and wanted to solve it.

However, the administration had a painful institutional memory of a well-liked Democratic president nearly having his legacy derailed by a website for a signature initiative that launched to great fanfare and immediately fell over. This was 2013’s launch of healthcare.gov, whose story clearly deserves a book. (This write-up on [Medium](https://medium.com/dataseries/small-is-beautiful-the-launch-failure-of-healthcare-gov-5e60f20eb967) largely aligns with my understanding.)

This meant that ‘spin up a website in a few weeks, as the federal government’ was deemed clearly a nonstarter. The administration wanted to find a partner and bless them as the official national initiative. (An optimist would say they had high confidence that the right team was already working somewhere in America but probably not employed by the federal government. A pessimist might say that an external partner needs little credit if the administration succeeds and the administration needs no blame if the partner fails.)

They found the right partner, by their lights. VaccineFinder is run out of Boston Children’s Hospital and had been doing yeoman work for a decade. They had the track record, the medical expertise, the institutional credibility, and the sheer _gravitas_ to partner with the White House.

VaccineFinder was an [organizational front end](https://www.statnews.com/2021/02/24/cdc-vaccinefinder-covid19-locations/) on top of a ‘data lake’ (technologists: Say data warehouse, but pronounce it with a DC accent) maintained by [Castlight Health](https://www.castlighthealth.com/), which was [tapped by the CDC](https://www.cdc.gov/vaccines/covid-19/reporting/downloads/vaccine-administration-data-agreement.pdf) to receive data directly from pharmacies participating in the FRPP. Castlight had performed a similar role previously for more routine vaccine distribution programs.

VaccineFinder was to dredge the data lake for signals and publish vaccine location information on its website. That website would become Vaccines.gov and be positioned as America’s answer to finding a vaccine. It would be launched by President Joe Biden in a speech to the nation. This site would be used by most Americans looking for the vaccine. It would also accelerate public workers and private citizens trying to find the vaccine for others.

Imagine that! A national database with information about where the vaccine was! Blessed by the authority of the subject matter experts reporting to the legitimately constituted government! With impeccable provenance for all their data! Where submitting accurate data in a timely fashion was a requirement of regulated entities in an official federal program!

Maybe we will be able to go back to our day jobs!

We did not go back to our day jobs.

I am a fan of tech’s ‘ [man in the arena](https://en.wikipedia.org/wiki/Citizenship_in_a_Republic) ’ ethos, where one should be mindful about criticizing people and organizations who are actually putting the work in. And so I want to be careful here.

VaccineFinder did excellent work for many years prior to the pandemic while operating under the constraints that they had.

They were, for example, understaffed for engineering. The US Digital Service [supplemented them](https://www.usds.gov/projects/vaccines-dot-gov) with a team that we had high regard for. I will report, solely as a matter of my personal opinion, that I am extremely glad that team existed and that nonetheless I did not consider the project staffed in a manner reflecting its complexity and importance.

Castlight’s system had technical debt accumulated over the years and was swiftly repurposed to do something it had never been designed for. Technologists can predict the consequences. One was that agility was compromised; it took upward of two weeks to add latitude/longitude pairs (data which they already had, to put pins on the map) to the file they were making available to publishing partners. VaccinateCA routinely turned around that sort of work in _minutes_.

As I’ve mentioned, software problems are people problems.

The US had negotiated _spiritedly_ with pharmacies to get them into the FRPP. Some of those pharmacies requested, as a condition of their cooperation, that availability data based on their (mandatory) reports to the CDC _not be published_.

Why would a pharmacy do that? Some didn’t want bad publicity. Again, brute logistical reality meant that seekers were going to outnumber doses for the first few months. Everywhere was going to be out of stock most of the time. While that was a good thing, because we wanted shots in arms, not shots in freezers, people would be _furious_ at the chains showing little supply.

Being desperate, the United States of America agreed.

Some pharmacies were happy administering the vaccine in the ordinary course of their operations but _did not want the government to publicize this_ because the vaccine was, again, a _distraction_ from their core operations. They were happy to have the vaccine, sure, but you’d probably only hear about it when, e.g., picking up your existing prescription.

Being desperate, the United States of America agreed.

Some pharmacies believed that their pharmacists, individual people with names who report to a known address daily and whom they owe a duty of care to, would be targeted for harassment or worse for administering the vaccines. They accordingly wanted the government to scrub the data, which included, e.g., the names and phone numbers of pharmacists signing off on required reports, of information which they believed would put their people at risk.

Being desperate, the United States of America agreed.

It may have not realized it was agreeing, because this one was subtle: The system, long since built and used for routine vaccinations (this was why it was picked!), had an opt-out button and a pharmacy chain ticking it per their standard operating procedure meant, _now in the context of the Covid pandemic and not the years-ago flu shot_, that America’s vaccine site would not display their doses _at all_. No one felt like they had the authority to swiftly un-negotiate or simply technologically dismantle a promise made by the United States of America.

Which pharmacies am I talking about? Well, most lawyers would insist that sensitive commercial negotiations happen under an NDA, and being desperate...

Pharmacies through the FRPP had roughly half of the doses; states and counties had roughly the other half (sometimes administered at pharmacies, because clearly this isn’t complicated enough yet). You would hope that state and county doses were findable on Vaccines.gov. It was going to be the centerpiece of the Biden administration’s effort to fix the vaccine finding problem and _take credit for doing so_.

Here we must, inevitably, turn to some observations about political actors and how they perceive the world.

It is not incentive compatible for all governors (or bureaucrats) to allow the president credit for work that their teams are doing at their direction. This goes beyond simple partisanship, although there is certainly _no small amount of that_ bound up in this issue. Many politicians (and bureaucrats) are _ambitious,_ and their performances on Covid got them acclaim, attention, and political capital. One governor even got an Emmy (an _Emmy_!) in the newly created category Talking Confidently on Television About the Consequences of One’s Bad Decisions.

What ambitious politician or bureaucrat wanted to say:

> Give Biden the credit for all the work I have been doing. I _hate_ being on television. I certainly have never thought about my next election. Oh, could you please minimize our health departments’ contribution to this effort, perhaps with language like, ‘It turned out all we needed was a simple website’. Thanks, that would be great.

And thus many governors were not in on the plan. But it gets worse. Since the optics would be _terrible_ if America _appeared_ to serve some states much better than others on the official website that everyone would assume must show all the doses, no state doses, not even from states that would opt in, would be shown on it, at least not at the moment of maximum publicity. Got that? Great. (This theory is a theory, from a person with much more experience in DC than me.)

So that was the hand dealt to VaccineFinder. I hope they write a book someday about their experience. I know some of what would be in it, but it is their story to tell.

## Some advantages private individuals and organizations have over official initiatives

Note that even the federal government, while being incomparably better resourced and having smarter experts than VaccinateCA, has constraints. We did not share some of them.

For example, VaccinateCA had no negotiated nondisclosure agreements with pharmacies. Nope, we had the default deal under the First Amendment: a near absolute right to publish true information, made _even stronger_ (under the jurisprudence and traditions of the US) because we were operating on an issue of intense public concern.

The government of the United States is an intrinsically political entity. We were formally nonpartisan (and even better, as a 501(c)(3) nonprofit, had to be). Informally, to quote a memo I wrote early on, we would do a deal with the devil himself if it got one more patient one more dose. We didn’t need to worry about compromising anyone’s reelection chances by being too maniacally focused on shots in arms to consider the big picture. We had no responsibilities to allies in our party, like not overshadowing their efforts, because we had no party and, for that matter, no shadow.

I knew that many political actors wanted to hoard the facts of their operations so that they could claim credit for them. I just didn’t particularly _care_. If an actor had a dose available to the public, it was going to be publicized anywhere we could cause it to be.

I really, really wanted to get our data onto Vaccines.gov as well, but don’t think we succeeded in doing that at scale, mostly due to aforementioned institutional constraints. But we negotiated an agreement with them, and it is a true statement that the United States federal government got things from us that it did not otherwise have available. Yes, I’m being deliberately vague.

This gave me the ammunition we needed to talk to publishers, government agencies, and similar and say:

> Yep, we are working hand in hand with the federally blessed initiative. We are now not merely a pro-social initiative but we are, unofficially, the shadow location information infrastructure for the US vaccine rollout. If you want you can go talk to the blessed federal initiative. They are _quite busy_ and may not exactly speak your language. We have more and better information than them about vaccine availability. We can show you a side-by-side comparison easily. If you can get on their calendar they will happily tell you the institutional constraints that explain the delta, and why there will always be a delta, and why it will widen over time.
> 
> This data is available to you and the public _immediately_, with no strings attached. We want nothing other than to get it to your users. What do you need from us to make that happen? What do you need to make that happen _today_?

So how did that collaboration come to be?

## VaccinateCA goes national

I told the team that the plan was to go national on Day 8. We did not talk about it in public, which is a difficult proposition when all of your work happens on a public Discord server next to very enthusiastic volunteers you barely know. When reporters asked if we planned to expand, we said variants of ‘We are totally focused right now on the prodigious amount of work ahead in California’.

Why? Underpromise and overdeliver. If I had told the media, in week two of our operations, that we were currently VaccinateCA but were soon to be VaccinateTheStates, the takeaway would be: ‘Ah, this group of do-gooders is currently failing at their mission in 49 out of 50 states. That is what happens when you let amateurs think they can do the government’s work, I suppose.’ We needed it to be: ‘Ah, this plucky group of do-gooders has made impressive progress in California!’

We picked Oregon as a test bed for expansion. It was geographically close to California (and in the same time zone as most of our callers), has a similar political economy and therefore a similar allocation strategy, and was small and achievable as a proof of concept. We were calling Oregon by Day 50.

This poses the question: Why California first? For most of the team, that was simple: They lived there. For me, it came down to historical accident. I was in a California state of mind when I tweeted. I had not previously spent more than four weeks of my life in California, but I had worked in tech for decades. Silicon Valley now exists in the hearts and minds of geeks worldwide, but prior to the pandemic it had a definite physical location. I felt some level of affinity to that physical location simply because of decades spent in its psychic orbit.

Anyhow, Oregon. The usual problems, the usual solutions. Let me compress a lot of hard work conducted over weeks: Our model worked in Oregon too.

A portion of that hard work was an overhaul of our systems to prepare for conducting national-scale operations; we couldn’t do everything out of a spreadsheet-based technology anymore. Simon Willison [wrote about](https://simonwillison.net/2021/Apr/12/porting-vaccinateca-to-django/) how we created VIAL, the Vaccine Information Archive and Library, which was the new heart of our operations. This required conducting open-heart surgery on ourselves while running a marathon. We did not die.

We ‘dark launched’ in Oregon, with no media presence and no first-party site for vaccine seekers. It was clear to us that our strategy would not be spinning up 50 state sites and doing 50 PR campaigns for them in parallel. We were working hand in glove with the largest publishers in the world and just wanted to get them the best possible data, for the entire nation, ideally with official imprimatur. That plus scaling the positive side effects of our data collection would be enough, even if we’d fade into the background pursuing this strategy.

So by the time VaccineFinder was capable of working with partners, in mid-March, we... didn’t look like a motley band of do-gooders anymore. We were a nonprofit with ample funding. We had Californian government officials saying we had the best data source in California. We had a strong endorsement from Google as being one of the best operations in the vaccine data ecosystem. We had recently expanded to Oregon, and were shortly to expand nationally.

It was almost... shockingly plausible that the official national effort should want to work with us too.

We then proposed bilateral data sharing. This would allow us to get useful things from the national effort, like a full list of every pharmacy ever expected to receive the vaccine from the feds and up-to-date reports from them about inventory. We could then give them back _a better version of that_, by using our operations teams to actually check the data against ground truth. And we could give them the data they didn’t have about state and county operations, so that they could merge it onto the officially blessed map of America’s vaccines.

So we bizdeved the bizdev, this time with the nationally blessed initiative. Cooperation candidly did not end up as deep as I would have preferred, but both sides got value out of it. And we snapped to attention regarding a few things that it was intimated that the feds wanted.

## What the United States of America wanted

The United States of America believed, strongly, that it needed to cut through the noise of a million different competing systems with an easy-to-remember national site, Vaccines.gov, which could be announced by the president on television.

The United States has learned one lesson about software launches that I heartily endorse: Don’t commit publicly to dates in advance for software that isn’t written yet. Instead, get the site up and running, shake out the bugs, and _then_ launch it. From the White House’s perspective, the site was launched when the president told the American people it was launched.

There existed a technical and organizational timeline required for Vaccines.gov to be ready for the official public launch. We weren’t closely tied to those timelines, but we were affected by them. We had, well in advance of launch, an increasingly valuable national data set. We quietly published it to partners but avoided making any splashy announcements. The administration wanted _a moment_ and partners critical to us had committed to giving it to them. Our carefully orchestrated PR operation went mostly radio silent, intentionally, and remained so for months.

The Vaccines.gov launch was delayed a few times. It happens.

We dark launched our national site, VaccinateTheStates, on Day 100.

I didn’t mind those weeks of not having a public national site, perhaps surprisingly for a tech founder who was maniacally focused on time to market. After all, I knew that the supermajority of our impact was coming not from any surface we controlled directly but rather from publishers with massive user bases publishing data we were giving to them. When we found out about a new dose being available, Google learned that from us _very quickly_, and Google has more Americans using it daily than we could recruit in our lifetimes.

Let the publishers get the click. Let the government get the credit. I did not care; I just wanted vaccine seekers to get the shot.

But this candidly complicated the narrative with funders and other partners. That narrative went something like this:

> Yes, we have national data. We actually have the best national data, by a constantly increasing margin. We can show your data science team a side-by-side comparison; we are a superset of the official data. Well, minus the data they have that we know to be wrong. We are working on getting them to fix that.
> 
> No, I can’t just point you to a website showing it like I can for California. We do not want to upstage the official site’s public launch. They have a data pipeline from pharmacies and we have negotiated access to it.
> 
> No, you should still want to fund this even though the president of the United States is going to say on live television that vaccine discoverability is a solved problem and that he has successfully guaranteed supply for all Americans. The site he directs Americans to will not show about half of the vials in the United States. The reasons for this are fascinating and you probably don’t care about them.
> 
> It remains absolutely critical that we work on increasing access to the vaccine. I know that the public narrative is that the supply problem has resolved. This is in fact only true for the professional-managerial class. That class, your class, my class, perceives there to be no supply problem because it preferentially allocated the supply to itself. We also control the narrative, which we _are wrong about_. There exist people, particularly at the margins of the healthcare system, who still urgently need to know where the second half of the vials are.

President Biden [announced](https://www.whitehouse.gov/briefing-room/speeches-remarks/2021/05/04/remarks-by-president-biden-on-the-covid-19-response-and-the-vaccination-program/) Vaccines.gov on 4th May. We announced our national site was live immediately after he stopped talking. It was Day 108.

Why bother with our own national _site_, given that there would be an ‘official’ national site and that almost all users who found our national _data_ from our national _data-gathering operation_ found it on, e.g., Google? I thought the most compelling reason to have one was because it made the explanation to funders and volunteers easy, and we needed funders and volunteers.

‘You should give us money so we can make phone calls on the behalf of Google. It will save many lives,’ is an _obviously true statement_ in context. It is not maximally palatable to charitable funders, including ones which have... complicated relationships with Google because _everyone in tech_ has a complicated relationship with Google. Volunteers also do not bounce with enthusiasm to do free work to curate Big Tech’s data feeds.

## Operating at national scale

Operating at a national scale posed some challenges. We certainly could not 50 times our team size. In addition to that not being feasible with our funding situation (about which, more in a moment), merely replicating our earlier operations wouldn’t have done the most good in the current environment.

With an integration with the blessed national initiative, we were able to receive, improve, and republish to partners information coming directly from the systems at some large pharmacy chains. This made redundantly calling those pharmacists far less pressing. We still did a bit of it, to audit data quality and similar, but we spent _far_ fewer calls per dose found. And remember, the pharmacies in the program had a significant share of all doses.

We started focusing much of our efforts on novel approaches. Now that we had something approaching an ongoing national census of pharmacies, we went after the other half of the doses.

Where we could, we tried to get this with partnerships. We had a team of volunteers that attempted to contact and then negotiate partnerships with almost every county in the United States. Since we could not successfully achieve a partnership everywhere, and since partnerships take time, we also scalably piggybacked on their own marketing efforts for their doses.

County health departments were trying to get the word out about their doses. We made sure that Google et al. heard about them, through a pipeline that they institutionally trusted.

This again involved scaled application of surprisingly low-tech approaches, like ‘web bankers’, a coinage that we used to distinguish it from phone banking (volunteering to call pharmacies).

Suppose you are a county health department. You have a pop-up vaccination event scheduled for next Tuesday, at the church down the road. No appointment required; come one, come all. How do you get that information out to potential patients?

For many counties, that involved a lot of one-on-one outreach and working through community partners. But it _also_ included: ‘We should probably post about this on Facebook. Like and subscribe for more lifesaving medication.’ (Fun fact: In many rural counties in California and across the US, a Facebook page is the only public presence the county health department has.)

There are 3,143 counties in the United States. That’s a lot of counties. How would you find the Facebook page for all of them? Well, first you find the Facebook page for one. Then you do it 3,142 more times. But you can have a lot of people doing it at once. This is fundamentally the same math problem as ‘Call all the pharmacies in California’. We were, by this point, very good at this math problem. We built a large spreadsheet and parceled out counties to many volunteers, and they spent hundreds of hours finding all the official channels they could.

If you want to impress a technologist in your life, read them that paragraph and then say, ‘Well, actually, it is less a math problem and more a disgustingly parallelizable job assignment. You could imagine a variety of approaches, most of them isomorphic to map/reduce. Barely engineering.’ They will say you do an excellent impression of a _Hacker News_ commenter.

When a county health department posted something, a complex system that took tens of thousands of engineer-years to build would convey that information to us in real time. By which I mean: Our volunteers had Facebook on their phones. Ding, County You’re Responsible For has just posted to your feed.

Then we would parse the county’s announcement using the cutting-edge AI technology called ‘literacy’. The web banker would retype the most important information, in a structured fashion, into VIAL (our back end). The important bits here: address of pop-up clinic; start of availability; stop of availability; restrictions: none; data reliability: public statement from government office; substantiation: copy/paste URL to county’s public Facebook post.

From there, VIAL would help that record get some human attention if it needed it. Is this a location we know about already? Two feet away from an existing location, information matches, hm, no need to add to data set, okay. But if it seems novel? Let’s check to make sure; VIAL adds it to a queue of an internal I-can’t-believe-it’s-not-a-video-game so that our team could check it against existing sites we knew about.

![](https://wip.gatspress.com/wp-content/uploads/2023/02/comparison-of-location-ui-1024x469.jpg)

VaccinateCA built a user interface, memorably described as ‘the best cow-clicker ever’, to allow volunteers to quickly determine whether newly discovered locations were duplicates of sites already in the data set or actually true new locations.

Image

Image by VaccinateCA.

It turns out that people have much better intuitions for this than we could quickly code. To the best of our knowledge, and we looked, automated tooling for this was not available and the way to build it is nonobvious. If our people comparing locations encountered a genuinely ambiguous situation, posting in Discord could quickly get someone to call and ask.

We faced an absolutely backbreaking amount of work in finding _concordances_, where two bits of data coming from different sources (say, a county health department Facebook page and VaccineFinder) do or do not correspond to the same location here in physical reality. I don’t understand most of that work and, luckily, neither I nor the web bankers had to. We baked our knowledge of it into the system.

Many of our volunteers _loved_ doing web banking.

Working in a call center environment is exhausting! You have to just power through calls. You will occasionally be made to feel bad by someone who does not want to talk to you. It’s really hard to do if you’re, e.g., watching your child at home.

Retrieving reliable information from Facebook is less exhausting than working in a call center environment, though it feels quite different than the experience of scrolling aimlessly. Finding concordances was even easier than that; many of us compared the experience to playing a video game.

We combined this process with our other operational competencies.

For example, if the county health department forgot to tweet the actual address to go to, we would add an edit button to Twitter. Okay, we couldn’t do that. But we could call them and tell them about the mix-up.

> Hiya, is this the county health department? Hey, I was just on Twitter and saw we were having a pop-up next Tuesday at St. Mary’s? So I noticed the flier doesn’t have an address for St. Mary’s. Do you have that address for me? Oh, you don’t? Well, is it, I don’t know, the St. Mary’s on Maple Street that I just googled? Oh, it is? Wonderful, I understand, you are having a pop-up clinic next Tuesday at 123 Maple Street. Maybe you could tweet that so people know. Alright, you have a nice day now.

And while the county got to work on finding who had the Twitter account to post a follow-up, we’d have already keyed the address into VIAL and marked it as verified by a county health official. This would, pretty quickly, put the pin on all the maps we published to.

Which maps? The PR line was ‘those of the largest publishers in the world’. We had to avoid playing favorites or breaking confidences. By this point, if it was a map and it had vaccines on it, and those vaccines were from more than a single source, that map was probably downstream of VaccinateCA. We weren’t the public/private national clearinghouse, but we were _extremely_ close to being that.

We also started partnering more deeply with some of our peer projects. Some of them were still operating, generally using the scraper model. They wrote software to read official websites. That software would pull salient details out. They would then republish those details, generally to a website they controlled.

We partnered with the scraper sites, and even put out an open invitation for OSS developers to pitch in by writing a scraper. Scrapers are a fun product for developers, can be written quickly, and have a low barrier to entry. Want to do something to help your community, a community you are concerned about, or for that matter _any_ community? Spend an hour or a few writing code to scrape an official website relevant to them. We’d take it from there.

Suppose you are Eli, the healthcare infrastructure maven for Illinois. You have written code to scrape all the counties that had, e.g., had a consultancy build a bespoke appointment portal. If you worked with us, you could get those results into our data pipeline. We could check, clean, and enhance them, and _then we could vouch for them_ to everyone who trusted VaccinateCA’s judgment and _therefore put a pin on their map automatically_ when we put it on ours.

Google didn’t have an arrangement with most counties in Illinois. But those counties published their appointment availability to the public internet. That information was seen by Eli. We had an arrangement with Eli. Google had an arrangement with us. By the transitive property, Google had a trustworthy data feed from every county in Illinois that Eli had gotten around to integrating into the national pandemic response effort.

Was this all rainbows and sunshine? No, it was months of hard work. A short selection of problems:

We always wanted more time to verify things than we had available. We were rate limited on volunteers to write scrapers to feed our pipeline; at even an hour a site, with thousands of sites, the problem was far larger than our committed engineering team even if we did nothing else. As more counties and healthcare providers figured out how to publish data to the internet we increasingly had the same doses listed in multiple places, and spent _so_ much effort removing duplicates, which is a much deeper problem than it sounds like. We had to have discussions with Facebook to say that our volunteers had only the most noble of intentions regarding vaccine policy so please do not ban their personal accounts if they access a statistically improbable number of vaccination program pages in a day.

By Day 115 (late May), we were tracking [more than 75,000 locations](https://www.mapbox.com/blog/tiling-thousands-of-points-to-vaccinate-the-states) across the United States.

![](https://wip.gatspress.com/wp-content/uploads/2023/02/75k-dots-on-map.png)

A map of the United States showing the 75,000 locations that we were aware of. There are very many, but not 75,000, green dots on it, because locations close to each other are combined at this resolution. The dots are useful to understand the population density across the country, but less useful to answer interesting questions about the vaccine. The map could be zoomed down to address-level resolution, for example after a user searched for the vaccine near them.

Image

Image by VaccinateCA / Mapbox.

Did we find every one? Nope. Some would be closed by the time we got around to looking at them. Darn. Next. Next. Next. Next.

Our goal was shots in arms, not being 100 percent comprehensive. If you were looking, for yourself or someone else, we surfaced as many options as possible for available shots near the patient, without you having to devote your life to the hunt.

Many counties, now that the vaccine was more available and running into surplus in many locations, were doing innovative tactics like running extra clinics in rural areas to make sure people far from the nearest pharmacy weren’t ‘left behind’. We watched them like we were an intelligence agency whose sole mission was spying for publicly announced vaccine locations. Then we made sure as many people as possible knew about their efforts. Most of the time, no one ever even knew we were there.

We even did on-the-ground data collection, though this was rare relative to the number of locations we were tracking. If we couldn’t get data on a site online or via telephone, and that was mentioned on Discord, sometimes a team member volunteered to visit them personally. ‘Hiya! I heard you have the Covid vaccine? Awesome! Mind if I ask you three quick questions. Oh, no thanks, I already got mine; I just wanted to tell some people I work with about you.’

The supply situation kept improving, through the hard work of people throughout the healthcare system. As it improved we tried to fan out information about the new doses to as many places as possible, so that patients could access them as soon as they arrived.

Where could we go after going national? International seems like one obvious option, but we ruled it out.

It seems silly that anyone thought that the pandemic was over in May 2021. Clearly, with the benefit of hindsight, we know that it wasn’t, but cast your memory back. There was a great deal of pandemic fatigue. People in positions of power, like all people, are insular creatures. They thought: I have received my vaccine. My family and friends have received their vaccines. All the blue checks I follow on Twitter have received their vaccines. Clearly, the supply problem has been solved.

The supply problem had not actually been solved. It was _getting better_.

But why not aim for international anyway, as the next major milestone? There is an excellent case for it: Because of the extreme way that Covid ratchets up in risk with age, the first doses delivered to a community (under any sensible prioritization strategy) save _hundreds of times the lives_ as the same number of marginal doses delivered months into an existing vaccination campaign. Plausibly we could have redirected some of our efforts at the margin to helping countries whose vaccination campaigns were just starting. (We couldn’t have directed the doses, of course. We never had authority to allocate a single dose. But we could have _discovered_ the doses that were beginning to be delivered in many places around the world.)

We didn’t do that.

The team had signed up for a short, sharp sprint for California and was now months into a project for the entire United States. Partners were getting antsy, children missed their parents, and employers were starting to ask, ‘So now that the pandemic seems basically done, when are you coming back to work?’ And despite all that, if we had had any reasonable path to international impact, the math remains the math and the moral case remains the moral case.

We just couldn’t find a path.

There were parts of the VaccinateCA model that took advantage of relatively unique features of US healthcare infrastructure, like widespread distribution of privately operated pharmacies that had been turned by the government into a primary distribution channel for the vaccine. We didn’t think we’d be able to take advantage of that in most nations. We would instead be back to understanding virtually nothing about relevant healthcare infrastructure while facing even more disadvantages than we had faced on Day 1.

We also benefited from another major strength of America: You cannot get arrested, jailed, or shot for publishing true facts, even if those facts happen to embarrass people in positions of power. Many funders wanted us to expand the model to a particular nation. In early talks with contacts there in civil society, it was explained repeatedly and at length that a local team that embarrassed the government’s vaccination rollout would be _arrested and beaten by people carrying guns_. This made it ethically challenging to take charitable donations and try to recruit that team.

So we continued doing what we did best: solving vaccine discovery issues throughout the United States through a combination of engineering, operational excellence, and partnerships. We planned to wind down as the supply situation improved.

On the demand side, which would continue to be a problem even after supply was abundant, we did not have much to contribute. We were never going to be able to convince every American to want the vaccine. We didn’t have the platform, the skills, or the resources. We just wanted to reduce barriers to accessing it, which incidentally _helps with demand at the margin_.

I cannot underscore enough how much ‘vaccine hesitancy’ was frequently a solvable problem invoked as an excuse for institutional incompetency or unwillingness to do hard work. Or easy work.

We do not call it ‘free-money hesitancy’ when you need to explain to students how Pell Grants work, patiently walk them through the application process for financial aid, and reassure them that the offer really is as good as it sounds, even if they come from a socioeconomic background where nobody, and certainly nobody with a graduate education, has ever given them anything with no strings attached.

Most publicity about the vaccine _failed to mention it was totally free_, because lawyers said, ‘Well, actually if you have insurance we’ll bill the insurance and by law you will have no out-of-pocket cost but that is not the same thing as free’. Lawyers, man. When I was six years old I learned ‘free\*’ is how you spell ‘not free’ in English, because they wanted shipping and handling for the G.I. Joe even though I had collected all the Cheerios box tops those lying liars said to. Many people in society vividly remember similar experiences that had _much worse_ consequences.

People _died_ over that asterisk. _Why?_

## Working at the margins

A lot of the improvements from this point were necessarily at the margins. Every day matters. Every dose matters.

Here’s a margin for you: county borders. Many people live in one county but work in another, or live in one county but (particularly in rural areas) are closer to a pharmacy that is just over the border. After county health departments became less zealous in guarding their doses, they started to relax residency restrictions. They asked good, patient-focused questions, like ‘What can we do not only to provide healthcare but to help our residents close to our borders navigate to healthcare that others provide?’

We told Alameda County we could provide them with the embeddable, searchable, interactive map they wanted. They could center their particular map on Alameda County but show close results, and put it right on the health department’s main Covid page. And we would keep doing the thing we had always done: keep the data as up-to-date and accurate as possible without requiring every consumer of it to replicate our entire operation.

We hammered out the details over email and built it within days. We were not a government contractor. I am very bad at responding to RFPs, trust me. But we were very good at writing software _quickly_. Every day mattered.

Alameda County was so overjoyed that they ended up publishing our staging server to the public website. Easily fixed, and the sort of tiny snag that happens when operating with urgency and focus. The fear of that sort of thing should not cause our society to delay and dither in rolling out programs, not when the cost of delay is so high.

Alameda County asked us to speak to every county public health director in California during their weekly meeting. We tried to give that map away to every county in California. We would eventually pitch it to almost every county in America that we could get in touch with.

We successfully got it installed on the public sites of, to my recollection, at least four county public health departments In California. We also published instructions for any government, nonprofit, or for that matter literally anyone at all, to embed it on their own site. You get a free vaccine map! You get a free vaccine map! You allllll get free vaccine maps! No talking no contracts no payment just go, go, go!

An aside: A not insignificant number of people consumed our data over a telephone, not in the sense that they used Google Maps on a smartphone but in the sense that they called someone they trusted to ask for advice. That was, perhaps, the county or local free clinic or their doctor or a friend. The person who answered that phone might have had a tab open to our site, or a public or internal county page that had our results embedded on it, or maybe they just googled [Covid vaccine in Modesto]. In any event, they’d find the internet’s best answer regarding appointment availability. Then they could either read the information over the phone or assist the vaccine seeker in getting an appointment.

Good software improves the lives of people, even people who do not directly interact with the software.

There were a lot of little wins like that, at the margins, enabled by having one small team of now-experts obsessing full-time about vaccine distribution data.

A pharmacist told a Mexican woman that _se necesitan papeles_ to get the vaccine? Oh, no, one does not, and that will not stand. We notified our contacts in the state, as they had asked us to do when we ran into situations like this, so that they could correct the pharmacist’s understanding. Callers were asked to bring cash payment for the vaccine? There exists an alternate universe where that was the plan, but in the one we actually live in, the vaccine was free by law. We again brought those vials, stranded by poor decisions being made, to the state’s attention.

## Winding down

By June we were looking at our graphs, extrapolating from them, and making our best educated guesses as to when our efforts would not create value for vaccine seekers. We penciled in the end of August, by which we thought that the vaccine would be as easily navigable as the United States healthcare system is generally. (That is not exactly a ringing endorsement, but both the vaccination program and the United States healthcare system are flawed civilizational achievements but achievements nonetheless.)

I wish I could say that this went exactly according to plan. In actual fact, the funding environment changed quickly as funders (again, themselves virtually universally in the professional-managerial class) perceived there as being no extant supply issues. The funders now had higher priorities for their charitable dollars than routing patients to vaccine supply in America. We were informed that promised grants would be redirected to other purposes.

We did not believe supply was, as of June, actually a solved problem in the United States. I think we had the right idea of it, but we did not persuade sufficient funders to keep operating for the final planned months.

We looked at our options for, e.g., finding a successor organization for the project. Those did not bear fruit. We were near the tail end of our model’s usefulness, and the short list of organizations that could have taken over our operations did not think the integration hassle was worth a few weeks of operating a public utility.

So we wrapped up a bit early. We let the employed team go at the end of June, fulfilling my promise at every job interview that successful execution at their job would result in swift unemployment. We wound down our contract with the commercial call center.

We kept our automated systems running on a volunteer basis for the next few weeks. This was as long as we could stomach without the team of professionals working to keep the data accurate. Our partners institutionally relied on our data being trustworthy and, while fragmentary and sometimes inaccurate data is better than no data, fragmentary and inaccurate data _that your system treats as trusted_ is dangerous.

We got in touch with partners about our plans and tried to arrange as soft of landings for them as possible. They were very understanding. Some had really hoped we were going to be there through August. I had hoped so too.

We made a public announcement of our wind down timeline in late July. We cut the data feeds and redirected our sites to Vaccines.gov in early August. I think it was Day 200.

I returned to Japan, went through two weeks of mandatory quarantine, and then reunited with my wife and children. On the day I [returned](https://twitter.com/patio11/status/1394171218278813700), less than two percent of Japan was vaccinated. Japan vaccinated more than half its population in the next three months. Meguro (a ward of Tokyo) vaccinated my wife.

I declined the opportunity and was asked why.

An approximate translation of my side of that conversation: ‘I have already received my shots. At the Zuckerberg San Francisco General Hospital. Yeah, that’s right, the guy from _Social Network_. No, I don’t know him. They had a walk-in clinic. I read about it. Oh, I don’t remember, it must have been somewhere on the internet.

![](https://wip.gatspress.com/wp-content/uploads/2023/02/Illustration-5-1024x677.jpeg)

Image

Illustration by Venus Krier.