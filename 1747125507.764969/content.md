> **Side­notes** & **mar­gin notes** are a ty­po­graphic con­ven­tion which im­proves on foot­notes & end­notes by in­stead putting the notes in the page mar­gin to let the reader in­stantly read them with­out need­ing to refer back and forth to the end of the doc­u­ment (end­notes) or suc­ces­sive pages (foot­notes spilling over).
> 
> They are par­tic­u­larly use­ful for web pages, where ‘foot­notes’ are de facto end­notes, and click­ing back and forth to end­notes is a pain for read­ers. (Foot­note vari­ants, like “float­ing foot­notes” which pop up on mouse hover, re­duce the reader’s ef­fort but don’t elim­i­nate it.)
> 
> How­ever, they are not com­monly used, per­haps be­cause web browsers until rel­a­tively re­cently made it hard to im­ple­ment side­notes eas­ily & re­li­ably. [⁠Tufte- CSS ⁠](https://edwardtufte.github.io/tufte-css/) has pop­u­lar­ized the idea and since then, there has been a pro­lif­er­a­tion of slightly vari­ant ap­proaches. I re­view some of the avail­able im­ple­men­ta­tions.
> 
> For gen­eral users, I rec­om­mend [⁠Tufte- CSS-style ap­proaches ⁠](https://gwern.net/sidenote#tufte-css): it is fast & sim­ple (using only compile- time gen­er­a­tion of side­notes, ren­dered by sta­tic HTML/ CSS), pop­u­lar, and Tufte- CSS-esque li­braries are easy to in­te­grate into many web­site work­flows. For heavy foot­note users or users who want a drop- in, run­time Javascript- based so­lu­tions like [`⁠sidenotes.js` ⁠](https://gwern.net/sidenote#sidenotes-js) may be more use­ful.
> 
> ![Demonstration of sidenotes.js handling multiple large dense endnote annotations on an annotated novel which has many allusions and technical references.](https://gwern.net/doc/cs/css/sidenotes.png)

Mak­ing use of mar­gins

Side­notes and mar­gin notes (some­times also called “asides”) are an al­ter­na­tive to [foot­notes/ end­notes ⁠](https://en.wikipedia.org/wiki/Note_\(typography\)) in de­sign. Where foot­notes put ad­di­tional ma­te­r­ial in small sec­tions at the bot­tom of the page, or­ga­nized by num­ber, and end­notes stuff them at the end of the doc­u­ment, side­notes & mar­gin notes in­stead use the large un­used left/ right mar­gin of the page. If it is num­bered & an­chored to a spe­cific point in the text, I call it a ‘side­note’; if it is un­num­bered & is merely placed next to a body of text, then I call it a ‘mar­gin note’. (Mar­gin notes are less use­ful & more ob­scure, so tend to be un­sup­ported; I oc­ca­sion­ally use mar­gin notes for sum­ma­riz­ing para­graphs, like the next para­graph here, where they func­tion as ex­tremely small ‘sec­tion head­ers’.)

Mak­ing use of mar­gins. Be­cause it’s un­com­fort­able to read sen­tences which wrap from edge to edge, par­tic­u­larly for large widths, doc­u­ments use [short lines ⁠](https://en.wikipedia.org/wiki/Line_length). But with large screens, many doc­u­ments have equally large mar­gins, and wind up look­ing like a nar­row river of text flow­ing down a vast blank map. This river of text may be stud­ded with the oc­ca­sional foot­note or end­note, in­clud­ing an­cil­lary ma­te­r­ial like ci­ta­tions or di­gres­sions or ex­tended dis­cus­sion of tricky points or an­tic­i­pa­tion of ob­jec­tions or just the au­thor being witty, which re­quire con­stant back and forth from the place in the text where they make sense and where they can ac­tu­ally be read. As a re­sult, who ever reads end­notes in a phys­i­cal book? Only the most dili­gent will keep a thumb in the back to ac­tu­ally look up end­notes, and so they are ei­ther un­read or tend to be rel­e­gated to the most util­i­tar­ian uses like raw ci­ta­tions.

The sit­u­a­tion is even worse on the In­ter­net, be­cause while foot­notes in a book aren’t _too_ bad (as long as they stay on the same page), web pages don’t re­ally have ‘pages’ and ‘foot­notes’ wind up de­grad­ing to sim­ply end­notes.⁠ [1](#fn:1)

Why do we use end­notes? For the most part, we use them for ci­ta­tion meta­data, ab­bre­vi­a­tions/ de­f­i­n­i­tions, and more ex­tended dis­cus­sions (often hu­mor­ous). But none of these are served well on­line by end­notes: ci­ta­tion meta­data is bet­ter pro­vided as hy­per­links to full­text, [de­f­i­n­i­tions (`<defn>`) ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn) / [ab­bre­vi­a­tions (`<abbr>`) ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr) have na­tive HTML sup­port as tooltips/ pop­ups—leav­ing only the ex­tended dis­cus­sions use- case.

[Bringhurst ⁠](https://en.wikipedia.org/wiki/Robert_Bringhurst) com­ments on the pros/ cons (_[The El­e­ments of Ty­po­graphic Style ⁠](https://en.wikipedia.org/wiki/The_Elements_of_Typographic_Style)_, 2004 21ya):

> Foot­notes are the very em­blem of fussi­ness, but they have their uses. If they are short and in­fre­quent, they can be made eco­nom­i­cal of space, easy to find when wanted and, when not wanted, easy to ig­nore. Long foot­notes are in­evitably a dis­trac­tion: te­dious to read and weary­ing to look at. Foot­notes that ex­tend to a sec­ond page (as some long foot­notes are bound to do) are an ab­ject fail­ure of de­sign.
> 
> End­notes can be just as eco­nom­i­cal of space, less trou­ble to de­sign and less ex­pen­sive to set, and they can com­fort­ably run to any length. They also leave the text page clean ex­cept for a pep­per­ing of su­per­scripts. They do, how­ever, re­quire the se­ri­ous reader to use two book­marks and to read with both hands as well as both eyes, swap­ping back and forth be­tween the pop­u­lar and the per­snick­ety parts of the text.
> 
> Side­notes give more life and va­ri­ety to the page and are the eas­i­est of all to find and read. If care­fully de­signed, they need not en­large ei­ther the page or the cost of print­ing it. Foot­notes rarely need to be larger than 8 or 9 point. End­notes are typ­i­cally set in small text sizes: 9 or 10 point. Side­notes can be set in any­thing up to the same size as the main text, de­pend­ing on their fre­quency and im­por­tance, and on the over­all for­mat of the page. If they are not too fre­quent, side­notes can be set with no su­per­scripts at all (as in this book), or with the same sym­bol (nor­mally an as­ter­isk) con­stantly reused, even when sev­eral notes ap­pear on a sin­gle page.

Our ex­tended dis­cus­sions ought to be made easy to read in con­text and not hid­den away at the end of the page. Side­notes let us reuse some of that un­used mar­gin, in a way which is com­fort­able to read, and which is com­pat­i­ble with ex­ist­ing doc­u­ments & work­flows using end­notes: sim­ply move those end­notes into the mar­gin of the text they refer to. The user can com­fort­ably sac­cade over to a side­note in­stantly to skim it and back, the in­for­ma­tion den­sity of the lay­out in­creases, it re­quires no ex­otic tech­nolo­gies or rewrites or user ed­u­ca­tion, it has a long re­spectable his­tory, and it’s just gen­er­ally a good idea.

To see na­tive side­notes & mar­gin notes on Gwern.net, use a wider screen.

## Examples

Some ex­am­ples of side­notes in books; Bringhurst uses side­notes him­self, of course:

![Bringhurst2004 example of sidenotes & margin notes (in this case, it repeats the section heading)](https://gwern.net/doc/design/typography/sidenote/2004-bringhurst-theelementsoftypographicstyle-pg70-marginsidenoteexample.png)

2004 ex­am­ple of side­notes & mar­gin notes (in this case, it re­peats the sec­tion head­ing)

Side­notes are ex­ten­sively used in me­dieval man­u­scripts and early mod­ern books such as the [Geneva Bible ⁠](https://en.wikipedia.org/wiki/Geneva_Bible#Format) ([first 2 pages ⁠](https://github.com/raphink/geneve_1564/releases/download/2015-07-08_01/geneve_1564.pdf)) (see also [rubri­ca­tion ⁠](https://gwern.net/red)), or Bayle’s awe- inspiringly am­bi­tious use of (re­cur­sive) mar­gin/ side notes:

![Screenshot of Google Books (https://books.google.com/books?id=JmtXAAAAYAAJ&pg=PA900), showing advanced typography in a single page which contains body text, footnotes, and (recursively) sidenotes to footnotes, of Pierre Bayle’s famous Enlightenment text, the ‘Historical and Critical Dictionary’ (pg900 of volume 4 of the 1737 English edition).](https://gwern.net/doc/design/typography/sidenote/1737-bayle-dictionary-vol4-pg901.jpg)

[Pierre Bayle’s ⁠](https://en.wikipedia.org/wiki/Pierre_Bayle) [_His­tor­i­cal and Crit­i­cal Dic­tio­nary_ ⁠](https://en.wikipedia.org/wiki/Dictionnaire_Historique_et_Critique), demon­strat­ing re­cur­sive foot­notes/ side­notes (1737 288ya, vol­ume 4, pg901; source: Google Books)

Side­notes (and mar­gin notes) have been less used in more con­tem­po­rary books; the best- known pop­u­lar­izer is [Ed­ward Tufte ⁠](https://en.wikipedia.org/wiki/Edward_Tufte):

![Example of Tufte’s use of sidenotes & margin notes: they provide additional examples, commentary, and citation metadata for the reader in context, without forcing inscrutable lookups buried deep at the end of the chapter (or worse, book) which few readers will ever bother with. (From pg61, “Layering & Separation”, Envisioning Information, Tufte1990)](https://gwern.net/doc/design/typography/sidenote/1990-tufte-envisioninginformation-pg61-sidenotes.png)

Ex­am­ple of Tufte’s use of side­notes & mar­gin notes: they pro­vide ad­di­tional ex­am­ples, com­men­tary, and ci­ta­tion meta­data for the reader in con­text, with­out forc­ing in­scrutable lookups buried deep at the end of the chap­ter (or worse, book) which few read­ers will ever bother with. (From pg61, “Lay­er­ing & Sep­a­ra­tion”, _En­vi­sion­ing In­for­ma­tion_, Tufte 1990)

[Don­ald Knuth ⁠](https://en.wikipedia.org/wiki/Donald_Knuth) uses mar­gin notes in [_Con­crete Math­e­mat­ics_ ⁠](https://en.wikipedia.org/wiki/Concrete_Mathematics) for a wide va­ri­ety of ‘math­e­mat­i­cal graf­fiti’ on the body con­tents: quotes from fa­mous peo­ple or just un­happy stu­dents, jokes, crit­i­cism, ques­tions to the reader, hints, etc. in his preprint drafts (‘fas­ci­cles’) of [_The Art of Com­puter Pro­gram­ming_ ⁠](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming) uses mar­gin notes as a kind of index, list­ing key­words in the mar­gin as re­minders for in­dex­ing in the final print ver­sion. The den­sity of key­words can make the mar­gins in­ter­est­ing to read on their own; an ex­am­ple from [TAOCP: pre- fascicle 4B: “A Draft of §7.2.1.7: His­tory of Com­bi­na­to­r­ial Gen­er­a­tion” ⁠](https://www.antiquark.com/blogimg/fasc4b.pdf):

![Margin notes showing keywords for discussion of Chinese/Indian algorithmic history in Knuth.](https://gwern.net/doc/design/typography/sidenote/2004-knuth-taocp-fascicle-4-b-historyofcombinatorialgeneration-iching-marginnotes.png)

Mar­gin notes show­ing key­words for dis­cus­sion of Chi­nese/ In­dian al­go­rith­mic his­tory in Knuth.

## Implementations

So, side­notes are great. They are also easy in L a T e X PDFs.⁠ [2](#fn:2) But how do we use them on­line for _HTML_?

Al­though side­notes are ‘just’ snip­pets of text to the left or right of the main text and it might seem hard to screw it up, as al­ways, there are a lot of ways to ac­com­plish that goal, and many ways we can en­hance (or screw up) them.

Do we put them on the left, right, or both sides? What of the sev­eral pos­si­ble HTML el­e­ments are our side­notes de­lim­ited as (`<span>`, `<a>`, `<div>`, [`<aside>` ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside), [`<small>` ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small), or even `<table>`)? Do we use Javascript, ac­cept­ing that it’ll ‘flash’ an in­cor­rectly ren­dered page as the JS loads & runs, and out­right break for users with JS turned off (as is in­creas­ingly sen­si­ble on an ever- more-hostile In­ter­net)? Does the user have to click or do any­thing to make side­notes vis­i­ble? If not, what about on mo­bile or tiny screens, which don’t _have_ any mar­gins worth speak­ing of—do they get side­notes in any form, and if so, do they ren­der ‘in­line’ as sim­ply part of their para­graph, or do we dis­play them as sep­a­rate blocks (‘pop- in’) and by de­fault or after a user click? How are many (or large, or both) side­notes laid out, do they bump each other down the page or just over­lap—it would seem that JS is nec­es­sary to avoid over­laps in most ap­proaches, but is that too great a price? How does one add side­notes sup­port to an ex­ist­ing body of doc­u­ments (typ­i­cally [Mark­down ⁠](https://en.wikipedia.org/wiki/Markdown))? Are there any known SEO con­cerns? (No, un­less you do it in a bizarre way.) And so on.

Over­all, I would say that good side­notes should ide­ally: ren­der on ei­ther both sides or the right (but not the left), use spans or links where pos­si­ble, use sta­tic HTML/ CSS, dis­play by de­fault (any user ef­fort de­feats the point!) but col­lapse to pop- ins (be­cause mo­bile users don’t have screen real es­tate to spare for op­tional ma­te­r­ial al­though many au­thors choose ex­panded) with in­line being an op­tion for mar­gin notes de­pend­ing on how the writer uses them, with side­notes over­lap­ping as a trade­off for not re­quir­ing JS (the au­thor will just have to rewrite such ex­ces­sive side­note usage to avoid over­lap­ping bugs), and end­notes in ex­ist­ing cor­puses can be rewrit­ten by what­ever tool com­piles the HTML into the ap­pro­pri­ate span en­cod­ing.

Below I com­pare im­ple­men­ta­tions I have found, and com­pile a table of what seems to me to be the key parts of the side­notes tax­on­omy.

My rec­om­men­da­tion is that for new or lightly- noted writ­ings, one use Tufte- CSS-style side­notes. For heavy side­note use, a JS so­lu­tion like `sidenotes.js` is prob­a­bly nec­es­sary.

## Comparisons

Table columns:

1.  **Name**: name/ cre­ator
    
2.  **Ac­tive**: whether ap­peared ac­tively main­tained when last checked (usu­ally ~2020)
    
3.  **Lay­out**: whether it puts notes in the left, right, or both mar­gins
    
4.  **Mar­gin Notes**: whether it ap­pears to sup­port mar­gin notes (side­notes with­out a num­ber & an­chor in­side the text, just free- floating text)
    
5.  **El­e­ment**: which HTML el­e­ment/ tag is used to de­note the side­note in the HTML source (eg. Mark­down puts in a `<a>` link­ing to a de­f­i­n­i­tion in the footer)
    
6.  **Non- JS**: whether Javascript re­quired (which is bad if it can be done with­out JS)
    
7.  **No Click**: whether the reader has to ef­fort­fully click on a note to see it (rather than vis­i­ble by de­fault or eas­ily seen with hover)
    
8.  **Mo­bile/ Nar­row**: how it han­dles mo­bile browsers and/ or nar­row screens (often the same)
    
9.  **Long Col­lapse**: how it han­dles long notes which would threaten to over­load the mar­gin and push notes ‘off- screen’
    
10.  **FLOSS**: whether OSI- approved copy­right li­cense
    
11.  **Pros/ Cons**: mis­cel­la­neous com­ments.
    

## Tufte-CSS

Ex­per­i­ments in using CSS3 for side­notes date back to at least 2003 22ya, but by far the most pop­u­lar im­ple­men­ta­tion, and the pri­mary in­spi­ra­tion for most side­notes users, is the c. 2014 11ya [Tufte- CSS ⁠](https://edwardtufte.github.io/tufte-css/#sidenotes) ([Github ⁠](https://github.com/edwardtufte/tufte-css)). Tufte- CSS is out­dated in re­spects, but does side­notes sen­si­bly:

![Tufte-CSS’s section on sidenotes/margin notes, demonstrating sidenotes/margin notes (default desktop appearance).](https://gwern.net/doc/design/typography/sidenote/2020-tuftecss-sidenotesmarginnotes.png)

Tufte- CSS’s sec­tion on side­notes/ mar­gin notes, demon­strat­ing side­notes/ mar­gin notes (de­fault desk­top ap­pear­ance).

![Tufte-CSS “pop-in” sidenotes, collapsed vs uncollapsed (on a narrow window or mobile)](https://gwern.net/doc/design/typography/sidenote/2020-tuftecss-sidenotesmarginnotes-mobilecollapsed.png)

Tufte- CSS “pop- in” side­notes, col­lapsed vs un­col­lapsed (on a nar­row win­dow or mo­bile)

A Tufte- CSS-formatted side­note looks like this:

```
<label for="sn-extensive-use-of-sidenotes" class="margin-toggle sidenote-number"></label>
 
<input type="checkbox" id="sn-extensive-use-of-sidenotes" class="margin-toggle">
 
<span class="sidenote">This is a sidenote.</span>
```

By de­fault (on desk­top), the notes are floated right into the mar­gin; no mea­sures are taken to avoid col­li­sions or over­laps (pre­sum­ably if you have that prob­lem, you ought to just rewrite your page or fix it your­self). On nar­row win­dows & mo­bile, a media- query over­rides the reg­u­lar CSS, so the mar­gin notes are not floated, sim­ply in­dented, and tog­gled. The CSS looks like:

```
.sidenote,
.marginnote {
    float: right;
    clear: right;
    margin-right: -60%;
    width: 50%;
    margin-top: 0.3rem;
    margin-bottom: 0;
    font-size: 1.1rem;
    line-height: 1.3;
    vertical-align: baseline;
    position: relative;
}
 
...
label.sidenote-number {
    display: inline;
}
 
label.margin-toggle:not(.sidenote-number) {
    display: none;
}
 
...
/* The mobile fallback: */
@media (max-width: 760px) {
    .sidenote,
        .marginnote {
            display: none;
        }
        .margin-toggle:checked + .sidenote,
        .margin-toggle:checked + .marginnote {
            display: block;
            float: left;
            left: 1rem;
            clear: both;
            width: 95%;
            margin: 1rem 2.5%;
            vertical-align: baseline;
            position: relative;
        }
}
```

Mar­gin notes are im­ple­mented sim­i­larly to side­notes be­cause a mar­gin note can just be a side­note whose num­ber is hid­den (at the pos­si­bil­ity of some user con­fu­sion at the ‘miss­ing’ end­note/ side­note, fix­able with fur­ther CSS tweaks using num­ber coun­ters).

One thing to note about Tufte- CSS is that, like books, it dis­plays side­notes by de­fault. Many web­sites ex­per­i­ment­ing with note vari­a­tions throw away the great­est ad­van­tage—the ef­fort­less­ness of read­ing side­notes by sim­ply sac­cad­ing left/ right—in favor of has­sling the user and forc­ing them to do quite as much work by click­ing var­i­ous UI el­e­ments to ex­pand/ col­lapse notes, de­feat­ing much of the point com­pared to a nor­mal hy­per­linked end­note.

Tufte- CSS re­quires no JavaScript and is pure HTML/ CSS, del­e­gat­ing lay­out to the browser. It is sim­ple, fast, sup­ports mo­bile well, and widely- used—it is def­i­nitely the most pop­u­lar of HTML side­note im­ple­men­ta­tions. Its dis­ad­van­tages are it will not han­dle grace­fully many com­plex⁠ [3](#fn:3) or lengthy side­notes (which will over­lap), and Tufte- CSS-style notes are not gen­er­ated by de­fault by many sys­tems (so some sort of rewrite step is nec­es­sary to in­te­grate Tufte- CSS into how­ever one ac­tu­ally cre­ates one’s web­site).

Be­cause Tufte- CSS side­notes/ mar­gin notes are lo­cated in­line, rather than put at the end of the text like most doc­u­ment sys­tems im­ple­ment it (eg. Pan­doc), one needs ei­ther to use JS to rewrite end­notes at run­time or to rewrite them at compile- time. Many projects gen­er­ate Tufte- CSS side­note spans di­rectly or rewrite stan­dard Mark­down `<a>` end­notes to spans, such as the R pack­ages [⁠“tufte” ⁠](https://cran.r-project.org/web/packages/tufte/index.html) & [⁠“Tint Is Not Tufte: An im­ple­men­ta­tion in R Mark­down”](https://eddelbuettel.github.io/tint/). For Pan­doc, [pandoc- sidenote ⁠](https://github.com/jez/pandoc-sidenote) is a [Haskell ⁠](https://en.wikipedia.org/wiki/Haskell) [⁠Pan­doc fil­ter ⁠](https://pandoc.org/filters.html) which rewrites Pan­doc’s end­notes in Tufte- CSS-style spans, and can be used with Pandoc- based site builders like Hakyll or Jekyll (for the lat­ter, see [tufte- pandoc-jekyll ⁠](https://github.com/jez/tufte-pandoc-jekyll) & [tufte- jekyll ⁠](https://github.com/clayh53/tufte-jekyll)); [Guil­laume Pau­mier ⁠](https://github.com/gpaumier/gp2/commit/6f132a4cc684df807b0f3b6ad9d337e073bc3260) & [⁠Matt Palmer](https://mattwetmore.me/posts/hakyll-custom-writer) have Lua ver­sions.

Tufte- CSS user ex­am­ples: [⁠Nico­las J. Du­quette](http://nicolasduquette.com/research.html), [⁠David Schmudde](https://schmud.de/posts/2020-08-04-mother-of-mothers.html), [⁠in He­brew](https://digitalwords.net/about/), [⁠Robin Schroer](https://blog.sulami.xyz/posts/common-lisp-restarts/), [⁠Dan Pittman](https://blog.auxon.io/2019/10/25/type-level-registers/), [⁠Jason Mer­rill](https://www.shapeoperator.com/2016/12/12/sunset-geometry/), [⁠An­drew Zuck­er­man](https://andzuck.com/blog/sfw/), [⁠Taeer Bar- Yam](https://taeer.bar-yam.me/blog/posts/hakyll-tikz/), [⁠Eric Mars­den (_Risk En­gi­neer­ing_)](https://risk-engineering.org/concept/Rasmussen-practical-drift), [⁠Tom Critchlow](https://tomcritchlow.com/2019/11/18/yes-and/), [⁠Phil Criss­man](http://philcrissman.net/posts/eulers-fizzbuzz/).

Sim­i­lar ap­proaches (some of these are more lim­ited than Tufte- CSS; typ­i­cally, au­thors fail to han­dle nar­row/ mo­bile):

-   [“How can we de­velop trans­for­ma­tive tools for thought?” ⁠](https://numinous.productions/ttft/), [⁠Andy Ma­tuschak](https://andymatuschak.org/) & [⁠Michael Nielsen ⁠](https://michaelnielsen.org/) 2019 (mo­bile: float­ing foot­notes)
    
-   [Arxiv Van­ity](https://www.arxiv-vanity.com/) (mo­bile: float­ing foot­notes)
    
-   [⁠Nin­til ⁠](https://nintil.com/science-ending-frontier) (mo­bile: pop- in, ex­panded)
    
-   [⁠Danila Fe­dorin’s](https://danilafe.com/blog/sidenotes/) side­notes (mo­bile: pop- in, col­lapsed) are in­spired by Koos Looi­jesteijn’s ap­proach, Fe­dorin’s im­ple­men­ta­tion re­moves the JS but at the cost of guar­an­tee­ing ac­ces­si­bil­ity and in­her­it­ing Tufte- CSS’s lim­i­ta­tions on block el­e­ments/ Mark­down in side­notes
    
-   [“What does BERT dream of?”](https://pair-code.github.io/interpretability/text-dream/blogpost/) (mo­bile: pop- in, ex­panded)
    
-   [_⁠In­cre­ment_](https://increment.com/open-source/the-rise-of-few-maintainer-projects/) (mo­bile: pop- in, ex­panded)
    
-   [⁠Matt Wilcox](https://mattwilcox.net/musing/the-ineffectiveness-of-icons), with an un­usual use of mar­gin notes for para­graph/ sec­tion _sum­maries_, sim­i­lar to my use (mo­bile: pop- in, ex­panded)
    
-   [⁠“Dic­tio­nary of Num­bers”](http://glench.com/closed-source/dictionaryofnumbers/), Glen Chi­ac­chieri (mo­bile: ❌)
    
-   [⁠Roman Gor­nit­sky (The Tem­po­rary State)](https://letters.temporarystate.net/entry/3/) (mo­bile: ❌)
    
-   [⁠Richard Rut­ter](https://clagnut.com/blog/2395) (mo­bile: pop- in, ex­panded)
    
-   [“Sin­gu­lar: Pos­si­ble fu­tures of the sin­gu­lar­ity”](https://jamesyu.org/singular/), James Yu & [GPT-3 ⁠](https://arxiv.org/abs/2005.14165#openai) (mo­bile: click- to-expand as a sticky pop- up)
    
-   [⁠“The Prob­lem of De­tect­ing Poly­genic Se­lec­tion from Tem­po­ral Data”](https://vincebuffalo.com/blog/2020/08/20/the-problem-of-detecting-polygenic-selection-from-temporal-data.html), Vince Buf­falo (mo­bile: pop- in, ex­panded)
    
-   [⁠“How to do side­notes in HTML doc­u­ments using CSS and Javascript”](https://fransdejonge.com/wp-content/uploads/2010/01/sidenotes.html), Frans de Jonge 2005 (an early ex­am­ple, with con­sid­er­a­tion of cross- browser com­pat­i­bil­ity for the era)
    
-   [⁠Omar Rizwan](https://omar.website/posts/against-recognition/) (Hugo)
    
-   [Dar­ius Kazemi/ Emma Win­ston](https://runyourown.social/) (‘mar­gin notes’, no ap­par­ent use of num­ber­ing to sup­port ‘side­notes’; nice retro theme; `<aside>`; pop- in, ex­panded; no trun­ca­tion/ wrap­ping; ab­solute po­si­tion­ing off­set based on div around as­so­ci­ated para­graph, so can’t han­dle over­laps which leads to bugs as [⁠can be seen ⁠](https://gwern.net/doc/design/typography/sidenote/2022-10-31-dariuskazemi-runyourownsocial-exampleofoverlappingsidenotesbug.png) in that page; ap­par­ently ex­tra­ne­ous use of grid?)
    
-   [⁠Vale](https://verdagon.dev/blog/perfect-replayability-prototyped) (no­table for strange han­dling of mo­bile: the side­notes are hid­den and their foot­note num­bers left in place, by being moved to the end of a sec­tion and grouped in a sin­gle list while being col­lapsed; click­ing or tap­ping the foot­note jumps to the end- block but does _not_ ex­pand them, and they must be clicked on to ex­pand them all.)
    
-   [Tyler Vigen ⁠](https://tylervigen.com/the-mystery-of-the-bloomfield-bridge): pop- in-only; tooltips used for ‘hover’, which is a bad idea⁠ [4](#fn:4)
    
-   [xkqr](https://entropicthoughts.com/markov-chains-for-queueing-systems) (input check­box mo­bile ap­proach)
    
-   ex­am­ples with **no mo­bile** (❌) sup­port:
    
    -   [⁠Hoe­fler&Co.](https://www.typography.com/blog/text-for-proofing-fonts)
        
    -   [⁠Michael Pe­tralia](http://www.michaelpetralia.com/theartofliving_epictetus.html)
        
    -   The Morn­ing After Word­Press tem­plate’s “asides” ([ex­am­ple](https://thecityasaproject.org/2020/05/a-pilgrimage-round-my-room-virtual-travel-to-the-holy-land-in-the-middle-ages/))
        
    -   [⁠Francesco](https://mazzo.li/posts/vectorized-atan2.html) (over­loads `<section>` & man­u­ally over­rides list mark­ers for num­ber­ing for one sec­tion per side­note, with frag­ile grid de­fault po­si­tion­ing; mo­bile is just desk­top but made mi­cro­scopic)
        

## sidenotes.js

[`⁠sidenotes.js` ⁠](https://gwern.net/static/js/sidenotes.js) was de­vel­oped by [⁠Said Achmiz](https://wiki.obormot.net/) in 2019 for use on Gwern.net after look­ing at Tufte- CSS and de­cid­ing that Tufte- CSS’s sim­ple ap­proach (while ap­pro­pri­ate for most users) would fail on particularly- heavily end­noted pages:

![Demonstration of sidenotes.js handling multiple large dense endnote annotations on Radiance.](https://gwern.net/doc/cs/css/sidenotes.png)

Demon­stra­tion of `sidenotes.js` han­dling mul­ti­ple large dense end­note an­no­ta­tions on [_Ra­di­ance_ ⁠](https://gwern.net/doc/radiance/2002-scholz-radiance).

![Pop-in of footnotes (handled by extracts.js/popins.js as a special-case of generalized annotations).](https://gwern.net/doc/design/2021-03-30-gwern-sidenotes-gwernnet-popins.png)

Pop- in of foot­notes (han­dled by `extracts.js` / `popins.js` as a special- case of gen­er­al­ized an­no­ta­tions).

The ad­van­tage over Tufte- css is that `sidenotes.js` ‘man­u­ally’ lays out side­notes at run­time to min­i­mize over­lap while try­ing to keep side­notes within the same win­dow as the an­chor, en­abling it to han­dle al­most ar­bi­trar­ily many long end­notes with­out ren­der­ing any un­read­able. Side­notes/ end­notes can be ar­bi­trar­ily long and con­tain most block el­e­ments like code blocks, block­quotes, lists, im­ages, ta­bles, etc. While it’s at it, side­notes are high­lighted & their match­ing an­chors high­lighted on hover, too- long side­notes are par­tially col­lapsed (the user clicks to ex­pand them). Fur­ther, it sup­ports a cus­tom “mar­gin note” fea­ture: any HTML spans of text with the class `marginnote` will be popped out of the text into the mar­gin if there is room, or it will be left in place & ital­i­cized. (I place mar­gin notes at the be­gin­ning of para­graphs as sum­maries, let­ting users more eas­ily skim.) Fi­nally, as a bit of an easter egg in­spired by [`xeyes` ⁠](https://en.wikipedia.org/wiki/Xeyes), the side­note return- to-anchor ar­rows are an­gled up or down so as to point to the orig­i­nal link in the body.

The dis­ad­van­tage com­pared to pure sta­tic HTML/ CSS ap­proaches is that the JS needs to load and copy the end­notes into side­notes, re­flow as nec­es­sary over the whole page, which is user- visible & dis­tract­ing; this is no­tice­able even putting the load in the HEAD to speed it up. It can also in­ter­act with other com­pli­cated fea­tures and while it will han­dle heavy note loads much bet­ter than most sta­tic ap­proaches (most of which don’t even try to avoid er­rors like over­laps), it still has the oc­ca­sional sub­tle bug.

For nar­row win­dows, other ap­proaches can be used. On Gwern.net, I use [float­ing foot­notes ⁠](https://gwern.net/static/js/popups.js) which ‘pop up’ when the user hov­ers over a foot­note an­chor⁠ [5](#fn:5), which avoids the need to nav­i­gate to the end of the page & back.

`sidenotes.js` as­sumes that the doc­u­ment has been gen­er­ated from Pan­doc Mark­down and has nor­mal Pan­doc end­notes (of the form `<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>` for the an­chor, and `<li id="fn1" role="doc-endnote"><p>Example</p></li>` for the end­note body at the end of the doc­u­ment). Hence, im­ple­ment­ing side­notes with it re­quires lit­tle more than a JS im­port like `<script src="/static/js/sidenotes.js" async></script>`. (This has some ad­van­tages: for ex­am­ple, foot­notes/ side­notes re­main link­able—one can link to `#fn1` or `#sn1` as de­sired.⁠ [6](#fn:6))

Users or sim­i­lar im­ple­men­ta­tions:

-   [Fan­tas­tic Anachro­nism](https://fantasticanachronism.com/2020/01/17/having-had-no-predecessor-to-imitate/index.html)
    
-   Leo Gao (eg. [⁠1](https://bmk.sh/2019/10/27/The-Difficulties-of-Text-Generation-with-Autoregressive-Language-Models/), [⁠2](https://bmk.sh/2020/05/29/GPT-3-A-Brief-Summary/)) de­signed his site in­spired a lit­tle by Gwern.net, and uses side­notes sim­i­larly; his ap­proach seems to be sim­pler. (mo­bile: end­notes)
    
-   Ope­nAI (eg. [1 ⁠](https://openai.com/research/how-ai-training-scales)) (mo­bile: end­notes)
    
-   [⁠Mar­shall (Van­de­grift) Bock­rath](http://blog.platypope.org/2010/1/7/solving-puzzles-with-computer-science/), from [⁠pre-2012](http://blog.platypope.org/2012/4/5/restore-features/)! (mo­bile: ❌)
    

## Ink & Switch

[⁠Ink & Switch’s](https://www.inkandswitch.com/index.html) pages like [“Local- first soft­ware: You own your data, in spite of the cloud”’s](https://www.inkandswitch.com/local-first.html) 2016 sta­tic mar­gin notes fea­ture looks much like Tufte- CSS in using HTML/ CSS to cre­ate right- aligned side­notes, al­though Ink & Switch es­chews ex­plicit foot­note num­ber­ing and its pop- ins are un­col­lapsed by de­fault.

![Ink & Switch, “Local-first software” margin notes](https://gwern.net/doc/design/typography/sidenote/2016-inkandswitch-localfirstdesign-marginnotes.png)

Ink & Switch, “Local- first soft­ware” mar­gin notes

![Ink & Switch, “Local-first software” margin notes, mobile (pop-in, default expanded)](https://gwern.net/doc/design/typography/sidenote/2016-inkandswitch-localfirstdesign-marginnotes-mobile.png)

Ink & Switch, “Local- first soft­ware” mar­gin notes, mo­bile (pop- in, de­fault ex­panded)

Implementation- wise, it takes a no­tice­ably dif­fer­ent tack in which CSS fea­tures it uses. The HTML it­self is just an `<aside>` el­e­ment:

```
<aside><p><a href="https://ourincrediblejourney.tumblr.com/">Our incredible journey</a>
    is a blog that documents startup products getting shut down after an acquisition.</p></aside>
```

But [their CSS](https://gitlab.developers.cam.ac.uk/cst/dtg/trvedata/local-first/-/commit/7a8819e817a85173af7033e64bcdcc5054b9af50?expanded=1#e74ca419c79e4a87cb170f6eb8a6c0d2719e1c73_0_726) uses [`calc()` ⁠](https://developer.mozilla.org/en-US/docs/Web/CSS/calc) ex­ten­sively to cre­ate po­si­tion­ing & read­just over­laps with­out JS:

```
article aside, figcaption, header>#byline {
  --aside-offset: 1rem;
  --aside-offset-lineheight: 1.5rem;
  box-sizing: border-box;
  margin-bottom: calc(var(--padding) * 2);
  padding: var(--padding);
  position: absolute;
  right: 0;
  width: var(--aside-width);
}
 
aside, figcaption, figure img, figure video {
  border-radius: calc(var(--padding)/4);
  max-width: 100%;
}
 
aside, aside>*, #byline, #byline li, figcaption, figcaption>*, blockquote footer {
  font-size: 0.8125rem;
  font-weight: 400;
  -ms-hyphens: none;
  -webkit-hyphens: none;
  hyphens: none;
  line-height: 1.25rem;
  margin-bottom: 0.5rem;
  text-align: left;
}
 
...
/* aside and figcaption nudge ---------------- */
 
/* using these can cause overlapping of elements. if you apply to one aside, you may
    need to apply and adjust other that precede clearing the blocks figcaption or section */
 
.move-up-1 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*1))/-1);
}
 
.move-up-2 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*2))/-1);
}
...
.move-up-25 {
  margin-top: calc((var(--aside-offset) + (var(--aside-offset-lineheight)*25))/-1);
}
```

One down­side is that there is no sup­port for num­ber­ing I can see, so they’re all mar­gin notes. The CSS is con­sid­er­ably more com­plex and I’m not sure what the com­plex­ity gains one com­pared to Tufte- CSS—cor­rect­ness?

## Robert Nystrom

Game pro­gram­mer Robert Ny­s­trom’s 2014 book [_⁠Game Pro­gram­ming Pat­terns_ ⁠](https://gameprogrammingpatterns.com/), makes heavy use of side­notes im­ple­mented in HTML/ CSS/ JS, mostly sim­i­lar to Tufte- CSS.

![Game Programming Patterns, desktop sidenotes](https://gwern.net/doc/design/typography/sidenote/2013-robertnystrom-gameprogrammingpatterns-doublebuffer-sidenotes.png)

_Game Pro­gram­ming Pat­terns_, desk­top side­notes

![Game Programming Patterns, mobile (inline, expanded by default)](https://gwern.net/doc/design/typography/sidenote/2013-robertnystrom-gameprogrammingpatterns-doublebuffer-sidenotes-mobile.png)

_Game Pro­gram­ming Pat­terns_, mo­bile (in­line, ex­panded by de­fault)

He takes a dif­fer­ent ap­proach: side­notes are writ­ten using the HTML `<aside>` el­e­ment, and a `<span>` with each aside’s ID spec­i­fies their place­ment in the text; [⁠the JS ⁠](https://gameprogrammingpatterns.com/script.js) then moves the aside into the mar­gin. He de­signed it to han­dle re­siz­ing below <800px not by pop- in foot­notes in a block, but by media- queries sim­ply shift­ing the aside into the text, in­line. (With no JS, the fall­back is also in­clud­ing it in­line.)

```
<p>Let&#8217;s say we want a happy face to appear on screen. Our program starts looping
through the framebuffer, coloring pixels. What we don&#8217;t realize is that the
video driver is pulling from the framebuffer right as we&#8217;re writing to it. As it
scans across the pixels we&#8217;ve written, our face starts to appear, but then it
outpaces us and moves into pixels we haven&#8217;t written yet. The result is
<em>tearing</em>, a hideous visual bug where you see half of something drawn on screen.</p>
<p><span name="tearing"></span></p>
<p><img src="images/double-buffer-tearing.png" alt="A series of images of an in-progress frame
    being rendered. A pointer writes pixels while another reads them. The reader outpaces the writer
    until it starts reading pixels that haven't been rendered yet."></p>
<aside name="tearing">
 
<p>We start drawing pixels just as the video driver starts reading from the
framebuffer (Fig. 1). The video driver eventually catches up to the renderer and
then races past it to pixels we haven&#8217;t written yet (Fig. 2). We finish drawing
(Fig. 3), but the driver doesn&#8217;t catch those new pixels.</p>
<p>The result (Fig. 4) is that the user sees half of the drawing. The name
&#8220;tearing&#8221; comes from the fact that it looks like the bottom half was torn off.</p>
</aside>
```

```
@media only screen and (min-width: 800px) {
  .page {
    padding-right: 300px; }
 
  aside {
    position: absolute;
    width: 240px;
    right: 30px;
    padding: 0;
    background: none;
    border: none;
    padding-left: 22px;
    border-radius: 0;
    border-left: solid 8px #f0e9db; }
  aside p, aside li {
      font: 14px/20px "Source Sans Pro", "Lucida Grande", "Lucida Sans Unicode", Verdana, sans-serif; } }
```

It’s un­clear to me whether the JS is nec­es­sary, or whether in­line is the best fall­back for side­notes. The use of `<aside>` is also a com­pli­ca­tion, as few for­mats in­clude any na­tive sup­port for that.

Ny­s­trom’s books are an in­ter­est­ing read for pro­gram­mers, and also have some other in­ter­est­ing de­sign as­pects: see [⁠“Zero to 95,688: How I wrote _Game Pro­gram­ming Pat­terns_ ”](https://journal.stuffwithstuff.com/2014/04/22/zero-to-95688-how-i-wrote-game-programming-patterns/) / [⁠“Craft­ing _Craft­ing In­ter­preters_ ”](https://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/) on the build sys­tem & lit­er­ate pro­gram­ming & his hand- drawn il­lus­tra­tion work­flow; & [⁠“Zero to 353 Pages: Bring­ing My Web Book to Print and eBook”](https://journal.stuffwithstuff.com/2014/11/03/bringing-my-web-book-to-print-and-ebook/) on work­ing with EPUB & type­set­ting the print book.

## Matthew Butterick

[Matthew But­t­er­ick’s ⁠](https://en.wikipedia.org/wiki/Matthew_Butterick) 2013 12ya ebook/ web­site [_Prac­ti­cal Ty­pog­ra­phy_](https://practicaltypography.com/) uses mar­gin notes, but in a side­notes way, on the left:

![Margin note left in Practical Typography.](https://gwern.net/doc/design/typography/sidenote/2013-matthewbutterick-practicaltypography-webemailaddresses-marginnote.jpg)

Mar­gin note left in [_Prac­ti­cal Ty­pog­ra­phy_](https://practicaltypography.com/web-and-email-addresses.html).

They fall­back to pop- ins de­faulted to ex­panded on nar­row/ mo­bile win­dows:

![The same margin note, on a narrow window: it now appears as a pop-in block element, but expanded without the user needing to click (as they would in Tufte-CSS).](https://gwern.net/doc/design/typography/sidenote/2013-matthewbutterick-practicaltypography-webemailaddresses-marginnote-mobile.png)

The same mar­gin note, on a nar­row win­dow: it now ap­pears as a pop- in block el­e­ment, but ex­panded with­out the user need­ing to click (as they would in Tufte- CSS).

The ap­proach is HTML/ CSS, but using `<aside>` el­e­ments, which are styled in CSS:

```
title-block, aside {
    display: block;
    float: left;
    position: absolute;
    margin-left: 0;
    left: 2.5rem;
    width: calc(2.5rem * 3);
    text-align: right;
    list-style-type: none;
    clear:both; margin-bottom: 1rem;
    font-variant-numeric: normal;
}
 
@media all and (min-width:1200px) {
    aside {
        left : 0;
        width: calc(2.5rem * 4);
    }
}
 
@media all and (max-width:520px) {
    title-block, aside { float: inherit;
    position: inherit;
    width: 100%;
    text-align: left;}
 
    aside {
        background: #fefefe;
        padding: 0.3rem 0.5rem;
        width: 90%;
        border: 1px solid #ccc;
        border-left: 3px solid #ccc;
    }
 
    aside > p:last-child {
        margin-bottom: 0;
    }
}
```

Pre­sum­ably But­t­er­ick used his Racket- based [Pollen doc­u­ment sys­tem](https://docs.racket-lang.org/pollen/) with cus­tom tags, since the base sys­tem doesn’t cover notes; [⁠San­cho Mc­Cann](https://sanchom.github.io/pollen-footnotes.html) & [⁠Jonas Hi­etala](https://www.jonashietala.se/blog/2019/03/04/pollen_sidenotes/) has doc­u­mented Pollen side­notes.

## Koos Looijesteijn

[⁠Koos Looi­jesteijn’s](https://www.kooslooijesteijn.net/) loosely Tufte- CSS-like side­notes are right- aligned, sym­bol rather than num­ber in­cre­mented, and nar­row/ mo­bile col­lapsed pop- ins:

![KL, desktop](https://gwern.net/doc/design/typography/sidenote/2019-looijesteijn-sidenotes.png)

KL, desk­top

![KL, mobile (pop-in clicked)](https://gwern.net/doc/design/typography/sidenote/2019-looijesteijn-sidenotes-mobile.png)

KL, mo­bile (pop- in clicked)

In [⁠“Se­man­tic side­notes for the web”](https://www.kooslooijesteijn.net/blog/semantic-sidenotes) 2019, he dis­cusses his ap­proach, in­tended to sat­isfy ad­di­tional re­quire­ments:

> -   The span that the side­note refers to should have a proper se­man­tic HTML el­e­ment (no abuse of el­e­ments made for other pur­poses)
>     
> -   The con­tent of the side­note should have a sim­i­larly valid HTML tag. Ad­di­tion­ally:
>     
>     -   The side­note con­tent may con­tain span el­e­ments such as `<a>` and `<em>`.
>         
>     -   The side­note con­tent may con­tain click­able el­e­ments that can re­ceive key­board focus.
>         
>     -   The side­note con­tent must be sty­lable.
>         
> -   The el­e­ments should not cause auto clos­ing of their par­ent `<p>` tag.
>     
> -   Reader modes and apps like Pocket and RSS read­ers should show side­note con­tent in a ty­po­graph­i­cally ac­cept­able way. That means at the very least that I can’t rely on web­site’s CSS to place and style the el­e­ments cor­rectly.
>     
> -   The side­note con­tent should be read by screen read­ers, in a flow that makes sense. That likely means the two parts should be placed to­gether.
>     

He came up with some­thing ini­tially like Tufte- CSS, but re­jected pure `<span>`, `<aside>` as being not quite the right se­man­tics, purely sta­tic as break­ing reader mode/ apps, and set­tled on JS- enhanced `<span>` / `<small>` com­bi­na­tion.

## Harvard Law Review

The [Har­vard Law Re­view’s ⁠](https://en.wikipedia.org/wiki/Harvard_Law_Review) web­site has, since at least 2016, em­ployed side­notes, as is par­tic­u­larly ap­pro­pri­ate for legal writ­ing, which no­to­ri­ously overuses foot­notes for ci­ta­tions, prece­dents, and di­gres­sions. From [“The Potential- Use Test and the North­west Pas­sage”](https://harvardlawreview.org/print/vol-133/the-potential-use-test-and-the-northwest-passage/) (HLR ed­i­tors 2020):

![HLR, desktop; note the default collapse/fade](https://gwern.net/doc/design/typography/sidenote/2020-harvardlawreview-sidenotes.png)

HLR, desk­top; note the de­fault col­lapse/ fade

![HLR, mobile (pop-in on click)](https://gwern.net/doc/design/typography/sidenote/2020-harvardlawreview-sidenotes-mobile.png)

HLR, mo­bile (pop- in on click)

HLR’s pro­pri­etary are bidi­rec­tional, JS- based, and col­lapsed pop- in on mo­bile; they use `<span>` s which are re­arranged by the JS:

```
Canada, on the other hand, asserts that the Northwest Passage constitutes internal waters and does
not fall under any definition of international strait.
<sup class="footnote-ref js-article-aside-trigger "><i class="ref-txt">2</em><i class="close-txt">&times;</em></sup>
<cite class="article-aside footnote short-crop">
    <span class="article-aside-txt">
        <span class="footnote-num">2.</span>
        <em>See</em> Territorial Sea Geographical Coordinates (Area 7) Order, SOR/1985-872 (Can.) (detailing Canada’s
        claims to land and waters that include the Northwest Passage); Note from the Canadian Embassy, Washington, D.C.,
        to the U.S. Department of State (June 11, 1985), <em>reprinted in</em> 2 <span class="small-caps">Marion Nash (Leich),
        Dep’t of State, Cumulative Digest of United States Practice in International Law 1981–1988</span>, at 2047 (1994).
    </span>
</cite>
```

Since it uses in­line `<span>` in the usual Tufte- CSS, one might won­der why the JS is nec­es­sary, but check­ing with No­Script, one sees that with­out the JS, the side­notes are all piled up on the left mar­gin, over­lap­ping badly, so the JS does the ‘al­ter­nat­ing’. (Is it pos­si­ble to use CSS to do this al­ter­na­tion au­to­mat­i­cally, re­mov­ing the need for JS to do bidi­rec­tional side­notes?)

More dis­tress­ingly, HLR’s side­notes are also on de­fault col­lapsed on _desk­top_, trimmed at a shock­ingly short length—typ­i­cally not even half a sen­tence! While col­laps­ing long foot­notes is a good idea, it’s puz­zling to col­lapse at such a short length that lit­er­ally every side­note will be col­lapsed, since this again de­feats the point of hav­ing side­notes, and mak­ing it hard to see if a side­note is worth click­ing on since only the first few words are ex­posed so one can­not even see if the side­note is short (merely a bit of ci­ta­tion) or long (a more in- depth dis­cus­sion).

## Yale Law Journal

The [_Yale Law Jour­nal_ ⁠](https://en.wikipedia.org/wiki/The_Yale_Law_Journal), like HLR, uses side­notes in on­line ar­ti­cles like [⁠“Ama­zon’s An­titrust Para­dox”](https://www.yalelawjournal.org/note/amazons-antitrust-paradox) (Khan 2017), since at least 2016. Like HLR, all side­notes are ag­gres­sively col­lapsed to near- unreadability, re­quir­ing a click to ex­pand, where­upon they turn into float­ing foot­notes.

![YLJ, default desktop](https://gwern.net/doc/design/typography/sidenote/2017-yalelawjournal-khan-sidenotes.png)

YLJ, de­fault desk­top

![YLJ, sidenotes clicked on to expand](https://gwern.net/doc/design/typography/sidenote/2017-yalelawjournal-khan-sidenotes-expanded.png)

YLJ, side­notes clicked on to ex­pand

They are JS- based, re­lo­cat­ing foot­notes grouped at the end of the ar­ti­cle, but in­side `<div>` el­e­ments rather than `<a>` el­e­ments like usual:

```
<div id="footnote_wrapper" style="position:relative;">
    <div id="footnote_1" style="display:none;" class="footnote_truncated">
        <div class="truncated_footnote_number">1</div>
        <div class="truncated_footnote_inner"><span> </span>David <span class="SpellE">Streitfeld</span>,
            <em>As Competition Wanes, Amazon Cuts Back Discounts</em>,
            <span class="forced_sans_reg">N.Y. Times</span> (July 4, 2013), http&hellip;
            </div>
    </div>
...</div>
```

Worse, YLJ ap­pears to have no nar­row or mo­bile sup­port what­so­ever—the page just gets smaller. YLJ is un­read­able on mo­bile, re­quir­ing zoom­ing & pan­ning.

## Knight Institute

The [⁠Knight First Amend­ment In­sti­tute](https://knightcolumbia.org/page/about-the-knight-institute) of [Co­lum­bia Uni­ver­sity ⁠](https://en.wikipedia.org/wiki/Columbia_University) uses side­notes some­what like HLR/ YLJ in its long­form pages (eg. [⁠“The Case for Dig­i­tal Pub­lic In­fra­struc­ture: Har­ness­ing past suc­cesses in pub­lic broad­cast­ing to build community- oriented dig­i­tal tools”](https://knightcolumbia.org/content/the-case-for-digital-public-infrastructure), Zuck­er­man 2020):

![Knight Institute sidenotes (not expanded)](https://gwern.net/doc/design/typography/sidenote/2020-knightinstitute-zuckerman-sidenotes.png)

Knight In­sti­tute side­notes (not ex­panded)

They are JS- based, right- aligned, col­lapsed (but with a slightly more gen­er­ous length limit than HLR/ YLJ), and fall­back to Tufte- CSS-like pop- in blocks (de­fault col­lapsed). As sim­i­lar as it seems to those, Knight ap­pears to have rolled its own JS, as the `site.js` ’s im­ple­men­ta­tion doesn’t have any Google/ [Github ⁠](https://en.wikipedia.org/wiki/GitHub) hits.

The fad­ing, font size, and de­fault col­laps­ing of ‘long’ side­notes are all not nearly as ex­treme as HLR/ YLJ, so the Knight side­notes are sub­stan­tially more pleas­ant to read, as it’s much eas­ier to see what side­notes are merely a brief ci­ta­tion and what ac­tu­ally in­clude ad­di­tional com­men­tary. (The use of but­tons & chevrons are also nice touches in ex­plain­ing the func­tion­al­ity to the reader.)

## New York

[_New York_ ’s ⁠](https://en.wikipedia.org/wiki/New_York_\(magazine\)) web­site CMS [Clay/ Kiln ⁠](https://github.com/clay) (used on NYmag.com/ Vul­ture/ the Cut/ Grub Street/ Slate) pro­vide JS- based left side­notes which re­quire hover to ex­pose and then fall back to click- driven float­ing foot­notes:

![Vulture, desktop (on hover)](https://gwern.net/doc/design/typography/sidenote/2020-newyork-vulture-chrisrockinterview-sidenotes.png)

_Vul­ture_, desk­top (on hover)

![Vulture, mobile (after clicking)](https://gwern.net/doc/design/typography/sidenote/2020-newyork-vulture-chrisrockinterview-sidenotes-mobile.png)

_Vul­ture_, mo­bile (after click­ing)

NY uses spans, but they are put at the end and then JS re­veals them when the user hov­ers:

```
<span class="clay-annotated kiln-phrase" aria-describedby="annotation-1" tabindex="0">Virgin Airlines first-class lounge</span>
...
<div data-uri="www.vulture.com/_components/annotations/instances/cjg2jwsso00c23k62pm0yv0qg@published"
     class="annotations" data-editable="content">
    <span role="tooltip" id="annotation-1" data-uri="www.vulture.com/_components/annotation/instances/cjg2jx3el00c73k62em8v15xy@published"
       class="annotation" data-editable="text">
       Offers spa treatments, “expert mixologists”, and, at Heathrow, a “lodge and viewing deck” with an “après-ski vibe.”
   </span>
</div>
```

I couldn’t find men­tion of side­notes in the var­i­ous Clay/ Kiln Github repos but there are enough of them and it’s all com­pli­cated enough I may have missed them, so I don’t know if the rel­e­vant JS/ CSS is MIT- licensed like the Clay/ Kiln ecosys­tem gen­er­ally seems to be.

While float­ing foot­notes on mo­bile is a jus­ti­fi­able choice, the rest is not, and I do not like this side­note de­sign at all.

## JQuery.sidenotes

An­drew Clark’s 2013 [⁠jQuery.side­notes](https://acdlite.github.io/jquery.sidenotes/) ([Github ⁠](https://github.com/acdlite/jquery.sidenotes)) JS li­brary im­ple­ments side­notes to the left, pars­ing Mark­down end­notes; for nar­row win­dows, it does in­lined ‘pop- in’ but ex­panded by de­fault; and for mo­bile it is just end­notes. Un­usu­ally, Clark’s demo puts side­notes on the _left_ mar­gin (there doesn’t seem to be an op­tion for plac­ing on the right, or both), and in­cludes some key­bind­ings.

![jQuery.sidenotes (default desktop appearance)](https://gwern.net/doc/design/typography/sidenote/2013-clark-jquerysidenotes-sidenotes.png)

jQuery.side­notes (de­fault desk­top ap­pear­ance)

The pop- in ap­pear­ance looks like Tufte- CSS’s.

The im­ple­men­ta­tion seems to take the ex­pected ap­proach of pop­ping match­ing el­e­ments out into the mar­gin with media queries con­trol­ling width- related be­hav­ior.

Clark’s jQuery.side­notes of­fers more fea­tures than usual, but I’m not sure how use­ful they are. It’s also quite ‘heavy­weight’ in being weighed down by jQuery/ NPM in­fra­struc­ture. One fur­ther caveat: I think the ex­pected for­mat/ classes of end­notes has long since changed and the li­brary has not been up­dated since 2013 12ya, at least for Pan­doc, so jQuery.side­notes’s de­faults will prob­a­bly break for re­cent Mark­down doc­u­ments.

## Sidenotes.js, Correia

Bruno Cor­reia’s 2015 [⁠Side­notes.js](http://bcorreia.com/projects/sidenotes.js/src/demo.html) ([Github ⁠](https://github.com/bcorreia/sidenotes.js)), not to be con­fused with Said Achmiz’s [`⁠sidenotes.js` ⁠](https://gwern.net/sidenote#sidenotes-js), takes an en­tirely dif­fer­ent ap­proach to both pre­sen­ta­tion & en­cod­ing of side­notes. In­stead of reusing the ex­ist­ing mar­gin, Side­notes.js cre­ates a new view by _slid­ing_ a sticky- element ‘tab’ into view with the side­note con­tents, hid­ing the orig­i­nal page:

![Sidenotes.js, before/after clicking on an annotated link (desktop)](https://gwern.net/doc/design/typography/sidenote/2015-correia-sidenotes-slide.png)

Side­notes.js, be­fore/ after click­ing on an an­no­tated link (desk­top)

On nar­row or mo­bile, the slid- in new page just takes up the whole screen.

The an­no­ta­tions are them­selves writ­ten as [cus­tom data at­trib­utes ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*) on el­e­ments such as links (by de­fault, oth­ers are sup­ported):

```
<p>While the two headsmen were engaged in making fast cords to his flukes,
and in other ways getting the mass in readiness for towing,
some <a
    href="#"
    data-sidenote="&gt;strong&lt;Conversation:&gt;/strong&lt; the informal exchange of ideas by spoken words:
                   'the two men were deep in conversation'.">
    conversation</a>
ensued between them.</p>
```

This is a unique ap­proach en­tirely un­like the oth­ers and an in­ter­est­ing ex­per­i­ment, but I do not rec­om­mend it for side­notes.

## The India Forum

[_⁠The India Forum_](https://www.theindiaforum.in/article/revolt-upper-castes) uses jQuery for a slide- in ap­proach but im­proves over Cor­reia’s by show­ing all the side­notes in a pane after click­ing:

![TIF, after clicking on footnotes](https://gwern.net/doc/design/typography/sidenote/2020-theindiaforum-revoltoftheuppercastes-sidenotes.png)

TIF, after click­ing on foot­notes

The ‘slide- in’ ap­proach can be con­trasted with the ‘slide- up’ ap­proach used by Wikipedia:

![Screenshot of Artemy Vedel WP article after tapping a footnote in a mobile browser, showing a faded body and a highlighted footnote section which has ‘slid up’; this shows the footnote text (usually a brief citation) without shifting the overall layout or being too small to read.](https://gwern.net/doc/design/typography/sidenote/2023-02-23-wikipedia-mobilemode-tappedfootnoteslideupexample.png)

Screen­shot of [Artemy Vedel ⁠](https://en.wikipedia.org/wiki/Artemy_Vedel) WP ar­ti­cle after tap­ping a foot­note in a mo­bile browser, show­ing a faded body and a high­lighted foot­note sec­tion which has ‘slid up’; this shows the foot­note text (usu­ally a brief ci­ta­tion) with­out shift­ing the over­all lay­out or being too small to read.

And some other sites, like [Justin Duke](https://www.arcana.computer/):

![A tapped ‘footnote’ on Justin Duke’s website, showing how the footnote text has ‘slid up’ from the bottom in a floating/sticky element.](https://gwern.net/doc/design/typography/sidenote/2023-02-23-justinduke-aboutpage-mobileslideupfootnotescreenshot.png)

A tapped ‘foot­note’ on Justin Duke’s web­site, show­ing how the foot­note text has ‘slid up’ from the bot­tom in a float­ing/ sticky el­e­ment.

The ‘slide- in’ from left/ right can make use of mar­gin on big­ger screens, but there is usu­ally no mar­gin on cramped mo­bile screens, so one faces a fun­da­men­tal choice be­tween in­sert­ing the foot­note/ side­note text ‘into’ the body, usu­ally forc­ing lay­out shift, and ‘over’ the body, ob­scur­ing some of it. (For Gwern.net, pop- ins were the only ac­cept­able so­lu­tion as they are less [modal ⁠](https://en.wikipedia.org/wiki/Mode_\(user_interface\)): they let the reader con­tinue nav­i­gat­ing/ read­ing the page, no mat­ter how deep they drill into the recursively- linked pop- ins.)

## Tables

[⁠Jukka “Yucca” Ko­r­pela](https://jkorpela.fi/www/fn.html#side), ~2007, demon­strates a com­pletely dif­fer­ent ap­proach using HTML _ta­bles_: de­fine two columns with dif­fer­ent sizes/ style, and put the side­notes in the sec­ond col­umn.

> There are many pos­si­ble ap­proaches to in­clud­ing side­notes on web pages. Hav­ing stud­ied al­ter­nate meth­ods like CSS po­si­tion­ing and float­ing, I have come to the con­clu­sion that the sim­plest method gives the best re­sults. This method con­sists of a two- column table, with the main text in one col­umn, the side­notes in the other. Using the CSS meth­ods, it be­comes awk­ward to con­trol the heights of pieces of text so that each side­note starts at the same ver­ti­cal po­si­tion as the main text that it re­lates to.

Easy:

![Sidenotes via 2-column HTML tables.](https://gwern.net/doc/design/typography/sidenote/2007-korpela-sidenotes-tablelayout.png)

Side­notes via 2- column HTML ta­bles.

This has the usual ad­van­tages/ dis­ad­van­tages of using ta­bles for web de­sign: it is fast, avoids Javascript & (most) CSS com­plex­i­ties, and is straight­for­ward; but it is rigid, de­grades on smaller screens, dif­fi­cult to write (eg. no num­ber­ing in Ko­r­pela’s ex­am­ples, mak­ing them mar­gin notes, un­less the au­thor man­u­ally adds su­per­scripts or oth­er­wise com­pli­cates it).

I in­clude this for its his­tor­i­cal in­ter­est—while this strat­egy may have made sense in 2007 18ya, the trade­offs now are highly un­fa­vor­able given that [⁠Tufte- CSS ⁠](https://gwern.net/sidenote#tufte-css) etc work, and I’m not sure any­one should use it.

## Annotate, Molly White

[“An­no­tate” ⁠](https://github.com/molly/annotate) ([⁠demo](https://molly.github.io/annotate/)) is a CSS+JS frame­work by [Molly White ⁠](https://en.wikipedia.org/wiki/Molly_White_\(writer\)), cre­ated for her [“The Edited Late­com­ers’ Guide To Crypto”](https://www.mollywhite.net/annotations/latecomers-guide-to-crypto/), which is a heavily- commentated (side by side) fisk­ing of an ar­ti­cle on cryp­tocur­rency.

Per­haps be­cause the com­men­tary may be longer than the text & com­plex, An­no­tate takes a novel ap­proach: text+com­men­tary pairs live in `<section>` el­e­ments, in­ter­leav­ing `<div>` s (pos­si­bly nested or ‘grouped’), with `<mark>` el­e­ments to spec­ify high­lighted ranges (eg. in yel­low high­light­ing) for which part of the text a com­men­tary is re­fer­ring to. The CSS then uses CSS grids (row- based lay­out) to lay them out side by side. (Javascript is used for live high­light­ing/ fo­cus­ing of ranges when clicked on, but oth­er­wise ap­pears op­tional.)

For mo­bile, it de­faults to ex­panded pop- ins but does not ap­pear to make any ef­fort to in­ter­leave or sep­a­rate pairs to en­sure that the com­men­tary for each vis­i­ble high­lighted range is also vis­i­ble.

![Screenshot from its Github repo of Annotate used on “The Edited Latecomers’ Guide To Crypto”.](https://gwern.net/doc/design/typography/sidenote/2022-10-02-mollywhite-annotate-latecomersdesktopscreenshot.png)

Screen­shot from its Github repo of An­no­tate used on “The Edited Late­com­ers’ Guide To Crypto”.

## George Pollard

In­spired by [⁠Type Classes](https://typeclasses.com/coerce) & Tufte- CSS; pure CSS ([⁠⁠web­site repo ⁠](https://github.com/Porges/ways-to-play/tree/main)), by [⁠George Pol­lard](https://games.porg.es/about/).

Ex­am­ple pages: [⁠“The Pi­geon Lot­tery”](https://games.porg.es/games/pigeon-lottery/), [⁠“The His­tory & Art of _Hana­fuda_ ”](https://games.porg.es/articles/cards/japan/hanafuda/art/).

![Screenshot of “The Pigeon Lottery” showing rubricated margin-notes & sidenotes.](https://gwern.net/doc/design/typography/sidenote/2025-04-06-georgepollard-waystoplay-thepigeonlottery-sidenotescreenshot.png)

Screen­shot of “The Pi­geon Lot­tery” show­ing rubri­cated margin- notes & side­notes.

## Miscellaneous

Some im­ple­men­ta­tions are just bad ideas or not worth dis­cussing in de­tail with screen­shots:

-   [⁠ILoveTy­pog­ra­phy.com](https://ilovetypography.com/2019/03/14/the-first-printed-math-books/) uses image cap­tions & mar­gin notes which, like Tufte- CSS, are floated/ out­dented right, but bizarrely, it uses _fig­ure cap­tions_ —just [`<figcaption>` ⁠](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) with a spe­cial class in­side an empty `<figure>` with no im­ages!
    
    This is in­valid HTML, fails badly in some cases (eg. in the linked ex­am­ple, one mar­gin note is al­most un­read­able be­cause it over­laps with a giant pull- quote il­lus­tra­tion), and has no ad­van­tage over a `<span>` that I can find; it does at least de­grade grace­fully into pop- in (de­fault ex­panded) block el­e­ments on nar­row/ mo­bile.
    
-   [⁠BLD­BLOG ⁠](https://bldgblog.com/2015/12/four-floor-war/) gen­er­ally avoids com­plex lay­out and foot­notes en­tirely, and doesn’t have much mar­gin to put side­notes in, so I was sur­prised while read­ing the archives to find one post which has a left mar­gin note, and even more sur­prised to check the HTML source and see that the ‘mar­gin note’ is in fact a _header_: a `<h6>`.
    
    Huh‽ It turns out that the header is floated left with some grue­some CSS. Said Achmiz sum­maries how the Rube Gold­berg con­trap­tion works:
    
    > The CSS uses ab­solute po­si­tion­ing. The near­est po­si­tioned an­ces­tor is `<article>`, not `.entry-content`. Within `<article>`, `.entry-content` is right- floated and has a fixed width. This cre­ates a variable- width space on the left (de­ter­mined by how much hor­i­zon­tal space is left within `<article` > after that fixed width is sub­tracted). The side­note `<h6>` is then set with `position:absolute` and `left:0`. Ver­ti­cal po­si­tion is left un­spec­i­fied, re­ly­ing on the way browsers im­ple­ment ab­solute po­si­tion­ing (ie. to place an el­e­ment where it would be placed if po­si­tion were `static`) to put it in the right place. Frag­ile, un­se­man­tic, & hacky.
    
-   [MIT Ad­mis­sions](https://mitadmissions.org/blogs/entry/we-are-reinstating-our-sat-act-requirement-for-future-admissions-cycles/) uses a footnote- sidenote hy­brid:
    
    ![MIT Admissions blog, demonstrating fixed-floating sidenote](https://gwern.net/doc/design/typography/sidenote/2022-03-28-mitadmissions-footnotesidenote.png)
    
    MIT Ad­mis­sions blog, demon­strat­ing fixed- floating side­note
    
    Span- annotated foot­note links (with the trig­ger text lightly high­lighted in red), on hover, trig­ger JS to cre­ate a sin­gle sticky/ float­ing ‘side­note’ which is lo­cated in the bottom- right cor­ner; hov­ers on other foot­notes re­place it with their con­tents. (Lay­out does not take into ac­count the side­bar or any­thing that may al­ready be there, and the foot­note popup box sim­ply ap­pears over it.)
    
    For mo­bile/ nar­row win­dows, it uses pop- in, but not as a block el­e­ment, in­stead, in­line with red- colored brack­ets to de­limit it:
    
    ![Mobile: popins but using rubricated bracket delimiters.](https://gwern.net/doc/design/typography/sidenote/2022-03-28-mitadmissions-footnotesidenote-mobilepopins-rubricated.png)
    
    Mo­bile: popins but using rubri­cated bracket de­lim­iters.
    
-   [⁠Evan Ova­dia](https://verdagon.dev/home) ([⁠eg.](https://verdagon.dev/blog/linear-types-borrowing)): con­tent & side­notes are put into pairs of columns. Pre­sum­ably does not han­dle many long side­notes grace­fully.
    
    For mo­bile/ nar­row, it col­lapses them as a row of num­bered links to ex­pand on click.
    
-   [⁠Simon Tatham](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/commit-messages/): uses a highly un­usual foot­note for­mat which I can’t de­cide if it’s a foot­note or a side­note.
    
    Foot­notes are du­pli­cated in but­ton tog­gles & at the bot­tom; foot­note num­bered an­chors are set to the right mar­gin, and when clicked, ‘popin’, but _to the side_ of the text, which re­flows into a left text col­umn vs right foot­note col­umn (no JS, just CSS+HTML):
    
    ![Tatham’s popin-sidenotes, expanded](https://gwern.net/doc/design/typography/sidenote/2024-05-25-simontatham-popinfootnotesidenote-expanded.png)
    
    Tatham’s popin- sidenotes, ex­panded
    

## See Also

-   [Project Xanadu ⁠](https://en.wikipedia.org/wiki/Project_Xanadu)
    

## External Links

-   Dis­cus­sion: [⁠HN ⁠](https://news.ycombinator.com/item?id=37619361)
    
-   [⁠Quote­backs](https://quotebacks.net/) ([⁠“In­tro­duc­ing: Quote­backs—A Chrome ex­ten­sion to quote the web”](https://tomcritchlow.com/2020/06/09/quotebacks/))
    
-   [⁠“Ex­pounder”](https://skorokithakis.github.io/expounder/), Stavros Ko­rokithakis (in­line al­ter­na­tive to [`⁠<abbr` ⁠](https://gwern.net/sidenote#mozdev-abbr) / [`⁠<defn>` ⁠](https://gwern.net/sidenote#mozdev-defn) tags)
    
-   [⁠“Us­abil­ity of Foot­notes”](https://shkspr.mobi/blog/2020/07/usability-of-footnotes/); [⁠“A (ter­ri­ble?) way to do foot­notes in HTML”](https://shkspr.mobi/blog/2020/12/a-terrible-way-to-do-footnotes-in-html/)
    
-   [⁠“Nut­shell”](https://ncase.me/nutshell-wip/), Nicky Case 2021
    
-   [⁠“LW Beta Fea­ture: Side- Comments” ⁠](https://www.lesswrong.com/posts/A33sgjYoM4Ko9viJv/lw-beta-feature-side-comments)
    
-   [“A li­brary of words: Dis­cov­er­ing _Roget’s The­saurus_ ” ⁠](https://austinkleon.substack.com/p/a-library-of-words)
    

## Bibliography

1.  You _can_ imag­ine web pages with true foot­notes: where a sticky bot­tom mar­gin is cre­ated, re­served for foot­notes, and JS in­serts the rel­e­vant foot­notes into that as the user scrolls, but I’m not sure I’ve ever seen this out­side of book skeuo­morph web de­signs with ex­plicit pag­i­na­tion, and screens are small enough that users would chafe at the loss of [ver­ti­cal pix­els ⁠](https://x.com/admittedlyhuman/status/430532517389561856).
    
    Then should we put our notes on en­tirely sep­a­rate pages? No: this only adds to the reader’s bur­den, and it’s even more work for the au­thor. (The ded­i­cated might em­brace hy­per­tex­tu­al­ity and cre­ate an enor­mous web of small nuggets of text which in­clude and go be­yond end­notes, but for peo­ple writ­ing on­line, URLs/ pages tend to be “heavy­weight”, and a com­mit­ment, often cor­re­spond­ing to a sin­gle file on disk; cre­at­ing hun­dreds of endnote- sized URLs also cre­ates its own prob­lems like nam­ing, re­find­ing, and nav­i­gat­ing them.) [](https://gwern.net/sidenote#fnref1)[↩](#fnref:1)
    
2.  You can use the [`⁠sidenotes` ⁠](https://ctan.org/pkg/sidenotes) / [`⁠sidenotesplus` ⁠](https://ctan.org/pkg/sidenotesplus) / [`⁠snotez` ⁠](https://ctan.org/pkg/snotez) pack­ages, or the some­what dif­fer­ent [`⁠marginnote` ⁠](https://ctan.org/pkg/marginnote) (where the na­tive `\marginpar{}` com­mand fails) pack­ages.[](https://gwern.net/sidenote#fnref2) [↩](#fnref:2)
    
3.  Tufte- CSS side­notes do not cor­rectly sup­port block el­e­ments like lists or para­graphs, be­cause spans are in­line and those are block el­e­ments; but [this is fix­able ⁠](https://github.com/edwardtufte/tufte-css/issues/93#issuecomment-670695382).[](https://gwern.net/sidenote#fnref3) [↩](#fnref:3)
    
4.  A sim­ple way to pro­vide ‘on hover’ an­no­ta­tions is to use HTML title tooltips, which was; Tyler Vigen at­tempts to pro­vide his collapsed- inline foot­notes as tooltips as well to min­i­mize click­ing & ef­fort.
    
    But while sim­ple, tooltips bring in many prob­lem dis­cussed in my tooltip post- mortem, and sev­eral of them show up here: there is no way to ‘ex­pand’ or search any of the tooltips, and be­cause tooltips are ca­pa­ble only of con­tain­ing plain text, while foot­notes can (and Vigen’s do) con­tain mul­ti­ple block el­e­ments like block­quotes or pho­tos. There is no use­ful way to con­dense such foot­notes into a tooltip, and Vigen’s tooltips often silently drop large parts of the foot­note—ren­der­ing them worse than use­less.[](https://gwern.net/sidenote#fnref4) [↩](#fnref:4)
    
5.  Some web­sites, like Grant­land or Strat­e­ch­ery, sup­port float­ing foot­notes… but only when the user clicks! (Bet­ter is Grant­land’s [his­tory of the Gra­cies](https://grantland.com/one-hundred-years-arm-bars-gracie-jiu-jitsu-mma/), which helps the reader keep the clan straight by pop­ping into the left mar­gin an an­no­tated fam­ily tree when­ever they click a Gra­cie name.) FiveThir­tyEight, on the other hand, does pop- in foot­notes—but not side­notes, de­spite ample mar­gin. Com­pare [_At­lantic_ ’s web ren­der­ing ⁠](https://www.theatlantic.com/magazine/archive/2005/04/host/303812/) using pop- ins with the orig­i­nal [2005 David Fos­ter Wal­lace ⁠](https://gwern.net/doc/sociology/2005-wallace.pdf) print essay which used elab­o­rate re­cur­sive side­notes in­te­grated in un­usual geome­tries. (Said Achmiz of­fers [an ex­am­ple ⁠](https://gwern.net/doc/design/typography/sidenote/2005-wallace-redesign.pdf) of a less ugly re­design of that.) [](https://gwern.net/sidenote#fnref5)[↩](#fnref:5)
    
6.  Al­though ar­guably one should not (and I avoid doing so). If a foot­note needs to be linked, it should be given a `<span>` an­chor with a name. Pan­doc foot­note an­chors/ num­bers are in­her­ently un­sta­ble, and worse, tend to fail silently: the link just changes to a dif­fer­ent foot­note, and con­tin­ues to ‘work’. And if any­one _needs_ to link a spe­cific foot­note it may be time to rewrite that foot­note into a more- linkable sec­tion or ap­pen­dix.[](https://gwern.net/sidenote#fnref6) [↩](#fnref:6)