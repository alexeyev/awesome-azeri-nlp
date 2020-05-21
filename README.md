# Awesome Azeri NLP [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome Azerbaijani language processing software, models and datasets. Inspired by [awesome-ML](https://github.com/josephmisiti/awesome-machine-learning). 

The main focus is on **open source** tools, **downloadable** data and research **papers with code**.

If you want to contribute to this list (please do), send me a pull request.
Also, a listed repository should be tagged as deprecated if:

* Repository's owners explicitly say that "this library is not maintained".
* Not committed for long time (2~3 years).

## Table of Contents
<!-- MarkdownTOC depth=3 -->
- [Awesome Azeri NLP](#awesome-azeri-nlp)
  - [Table of Contents](#table-of-contents)
  - [Datasets](#data)
  - [Pretrained models](#pretrained-models)
  - [Methods/Software](#software)
      - [Morphology](#morphology-s)
      - [Syntax](#syntax-s)
  - [Online Demos](#demos)
  - [Miscellaneous](#misc)
<!-- /MarkdownTOC -->

<a name="data"></a>
## Datasets

#### Raw text
* [University of Leipzig corpus collection](https://cls.corpora.uni-leipzig.de/en?corpusLanguage=aze#tblselect) — Newscrawl (2011, 2013) and Wikipedia (misc) datasets
* [Helsinki University corpus](http://www.ling.helsinki.fi/uhlcs/readme-all/README-turkic-lgs.html#C21) — New Testament in the Azerbaijani language
* [Latest **azwiki** dump](https://dumps.wikimedia.org/azwiki/latest/): [**download** directly](https://dumps.wikimedia.org/azwiki/latest/azwiki-latest-pages-articles.xml.bz2)
* [Azeri at An Crúbadán](http://crubadan.org/languages/az) — 8M+ words, Latin script
* [**az-corpus-nlp**](https://github.com/raminrahimzada/az-corpus-nlp) —  2000+ texts, Latin script
* [azWaC: Azerbaijani corpus from the web](https://www.sketchengine.eu/azwac-azerbaijani-corpus/) — SketchEngine-hosted corpus crawled from the web in 2012,  ~94 million words
* [Domrachev-Sudoplatova scraped corpus](https://github.com/svetlana21/Nutch_parser/) — 2189398 words, 100560 sentences

**Several corpora are also mentioned in research works:**
* S. Mammadova, G. Azimova, and A. Fatullayev. 2010.Text corpora and its role in development of the linguistic technologies for the azerbaijani language.  In The Third International Conference Problems of Cybernetics and Informatics.
* Baisa, Vıt, and Vıt Suchomel. "Large corpora for turkic languages and unsupervised morphological analysis." Proceedings of the Eighth conference on International Language Resources and Evaluation (LREC’12), Istanbul, Turkey. European Language Resources Association (ELRA). 2012. [**SketchEngine corpora?**]
* C. Biemann, S. Bordag, G. Heyer, U. Quasthoff, and C. Wolff. 2004. Language-independent  methods  for compiling monolingual lexical data. Computational linguistics and intelligent text processing, pages 217–228.
* Domrachev M. A., Sudoplatova S. N. Testing Methods for Automatic Detection of Mor-
pheme Boundaries in the Azerbaijani Language. Vestnik NSU. Series: Linguistics and Intercultural
Communication , 2018, vol. 16, no. 2, p. 34–47. (in Russ.) [Downloadable corpus](https://github.com/svetlana21/Nutch_parser/)
* Özenç B., Ehsani R., Solak E. Moraz: an open-source morphological analyzer for Azerbaijani Turkish //Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. – 2018. – С. 25-29. [**BBC Azerbaijan**]

#### Syntax
* [UD project comments](https://universaldependencies.org/tr/) on difficulties in Turkish language processing, might bring light to the question why parsing Azeri is hard as well

#### Machine-readable dictionaries
TODO

#### Summarization
* [AZ summarization](https://github.com/derintelligence/az-summarization) — articles and titles, available on request

#### Translation
* [AZ-EN parallel corpus](https://github.com/derintelligence/en-az-parallel-corpus)  — 68K+ sentences, available on request

#### Sentiment
Mentioned in:
* [N. Gasimli's MS thesis](https://www.academia.edu/32330261/Analysis_of_the_use_of_Twitter_in_Azerbaijan) "Analysis of the use of Twitter in Azerbaijan"  —  2194+700 tweets

<a name="pretrained-models"></a>
## Pretrained models
* [Polyglot morfessor](https://github.com/aboSamoor/polyglot/blob/master/docs/MorphologicalAnalysis.rst) —  pretrained [morfessor](http://www.cis.hut.fi/cis/projects/morpho/) model, number 53
* [fastText](https://fasttext.cc/docs/en/crawl-vectors.html) — 300-dimensional fastText vectors provided by the authors


<a name="software"></a>
## Methods/Software

#### Morphology <a name="morphology-s"></a>
* [Azmorph](http://wiki.apertium.org/wiki/Azmorph) — morphological analyzer for Azerbaijani (Azerbaycan dili), said to be in pre-ALPHA state; however, was [used for web corpora preparation](https://www.sketchengine.eu/wp-content/uploads/Large_Corpora_for_turkic_2012.pdf)
* [Wiktionary word forms extraction](https://github.com/svetlana21/az_morphology) — Python code on github
* [MorAz](https://github.com/berkeozenc/MorAz) — open-source morph. analyzer, [paper](https://www.aclweb.org/anthology/D18-2005v1.pdf), [demo](http://ddil.isikun.edu.tr/moraz/), [related slides on AZ morphology](http://fsmnlp2017.cs.umu.se/wp-content/uploads/2017/08/RaziehEhsani.pdf).

**Mentioned in papers:**
* [POS-tagging](https://www.researchgate.net/publication/334074082_Part-of-Speech_Tagging_for_Azerbaijani_Language) paper  —  Mammadov, S., Rustamov, S., Mustafali, A., Sadigov, Z., Mollayev, R., & Mammadov, Z. (2018, October). Part-of-Speech Tagging for Azerbaijani Language. In 2018 IEEE 12th International Conference on Application of Information and Communication Technologies (AICT) (pp. 1-6). IEEE. [**Probable implementation: [aznlp repo](https://github.com/aznlp/azerbaijani-language-pos-tagger)**]
* [Stemming paper, 2019](https://jpit.az/en/journals/227/) — Alizadeh, M. B. H., & Seyyedi, S. A. H. (2019). AUTO STEMMING OF AZERBAIJANI LANGUAGE. Problems of Information Technology, 59-66.
* [N. Gasimli's MS thesis](https://www.academia.edu/32330261/Analysis_of_the_use_of_Twitter_in_Azerbaijan) "Analysis of the use of Twitter in Azerbaijan"  — [Zemberek](https://github.com/ahmetaa/zemberek-nlp) is extended for Azerbaijani; though stated a lot of effort is still required for it to work properly for Azeri language.

#### Syntax <a name="syntax-s"></a>
* TODO

<a name="demos"></a>
## Online Demos
* [Cyrillic ⇄ Latin conversion](http://www.ismanov.com/Projects/CyrLatConverter/index.php)  — PHP-based online tool

<a name="misc"></a>
## Miscellaneous
* [Turkic languages-related resources](http://ddi.itu.edu.tr/en/toolsandresources) compiled by Dr. Gülşen Eryiğit and her team at Istanbul Technical University 
* [Azeribaijani corpora data review](https://www.elibrary.ru/item.asp?id=37146771&) 
* [Dilmanc](http://dilmanc.az/en/project/about)  — government-funded Azerbaijani language-related initiative
* [Dilmanc EAMT paper](http://dilmanc.az/pdf/EAMT-2008-Fatullayev.pdf) on MT peculiarities
* [Apertium page](http://wiki.apertium.org/wiki/Azerbaijani) — a list of various online language-related resources 
* [AZNLP github](https://github.com/aznlp) — a repo hub with various language-related software: stemmer, POS-tagger
* [MozillaAZ community spellchecker](https://github.com/mozillaz/spellchecker) — spellchecker plugin
