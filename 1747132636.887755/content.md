“Where do you get your blog post ideas?” people occasionally ask me. “Uh, I’m not sure,” I usually quip back.

In the future I’ll just link them to this post.

![](https://robertheaton.com/images/ideas-cover-2.png)

I’m going to start with what I believe the marketers call “establishing credibility”.

I’ve published 140 blog posts, or 270,000 words, or 1.5 _Fellowship of the Ring_ s. According to Google Analytics, these posts have been read by over 2 million people. I’d guess that the true number is at least 20% higher than this, since no doubt a good fraction of my audience block third-party web trackers (I may have a visceral dislike of online tracking but I still find surveillance capitalism as useful as the next publisher of online content, although no one pays me to do this so I don’t think it counts). Either way, my blog is one of my main hobbies, and I’m always very happy when it comes up in conversation with friends or strangers. I get to talk about myself, they get to talk about me, and everyone has a good time.

In this post I’m going to explain how I come up with blog posts ideas and give suggestions for how you can come up with ideas of your own. I’m going to reference my own work a lot, because I find specifics and examples useful. This may make this post read like content marketing for everything else I’ve ever written, which is itself content marketing for nothing. But I think it’s worth it in order to be able to talk about “technical stories” or “gentle introductions for generalist programmers” in concrete terms.

## What should I write about?

When deciding what to write about, I have two principles that I try to follow:

1.  The Made-Up-Award Principle: every post should at least try to be the best on the internet at _something_
2.  The Netflix Principle: every post should provide long-term, incremental value to readers of my blog for at least the next 5 years

Let’s go into more detail.

## 1\. The Made-Up-Award Principle

For every post I write, especially those whose primary goal is to teach the reader something, I try to ensure that there exists at least one category, however specific, for which my post is the best on the internet. This might sound over-ambitious and self-aggrandizing, but it’s not. You can win a lot of imaginary awards when you get to define the judging criteria:

-   [“Making peace with Simpsons Paradox”](https://robertheaton.com/2019/02/24/making-peace-with-simpsons-paradox/) is not the best explanation of Simpson’s Paradox in the internet. But it might be the most entertaining introduction to it for people who don’t care much about the maths.
-   [“How does HTTPS actually work?”](https://robertheaton.com/2014/03/27/how-does-https-actually-work/) is not the best explanation of HTTPS on the internet. But I think that it is arguably the most efficient 1500-word introduction for generalist programmers who currently know nothing about HTTPS and would like to learn enough to be able to bluff their way through a locker-room discussion.
-   [“HTTPS in the real world”](https://robertheaton.com/2018/11/28/https-in-the-real-world/) is not the best explanation of public key infrastructure on the internet. But it could be the best incomplete whirlwind tour of the nooks and crannies of TLS for people who currently only know what I told them in [“How does HTTPS actually work?](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)”
-   [“Programming Projects for Advanced Beginners”](https://robertheaton.com/ppab) is not the best way to learn programming. But if you’re looking for semi-guided projects that help you write complex programs without giving you too many hints then you could do a lot worse.

Many of my technical, explanatory posts have come from times when I had originally wanted to spend 30 minutes learning the basics of something. Finding no existing material targeted at whatever my specific level of knowledge and depth of interest happened to be, I instead spent 10 hours or more writing the post that I wish had been there already. These posts are by definition entering a relatively sparsely-populated market, which gives them a decent shot at being the best at what they do. For example:

-   I believe that [“How does Tor work?”](https://robertheaton.com/2019/04/06/how-does-tor-work/) is one of the better introductions to Tor for generalist programmers who currently know next-to-nothing about it. I tried to make it more detailed than almost everything that I read while I was researching it, but much less detailed than the Tor whitepaper.
-   I wrote [“The Wavefunction Collapse Algorithm explained very clearly”](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/) after watching [this video](https://www.youtube.com/watch?v=-W7zt8181Zo) about an infinite city generated using the algorithm. When I published the post at the end of 2018, I was relatively confident that it was the best introduction to the Wavefunction Collapse Algorithm in existence, period. Now I suspect that this made-up honor might belong to a newer post on [GridBugs.orgs](https://gridbugs.org/wave-function-collapse/). But even then it still all depends on the audience. “Best for who?” I think mine is probably better if you’re starting from no knowledge of procedural generation and are just interested in experimenting with a new toy. But GridBugs’s is better if you’re already familiar with this general class of algorithm and are planning on implementing Wavefunction Collapse in an efficient, scalable manner.
-   I wrote [“The Padding Oracle Attack”](https://robertheaton.com/2013/07/29/padding-oracle-attack/) while working through the [Matasano Crypto Challenges](https://cryptopals.com/). I don’t know if it really is the best explanation of the Padding Oracle Attack for first- or second-year Computer Science undergraduates, but it’s on the reading list for a lot of university courses so I imagine it’s up there.

Many of my more off-the-wall posts have come from times when I had found a topic that I thought was interesting, but for which I didn’t think I could write the best vanilla explanation on the internet for even a very specific audience. This might have been because the topic was too broad, too well-covered, too detail-dependent, or too controversial. I therefore sought out an oddball angle that didn’t require either the reader or the writer to have a PhD, but still added something to an interested reader’s Google-searching experience. In such posts I try to make it clear that I’m not being serious or intellectually rigorous through the use of wacky characters and an even wackier narrative, and my hope is that these posts come across as “thought-provoking” (which I believe is commentariat-speak for “I have not considered any of the details”). Some examples:

-   [“A brief history of wi-fi privacy vulnerabilities”](https://robertheaton.com/2019/01/15/a-brief-history-of-wi-fi-privacy-vulnerabilities/) - I didn’t think I could write the best detailed introduction to wi-fi privacy on the internet, because it’s too large of a field and too many well-researched papers and blog posts have been written about it already. However, I did think that I could make a good stab at a whimsical, twenty-thousand feet overview of the topic, aimed at broadly technical readers with no prior experience with the wi-fi protocol.
-   [“A zero-knowledge proof for the existence of God”](https://robertheaton.com/2017/11/13/a-zero-knowledge-proof-for-the-existence-of-god/) - zero-knowledge proofs are fascinating, but they’re also very subtle and detail-dependent. I’m scared of trying to write about them in case I say anything provably false. Nonetheless, while doing some background reading I came up with an idea for how God could use zero-knowledge proofs to provide mathematical evidence for his existence, without proving himself entirely. The idea doesn’t stand up to much scrutiny, but then again neither did _Inception_ and that still won four Oscars. I think that my post could have at least been nominated for “best story about zero-knowledge proofs, hand-wavy category, 2017”.
-   [“I might be Spartacus”](https://robertheaton.com/2018/10/28/i-might-be-spartacus-differential-privacy-marketplace/) - the subject of differential privacy is just as fascinating as that of zero-knowledge proofs, and just as easy to get wrong. Once again, I didn’t fancy my chances of writing the best explanation of differential privacy on the internet. However, I did dream up another vague idea about how differential privacy could be used to revolutionize consumer data protection and allow people to get paid for sharing their personal information. It was time for recurring character Hobert Reaton, sketchy Silicon Valley CEO, to make a comeback and present his new startup on a late-night TV talk show. The post made absolutely no claim to being accurate or having any practical application whatsoever, and I think it turned out well for it.

It doesn’t even matter whether or not a post does in fact turn out to be the best on the internet. [Often it won’t](https://robertheaton.com/2015/12/22/how-they-solved-true-detective-season-1/), but I still find the framing helpful for focus and motivation. I’m not writing for the advertising revenue, because I don’t get any. I’m writing for myself and for the satisfaction of clicks well-earned. There’s no point in me or you writing dreary clickbait unless it’s as a writing exercise, which come to think of it might actually be quite educational the first few times.

## 2\. The Netflix Principle

On an old episode of “The Exponent” podcast, host Ben Thompson points out that almost every show on Netflix has a very long shelf-life. Good dramas are watched by millions of people for years after they are first released. Even bad dramas are watched by thousands of people who don’t read reviews for a good few months. By contrast, most sports and news shows go stale after 24 hours, tops. Netflix’s focus on the former type of evergreen content means that every show that it adds to its catalog makes Netflix permanently better for every future subscriber. Even though its share price has been wobbling rather violently over the last year, this makes Netflix a big, unstoppable ball of continuously agglomerating value.

I don’t know if this is really how Netflix really thinks about their portfolio of shows, but it nicely encapsulates how I think about writing. I want every new post I publish to durably increase the amount of enjoyment that someone has access to while browsing through my archives, for at least the next 5 years. This explains why I’ll write about general concepts like self-hosting compilers, but rarely about specifics with a short shelf-life, like new features in Terraform 0.12.

Why do I care about this? The same reason I care about anything - a combination of vanity and a desire to be enduringly useful.

## Subject and Angle

I’ve said that I’m looking for ideas for posts that will stand the test of time (where time is defined as the next 5 years) and are sufficiently tight and well-targeted so as to be the best on the internet at something. That’s all very well in theory, but how does one come up with such ideas?

I like to think about post ideas in two parts:

-   Subject - what are you going to write about?
-   Angle - how are you going to write about it?

Let’s talk about each part in turn.

### Subject

First I decide which subject area to write about. I maintain an enormous list of hundreds of possible subjects, which contains:

-   Links to interesting Wikipedia pages (“Smipsons paradox https://en.wikipedia.org/wiki/Simpson%27s\_paradox” became [“Making Peace With Simpson’s Paradox”](https://robertheaton.com/2019/02/24/making-peace-with-simpsons-paradox/))
-   Links to blog posts (“Cool! https://blog.includesecurity.com/2014/02/how-i-was-able-to-track-location-of-any.html” became [“How Tinder keeps your exact location (a bit) private”](https://robertheaton.com/2018/07/09/how-tinder-keeps-your-location-a-bit-private/))
-   The names of a technical concept I heard about that I’d never come across before (“Something about RFID apartment keys??” could become “Something about RFID apartment keys, I don’t know, if I knew then I’d have written it already”)
-   The names of technical concepts I’ve heard of before but have never got round to understanding (“How does Tor work?” became [“How does Tor work?”](https://robertheaton.com/2019/04/06/how-does-tor-work/))
-   Ideas for an almost-always entirely hypothetical and impractical application of an algorithm (“Could use hashes of data to randomize RCTs?” became [“ROBERT: prove that your randomized trial really was random”](https://robertheaton.com/2019/03/17/robert-prove-that-your-randomized-trial-really-was-random/))
-   Explanations of something difficult I did at work (“Write about the LE migration” became [“Migrating bajillions of database records at Stripe”](https://robertheaton.com/2015/08/31/migrating-bajillions-of-database-records-at-stripe/))
-   Things that have happened to me that I think I could write compellingly about (“Write about Oscar” became [“Childbirth: a father’s-eye view”](https://robertheaton.com/2019/08/25/parenthood-3-oscar-heaton-quarterly-baby-review/))

A lot of the non-technical posts that I’ve written have come from writing down ideas or sentence fragments about a topic that I find interesting, and then eventually realizing that I’ve got enough of these fragments to form the kernel of a blog post ([“Oscar Heaton: Quarterly Baby Review”](https://robertheaton.com/2019/08/25/parenthood-3-oscar-heaton-quarterly-baby-review/), [“Lessons from my first 20 office hours”](https://robertheaton.com/2018/10/02/lessons-from-my-first-20-office-hours/), [“How to read”](https://robertheaton.com/2018/06/25/how-to-read/)). The key to good writing is to seamlessly stitch together these disparate fragments into a coherent tapestry. The key to quick writing is to slap together a listicle and call it a day.

### Angle

Once I’ve picked a subject area to write about, I still have to figure out how to write about it. Simply put, what’s the angle? For technical topics my default angle is “moderately-detailed introduction, written for a generalist computer programmer”. However, sometimes I don’t think I can or want to pull this off for a subject, which is when I go searching for alternatives like:

-   A how-to guide for some specific aspect of the subject ([“How to build a TCP proxy”](https://robertheaton.com/2018/08/31/how-to-build-a-tcp-proxy-1/))
-   A guide of some sort for “advanced beginner” programmers - people who know the basics of programming but aren’t sure where to find the skills they need to get to the next level ([“PPAB #6: User logins”](https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/))
-   A tongue-in-cheek musing about an off-the-wall way in which to look at the subject from a novel, if technically completely wrong angle ([“The Robot Reserve Army of Labor”](https://robertheaton.com/2019/03/31/the-robot-reserve-army-of-labor/))
-   A technical story that describes the thing in detail and might teach the reader a thing or two ([“Tracking friends and strangers using WhatsApp”](https://robertheaton.com/2017/10/09/tracking-friends-and-strangers-using-whatsapp/))
-   A non-technical story that requires no prior knowledge and teaches the reader nothing ([“Third-party dream cookies”](https://robertheaton.com/2019/01/27/third-party-dream-cookies/))

Non-technical blog posts need angles too:

-   A serious recommendation for how the reader should live their life ([“Why you should be vegetarian”](https://robertheaton.com/2014/04/18/why-you-should-be-vegetarian/))
-   A flippant recommendation for how the reader should live their life ([“Randomness-Driven Recruiting”](https://robertheaton.com/2016/07/05/improve-your-recruiting-using-math-rand/))
-   A personal history ([“I went to Skyrim, once”](https://robertheaton.com/2018/07/04/i-went-to-skyrim-once/))

An post’s angle can be almost anything, but once I know what it is I find it extremely useful to explicitly write it down. Knowing a post’s angle helps with deciding what information should go into it, and what can be skipped.

### Templates

Sometimes an angle, or a combination of an angle and a topic, is sufficiently successful and reproducible that I’ll reuse the entire thing, sometimes multiple times. Posts that reuse an existing template are often the most enjoyable to write, because the difficult questions of “what am I writing about?” and “how am I writing about it?” come pre-answered. I can think of at least 7 templates that I have reused, or intend to reuse in the future:

-   _The Steve Steveington Chronicles_ [(1)](https://robertheaton.com/2014/12/08/fun-with-your-friends-facebook-and-tinder-session-tokens/), [(2)](https://robertheaton.com/2016/10/22/a-tale-of-love-betrayal-social-engineering-and-whatsapp/), [(3)](https://robertheaton.com/2017/10/09/tracking-friends-and-strangers-using-whatsapp/), [(4)](https://robertheaton.com/2018/07/09/how-tinder-keeps-your-location-a-bit-private/), [(5)](https://robertheaton.com/2019/01/15/a-brief-history-of-wi-fi-privacy-vulnerabilities/) - the adventures of you and your good buddy, Steve Steveington. You use your knowledge of weird technical edge-cases to hack, trick, phish, and generally inconvenience your friend. Many of my non-programmer readers say “I didn’t understand any of the coding bits but I still enjoyed the rest of it,” which is exactly what I’m aiming for
-   _The many companies of Hobert Reaton, disreputable Silicon Valley CEO_ [(1)](https://robertheaton.com/2017/10/17/we-see-you-democratizing-de-anonymization/), [(2)](https://robertheaton.com/2018/10/28/i-might-be-spartacus-differential-privacy-marketplace/) - Hobert is forever coming up with new ways to siphon off his users’ data and cause mischief with it. I reach for him when I’ve got an idea for a caper that seems too large-scale for you and Steve Steveington to handle.
-   _Programming Projects for Advanced Beginners_ [(1)](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/), [(2)](https://robertheaton.com/2018/07/20/project-2-game-of-life/), [(3)](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/), [(4)](https://robertheaton.com/2018/11/03/programming-project-4-photomosaics/), [(5)](https://robertheaton.com/2018/12/02/programming-project-5-snake/), [(6)](https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/), [(7)](https://robertheaton.com/2019/07/27/programming-videos-for-advanced-beginners-battleships/) - semi-guided projects for people who know the basics of writing code and want to practice working on larger programs.
-   _Parenthood_ [(1)](https://robertheaton.com/2019/08/25/parenthood-3-oscar-heaton-quarterly-baby-review/), [(2)](https://robertheaton.com/2019/06/30/1-month-of-parenthood/), [(3)](https://robertheaton.com/2019/08/25/parenthood-3-oscar-heaton-quarterly-baby-review/) - I’ve been writing series of semi-connected vignettes about the first few months of my first child. Every time I think of a good line I email it to myself, and when I’ve got enough I string them all together and publish them. Sometimes this processes produces an elegant tapestry of life; sometimes it produces something that is essentially a listicle without the numbers. You take the rough with the smooth, and if you run out of sandpaper or patience then you just hit publish.
-   _10 somewhat advanced Magic: The Gathering plays_ [(1)](https://robertheaton.com/2016/09/03/ten-somewhat-advanced-magic-the-gathering-plays/), [(2)](https://robertheaton.com/2017/12/09/another-10-somewhat-advanced-magic-the-gathering-plays/) - similarly, whenever I think of or am shown a neat Magic: The Gathering Play, I email it to myself. Whenever I reach 10 plays I publish them as a new post. So far I’ve written “10 somewhat advanced Magic: The Gathering plays” and “Another 10 somewhat advanced Magic: The Gathering plays”. I have another 4 plays waiting in my inbox.
-   _Computer games_ [(1)](https://robertheaton.com/2018/07/04/i-went-to-skyrim-once/), [(2)](https://robertheaton.com/2018/09/07/what-playing-the-witness-will-teach-my-kid/), [(3)](https://robertheaton.com/2018/11/23/the-therapeutic-properties-and-applications-of-dark-souls/), [(4)](https://robertheaton.com/2019/03/07/how-to-get-to-silver-in-rocket-league-1-v-1/) - I’ve written about my experiences playing [Skyrim](https://robertheaton.com/2018/07/04/i-went-to-skyrim-once/), [The Witness](https://robertheaton.com/2018/09/07/what-playing-the-witness-will-teach-my-kid/), [Dark Souls](https://robertheaton.com/2018/11/23/the-therapeutic-properties-and-applications-of-dark-souls/), and [Rocket League](https://robertheaton.com/2019/03/07/how-to-get-to-silver-in-rocket-league-1-v-1/). They’re more personal reflections than reviews, and I don’t think they have a target audience. I would call them clickbait, but nobody clicks on them so I don’t think I’m legally allowed to.
-   _Writing_ [(1)](https://robertheaton.com/2014/07/26/lessons-from-a-surprisingly-successful-blog/), [(2)](https://robertheaton.com/2018/12/06/a-blogging-style-guide/) - I’ve written [“A blogging style guide”](https://robertheaton.com/2018/12/06/a-blogging-style-guide/) and [“Lessons from a surprisingly successful blog”](https://robertheaton.com/2014/07/26/lessons-from-a-surprisingly-successful-blog/), and now I’ve written the post that you’re reading right now too. [“A blogging style guide”](https://robertheaton.com/2018/12/06/a-blogging-style-guide/) was a 39-point listicle that became very popular, and I’ve been collecting new items for a second volume. So far I’m only at 11, but I’ll get there one day.

If you find something that works, keep doing it.

## Prompts

Some prompts to help you come up with post ideas:

-   Think of a topic that you learned about recently that was lacking on material targeted at you specifically. Write the post that would have saved you hours of Googling and head-scratching
-   Think of something that you learned how to do recently that required you to piece together several different sources. Write the single post that would have told you how to do it in one click
-   Whenever you’re learning about something new, think about whether there’s are any angles from which you could write about it
-   For whatever your field or interest is, write about how someone who has learned that basics but doesn’t know what to do next can keep improving
-   Read an End-User License Agreement (EULA). Write indignantly about the most egregious privacy invasions
-   Think of an offbeat idea for how to use an existing technique or process in a novel way, or how to apply it to a novel situation. If it’s not completely ridiculous, write about it with a straight face.
-   If it is completely ridiculous, write about it anyway but make it clearer that you’re mostly joking
-   Write about something that you did recently that caused you to have any thoughts that felt even slightly original
-   Write a short story related to your field or interest
-   Write a short story unrelated to your field or interest
-   Take an existing blog post that you enjoyed. Write about the same topic from a different angle, or a different topic from the same angle

## Conclusion

Every post that I’ve written has made it easier to write the next one. This is in part simply because the more you write, the better you get. But it’s also because writing more today makes it easier to find the time and energy to write more in the future, and writing more at any time increases your confidence, making you more likely to feel qualified to write even more and about a wider range of subjects (nb. on the internet there are actually no qualifications and you can already write about almost anything you want). I haven’t drawn the flow chart but I’m pretty sure there’s a virtuous circle in there somewhere.

So despite everything that I’ve just said, the best post to write is the one that you are able and excited to start writing immediately. Hopefully this post helps you methodically devise your own topics and angles, but any idea that you come up with is perfect if you can and want to begin work on it right now.