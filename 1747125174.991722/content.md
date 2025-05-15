> Links on the In­ter­net last for­ever or a year, whichever in­con­ve­niences you more. This is a major prob­lem for any­one se­ri­ous about writ­ing with good ref­er­ences, as link rot will crip­ple sev­eral per­cent of all links each year, and com­pound­ing.
> 
> To deal with link rot, I present my multi- pronged archival strat­egy using a com­bi­na­tion of scripts, dae­mons, and In­ter­net archival ser­vices: URLs are reg­u­larly dumped from both my web browser’s daily brows­ing and my web­site pages into an archival dae­mon I wrote, which pre- emptively down­loads copies lo­cally and at­tempts to archive them in the In­ter­net Archive. This en­sures a copy will be avail­able in­def­i­nitely from one of sev­eral sources. Link rot is then de­tected by reg­u­lar runs of `linkchecker`, and any newly dead links can be im­me­di­ately checked for al­ter­na­tive lo­ca­tions, or re­stored from one of the archive sources.
> 
> As an ad­di­tional flour­ish, my local archives are in case forgery is a con­cern, and I demon­strate a sim­ple com­pres­sion trick for [sub­stan­tially re­duc­ing sizes of large web archives ⁠](https://gwern.net/sort) such as crawls (par­tic­u­larly use­ful for re­peated crawls such as my [DNM archives ⁠](https://gwern.net/dnm-archive)).

Given my in­ter­est in [⁠long term con­tent ⁠](https://gwern.net/about#long-content) and ex­ten­sive link­ing, [link rot ⁠](https://en.wikipedia.org/wiki/Link_rot) is an issue of deep con­cern to me. I need back­ups not just for my files⁠ [1](#fn:1), but for the web pages I read and use—they’re all part of my [⁠ex­o­mind ⁠](https://en.wikipedia.org/wiki/Extended_mind_thesis#%22The_Extended_Mind%22). It’s not much good to have an ex­ten­sive essay on some topic where half the links are dead and the reader can nei­ther ver­ify my claims nor get con­text for my claims.

## Link Rot

> Decay is in­her­ent in all com­pound things. Work out your own sal­va­tion with dili­gence.
> 
> Last words of the Bud­dha

The di­men­sion of dig­i­tal decay is dis­mal and dis­tress­ing. [Wikipedia ⁠](https://en.wikipedia.org/wiki/Link_rot#Prevalence):

> In a 2003 22ya ex­per­i­ment, [et al 2003](https://www2003.org/cdrom/papers/refereed/p097/P97%20sources/p97-fetterly.html) dis­cov­ered that about one link out of every 200 dis­ap­peared each week from the In­ter­net. [Mc­Cown et al 2005 ⁠](https://arxiv.org/abs/cs/0511077) dis­cov­ered that half of the URLs cited in [D-Lib Mag­a­zine ⁠](https://en.wikipedia.org/wiki/D-Lib_Magazine) ar­ti­cles were no longer ac­ces­si­ble 10 years after pub­li­ca­tion [the irony!], and other stud­ies have shown link rot in aca­d­e­mic lit­er­a­ture to be even worse ([Spinel­lis, 2003 ⁠](https://www.spinellis.gr/pubs/jrnl/2003-CACM-URLcite/html/urlcite.pdf), [Lawrence et al 2001 ⁠](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.97.9695&rep=rep1&type=pdf)). [⁠Nel­son & Allen 2002](https://www.dlib.org/dlib/january02/nelson/01nelson.html) ex­am­ined link rot in dig­i­tal li­braries and found that about 3% of the ob­jects were no longer ac­ces­si­ble after one year.

[Bruce Schneier ⁠](https://en.wikipedia.org/wiki/Bruce_Schneier) re­marks that one friend ex­pe­ri­enced 50% linkrot in one of his pages over less than 9 years (not that the sit­u­a­tion was any bet­ter [⁠in 1998 ⁠](https://web.archive.org/web/19971015094640/http://www.pantos.org/atw/35654.html)), and that his own blog posts link to news ar­ti­cles that go dead in days⁠ [2](#fn:2); [⁠Vi­to­rio checks book­marks from 1997](https://notes.pinboard.in/u:vitorio/05dec9f04909d9b6edff), find­ing that hand- checking in­di­cates a total link rot of 91% with only half of the dead avail­able in sources like the In­ter­net Archive; [Ernie Smith found 1 semi- working link ⁠](https://www.vice.com/en/article/i-bought-a-book-about-the-internet-from-1994-and-none-of-the-links-worked/) in a 1994 31ya book about the In­ter­net; the [In­ter­net Archive ⁠](https://en.wikipedia.org/wiki/Internet_Archive) it­self has es­ti­mated the av­er­age lifes­pan of a Web page at [⁠100 days ⁠](https://web.archive.org/web/20080602034359/https://www.wired.com/culture/lifestyle/news/2001/10/47894). A _[Sci­ence ⁠](https://en.wikipedia.org/wiki/Science_\(journal\))_ study looked at ar­ti­cles in pres­ti­gious jour­nals; they didn’t use many In­ter­net links, but when they did, 2 years later ~13% were dead⁠ [3](#fn:3). The French com­pany Lin­ter­web stud­ied ex­ter­nal links on the [French Wikipedia ⁠](https://en.wikipedia.org/wiki/French_Wikipedia) be­fore set­ting up [their cache](https://wikiwix.com/) of French ex­ter­nal links, and found—back in 2008 17ya —al­ready [5% were dead ⁠](https://fr.wikipedia.org/wiki/Utilisateur:Pmartin/Cache). (The Eng­lish Wikipedia has seen a 2010–Jan­u­ary 2011 14ya spike from a few thou­sand dead links to [⁠~110,000 ⁠](https://gwern.net/doc/wikipedia/2011-01-wikipedia-articleswithdeadexternallinks.png) out of [~17.5m live links ⁠](https://en.wikipedia.org/wiki/Wikipedia_talk:WikiProject_External_links/Webcitebot2#Summary).) [⁠A fol­lowup check ⁠](https://lil.law.harvard.edu/blog/2017/07/21/a-million-squandered-the-million-dollar-homepage-as-a-decaying-digital-artifact/) of the viral [The Mil­lion Dol­lar Home­page ⁠](https://en.wikipedia.org/wiki/The_Million_Dollar_Homepage), where it cost up to $62 $38 2006 k to in­sert a link by the last in­ser­tion on Jan­u­ary 2006 19ya, found that a decade later in 2017, at least half the links were dead or squat­ted.⁠ [4](#fn:4) Book­mark­ing web­site [Pin­board ⁠](https://en.wikipedia.org/wiki/Pinboard_\(website\)), which pro­vides some archiv­ing ser­vices, [noted in Au­gust 2014 ⁠](https://x.com/pinboard/status/501406303747457024) that 17% of 3- year-old links & 25% of 5- year-old links were dead. The dis­mal [stud­ies ⁠](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253) [just ⁠](https://academic.oup.com/jnci/article/96/12/969/2520849) [go ⁠](https://gwern.net/doc/cs/linkrot/2007-dimitrova.pdf) [on ⁠](https://gwern.net/doc/cs/linkrot/2008-wren.pdf) [and ⁠](https://gwern.net/doc/cs/linkrot/2006-wren.pdf) [on ⁠](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2213465/) [and ⁠](https://pdfs.semanticscholar.org/1ae0/d55d0af02cdd77a3147c4f652bf4e3749194.pdf) [on ⁠](https://onlinelibrary.wiley.com/doi/full/10.1096/fj.05-4784lsf) ([and ⁠](https://gwern.net/doc/cs/linkrot/2012-moghaddam.pdf) [on ⁠](https://gwern.net/doc/cs/linkrot/archiving/2014-zittrain.pdf)). Even in a highly sta­ble, funded, cu­rated en­vi­ron­ment, link rot hap­pens any­way. For ex­am­ple, about [11% of Arab Spring- related tweets ⁠](https://arxiv.org/abs/1209.3026) were gone within a year (even though Twit­ter is—cur­rently—still around). And some­times they just get qui­etly lost, like when My­Space ad­mit­ted it lost [⁠all music world­wide up­loaded 2003 – 12 2015 ⁠](https://www.reddit.com/r/techsupport/comments/7uiv8b/myspace_player_wont_play_songs_and_i_want_to/#t1_e1n8hzn), eu­phemisti­cally de­scrib­ing the mass dele­tion as [⁠“We com­pletely re­built My­Space and de­cided to move over _some_ of your con­tent from the old My­Space” ⁠](https://web.archive.org/web/20150905205955/https://help.myspace.com/hc/en-us/articles/202233310-Where-Is-All-My-Old-Stuff-) (em­pha­sis added; only some of the 2008–2010 15ya My­Space music could be res­cued & put on the IA by [⁠“an anony­mous aca­d­e­mic study” ⁠](https://archive.org/details/myspace_dragon_hoard_2010)).

Worlds are al­ways end­ing. If you get any­thing out of read­ing his­tory or an­thro­pol­ogy, it should be that: it’s al­ways the apoc­a­lypse some­where for some­one. What comes after each apoc­a­lypse may be bet­ter or worse, but nev­er­the­less, it comes. Every­thing that is solid will one day melt into thin air, and noth­ing you value—the things you will miss, the small­est every­day de­tails of life, your se­cret rit­u­als and pri­vate jokes, the odd thoughts that cur and recur, those things of beauty not writ­ten in any book—none of that will sur­vive on its own, will be lost and for­got­ten, and if you don’t pre­serve it, prob­a­bly no one else will ei­ther. You may not care about that, and that is your choice. Your time can be well- spent oth­er­wise. But if you do, you should know that: worlds are al­ready end­ing, and in an im­por­tant sense, yours al­ready has, it just takes a while.

## Linkrot Quantities

My spe­cific tar­get date is 2070, 60 years from now. As of 2011-03-10, Gwern.net has around 6,800 ex­ter­nal links (with around 2,200 to non- Wikipedia web­sites)⁠ [5](#fn:5). Even at the low­est es­ti­mate of 3% an­nual linkrot, few will sur­vive to 2070. If each link has a 97% chance of sur­viv­ing each year, then the chance a link will be alive in 2070 is 0.97 2070 − 2011 ≈ 0.16 (or to put it an­other way, an 84% chance any given link _will_ die). The 95% [con­fi­dence in­ter­val ⁠](https://en.wikipedia.org/wiki/Confidence_interval) for such a [bi­no­mial dis­tri­b­u­tion ⁠](https://en.wikipedia.org/wiki/Binomial_distribution) says that of the 2,200 non- Wikipedia links, ~336–394 will sur­vive to 2070⁠ [6](#fn:6). If we try to pre­dict using a more rea­son­able es­ti­mate of 50% linkrot, then an av­er­age of 0 links will sur­vive (0.50 2070-2011 × 2,200 = 1.735 × 10 -16 × 2,200 ≈ 0). It would be a good idea to sim­ply as­sume that _no_ link will sur­vive.

With that in mind, one can con­sider reme­dies. (If we lie to our­selves and say it won’t be a prob­lem in the fu­ture, then we guar­an­tee that it _will_ be a prob­lem. )

If you want to _pre- emptively_ archive a spe­cific page, that is easy: go to the IA and archive it, or in your web browser, print a PDF of it, or for more com­plex pages, use a browser plu­gin (eg. [Scrap­Book ⁠](https://github.com/danny0838/firefox-scrapbook/wiki/Features)). But I find I visit and link so many web pages that I rarely think in ad­vance of link rot to save a copy; what I need is a more sys­tem­atic ap­proach to de­tect and cre­ate links for all web pages I might need.

## Detection

> With every new spring
> 
> the blos­soms speak not a word
> 
> yet ex­pound the Law—
> 
> know­ing what is at its heart
> 
> by the scat­ter­ing storm winds.
> 
> Shōtetsu⁠ [7](#fn:7)

The first rem­edy is to learn about bro­ken links as soon as they hap­pen, which al­lows one to react quickly and scrape archives or search en­gine caches ([‘lazy preser­va­tion’ ⁠](https://www.cs.odu.edu/~mln/pubs/widm-2006/lazyp-widm06.pdf)). I cur­rently use [`linkchecker` ⁠](https://github.com/linkchecker/linkchecker) to spi­der Gwern.net look­ing for bro­ken links. `linkchecker` is run in a [cron ⁠](https://en.wikipedia.org/wiki/Cron) job like so:

```
@monthly linkchecker --check-extern --timeout=35 --no-warnings --file-output=html \
                      --ignore-url=^mailto --ignore-url=^irc --ignore-url=http://.*\.onion \
                      --ignore-url=paypal.com --ignore-url=web.archive.org \
                     https://gwern.net
```

Just this com­mand would turn up many false pos­i­tives. For ex­am­ple, there would be sev­eral hun­dred warn­ings on Wikipedia links be­cause I link to redi­rects; and `linkchecker` re­spects [ro­bots.txts ⁠](https://en.wikipedia.org/wiki/Robots.txt) which for­bid it to check live­ness, but emits a warn­ing about this. These can be sup­pressed by edit­ing `~/.linkchecker/linkcheckerrc` to say `ignorewarnings=http-moved-permanent,http-robots-denied` (the avail­able warn­ing classes are listed in `linkchecker -h`).

The quicker you know about a dead link, the sooner you can look for re­place­ments or its new home.

## Prevention

## Remote Caching

> Any­thing you post on the in­ter­net will be there as long as it’s em­bar­rass­ing and gone as soon as it would be use­ful.⁠ [8](#fn:8)
> 
> [⁠taejo ⁠](https://news.ycombinator.com/item?id=21270467)

We can ask a third party to keep a cache for us. There are sev­eral [archive site ⁠](https://en.wikipedia.org/wiki/Archive_site) pos­si­bil­i­ties:

1.  the [In­ter­net Archive ⁠](https://en.wikipedia.org/wiki/Internet_Archive)
    
2.  [We­bCite ⁠](https://en.wikipedia.org/wiki/WebCite)
    
3.  [Perma.cc](https://perma.cc/) ([highly lim­ited ⁠](https://archive.blogs.harvard.edu/perma/2019/01/07/introducing-individual-account-subscription-tiers-for-perma/); has [lost some archives ⁠](https://arxiv.org/abs/2108.05939))
    
4.  Lin­ter­web’s Wiki­Wix⁠ [9](#fn:9).
    
5.  Peeep.us (de­funct as of 2018)
    
6.  [Archive.is ⁠](https://archive.is/)
    
7.  [⁠Pin­board](https://pinboard.in/) (with the $27 $22 2021 / year archiv­ing op­tion⁠ [10](#fn:10))
    

There are other op­tions but they are not avail­able like Google⁠ [11](#fn:11) or var­i­ous com­mer­cial/ gov­ern­ment archives⁠ [12](#fn:12)

(An ex­am­ple would be [`⁠bits.blogs.nytimes.com/2010/12/07/palm-is-far-from-game-over-says-former-chief/` ⁠](https://archive.nytimes.com/bits.blogs.nytimes.com/2010/12/07/palm-is-far-from-game-over-says-former-chief/) being archived at [`⁠webcitation.org/5ur7ifr12` ⁠](https://webcitation.org/5ur7ifr12).)

These archives are also good for archiv­ing your own web­site:

1.  you may be keep­ing back­ups of it, but your own web­site/ server back­ups can be lost (I can speak from per­sonal ex­pe­ri­ence here), so it’s good to have ex­ter­nal copies
    
2.  An­other ben­e­fit is the re­duc­tion in ‘bus- factor’: if you were hit by a bus to­mor­row, who would get your archives and be able to main­tain the web­sites and un­der­stand the back­ups etc? While if archived in IA, peo­ple al­ready know how to get copies and there are tools to down­load en­tire do­mains.
    
3.  A focus on back­ing up only one’s web­site can blind one to the need for archiv­ing the _ex­ter­nal links_ as well. Many pages are mean­ing­less or less valu­able with bro­ken links. A linkchecker script/ dae­mon can also archive all the ex­ter­nal links.
    

So there are sev­eral ben­e­fits to doing web archiv­ing be­yond sim­ple server back­ups.

My first pro­gram in this vein of thought was a bot which fired off We­bCite, In­ter­net Archive/ Alexa, & Archive.is re­quests: [Wikipedia Archiv­ing Bot ⁠](https://gwern.net/haskell/wikipedia-archive-bot), quickly fol­lowed up by a [RSS ver­sion ⁠](https://gwern.net/haskell/wikipedia-rss-archive-bot). (Or you could in­stall the [Alexa Tool­bar ⁠](https://en.wikipedia.org/wiki/Alexa_Internet#Toolbar) to get au­to­matic sub­mis­sion to the In­ter­net Archive, if you have ceased to care about pri­vacy.)

The core code was quickly adapted into a [⁠gitit ⁠](https://hackage.haskell.org/package/gitit) wiki plu­gin which hooked into the save- page func­tion­al­ity and tried to archive every link in the newly- modified page, [In­ter­wiki.hs ⁠](https://github.com/jgm/gitit/blob/master/plugins/Interwiki.hs)

Fi­nally, I wrote [⁠archiver ⁠](https://hackage.haskell.org/package/archiver), a dae­mon which watches⁠ [13](#fn:13) / reads a text file. Source is avail­able via `git clone https://github.com/gwern/archiver-bot.git`. (A sim­i­lar tool is [Archiveror ⁠](https://github.com/rahiel/archiveror); the Python pack­age [`archivenow` ⁠](https://github.com/oduwsdl/archivenow) does some­thing sim­i­lar & as of Jan­u­ary 2021 is prob­a­bly bet­ter.)

The li­brary half of `archiver` is a sim­ple wrap­per around the ap­pro­pri­ate HTTP re­quests; the ex­e­cutable half reads a spec­i­fied text file and loops as it (slowly) fires off re­quests and deletes the ap­pro­pri­ate URL.

That is, `archiver` is a dae­mon which will process a spec­i­fied text file, each line of which is a URL, and will one by one re­quest that the URLs be archived or spi­dered

Usage of `archiver` might look like `archiver ~/.urls.txt gwern@gwern.net`. In the past, `archiver` would some­times crash for un­known rea­sons, so I usu­ally wrap it in a `while` loop like so: `while true; do archiver ~/.urls.txt gwern@gwern.net; done`. If I wanted to put it in a de­tached [GNU screen ⁠](https://en.wikipedia.org/wiki/GNU_Screen) ses­sion: `screen -d -m -S "archiver" sh -c 'while true; do archiver ~/.urls.txt gwern@gwern.net; done'`. Fi­nally, rather than start it man­u­ally, I use a cron job to start it at boot, for a final in­vo­ca­tion of

```
@reboot sleep 4m && screen -d -m -S "archiver" sh -c 'while true; do archiver ~/.urls.txt \
        "cd ~/www && nice -n 20 ionice -c3 wget --unlink --limit-rate=20k --page-requisites --timestamping \
        -e robots=off --reject .iso,.exe,.gz,.xz,.rar,.7z,.tar,.bin,.zip,.jar,.flv,.mp4,.avi,.webm \
        --user-agent='Firefox/4.9'" 500; done'
```

## Local Caching

Re­mote archiv­ing, while con­ve­nient, has a major flaw: the archive ser­vices can­not keep up with the growth of the In­ter­net and are woe­fully in­com­plete. I ex­pe­ri­ence this reg­u­larly, where a link on Gwern.net goes dead and I can­not find it in the In­ter­net Archive or We­bCite, and it is a gen­eral phe­nom­e­non: [Ainsworth et al 2012 ⁠](https://arxiv.org/abs/1212.6177) find <35% of com­mon Web pages ever copied into an archive ser­vice, and typ­i­cally only one copy ex­ists.

### Caching Proxy

The most am­bi­tious & total ap­proach to local caching is to set up a proxy to do your brows­ing through, and record lit­er­ally all your web traf­fic; for ex­am­ple, using [Live Archiv­ing Proxy (LAP) ⁠](https://github.com/INA-DLWeb/LiveArchivingProxy) or [War­cProxy ⁠](https://github.com/odie5533/WarcProxy) which will save as [WARC files ⁠](https://en.wikipedia.org/wiki/WARC_\(file_format\)) every page you visit through it. ([⁠Zachary Vance](https://blog.za3k.com/archiving-all-web-traffic/) ex­plains how to set up a local HTTPS cer­tifi­cate to MITM your HTTPS brows­ing as well.)

One may be re­luc­tant to go this far, and pre­fer some­thing lighter- weight, such as pe­ri­od­i­cally ex­tract­ing a list of vis­ited URLs from one’s web browser and then at­tempt­ing to archive them.

### Batch Job Downloads

For a while, I used a shell script named, imag­i­na­tively enough, `local-archiver`:

```
#!/bin/sh
set -euo pipefail
 
cp `find ~/.mozilla/ -name "places.sqlite"` ~/
sqlite3 places.sqlite "SELECT url FROM moz_places, moz_historyvisits \
                       WHERE moz_places.id = moz_historyvisits.place_id \
                             and visit_date > strftime('%s','now','-1.5 month')*1000000 ORDER by \
                       visit_date;" | filter-urls >> ~/.tmp
rm ~/places.sqlite
split -l500 ~/.tmp ~/.tmp-urls
rm ~/.tmp
 
cd ~/www/
for file in ~/.tmp-urls*;
 do (wget --unlink --continue --page-requisites --timestamping --input-file $file && rm $file &);
done
 
find ~/www -size +4M -delete
```

The code is not the pret­ti­est, but it’s fairly straight­for­ward:

1.  the script grabs my Fire­fox brows­ing his­tory by ex­tract­ing it from the his­tory SQL data­base file⁠ [14](#fn:14), and feeds the URLs into [wget ⁠](https://en.wikipedia.org/wiki/Wget).
    
    `wget` is not the best tool for archiv­ing as it will not run JavaScript or [Flash ⁠](https://en.wikipedia.org/wiki/Adobe_Flash) or down­load videos etc. It will down­load in­cluded JS files but the JS will be ob­so­lete when run in the fu­ture and any dy­namic con­tent will be long gone. To do bet­ter would re­quire a head­less browser like [Phan­tomJS ⁠](https://en.wikipedia.org/wiki/PhantomJS) which saves to MHT/ MHTML, but Phan­tomJS [re­fuses to sup­port it ⁠](https://github.com/ariya/phantomjs/issues/10117) and I’m not aware of an ex­ist­ing pack­age to do this. In prac­tice, sta­tic con­tent is what is most im­por­tant to archive, most JS is of highly ques­tion­able value in the first place, and any im­por­tant YouTube videos can be archived man­u­ally with `youtube-dl`, so `wget` ’s lim­i­ta­tions haven’t been so bad.
    
2.  The script `split` s the long list of URLs into a bunch of files and runs that many `wget` s in par­al­lel be­cause `wget` ap­par­ently has no way of si­mul­ta­ne­ously down­load­ing from mul­ti­ple do­mains. There’s also the chance of `wget` hang­ing in­def­i­nitely, so par­al­lel down­loads con­tin­ues to make progress.
    
3.  The [`⁠filter-urls` ⁠](https://gwern.net/archiving#filter-urls) com­mand is an­other shell script, which re­moves URLs I don’t want archived. This script is a hack which looks like this:
    
    ```
    #!/bin/sh
    set -euo pipefail
    cat /dev/stdin | sed -e "s/#.*//" | sed -e "s/&sid=.*$//" | sed -e "s/\/$//" | grep -v -e 4chan -e reddit ...
    ```
    
4.  delete any par­tic­u­larly large (>4MB) files which might be media files like videos or au­dios (pod­casts are par­tic­u­lar of­fend­ers)
    

A local copy is not the best re­source—what if a link goes dead in a way your tool can­not de­tect so you don’t _know_ to put up your copy some­where? But it solves the prob­lem de­ci­sively.

The down­side of this script’s batch ap­proach soon be­came ap­par­ent to me:

1.  not au­to­matic: you have to re­mem­ber to in­voke it and it only pro­vides a sin­gle local archive, or if you in­voke it reg­u­larly as a cron job, you may cre­ate lots of du­pli­cates.
    
2.  un­re­li­able: `wget` may hang, URLs may be archived too late, it may not be in­voked fre­quently enough, >4MB non- video/ audio files are in­creas­ingly com­mon…
    
3.  I wanted copies in the In­ter­net Archive & else­where as well to let other peo­ple ben­e­fit and pro­vide re­dun­dancy to my local archive
    

It was to fix these prob­lems that I began work­ing on `archiver` —which would run con­stantly archiv­ing URLs in the back­ground, archive them into the IA as well, and be smarter about media file down­loads. It has been much more sat­is­fac­tory.

### Daemon

`archiver` has an extra fea­ture where any third ar­gu­ment is treated as an ar­bi­trary `sh` com­mand to run after each URL is archived, to which is ap­pended said URL. You might use this fea­ture if you wanted to load each URL into Fire­fox, or ap­pend them to a log file, or sim­ply down­load or archive the URL in some other way.

For ex­am­ple, in­stead of a big `local-archiver` run, I have `archiver` run `wget` on each in­di­vid­ual URL: `screen -d -m -S "archiver" sh -c 'while true; do archiver ~/.urls.txt gwern@gwern.net "cd ~/www && wget --unlink --continue --page-requisites --timestamping -e robots=off --reject .iso,.exe,.gz,.xz,.rar,.7z,.tar,.bin,.zip,.jar,.flv,.mp4,.avi,.webm --user-agent='Firefox/3.6' 120"; done'`. (For pri­vate URLs which re­quire lo­gins, such as [⁠dark­net mar­kets ⁠](https://gwern.net/dnm-archive#how-to-crawl-markets), `wget` can still grab them with some help: in­stalling the Fire­fox ex­ten­sion [Ex­port Cook­ies ⁠](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/), log­ging into the site in Fire­fox like usual, ex­port­ing one’s `cookies.txt`, and adding the op­tion `--load-cookies cookies.txt` to give it ac­cess to the cook­ies.)

Al­ter­nately, you might use [`curl` ⁠](https://en.wikipedia.org/wiki/CURL) or a spe­cial­ized archive down­loader like the In­ter­net Archive’s crawler [Her­itrix ⁠](https://github.com/internetarchive/heritrix3/wiki).

### Resource Consumption

The space con­sumed by such a backup is not that bad; only 30–50 gi­ga­bytes for a year of brows­ing, and less de­pend­ing on how hard you prune the down­loads. (More, of course, if you use `linkchecker` to archive en­tire sites and not just the pages you visit.) Stor­ing this is quite vi­able in the long term; while page sizes have [⁠in­creased 7×](https://www.websiteoptimization.com/speed/tweak/average-web-page/) be­tween 2003 22ya and 2011 14ya and pages av­er­age around 400kb⁠ [15](#fn:15), [Kry­der’s law ⁠](https://en.wikipedia.org/wiki/Mark_Kryder#Kryder%27s_law_projection) has also been op­er­at­ing and has in­creased disk ca­pac­ity by ~128×—in 2011 14ya, $124 $80 2011 will buy you at least [⁠2 ter­abytes](https://forre.st/storage#hdd), that works out to 4 cents a gi­ga­byte or 80 cents for the low es­ti­mate for down­loads; that is much bet­ter than the an­nual fee that some­where like [⁠Pin­board](https://pinboard.in/upgrade/) charges. Of course, you need to back this up your­self. We’re rel­a­tively for­tu­nate here—most In­ter­net doc­u­ments are ‘born dig­i­tal’ and easy to mi­grate to new for­mats or in­spect in the fu­ture. We can down­load them and worry about how to view them only when we need a par­tic­u­lar doc­u­ment, and Web browser backwards- compatibility al­ready stretches back to files writ­ten in the early 1990s. (Of course, we’re prob­a­bly screwed if we dis­cover the con­tent we wanted was dy­nam­i­cally pre­sented only in Adobe Flash or as an in­ac­ces­si­ble ‘cloud’ ser­vice.) In con­trast, if we were try­ing to pre­serve pro­grams or soft­ware li­braries in­stead, we would face a much more for­mi­da­ble task in keep­ing a work­ing lad­der of binary- compatible vir­tual ma­chines or in­ter­preters⁠ [16](#fn:16). The sit­u­a­tion with [⁠dig­i­tal movie preser­va­tion](https://www.davidbordwell.net/blog/2012/02/13/pandoras-digital-box-pix-and-pixels/) hardly bears think­ing on.

There are ways to cut down on the size; if you tar it all up and run [7-Zip ⁠](https://en.wikipedia.org/wiki/7-Zip) with max­i­mum com­pres­sion op­tions, you could prob­a­bly com­pact it to 1⁄5 th the size. I found that the un­com­pressed files could be re­duced by around 10% by using [fdupes ⁠](https://en.wikipedia.org/wiki/Fdupes) to look for du­pli­cate files and turn­ing the du­pli­cates into a space- saving [hard link ⁠](https://en.wikipedia.org/wiki/Hard_link) to the orig­i­nal with a com­mand like `fdupes --recurse --hardlink ~/www/`. (Ap­par­ently there are a _lot_ of bit- identical JavaScript (eg. [JQuery ⁠](https://en.wikipedia.org/wiki/JQuery)) and im­ages out there.)

Good fil­ter­ing of URL sources can help re­duce URL archiv­ing count by a large amount. Ex­am­in­ing my man­ual back­ups of Fire­fox brows­ing his­tory, over the 1153 days from 2014-02-25 to 2017-04-22, I vis­ited 2,370,111 URLs or 2055 URLs per day; after pass­ing through my fil­ter­ing script, that leaves 171,446 URLs, which after de- duplication yields 39,523 URLs or ~34 unique URLs per day or 12,520 unique URLs per year to archive.

This shrunk my archive by 9GB from 65GB to 56GB, al­though at the cost of some archiv­ing fi­delity by re­mov­ing many file­types like CSS or JavaScript or GIF im­ages. As of 2017-04-22, after ~6 years of archiv­ing, be­tween `xz` com­pres­sion (at the cost of easy search­a­bil­ity), ag­gres­sive fil­ter­ing, oc­ca­sional man­ual dele­tion of overly bulky do­mains I feel are prob­a­bly ad­e­quately cov­ered in the IA etc, my full WWW archives weigh 55GB.

### URL Sources

#### Browser History

There are a num­ber of ways to pop­u­late the source text file. For ex­am­ple, I have a script `firefox-urls`:

```
#!/bin/sh
set -euo pipefail
 
cp --force `find ~/.mozilla/firefox/ -name "places.sqlite"|sort|head -1` ~/
sqlite3 -batch places.sqlite "SELECT url FROM moz_places, moz_historyvisits \
                       WHERE moz_places.id = moz_historyvisits.place_id and \
                       visit_date > strftime('%s','now','-1 day')*1000000 ORDER by \
                       visit_date;" | filter-urls
rm ~/places.sqlite
```

(`filter-urls` is the same script as in `local-archiver`. If I don’t want a do­main lo­cally, I’m not going to bother with re­mote back­ups ei­ther. In fact, be­cause of We­bCite’s rate- limiting, `archiver` is al­most per­pet­u­ally back- logged, and I _es­pe­cially_ don’t want it wast­ing time on worth­less links like [4chan ⁠](https://en.wikipedia.org/wiki/4chan).)

This is called every hour by `cron`:

```
@hourly firefox-urls >> ~/.urls.txt
```

This gets all vis­ited URLs in the last time pe­riod and prints them out to the file for archiver to process. Hence, every­thing I browse is backed- up through `archiver`.

Non- Firefox browsers can be sup­ported with sim­i­lar strate­gies; for ex­am­ple, Zachary Vance’s Chromium scripts like­wise ex­tracts URLs from Chromium’s [SQL his­tory ⁠](https://github.com/za3k/rip-chrome-history) & [book­marks ⁠](https://github.com/za3k/export-chrome-bookmarks).

#### Document Links

More use­ful per­haps is a script to ex­tract ex­ter­nal links from [Mark­down ⁠](https://en.wikipedia.org/wiki/Markdown) files and print them to stan­dard out: [`⁠link-extractor.hs` ⁠](https://gwern.net/static/build/link-extractor.hs)

So now I can take `find . -name "*.md"`, pass the 100 or so Mark­down files in my wiki as ar­gu­ments, and add the thou­sand or so ex­ter­nal links to the archiver queue (eg. `find . -name "*.md" -type f -print0 | xargs -0 ~/wiki/static/build/link-extractor.hs | filter-urls >> ~/.urls.txt`); they will even­tu­ally be archived/ backed up.

#### Website Spidering

Some­times a par­tic­u­lar web­site is of long- term in­ter­est to one even if one has not vis­ited _every_ page on it; one could man­u­ally visit them and rely on the pre­vi­ous Fire­fox script to dump the URLs into `archiver` but this isn’t al­ways prac­ti­cal or time- efficient. `linkchecker` in­her­ently spi­ders the web­sites it is turned upon, so it’s not a sur­prise that it can build a [site map ⁠](https://en.wikipedia.org/wiki/Site_map) or sim­ply spit out all URLs on a do­main; un­for­tu­nately, while `linkchecker` has the abil­ity to out­put in a re­mark­able va­ri­ety of for­mats, it can­not sim­ply out­put a newline- delimited list of URLs, so we need to post- process the out­put con­sid­er­ably. The fol­low­ing is the shell one- liner I use when I want to archive an en­tire site (note that this is a bad com­mand to run on a large or heav­ily hyper- linked site like the Eng­lish Wikipedia or [⁠Less­Wrong ⁠](https://www.lesswrong.com/)!); edit the tar­get do­main as nec­es­sary:

```
linkchecker --check-extern -odot --complete -v --ignore-url=^mailto --no-warnings http://www.longbets.org
    | grep -F http #
    | grep -F -v -e "label=" -e "->" -e '" [' -e '" ]' -e "/ "
    | sed -e "s/href=\"//" -e "s/\",//" -e "s/ //"
    | filter-urls
    | sort --unique >> ~/.urls.txt
```

When `linkchecker` does not work, one al­ter­na­tive is to do a `wget --mirror` and ex­tract the URLs from the file­names—list all the files and pre­fix with a “http:// ” etc.

## Fixing Redirects

[Redi­rected URLS ⁠](https://en.wikipedia.org/wiki/URL_redirection) (pri­mar­ily [HTTP 301 ⁠](https://en.wikipedia.org/wiki/HTTP_301)) are not hard to fix, and are worth treat­ing as bro­ken links and up­dat­ing/ fix­ing:

1.  redi­rects are **bro­ken links in dis­guise**:
    
    This is par­tic­u­larly ob­vi­ous when every URL is redi­rected to a home­page or error page be­cause they were too lazy to set up the cor­rect redi­rects and de­cide to lie by mask­ing the un­der­ly­ing 404 error. Some bro­ken redi­rects are sub­tler and use longer URLs, but can be spot­ted by read­ing the final URL: often there will be a tell- tale word or pa­ra­me­ter like `paywall` or `accessDenied` or `?cookie=missing`. (It would be hard to de­tect these au­to­mat­i­cally by any content- based so­lu­tion be­cause they are site- specific, con­stantly chang­ing, and in many cases pre­serve a ‘teaser’ or ab­stract, and sim­ply hide the rest.)
    
2.  redi­rects are **pre­lude to link break­ing**:
    
    Redi­rects sig­nal changes in a web­site, and on the In­ter­net, change is usu­ally for the worse. Many do­main moves, `www` → naked sub­do­main, or HTTP → HTTPS mi­gra­tions will main­tain redi­rects for a time, and then a later change will break them. (I don’t know if the web­mas­ters in ques­tion re­gard the in­terim as ‘ad­e­quate time to fix’ or if later changes make it hard to main­tain the redi­rect.) The ‘new’ web­page may be sub­stan­tially dif­fer­ent (as­sets like im­ages are fre­quently bro­ken in mi­gra­tions) and needs to be checked to see if it is de facto dead. (This is es­pe­cially true of Wikipedia ar­ti­cles: when a page is ‘redi­rected’ or ‘merged’, it usu­ally [comes out the worse ⁠](https://gwern.net/inclusionism).) Redi­rects risk bugs when part of a page’s in­fra­struc­ture: if a re­source is sup­posed to be loaded over HTTP but gets redi­rected by a site- wide redi­rect to HTTPS, say, or vice- versa, then a web browser may kill the re­quest for se­cu­rity rea­sons, per­ma­nently break­ing what­ever that re­source does. The new do­main may be a spam­mer do­main, who has pur­chased it to ex­ploit you & your read­ers’ in­bound traf­fic. Some­times an old do­main will be aban­doned en­tirely and all its redi­rects break in­stantly.
    
3.  Redi­rects cause **am­bigu­ous, com­plex, & re­dun­dant names**:
    
    If one links a URL and also a redi­rect to the URL, even stip­u­lat­ing that the redi­rect never breaks, this causes a wide va­ri­ety of prob­lems.
    
    Broadly: one will not get the ben­e­fits of the browser high­light­ing an already- visited link, so one may waste time click­ing on a known ref­er­ence. If one searches the cor­pus for one URL, they will miss the other hits. If one fixes a bro­ken URL, one hasn’t fixed the redi­rects to that bro­ken URL & they re­main bro­ken. It is harder _to_ fix bro­ken URLs in the first place: you might find that it’s not archived under one URL but an archive ex­ists under the _other_ URL, if only you knew to check.⁠ [17](#fn:17) One (and one’s read­ers) may check the cor­pus for a ref­er­ence & copy an out­dated URL else­where like a com­ment, set­ting that com­ment up for all these prob­lems down the line.
    
    Redi­rects in­ter­fere with many Gwern.net fea­tures: with my local archives & an­no­ta­tions, use of mul­ti­ple URLs causes glitches: be­yond the missing- archives, I might write a high- quality an­no­ta­tion for one URL while the other URL has no an­no­ta­tion or just an au­to­matic (low- quality) an­no­ta­tion, or they might be the same an­no­ta­tion but di­verge over time. Re­dun­dant en­tries cause is­sues with the similar- links rec­om­men­da­tions, be­cause of course if one ver­sion is sim­i­lar to some other an­no­ta­tion, then the other ver­sions will be near- identically sim­i­lar. Use of re­dun­dant names also in­creases the risk of ac­ci­den­tally set­ting up redi­rect loops or redi­rect­ing to the wrong place. It clut­ters my link- checking re­ports, hid­ing bro­ken links & bugs in other fea­tures (eg. there might be a bug where Gwern.net sys­tem­at­i­cally gen­er­ates the wrong links, which are fixed by redi­rects, hid­ing the bug, but re­main­ing vis­i­ble in link- checking re­ports—if it’s not buried under a ton of other redi­rects or er­rors). It can break tools like `curl` which by de­fault won’t fol­low redi­rects (be­cause that might be dan­ger­ous or wrong), and archiv­ing tools may not work. The final URL/ do­main may act dif­fer­ently from the orig­i­nal (eg. it might set dif­fer­ent [`X-Frame-Options` ⁠](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) head­ers, break­ing my [⁠live- link func­tion­al­ity ⁠](https://gwern.net/static/build/LinkLive.hs), as is es­pe­cially likely given that newer web soft­ware tends to dis­able as much as pos­si­ble—‘change is bad’, see #2).
    
    None of these are _major_ prob­lems, but each one is a paper- cut which comes up more & more the larger & more com­plex the Gwern.net cor­pus & web­site get. So it helps to squash redi­rects where I find them and keep URLs as canon­i­cal as pos­si­ble.
    
4.  Redi­rects are **slower**:
    
    Each redi­rect costs some mil­lisec­onds, and if they cross do­mains, the lookup can take a while. It is not ter­ri­bly hard for redi­rects to stack up: on Gwern.net, a link to an old doc­u­ment could eas­ily incur 4+ redi­rects.⁠ [18](#fn:18) Given how much one sweats to elim­i­nate even 100ms from load- time, why tol­er­ate redi­rects which can be fixed with the swipe of a search- and-replace?
    

Redi­rects are re­ported by `linkchecker` & the [W3C linkchecker](https://validator.w3.org/checklink).

To fix a redi­rect, one can hand- edit case by case, but redi­rects are so per­va­sive that one should use some sort of global search- and-replace.

### Gwern.net Redirect Fixing

Be­cause Gwern.net is pri­mar­ily text- file based and its code­base has unit- tests, I have scripts to heav­ily au­to­mate find­ing & fix­ing redi­rects—no need to edit the source files by hand! (Ain’t no one got time for that.)

For Gwern.net use, I wrote a sim­ple site- wide [⁠string search- and-replace ⁠](https://gwern.net/static/build/stringReplace.hs) [`⁠gwsed.sh` ⁠](https://gwern.net/static/build/gwsed.sh) to allow easy up­dates like `gwsed.sh 'URL1' 'URL2'`. (It in­cludes a spe­cial case for the com­mon sce­nario of a site- wide HTTP → HTTPS mi­gra­tion, to de­tect `gwsed.sh 'http://DOMAIN/URL1' 'https://DOMAIN/URL2'`, where the two strings dif­fer solely by a `http` vs `https` pre­fix, and rewrite it to do `gwsed.sh 'http://DOMAIN' 'https://DOMAIN'` in­stead to up­date all links to that do­main. It also in­cludes a special- case for the for­mat of the W3C linkchecker: a com­mand like `gwsed.sh URL1 redirected to URL2` will be con­verted to `gwsed.sh URL1 URL2` so I can sim­ply copy- paste right into the ter­mi­nal.) This also makes up­dates script­able in bulk; for ex­am­ple, if I want to do a site- wide check in­stead of a page- by-page check with the linkchecker tools, I can ex­tract the URLs from all site files, process in a loop to see if they have non- zero redi­rects when down­loaded using `curl`, print out the old/ new, re­view by eye to delete evil or spu­ri­ous ones, and au­to­mat­i­cally string- rewrite the rest:

```
cd ~/wiki/
URLS=$(find ./ -type f -name "*.md" | \
    parallel runghc -istatic/build/ ./static/build/link-extractor.hs | \
    grep -E -e '^http' | head -500 | sort --unique)
 
for URL in "$URLS"; do
    URLNEW=$(curl --write-out '%{url_effective}\n' --head --location --silent --show-error \
            "$URL" --output /dev/null);
    if [ "$URL" != "$URLNEW" ]; then echo "$URL redirected to $URLNEW"; fi;
done
```

The [⁠link- icon ⁠](https://gwern.net/static/build/LinkIcon.hs) & [⁠live- link ⁠](https://gwern.net/static/build/LinkLive.hs) fea­tures rely heav­ily on do­main name matches, so they are vul­ner­a­ble to web­sites chang­ing; fix­ing redi­rects can silently break them. How­ever, they in­clude test suites with at least one ex­am­ple per rule and ex­er­cis­ing all of the branches or do­mains that a rule matches, and the search- and-replace mod­i­fies those files as well; so if URLs up­date, the test- suites will show up on a diff, and if they break the rules, the test- suites will error out on the next sync. So I can sim­ply toss off `gwsed.sh` calls and be sure that they won’t silently break any­thing.

## Preemptive Local Archiving

> In 2020-02, be­cause of the in­creas­ing dif­fi­culty of re­pair­ing old links, I switched Gwern.net’s pri­mary linkrot de­fense to **pre­emp­tive local archiv­ing**: au­to­mat­i­cally mir­ror­ing lo­cally all PDFs & web pages using manually- reviewed (and edited) [Sin­gle­File ⁠](https://github.com/gildas-lormeau/SingleFile/) snap­shots.
> 
> While it costs more time up­front (and pre­sented some sub­tle UX prob­lems like the [⁠“Arxiv prob­lem” ⁠](https://gwern.net/archiving#the-arxiv-problem)), it re­duces total linkrot work.

Pre­ven­tion > cure Eas­ier Higher- quality Rip­ping off the bandaid

Around 2019, while work­ing on a [linkchecker ⁠](https://github.com/linkchecker/linkchecker) re­port, and spend­ing time track­ing down one par­tic­u­larly elu­sive bro­ken link and drum­ming my fin­gers wait­ing on the slow Way­back Ma­chine web­site, and com­par­ing the mess to the half- minute it’d’ve taken to make & up­load a snap­shot with Sin­gle­File, I re­al­ized: it’s a lot harder to _fix_ dead links than it is to _archive_ live links. And the more you try to up­date your links, the more prob­lems you run into, like the wide­spread abuse of adding pay­walls or lying redi­rects. Pre­ven­tion > cure.

Eas­ier. If you take the linkrot risk es­ti­mates se­ri­ously (and hav­ing watched so many links die on Gwern.net, I be­lieve them), then as long as fix­ing is >2–3× harder than archiv­ing (it def­i­nitely is), you are bet­ter off just archiv­ing from the start in­stead of wast­ing time on re­ports & man­ual fix­ing one by one.

Higher- quality. Worse, while the pre­emp­tive archiv­ing can be re­fined & im­proved, the re­ac­tive ap­proach is in­her­ently one of [⁠“toil” ⁠](https://gwern.net/socks#toil) —tread­ing water. Throw in the re­al­ity that the archives often fail or are in­ad­e­quate, and their de­creas­ing ef­fi­cacy at cap­tur­ing web pages as pages get ever more baroque and com­plex, that archives are ‘un- opinionated’ in mak­ing no at­tempt to strip ads/ spam⁠ [19](#fn:19) or op­ti­mize the snap­shots or work as a ‘live link’ popup (when the full page pops up in­side an [iframe ⁠](https://en.wikipedia.org/wiki/HTML_element#Frames) cf. the [⁠screen­shot fail­ure ⁠](https://gwern.net/design-graveyard#link-screenshot-previews)), the public- good of pro­vid­ing an in­de­pen­dent archive, the greater speed of load­ing links from Gwern.net in­stead of a for­eign do­main (es­pe­cially the slow IA), and I had to con­cede that the cost- benefit had long since fa­vored pre­emp­tive local archiv­ing.

Rip­ping off the bandaid. I had hoped this would not be the case be­cause I wanted to limit the num­ber of archives I had to make or host, but the bur­den was be­com­ing un­sus­tain­able when com­bined with other site main­te­nance needs. I had no ex­cuse from ex­pen­sive cloud stor­age (even 100GB would have near- zero mar­ginal cost after my move to [Het­zner ⁠](https://en.wikipedia.org/wiki/Hetzner) ded­i­cated host­ing in 2017), rewrit­ing links would be easy using the Pan­doc API, Sin­gle­File was work­ing well when I used it man­u­ally & had a con­ve­nient CLI mode for script­ing pur­poses like this, and work­ing on fix­ing bro­ken links was an­noy­ing me slightly more every time.

### Local Snapshots

So after mulling over the de­sign for a while, I pulled the trig­ger in 2020-02, cre­at­ing [`⁠LinkArchive.hs` ⁠](https://gwern.net/static/build/LinkArchive.hs), which main­tains a data­base of URL/ archive/ sta­tus tu­ples, and calls [`⁠linkArchive.sh` ⁠](https://gwern.net/static/build/linkArchive.sh) to lookup or gen­er­ate the snap­shots using [Sin­gle­File CLI ⁠](https://github.com/gildas-lormeau/single-file-cli). The snap­shots are re­viewed by hand to ver­ify that they work & are read­able; if they are not, I make a new one, and often in­vest some time in mak­ing a bunch of [uBlock Ori­gin ⁠](https://en.wikipedia.org/wiki/UBlock_Origin) rules to clean a page up.

While it did not solve ex­ist­ing bro­ken links or break­age of links where Sin­gle­File can’t make a good snap­shot, and it is a bit an­noy­ing to cu­rate snap­shots, it is a dra­matic im­prove­ment over the sta­tus quo and I ex­pect the ben­e­fits to only in­crease with time.

### Workflow

1.  **Data­base+di­rec­to­ries**: A sim­ple data­base of URLs is main­tained, with their sta­tus: ei­ther the first- seen date, or their on- disk path.
    
    The URL’s snap­shot lives at `/doc/www/$DOMAIN/SHA1($URL).html`; the hash makes it sim­ple to en­code the name with­out es­cap­ing is­sues or in­cur­ring the dif­fi­cul­ties of im­i­tat­ing the tar­get URL’s di­rec­tory struc­ture⁠ [20](#fn:20), and the sep­a­rate pre­fixed do­main helped com­pat­i­bil­ity with the link- icon rules.⁠ [21](#fn:21)
    
2.  **Compile- time archiv­ing:**
    
    When com­pil­ing a page, each link is checked to see if it is on the black­list (be­cause it is a link which can­not or should not be archived). If not, then if it has an archive, it is rewrit­ten to point to the archive in­stead. (The orig­i­nal URL is stored in an HTML at­tribute for any other tools that need to know what that was, such as the pop­ups.) If it doesn’t, then the date is checked: if it was first- seen >60⁠ [22](#fn:22) days ago, then it is time to archive the URL. (I limit the num­ber of archives per site com­pi­la­tion to 12, to spread out the bur­den.)
    
    The archiv­ing script checks the URL. If the URL re­turns a PDF MIME type, then it down­loads the PDF and (like ) runs [`ocrmypdf` ⁠](https://github.com/ocrmypdf/OCRmyPDF) on it to en­sure that it has de­cent OCR, is a stan­dard [PDF/ A ⁠](https://en.wikipedia.org/wiki/PDF/A) archival- quality PDF, and throws in [JBIG2 ⁠](https://en.wikipedia.org/wiki/JBIG2) com­pres­sion which will often save 2–3× space. If it’s a reg­u­lar HTML URL, it in­stead runs Sin­gle­File CLI, which opens the URL in a local [Chrome ⁠](https://en.wikipedia.org/wiki/Chromium_\(web_browser\)) in­stal­la­tion, loads all the JS and [lazy ⁠](https://en.wikipedia.org/wiki/Lazy_loading) im­ages etc, and writes out a sta­tic snap­shot. (In the­ory, this Chrome in­stance _should_ have all my usual ex­ten­sions en­abled like uBlock & cook­ies en­abling lo­gins⁠ [23](#fn:23), but in prac­tice I’ve run into prob­lems and I’m not sure what ex­actly is get­ting run be­cause it is im­pos­si­ble to debug.)
    
3.  **Man­ual re­view**: The URL & its new snap­shot (whether PDF or HTML) are then both opened in Fire­fox for man­ual re­view.
    
    A bad snap­shot may re­quire me to add the do­main or URL to the black­list. It may also just be bro­ken (in many dif­fer­ent ways, in­clud­ing re­load­ing to a nonex­is­tent URL!), in which case I have to find a re­place­ment URL & do a [⁠global rewrite ⁠](https://gwern.net/archiving#gwern-net-redirect-fixing) (and the re­place­ment URL will even­tu­ally be archived).
    
    Al­ter­nately, I may need to make a new snap­shot man­u­ally, after delet­ing sticky el­e­ments with [Al­ways Kill Sticky](https://git.sr.ht/~achmizs/AlwaysKillSticky.git), scrolling the page to load lazy el­e­ments, or spend­ing a while with the uBlock element- picker to delete the most ob­nox­ious el­e­ments. (I tried ini­tially to edit the raw HTML of the Sin­gle­File snap­shot, but the data- URI en­cod­ing of im­ages, and the spaghetti ar­chi­tec­ture of the pages most in need of de- cruddification, meant that it was far harder to edit it in a text ed­i­tor than to sim­ply use uBlock or the built- in web tool ‘in­spec­tor’ to se­lect & delete. This can also be done re­peat­edly: take a Sin­gle­File snap­shot, delete stuff with in­spec­tor, and save with Sin­gle­File again.) Some­times a page will fail in Chromium Sin­gle­File, but then suc­ceed in Fire­fox Sin­gle­File. Tak­ing the time to re­move all the ads & bric- a-brac is use­ful be­cause it makes the page less likely to break in the fu­ture, smaller & faster, more read­able as a ‘live’ popup, eas­ier to see if any­thing is miss­ing, and amor­tizes across fu­ture snap­shots (so the man­ual re­view gets a lit­tle eas­ier every time as the black­list & block­list ex­pand).
    
4.  **Meta­data/ hid­ing**: The local archives are treated mostly like reg­u­lar files, while try­ing to min­i­mize search en­gine or user ex­po­sure; this is be­cause var­i­ous en­ti­ties might not ap­pre­ci­ate the mir­rors⁠ [24](#fn:24), and I don’t want to have to main­tain them in­def­i­nitely (par­tic­u­larly by set­ting up redi­rects to avoid break­ing old hash- URLs due to churn). Peo­ple will still link to them, but there’s only so much one can do.
    
    The Gwern.net web server ([nginx ⁠](https://en.wikipedia.org/wiki/Nginx)) is in­structed to set ap­pro­pri­ate head­ers to block in­dex­ing (be­yond just [`noindex` ⁠](https://en.wikipedia.org/wiki/Noindex)):
    
    And for good mea­sure, [`robots.txt` ⁠](https://en.wikipedia.org/wiki/Robots.txt):
    
    ```
    User-agent: *
    Disallow: /doc/www/*
    ```
    
5.  **Re­sults**: As of 2023-03-09, there are 14,352 tar­geted links weigh­ing 47GB (in­clud­ing now- unused archives which will be re­moved at some point), which is no prob­lem.
    

### The Arxiv Problem

One sub­tlety that came up after a while was the issue of ‘URL trans­forms’. In some cases, like [BioRxiv ⁠](https://en.wikipedia.org/wiki/BioRxiv), it’s best to sim­ply rewrite URLs to the full- text HTML ver­sion (just ap­pend `.full` to the URL); this is sim­ple & one can en­sure it hap­pens by in­clud­ing a global search- and-replace in the com­pi­la­tion process, and for­get about it while link­ing BioRxiv nor­mally. Un­for­tu­nately, some­times a global search- and-replace is in­ad­e­quate: there is a set of URLs where you link to one URL, but for archiv­ing pur­poses, you want to archive an al­ter­na­tive, a trans­for­ma­tion of that URL. The mo­ti­vat­ing ex­am­ple was ‘the [Arxiv ⁠](https://en.wikipedia.org/wiki/ArXiv) prob­lem’, one of the most heavily- linked do­mains on Gwern.net, and a dif­fi­cult one to solve: I wound up need­ing _3_ sep­a­rate URLs to han­dle brows­ing as con­ve­niently as pos­si­ble for both desk­top & mo­bile users.

‘The Arxiv prob­lem’ is the dif­fi­culty in pre­sent­ing Arxiv links to both desk­top & mo­bile users which is not (1) slow, (2) re­dun­dant, or (3) foist­ing a PDF on read­ers (es­pe­cially mo­bile read­ers). It is po­lite to link to the Arxiv HTML land­ing page like `/abs/$ID` rather than its full­text PDF under `/pdf/$ID`, but that would be use­less to archive be­cause I al­ready ex­tract most of the rel­e­vant in­for­ma­tion to present as the an­no­ta­tion popup. It would be a waste of reader time to hover over an Arxiv an­no­tated link, read the an­no­ta­tion with the title/ au­thor/ date/ ab­stract, and then hover over the ‘live’ Arxiv link to… read the same thing, pre­sum­ably wast­ing their time until they can nav­i­gate to the full­text PDF which they must have de­cided is worth their time. Ob­vi­ously, the ‘live’ link should be the PDF, which can then be a local op­ti­mized PDF.⁠ [25](#fn:25) Straight­for­ward, ex­cept Arxiv has an ad­di­tional wrin­kle: whether HTML land­ing page or PDF, it’s bad for mo­bile read­ers on smart­phones, who re­ally need a re­spon­sive [dark mode ⁠](https://en.wikipedia.org/wiki/Light-on-dark_color_scheme) - compatible HTML ver­sion of the _paper_ —which often ex­ists, as there is yet a third set of Arxiv URLs lo­cated at the ex­per­i­men­tal [L a T e X → HTML ⁠](https://github.com/brucemiller/LaTeXML) ser­vice which cov­ers most (but not all) Arxiv pa­pers, ‘Ar5iv’ (ie. `https://arxiv.org/html/$ID`)!⁠ [26](#fn:26)

Arxiv is the main prob­lem, but there are a few other cases worth han­dling. The preprint web­site [⁠Open­Re­view ⁠](https://openreview.net/about) op­er­ates sim­i­larly to Arxiv, with an HTML land­ing page & PDF. And Red­dit turns out to archive very poorly by de­fault even using the ‘old’ Red­dit in­ter­face which is good for reg­u­lar brows­ing; but I dis­cov­ered that while the mo­bile Red­dit (`i.reddit.com`) didn’t look _great_, it at least pre­served the con­tent re­li­ably. (Par­tic­u­larly acute read­ers may note that [⁠Less­Wrong ⁠](https://www.lesswrong.com/) → [⁠Greater­Wrong ⁠](https://www.greaterwrong.com/about) is not men­tioned, be­cause that is treated like a Wikipedia popup in that the JS code calls a spe­cial­ized API.)

#### Every CS Problem…

What to do? One _could_ bite the bul­let & link Arxiv PDFs (ig­nor­ing mo­bile read­ers), or link to the Ar5iv HTML ver­sion (pleas­ing mo­bile but an­noy­ing desk­top), or al­ways link the ab­stract as a lowest- common-denominator (wast­ing a bit of every­one’s time but not foist­ing PDFs on them). How­ever, I came up with a 3-way ap­proach which in­te­grated seam­lessly into my ex­ist­ing popup sys­tem ap­proach to show­ing an­no­ta­tion → archive → live.

I chose to add a _sec­ond_ layer of in­di­rec­tion to archive rewrites: links will be rewrit­ten silently be­fore archiv­ing (so in the case of an Arxiv `/abs` / link, it gets rewrit­ten to the PDF & the PDF be­comes the local archive), _and_ the ‘orig­i­nal link’ may be rewrit­ten (so the pop­ups are lied to and told that Ar5iv was the ‘orig­i­nal’ URL and that is what gets shown as the ‘live’ link).

While tricky to get right and re­quir­ing some mod­i­fi­ca­tions to the JS, this solves the Arxiv prob­lem for Gwern.net read­ers:

1.  I link the Arxiv `/abs/` nor­mally & con­ve­niently.
    
2.  This au­to­mat­i­cally cre­ates an an­no­ta­tion con­tain­ing the land­ing page’s meta­data (plus all my ad­di­tions like tags, ex­cerpts, back­links, similar- link rec­om­men­da­tions, etc).
    
    This popup/ popover will sat­isfy most read­ers.
    
3.  For read­ers who want to go deeper and read the full­text: the title of the popup (popover) is an archive link to a local PDF mir­ror.
    
    This PDF is small & fast, and will pop up in an­other ‘live’ popup or tab (fine for desk­top read­ers), or to an ex­ter­nal PDF reader on mo­bile (less fine).
    
4.  _But_ —as an ‘archive’ link, it au­to­mat­i­cally comes with a `[LIVE]` link ap­pended point­ing to the orig­i­nal raw URL (which is ac­tu­ally the Ar5iv ver­sion).
    
    This is for read­ers who need to link the orig­i­nal, want to con­sult it, or when the local archive is un­for­tu­nately bro­ken (hav­ing been grand­fa­thered in back in 2020-02). In the case of an Ar5iv link, how­ever, this in­stead says _`[HTML]`_: this tells mo­bile read­ers where to click for the HTML ver­sion they want.
    

While com­pli­cated to ex­plain, it fol­lows our de­sign lan­guage of pop­ups/ popovers, and sat­is­fies all users with no wasted clicks or mouse move­ments—aside from users who do want to visit/ copy the `/abs/` URL specif­i­cally, which I con­sider a minor use- case worth sac­ri­fic­ing for the other read­ers.

## Reacting To Broken Links

> For Books are not ab­solutely dead things, but doe con­tain a po­ten­cie of life in them to be as ac­tive as that soule was whose prog­eny they are; nay they do pre­serve as in a violl the purest ef­fi­ca­cie and ex­trac­tion of that liv­ing in­tel­lect that bred them. I know they are as lively, and as vig­or­ously pro­duc­tive, as those fab­u­lous Drag­ons teeth; and being sown up and down, may chance to spring up armed men. And yet on the other hand, un­lesse wari­nesse be us’d, as good al­most kill a Man as kill a good Book; who kills a Man kills a rea­son­able crea­ture, Gods Image; but hee who de­stroyes a good Booke, kills rea­son it selfe, kills the Image of God, as it were in the eye. Many a man lives a bur­den to the Earth; but a good Booke is the pre­tious life- blood of a mas­ter spirit, im­balm’d and trea­sur’d up on pur­pose to a life be­yond life. ’Tis true, no age can re­store a life, whereof per­haps there is no great losse; and rev­o­lu­tions of ages do not oft re­cover the losse of a re­jected truth, for the want of which whole Na­tions fare the worse. We should be wary there­fore what per­se­cu­tion we raise against the liv­ing labours of pub­lick men, how we spill that sea­son’d life of man pre­serv’d and stor’d up in Books; since we see a kinde of homi­cide may be thus com­mit­ted, some­times a mar­tyr­dome, and if it ex­tend to the whole im­pres­sion, a kinde of mas­sacre, whereof the ex­e­cu­tion ends not in the slay­ing of an el­e­men­tall life, but strikes at that ethe­re­all and fift essence, the breath of rea­son it selfe, slaies an im­mor­tal­ity rather then a life.
> 
> [John Mil­ton ⁠](https://en.wikipedia.org/wiki/John_Milton) ([_Aeropagit­ica_ ⁠](https://en.wikipedia.org/wiki/Areopagitica))

`archiver` com­bined with a tool like `link-checker` means that there will rarely be any bro­ken links on Gwern.net since one can ei­ther find a live link or use the archived ver­sion. In the­ory, one has mul­ti­ple op­tions now:

1.  Search for a copy on the live Web
    
2.  link the In­ter­net Archive copy
    
3.  link the We­bCite copy
    
4.  link the Wiki­Wix copy
    
5.  use the `wget` dump
    
    If it’s been turned into a full local file- based ver­sion with `--convert-links --page-requisites`, one can eas­ily con­vert the dump into some­thing like a stand­alone PDF suit­able for pub­lic dis­tri­b­u­tion. (A PDF is eas­ier to store and link than the orig­i­nal di­rec­tory of bits and pieces or other HTML for­mats like a ZIP archive of said di­rec­tory.)
    
    I used to use [`wkhtmltopdf`](https://wkhtmltopdf.org/) which does a good job of mak­ing PDFs of HTML pages; an ex­am­ple of a dead web­page with no In­ter­net mir­rors is `http://www.aeiveos.com/~bradbury/MatrioshkaBrains/MatrioshkaBrainsPaper.html` which can be found at [`1999-bradbury-matrioshkabrains.pdf` ⁠](https://gwern.net/doc/ai/scaling/hardware/1999-bradbury-matrioshkabrains.pdf), or Stern­berg et al’s 2001 24ya re­view [“The Pre­dic­tive Value of IQ” ⁠](https://gwern.net/doc/iq/2001-sternberg.pdf). I have since switched to [Sin­gle­File ⁠](https://github.com/gildas-lormeau/SingleFile/) to make sta­tic HTML snap­shots, which un­like MAFF/ MHTML, are view­able with­out any prob­lems in main­stream browsers.
    

## Automatic Internet Archive Repairs

Old = bet­ter

The In­ter­net Archive can be [⁠queried via an API ⁠](https://archive.org/help/wayback_api.php) for avail­able snap­shots near a date. If you know that a URL has an acceptable- quality snap­shot, you can get it and use some search- and-replace util­ity to au­to­mat­i­cally rewrite a bro­ken link.

So we can ask for the near­est URL to an early date like 1990-01-01:

```
$ curl --silent 'https://archive.org/wayback/available?timestamp=19900101&url=https://eva.onegeek.org/pipermail/oldeva/2001-September/040368.html' | \
    jq --raw-output '.'
```

Yield­ing:

```
{
  "url": "https://eva.onegeek.org/pipermail/oldeva/2001-September/040368.html",
  "archived_snapshots": {
    "closest": {
      "status": "200",
      "available": true,
      "url": "https://web.archive.org/web/20110726181638/http://eva.onegeek.org/pipermail/oldeva/2001-September/040368.html",
      "timestamp": "20110726181638"
    }
  },
  "timestamp": "19900101"
}
```

So our bro­ken link `https://eva.onegeek.org/pipermail/oldeva/2001-September/040368.html` can be fixed with the `closest.url` field of the `archived_snapshots` ob­ject, `https://web.archive.org/web/20110726181638/http://eva.onegeek.org/pipermail/oldeva/2001-September/040368.html`. Straight­for­ward.

Old = bet­ter. If we do _not_ spec­ify a time­stamp, or if we spec­ify a re­cent time­stamp like `20230101`, the IA will re­turn the most re­cent snap­shot in­stead. For re­pair­ing links, this would usu­ally be a bad idea: for most URLs, the first snap­shot will be the highest- quality one, as later snap­shots will typ­i­cally be in­fected by bi­trot, linkrot, web­site de­sign ‘up­grades’, spam, do­main squat­ters, ma­li­ciously in­dis­crim­i­nate redi­rects to a home­page, etc. Still, for some URLs we would want to do this, and it’s good to know that is pos­si­ble.

If we have a search- and-replace util­ity, newline- delimited list of bro­ken URLs we’d like to re­place, and a list of text files to up­date, we can eas­ily script all the queries & up­dates:

```
for URL in `cat urls.txt`; do
    URL_ARCHIVE=$(curl --silent 'https://archive.org/wayback/available?timestamp=19900101&url='"$URL" | \
        jq --exit-status --raw-output '.archived_snapshots.closest.url');
        if [ "$URL_ARCHIVE" != "null" ]; then
            search-and-replace "$URL" "$URL_ARCHIVE" [FILE]...;
        fi
done
```

### Why Not Internet Archive?

> The In­ter­net Archive’s archives should be re­hosted when you use them, and it should not be re­lied on as the only host of an archived web­page: be­cause re­host­ing is a bet­ter reader ex­pe­ri­ence, and the IA is a dan­ger­ous single- point-of-failure with sev­eral fac­tors in­creas­ing its risk of fail­ure.

The above trick of automatic- repair is only in­tended to be _tem­po­rary_ and patch bro­ken links until they can be re­hosted lo­cally or rewrit­ten to a live host. I dis­cour­age use of links to the In­ter­net Archive as a com­plete so­lu­tion to linkrot. Even if the IA snap­shot is the best avail­able, one should re­host it one­self for sev­eral rea­sons:

1.  **Self- hosting fea­tures**: your host­ing is faster (IA servers are al­ways over­loaded), more con­trol­lable (eg. you can con­trol X- Frame op­tions so you can pop up the page in an iframe), and vis­i­ble to search en­gines (IA hides every­thing in the Way­back Ma­chine) so peo­ple look­ing for it can find it.
    
2.  **Archive qual­ity ver­i­fi­ca­tion**: when you copy it, you will see what parts might be bro­ken or need fix­ing, be­fore it’s too late.
    
    Blind use of IA links risks dis­cov­er­ing, years down the line, that one linked a use­less archive—it ac­tu­ally redi­rected to a spam site, or the site was bro­ken when the snap­shot was made, or got blocked by a pay­wall, or the page re­lied on some asset dy­nam­i­cally which the IA didn’t load it, or… IA crawlers gen­er­ally are sim­ple and do not ex­e­cute JS or deal with lazi­ness, so as the Web be­comes in­creas­ingly com­plex, dy­namic, & JS- based, IA snap­shots are fre­quently bro­ken.
    
    One case was the [_⁠Climb­ing Mount Im­prob­a­ble_ web­site ⁠](https://gwern.net/doc/genetics/selection/www.mountimprobable.com/index.html): I thought it was a pity the site had dis­ap­peared, and that while it was safely in the IA and ap­par­ently work­ing, it ought to be vis­i­ble to search en­gines; so I re­hosted it, only to dis­cover to my hor­ror that the rea­son it ‘worked’ was that it was still load­ing every­thing from the _orig­i­nal Ama­zon AWS S3 buck­ets_! The site dev had not _yet_ com­pletely deleted it. He would at some point, how­ever, when he no­ticed the bucket was still cost­ing him money or his AWS ac­count lapsed. I hur­ried to lo­cal­ize all files, and suc­ceeded. Had I not done so, I would have checked in a few years later and dis­cov­ered the IA ver­sion bro­ken—ir­re­triev­ably.
    
3.  **IA host­ing is riskier** than it seems: the IA is a cen­tral­ized sin­gle point of fail­ure.
    
    While I love the IA, I re­gard it as dan­ger­ously rick­ety, and at risk of col­lapse in the next earth­quake. It is more like Li­brary.nu/ Lib­gen/ Sci- Hub than one might hope, and just as one should avoid di­rect links to those, one should avoid di­rect IA links: you are putting a lot of eggs in one bas­ket. It would be bet­ter to make more eggs, and put them in a dif­fer­ent bas­ket, for your­self & oth­ers to use; if the orig­i­nal bas­ket never breaks any eggs, great, but some­times bas­kets break. And IA’s bas­ket is old & the bot­tom fray­ing:
    
    -   IA servers (Way­back & oth­er­wise) ap­pear to have few back­ups, re­dun­dancy, or error- correction. They are grossly un­der­funded, so how would they af­ford such fancy things? Some­times when I look things up, the server is just… of­fline. How many mir­rors are there of the IA as a whole? Are there _any_? (There was sup­pos­edly one es­tab­lished in Egypt back in the 2000s, but given Egypt’s prob­lems and that I have heard noth­ing about it in the past decade, I sus­pect that if it still ex­ists, it is ei­ther grossly out- of-date, cor­rupt, or both.)
        
    -   be­hind the scenes, IA is chaotic: it seems to be held to­gether by duct tape and lots of legacy code slowly bi­trot­ting away. They are chal­lenged to keep things run­ning and deal with is­sues like abuse, and can­not in­vest much in, say, bet­ter crawl­ing or backup so­lu­tions.
        
        They may _seem_ re­li­able from the out­side, sure, but that’s how other web­sites ap­pear be­fore they an­nounce that the data­base was cor­rupted in a hard drive crash and all the back­ups were bro­ken, and they are sorry for your data loss (“mis­takes were made”); sim­i­larly, sites like [What.cd ⁠](https://en.wikipedia.org/wiki/What.CD) or [Li­brary.nu ⁠](https://en.wikipedia.org/wiki/Library.nu), which were mir­a­cles of archives, had re­mark­able up­time until they went down for­ever. The past is but pro­logue, and a poor pre­dic­tor at that. Will a ran­dom IA link work in, say, a mere 20 years? I’d rather have a pol­icy of mak­ing re­hosted copies of IA links for my many dead links & dis­cover it was par­tially wasted ef­fort (see #1/ 2) than wake up one day to read the news & find out that half the links on my site are now dead.
        
    -   IA mis­man­age­ment: IA man­age­ment has many other pri­or­i­ties than the Way­back Ma­chine; some, like the book scan­ning projects are rea­son­able even if it’s not en­tirely ob­vi­ous that IA ought to be doing them, and some… are highly ques­tion­able or out­right in­com­pe­tent, like the quixotic IA credit union and the on­go­ing dis­as­ter of the Na­tional Emer­gency Li­brary:
        
        -   _Credit union_: IA dab­bles in some odd projects at the be­hest of its ec­cen­tric founder [Brew­ster Kahle ⁠](https://en.wikipedia.org/wiki/Brewster_Kahle). For ex­am­ple, he in­vested major ef­fort over many years in try­ing to set up an In­ter­net Archive [_credit union_ ⁠](https://en.wikipedia.org/wiki/Credit_union) to ap­par­ently help IA em­ploy­ees with hous­ing loans or some­thing which has equally lit­tle to do with archiv­ing, how­ever mer­i­to­ri­ous; those fa­mil­iar with the im­mense reg­u­la­tory bur­dens of Amer­i­can banks, and reg­u­la­tors’ ha­tred of small banks which might em­bar­rass them, will cor­rectly pre­dict that Kahle’s ef­fort was [⁠fu­tile right from the be­gin­ning ⁠](https://blog.archive.org/2015/11/24/difficult-times-at-our-credit-union/) (even with­out the reg­u­la­tors telling Brew­ster to his face that [⁠“that is not going to hap­pen” ⁠](https://blog.archive.org/2015/12/14/internet-credit-union-2011-2015-rip/)).
            
        -   _Na­tional Emer­gency Li­brary_: While the credit union was sim­ply a de­ba­cle in terms of re­source con­sump­tion, it was not an ex­is­ten­tial threat to the Way­back Ma­chine. But there is an­other which is: the ex­tra­or­di­nary mis­judge­ment in [⁠2020-03-24 ⁠](https://blog.archive.org/2020/03/24/announcing-a-national-emergency-library-to-provide-digitized-books-to-students-and-the-public/), under the pre­text of COVID- 19, of the IA in de­cid­ing (unasked, and un­forced) to make mil­lions of IA’s scanned/ dig­i­tal e- books avail­able for de facto un­lim­ited down­load to every­one (dub­bing [it ⁠](https://en.wikipedia.org/wiki/Internet_Archive#National_Emergency_Library) the [⁠“Na­tional Emer­gency Li­brary” ⁠](https://blog.archive.org/national-emergency-library/)). This shat­tered the stan­dard dig­i­tal lend­ing prac­tice of ‘lend­ing’ out a fixed num­ber of copies (usu­ally one) for a lim­ited time—a prac­tice not pro­tected by copy­right law (ex­cept by wish­ful think­ing of [‘fair use’](https://kylecourtney.com/covid-19-copyright-library-superpowers-part-i/)), but which prac­tice had long been in­for­mally tol­er­ated by com­mer­cial pub­lish­ers as long as li­braries like IA didn’t push it too far & main­tained the pre­tense of repli­cat­ing the of­fline ex­pe­ri­ence with phys­i­cal books, such as by using wait­lists for a lim­ited num­ber of ‘copies’ at a time.
            
            [Al­ready on thin ice ⁠](https://en.wikipedia.org/wiki/Open_Library#Copyright_violation_accusations), the Emer­gency Li­brary pushed _way_ too far and un­sur­pris­ingly, [⁠they got sued ⁠](https://blog.archive.org/2020/06/01/four-commercial-publishers-filed-a-complaint-about-the-internet-archives-lending-of-digitized-books/) by major pub­lish­ers, who were now seek­ing to kill dig­i­tal lend­ing en­tirely be­cause the IA was grossly abus­ing it. You might think that this is as pre­dictable as the sun ris­ing and so the IA’s lead­er­ship, being nei­ther se­nile nor in­sane (pre­sum­ably), must have had a _re­ally_ good de­fense in copy­right law, per­haps one of IA’s spe­cial loop­holes like [Last 20 ⁠](https://gwern.net/doc/economics/copyright/2017-gard.pdf)? As one lawyer po­litely put it be­fore the law­suit, [“seems like a stretch” ⁠](https://arstechnica.com/tech-policy/2020/03/internet-archive-offers-thousands-of-copyrighted-books-for-free-online/) (hav­ing lit­tle to go on, as the IA didn’t even have an FAQ ex­plain­ing how it would be legal at all, so poorly planned was the Emer­gency Li­brary). Nope. Noth­ing. Not even a fig leaf. The IA just wanted to do it and did it, and then was shocked when pub­lish­ers were dis­pleased by one of the most bla­tant & large- scale copy­right in­fringe­ments ever. (I was so shocked that they were shocked that I stopped do­nat­ing to the IA.)
            
            In a sin­gle mas­ter stroke, Brew­ster Kahle & the IA board man­aged to (1) fail at the Emer­gency Li­brary’s in­tended goal by trig­ger­ing a [“in­cred­i­bly ex­pen­sive”](https://thenewstack.io/a-visit-to-the-physical-internet-archive/) law­suit [⁠shut­ter­ing it early ⁠](https://blog.archive.org/2020/06/10/temporary-national-emergency-library-to-close-2-weeks-early-returning-to-traditional-controlled-digital-lending/) ⁠ [27](#fn:27), (2) em­broil the IA in a law­suit funded by large wealthy op­po­nents with ex­is­ten­tial stakes for IA due to the scale of its in­fringe­ment, and (3) threaten the _modus vivendi_ of IA & every­one else’s dig­i­tal lend­ing by cre­at­ing a test case on pos­si­bly the least sym­pa­thetic & shaky grounds pos­si­ble. Un­sur­pris­ingly to every­one with the slight­est fa­mil­iar­ity with IP law, the IA [⁠lost the case](https://file770.com/judge-decides-against-internet-archive/) [⁠on dig­i­tal lend­ing en­tirely ⁠](https://blog.archive.org/2023/03/25/the-fight-continues/). I am un­aware of any in­ter­nal reck­on­ing, as­sign­ment of re­spon­si­bil­ity, or fir­ing of the ex­ec­u­tives & di­rec­tors who signed off on the Na­tional Emer­gency Li­brary (at a min­i­mum, Brew­ster Kahle, and the di­rec­tor of the “Open Li­braries” di­vi­sion who an­nounced it, [⁠Chris Free­land ⁠](https://archive.org/about/bios.php)).
            
            The Na­tional Emer­gency Li­brary will, one de­voutly hopes, wind up in a set­tle­ment which does not dam­age IA _too_ badly. Per­haps the pub­lish­ers will be gen­tle and set­tle for the IA clamp­ing down on its lend­ing ac­tiv­i­ties—for­ever cur­tail­ing ac­cess and set­ting a dis­as­trous prece­dent for li­braries every­where be­cause of their grotesque id­iocy—but at least limp­ing away to live an­other day. How­ever, the long- term vi­a­bil­ity of any in­sti­tu­tion ca­pa­ble of mak­ing, and then learn­ing noth­ing from it and keep­ing the re­spon­si­ble decision- makers in power, is in ques­tion.
            

## External Links

-   [`archivenow` ⁠](https://github.com/oduwsdl/archivenow) (li­brary for sub­mis­sion to `archive.is`, `archive.st`, `perma.cc`, Mega­lodon, We­bCite, & IA)
    
-   [⁠Me­mento meta- archive search en­gine ⁠](https://timetravel.mementoweb.org/) (for check­ing IA & other archives)
    
-   [⁠Archive- It ⁠](https://www.archive-it.org/) -(by the In­ter­net Archive); [⁠do­nate to the IA ⁠](https://archive.org/donate/)
    
-   [⁠Pin­board](https://pinboard.in/)
    
    -   [⁠“Book­mark Archives That Don’t” ⁠](https://web.archive.org/web/20170707135337/http://blog.pinboard.in/2010/11/bookmark_archives_that_don_t)
        
-   [⁠“Test­ing 3 mil­lion hy­per­links, lessons learned”](https://samsaffron.com/archive/2012/06/07/testing-3-million-hyperlinks-lessons-learned#comment-31366), Stack Ex­change
    
-   [“Backup All The Things” ⁠](https://gwern.net/doc/cs/linkrot/archiving/2011-muflax-backup.pdf), mu­flax
    
-   [⁠“Dig­i­tal Re­source Lifes­pan” ⁠](https://xkcd.com/1909/), _XKCD_
    
-   [“Archiv­ing web sites” ⁠](https://lwn.net/Articles/766374/), LWN
    
-   **Soft­ware:**
    
    -   [⁠we­brecorder.io](https://conifer.rhizome.org/) (on­line ser­vice); [we­brecorder ⁠](https://github.com/Rhizome-Conifer/conifer) (of­fline tool; WARC- based & can deal with dynamically- loaded con­tent); [Disker­net ⁠](https://github.com/dosyago/dn)
        
    -   [pywb ⁠](https://github.com/webrecorder/pywb)
        
    -   [⁠Archive­Box](https://archivebox.io/) (head­less Chrome)
        
    -   [IPFS ⁠](https://en.wikipedia.org/wiki/InterPlanetary_File_System)
        
    -   [⁠Word­Press plu­gin: Bro­ken Link Checker](https://wordpress.org/plugins/broken-link-checker/)
        
    -   [`⁠youtube-dl`](https://rg3.github.io/youtube-dl/)
        
    -   [Phan­tomJS ⁠](https://en.wikipedia.org/wiki/PhantomJS)
        
    -   [erised ⁠](https://github.com/marvelm/erised)
        
    -   [wpull ⁠](https://github.com/ArchiveTeam/wpull)
        
    -   [wabarc way­back ⁠](https://github.com/wabarc/wayback) (sim­i­lar ‘meta’- archiver to `archiver-bot`)
        
-   [⁠Hacker News dis­cus­sion ⁠](https://news.ycombinator.com/item?id=6504331)
    
-   [⁠“In­deed, it seems that Google _is_ for­get­ting the old Web” ⁠](https://stop.zona-m.net/2018/01/indeed-it-seems-that-google-is-forgetting-the-old-web/) ([⁠HN ⁠](https://news.ycombinator.com/item?id=19604135))
    
-   [⁠“The Lost Pic­ture Show: Hol­ly­wood Archivists Can’t Out­pace Ob­so­les­cence—Stu­dios in­vested heav­ily in magnetic- tape stor­age for film archiv­ing but now strug­gle to keep up with the tech­nol­ogy” ⁠](https://spectrum.ieee.org/the-lost-picture-show-hollywood-archivists-cant-outpace-obsolescence)
    
-   [⁠“Use the in­ter­net, not just com­pa­nies”](https://sive.rs/netskill), [Derek Sivers](https://sive.rs/)
    

## Appendices

## filter-urls

A raw dump of URLs, while cer­tainly archiv­able, will typ­i­cally re­sult in a very large mir­ror of ques­tion­able value (is it re­ally nec­es­sary to archive Google search queries or Wikipedia ar­ti­cles? usu­ally, no) and worse, given the rate- limiting nec­es­sary to store URLs in the In­ter­net Archive or other ser­vices, may wind up de­lay­ing the archiv­ing of the im­por­tant links & risk­ing their total loss. Dis­abling the re­mote archiv­ing is un­ac­cept­able, so the best so­lu­tion is to sim­ply take a lit­tle time to man­u­ally black­list var­i­ous do­mains or URL pat­terns.

This black­list­ing can be as sim­ple as a com­mand like `filter-urls | grep -v en.wikipedia.org`, but can be much more elab­o­rate. The fol­low­ing shell script is the skele­ton of my own cus­tom black­list, de­rived from man­u­ally fil­ter­ing through sev­eral years of daily brows­ing as well as spi­ders of [⁠dozens of web­sites ⁠](https://www.lesswrong.com/posts/mMgiGy6i55iZbMzyx/rationalist-sites-worth-archiving) for var­i­ous peo­ple & pur­poses, demon­strat­ing a va­ri­ety of pos­si­ble tech­niques: reg­exps for do­mains & file- types & query- strings, `sed` - based rewrites, fixed- string matches (both black­lists and whitelists), etc:

```
#!/bin/sh
 
# USAGE: `filter-urls` accepts on standard input a list of newline-delimited URLs or filenames,
# and emits on standard output a list of newline-delimited URLs or filenames.
#
# This list may be shorter and entries altered. It tries to remove all unwanted entries, where 'unwanted'
# is a highly idiosyncratic list of regexps and fixed-string matches developed over hundreds of thousands
# of URLs/filenames output by my daily browsing, spidering of interesting sites, and requests
# from other people to spider sites for them.
#
# You are advised to test output to make sure it does not remove
# URLs or filenames you want to keep. (An easy way to test what is removed is to use the `comm` utility.)
#
# For performance, it does not sort or remove duplicates from output; both can be done by
# piping `filter-urls` to `sort --unique`.
 
set -euo pipefail
 
cat /dev/stdin \
    | sed -e "s/#.*//" -e 's/>$//' -e "s/&sid=.*$//" -e "s/\/$//" -e 's/$/\n/' -e 's/\?sort=.*$//' \
      -e 's/^[ \t]*//' -e 's/utm_source.*//' -e 's/https:\/\//http:\/\//' -e 's/\?showComment=.*//' \
    | grep "\." \
    | grep -F -v "*" \
    | grep -E -v -e '\/\.rss$' -e "\.tw$" -e "//%20www\." -e "/file-not-found" -e "258..\.com/$" \
       -e "3qavdvd" -e "://avdvd" -e "\.avi" -e "\.com\.tw" -e "\.onion" -e "\?fnid\=" -e "\?replytocom=" \
       -e "^lesswrong.com/r/discussion/comments$" -e "^lesswrong.com/user/gwern$" \
       -e "^webcitation.org/query$" \
       -e "ftp.*" -e "6..6\.com" -e "6..9\.com" -e "6??6\.com" -e "7..7\.com" -e "7..8\.com" -e "7..\.com" \
       -e "78..\.com" -e "7??7\.com" -e "8..8\.com" -e "8??8\.com" -e "9..9\.com" -e "9??9\.com" \
       -e gold.*sell -e vip.*club \
    | grep -F -v -e "#!" -e ".bin" -e ".mp4" -e ".swf" -e "/mediawiki/index.php?title=" -e "/search?q=cache:" \
      -e "/wiki/Special:Block/" -e "/wiki/Special:WikiActivity" -e "Special%3ASearch" \
      -e "Special:Search" -e "__setdomsess?dest="
      # ...
 
# prevent URLs from piling up at the end of the file
echo -e "\n"
```

`filter-urls` can be used on one’s local archive to save space by delet­ing files which may be down­loaded by `wget` as de­pen­den­cies. For ex­am­ple:

```
find ~/www | sort --unique >> full.txt && \
    find ~/www | filter-urls | sort --unique >> trimmed.txt
comm -23 full.txt trimmed.txt | xargs -d "\n" rm
rm full.txt trimmed.txt
```

## sort Key Compression Trick

[**Moved to “The Sort Key Trick”.**](https://gwern.net/sort)

## Bibliography

1.  I use [`duplicity`](https://duplicity.nongnu.org/) & [`⁠rdiff-backup`](https://rdiff-backup.net/) to backup my en­tire home di­rec­tory to a cheap 1.5TB hard drive (bought from Newegg using `forre.st` ’s [⁠“Stor­age Analy­sis—GB/ $ for dif­fer­ent sizes and media”](https://forre.st/storage#hdd) price- chart); a lim­ited se­lec­tion of fold­ers are backed up to [Back­blaze ⁠](https://en.wikipedia.org/wiki/Backblaze) B2 using `duplicity`.
    
    I used to semi­an­nu­ally tar up my im­por­tant fold­ers, add [PAR2 ⁠](https://en.wikipedia.org/wiki/Parchive) re­dun­dancy, and burn them to DVD, but that’s no longer re­ally fea­si­ble; if I ever get a Blu- ray burner, I’ll re­sume WORM back­ups. (Mag­netic media doesn’t strike me as re­li­able over many decades, and it would ease my mind to have op­ti­cal back­ups.) [](https://gwern.net/archiving#fnref1)[↩](#fnref:1)
    
2.  [⁠“When the In­ter­net Is My Hard Drive, Should I Trust Third Par­ties?” ⁠](https://web.archive.org/web/20121108093008/https://www.wired.com/politics/security/commentary/securitymatters/2008/02/securitymatters_0221), _Wired_:
    
    Bits and pieces of the web dis­ap­pear all the time. It’s called ‘link rot’, and we’re all used to it. A friend saved 65 links in 1999 26ya when he planned a trip to Tus­cany; only half of them still work today. In my own blog, es­says and news ar­ti­cles and web­sites that I link to reg­u­larly dis­ap­pear—some­times within a few days of my link­ing to them.[↩](#fnref:2)
    
3.  [“Going, Going, Gone: Lost In­ter­net Ref­er­ences” ⁠](https://gwern.net/doc/cs/linkrot/2003-dellavalle.pdf); ab­stract:
    
    The ex­tent of In­ter­net ref­er­enc­ing and In­ter­net ref­er­ence ac­tiv­ity in med­ical or sci­en­tific pub­li­ca­tions was sys­tem­at­i­cally ex­am­ined in more than 1000 ar­ti­cles pub­lished be­tween 2000 25ya and 2003 22ya in the New Eng­land Jour­nal of Med­i­cine, The Jour­nal of the Amer­i­can Med­ical As­so­ci­a­tion, and Sci­ence. In­ter­net ref­er­ences ac­counted for 2.6% of all ref­er­ences (672/ 25,548) and in ar­ti­cles 27 months old, 13% of In­ter­net ref­er­ences were in­ac­tive.[↩](#fnref:3)
    
4.  The Mil­lion Dol­lar Home­page still gets a sur­pris­ing amount of traf­fic, so one fun thing one could do is buy up ex­pired do­mains which paid for par­tic­u­larly large links.[](https://gwern.net/archiving#fnref4) [↩](#fnref:4)
    
5.  By 2013-01-06, the num­ber has in­creased to ~12,000 ex­ter­nal links, ~7,200 to non- Wikipedia do­mains.[](https://gwern.net/archiving#fnref5) [↩](#fnref:5)
    
6.  If each link has a fixed chance of dying in each time pe­riod, such as 3%, then the total risk of death is an [ex­po­nen­tial dis­tri­b­u­tion ⁠](https://en.wikipedia.org/wiki/Exponential_distribution); over the time pe­riod 2011 – 59 2070 the cu­mu­la­tive chance it will beat each of the 3% risks is 0.1658 367ya. So in 2070, how many of the 2200 links will have beat the odds? Each link is in­de­pen­dent, so they are like flip­ping a bi­ased coin and form a [bi­no­mial dis­tri­b­u­tion ⁠](https://en.wikipedia.org/wiki/Binomial_distribution). The bi­no­mial dis­tri­b­u­tion, being dis­crete, has no easy equa­tion, so we just ask R how many links sur­vive at the 5 th per­centile/ quan­tile (a lower bound) and how many sur­vive at the 95 th per­centile (an upper bound):[↩](#fnref:6)
    
7.  101, ‘Bud­dhism re­lated to Blos­soms’; [_Un­for­got­ten Dreams: Poems by the Zen monk Shōtetsu_ ⁠](https://gwern.net/doc/japan/poetry/shotetsu/1997-carter-shotetsu-unforgottendreams.pdf); trans. Steven D. Carter, ISBN 0-231-10576-2 [](https://gwern.net/archiving#fnref7)[↩](#fnref:7)
    
8.  My vari­ant: “So­cial media is a ma­chine for se­lec­tively bi­trot­ting every­thing good about you while pre­serv­ing mil­lions of copies of your worst tweet.” [](https://gwern.net/archiving#fnref8)[↩](#fnref:8)
    
9.  Which I sus­pect is only ac­ci­den­tally ‘gen­eral’ and would shut down ac­cess if there were some other way to en­sure that Wikipedia ex­ter­nal links still got archived.[](https://gwern.net/archiving#fnref9) [↩](#fnref:9)
    
10.  Since Pin­board is a book­mark­ing ser­vice more than an archive site, I asked in 2012 13ya whether treat­ing it as such would be ac­cept­able and Ma­ciej said “Your cur­rent archive size, grow­ing at 20 GB a year, should not be a prob­lem. I’ll put you on the heavy- duty server where my own stuff lives.”
    
    I ul­ti­mately did not take him up on this offer in part be­cause Pin­board’s archives were rel­a­tively low- quality. Pin­board started being ne­glected around 2017 by Ma­ciej, and as of mid-2022, er­rors are rou­tine. I do not rec­om­mend use of Pin­board.[](https://gwern.net/archiving#fnref10) [↩](#fnref:10)
    
11.  I’m con­vinced that Google would never just delete colos­sal amounts of In­ter­net data—this is Google, after all, the epit­ome of stor­ing un­think­able amounts of data—and that Google Cache has merely been hid­den. Be­sides its plau­si­bil­ity & long- standing ru­mors about its ex­is­tence, the 2024 ad API leak ap­par­ently con­firmed the ex­is­tence of the pri­vate Google In­ter­net archives going back many snap­shots.[](https://gwern.net/archiving#fnref11) [↩](#fnref:11)
    
12.  Which would not be pub­licly ac­ces­si­ble or sub­mit­table; I know they exist, but be­cause they hide them­selves, I know only from ran­dom com­ments on­line eg. [⁠“years ago a friend of mine who I’d lost con­tact with caught up with me and told me he found a cached copy of a web­site I’d taken down in his em­ployer’s equiv­a­lent to the Way­back Ma­chine. His em­ployer was a branch of the fed­eral gov­ern­ment.” ⁠](https://news.ycombinator.com/item?id=2880427).[](https://gwern.net/archiving#fnref12) [↩](#fnref:12)
    
13.  [⁠Ver­sion 0.1 ⁠](https://hackage.haskell.org/package/archiver-0.1) of my `archiver` dae­mon didn’t sim­ply read the file until it was empty and exit, but ac­tu­ally watched it for mod­i­fi­ca­tions with [in­o­tify ⁠](https://en.wikipedia.org/wiki/Inotify). I re­moved this func­tion­al­ity when I re­al­ized that the re­quired We­bCite chok­ing (just one URL every ~25 sec­onds) meant that `archiver` would _never_ fin­ish any rea­son­able work­load.[](https://gwern.net/archiving#fnref13) [↩](#fnref:13)
    
14.  Much eas­ier than it was in the past; [Jamie Za­w­in­ski ⁠](https://en.wikipedia.org/wiki/Jamie_Zawinski) records his tra­vails with the _pre­vi­ous_ Mozilla his­tory for­mat in the aptly- named [“when the data­base worms eat into your brain”](https://www.jwz.org/blog/2004/03/when-the-database-worms-eat-into-your-brain/).[](https://gwern.net/archiving#fnref14) [↩](#fnref:14)
    
15.  An older [⁠2010 Google ar­ti­cle ⁠](https://web.archive.org/web/20100628055041/https://code.google.com/speed/articles/web-metrics.html) put the av­er­age at 320kb, but that was an av­er­age over the en­tire Web, in­clud­ing all the old con­tent.[](https://gwern.net/archiving#fnref15) [↩](#fnref:15)
    
16.  Al­ready one runs old games like the clas­sic [Lu­casArts ad­ven­ture games ⁠](https://en.wikipedia.org/wiki/LucasArts_adventure_games) in em­u­la­tors of the DOS op­er­at­ing sys­tem like [DOS­Box ⁠](https://en.wikipedia.org/wiki/DOSBox); but those em­u­la­tors will not al­ways be main­tained. Who will em­u­late the em­u­la­tors? Pre­sum­ably in 2050, one will in­stead em­u­late some an­cient but com­pat­i­ble OS—Win­dows 7 or De­bian 6.0, per­haps—and in­side _that_ run DOS­Box (to run the DOS which can run the game).[](https://gwern.net/archiving#fnref16) [↩](#fnref:16)
    
17.  As­sid­u­ously up­dat­ing redi­rects can cause archive prob­lems when the new URL breaks be­fore archiv­ing, or it was a lying link & you look up archives of a long- dead link. But you can al­ways look through your version- control his­tory for older URLs to try, and you may not be able to check newer URLs if you weren’t up­dat­ing. So it’s bet­ter to up­date.[](https://gwern.net/archiving#fnref17) [↩](#fnref:17)
    
18.  Imag­ine a link to `http://www.gwern.net/docs/2010-anderson.pd` cre­ated in 2015 by a user mak­ing a com­mon typo; today it might bounce through the fol­low­ing se­quence of redi­rects (I _think_): HTTP → HTTPS, `www` → root, `/docs/` → `/doc/`, `...pd` → `...pdf`, and `/doc/` to `/doc/statistics/prediction/` to reach its cur­rent URL of `https://gwern.net/doc/statistics/prediction/2010-anderson.pdf`. And that’s just for now—the [`statistics/prediction` tag ⁠](https://gwern.net/doc/statistics/prediction/index) is over­loaded and needs refac­tor­ing into sub- tags, so [An­der­son & Sher­man 2010 ⁠](https://gwern.net/doc/statistics/prediction/2010-anderson.pdf) will at some point prob­a­bly be re­lo­cated to a [Fermi es­ti­mate ⁠](https://gwern.net/doc/science/fermi-problem/index) tag’s sub- directory, set­ting up a 6 th redi­rect. If each redi­rect takes 50ms (op­ti­mistic), then that’s 0.3s spent just to get the URL![](https://gwern.net/archiving#fnref18) [↩](#fnref:18)
    
19.  A sur­pris­ingly large frac­tion of Gwern.net read­ers—and [⁠read­ers in gen­eral ⁠](https://gwern.net/banner#they-just-dont-know) —still do not use [ad- blockers ⁠](https://en.wikipedia.org/wiki/Ad_blocking), es­pe­cially on mo­bile where they need one most.[](https://gwern.net/archiving#fnref19) [↩](#fnref:19)
    
20.  It may be tempt­ing to try to mir­ror a URL’s `/foo/bar/baz.ext` struc­ture, but this is not as use­ful as it seems (since you will typ­i­cally have rel­a­tively few archived URLs so the struc­ture will be sparse, and you want to tag them any­way), and has many edge- cases in sim­ply con­vert­ing ar­bi­trary URLs to us­able on- disk filepaths. The fact is, it is not 1995 30ya, and a web­site is not a [Unix ⁠](https://en.wikipedia.org/wiki/Unix) di­rec­tory. Con­tem­po­rary URLs do not map, in any way, onto HTML filepaths: URLs are stuffed with dan­ger­ous char­ac­ters which will should prob­a­bly be es­caped, [pun­y­code ⁠](https://en.wikipedia.org/wiki/Punycode) en­cod­ing of Uni­code, web­site di­rec­to­ries which are ac­tu­ally files/ pages (the ubiq­ui­tous trail­ing slash), sub­do­mains, query ar­gu­ments, hash an­chors (in­clud­ing the loathed and not com­pletely de­funct `#!` de­sign pat­tern), redi­rects, and so on. Fur­ther, URLs change at the drop of a hat, in­clud­ing any im­plied ‘di­rec­tory hi­er­ar­chy’, ren­der­ing up­dates dif­fi­cult—many re­dun­dant snap­shots or con­tra­dic­tory im­plied paths. No, no, just re­sist the temp­ta­tion to pun on URL ↔︎ filepath, and as­sign it an opaque unique ID and store _that_.[](https://gwern.net/archiving#fnref20) [↩](#fnref:20)
    
21.  No longer nec­es­sary with the final link- icon im­ple­men­ta­tion, but this was nec­es­sary be­fore [when using CSS reg­exp rules ⁠](https://gwern.net/design-graveyard#link-icon-css-regexps), so rules like `href=*"google.com"` would match both `https://www.google.com` and `/doc/www/www.google.com/XYZ.html`.[](https://gwern.net/archiving#fnref21) [↩](#fnref:21)
    
22.  Down from 120 days, then 90, as I kept hit­ting mov­ing pay­walls or sites out­right dying.[](https://gwern.net/archiving#fnref22) [↩](#fnref:22)
    
23.  This turned out to be a major flaw in archives of some web­sites like [Red­dit ⁠](https://en.wikipedia.org/wiki/Reddit): there are few archives of the / r/ Dark­Net­Mar­kets sub­red­dit be­cause it was set to over-18/ NSFW, which meant that any cookie- less archiver like IA archived noth­ing but login- walls![](https://gwern.net/archiving#fnref23) [↩](#fnref:23)
    
24.  I have thus far re­ceived only 1 DMCA take­down email, from, oddly, a local news­pa­per used in my [DNM ar­rests cen­sus ⁠](https://gwern.net/dnm-arrest).[](https://gwern.net/archiving#fnref24) [↩](#fnref:24)
    
25.  Re­host­ing Arxiv PDFs is es­pe­cially help­ful be­cause Arxiv PDFs can be _very_ large (eg. the [OFA ⁠](https://arxiv.org/abs/2202.03052#alibaba) paper is 35MB—most of my book scans are smaller), slow to down­load (in ad­di­tion to the extra do­main name lookup), and Arxiv is a non­profit with min­i­mal bud­get (so if one is en­cour­ag­ing read­ers to down­load PDFs prof­li­gately the way my pop­ups do, you should re­host them).[](https://gwern.net/archiving#fnref25) [↩](#fnref:25)
    
26.  Ar5iv comes with its own caveats: it can­not ren­der all Arxiv pa­pers, some­times the ren­dered one is bro­ken, and it at­tempts ren­ders with ap­prox­i­mately a 1 month lag. For­tu­nately, it is ca­pa­ble of redi­rect­ing to the reg­u­lar Arxiv land­ing page (ap­pend `?fallback=original`), so it is safe to link to it—at worst, a mo­bile reader just winds where they would’ve ended up any­way.[](https://gwern.net/archiving#fnref26) [↩](#fnref:26)
    
27.  IA de­scribes it as merely ‘clos­ing 2 weeks early’ to save face, but they had orig­i­nally said “This sus­pen­sion will run through June 30, 2020, or the end of the US na­tional emer­gency, whichever is later.”—the ‘US na­tional emer­gency’, such as the clo­sure of schools which was the pri­mary ra­tio­nale, was not over by 2020-06-30, need­less to say, or that year (or the year after that).[](https://gwern.net/archiving#fnref27) [↩](#fnref:27)