# Awesome Azeri NLP [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome Azerbaijani language processing software, models and datasets. Inspired by [awesome-ML](https://github.com/josephmisiti/awesome-machine-learning). 



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
  - [Miscellaneous](#misc)
<!-- /MarkdownTOC -->

<a name="data"></a>
## Datasets

#### Raw text
* [University of Leipzig corpus collection](https://cls.corpora.uni-leipzig.de/en?corpusLanguage=aze#tblselect) — Newscrawl (2011, 2013) and Wikipedia (misc) datasets
* [Helsinki University corpus](http://www.ling.helsinki.fi/uhlcs/readme-all/README-turkic-lgs.html#C21) — New Testament in the Azerbaijani language
* [Latest **azwiki** dump](https://dumps.wikimedia.org/azwiki/latest/): [**download** directly](https://dumps.wikimedia.org/azwiki/latest/azwiki-latest-pages-articles.xml.bz2)
* [Azeri at An Crúbadán](http://crubadan.org/languages/az) — 8M+ words, Latin script
* [Domrachyov-Sudoplatova scraped corpus](https://github.com/svetlana21/Nutch_parser/) — 2189398 words, 100560 sentences

**Corpora mentioned in the research papers**
* S. Mammadova, G. Azimova, and A. Fatullayev. 2010.Text corpora and its role in development of the linguistic technologies for the azerbaijani language.  In The Third International Conference Problems of Cybernetics and Informatics.
* Baisa, Vıt, and Vıt Suchomel. "Large corpora for turkic languages and unsupervised morphological analysis." Proceedings of the Eighth conference on International Language Resources and Evaluation (LREC’12), Istanbul, Turkey. European Language Resources Association (ELRA). 2012.
* C. Biemann, S. Bordag, G. Heyer, U. Quasthoff, and C. Wolff. 2004. Language-independent  methods  for compiling monolingual lexical data. Computational linguistics and intelligent text processing, pages 217–228.
* Домрачев М. А., Судоплатова С. Н. (2018). Тестирование методов автоматического обнаружения границ морфем на материале азербайджанского языка. Вестник Новосибирского государственного университета. Серия: Лингвистика и межкультурная коммуникация, 16 (2), 34-47. [корпус](https://github.com/svetlana21/Nutch_parser/)

#### Machine-readable dictionaries
TODO

#### Summarization
* [AZ summarization](https://github.com/derintelligence/az-summarization) — articles and titles, available on request

#### Translation
* [AZ-EN parallel corpus](https://github.com/derintelligence/en-az-parallel-corpus)  — 68K+ sentences, available on request

<a name="pretrained-models"></a>
## Pretrained models
* [Polyglot morfessor](https://github.com/aboSamoor/polyglot/blob/master/docs/MorphologicalAnalysis.rst) —  pretrained [morfessor](http://www.cis.hut.fi/cis/projects/morpho/) model, number 53
* [fastText](https://fasttext.cc/docs/en/crawl-vectors.html) — 300-dimensional fastText vectors provided by the authors


<a name="software"></a>
## Methods/Software

#### Morphology <a name="morphology-s"></a>
* [Azmorph](http://wiki.apertium.org/wiki/Azmorph) — morphological analyzer for Azerbaijani (Azerbaycan dili), said to be in pre-ALPHA state; however, was [used for web corpora preparation](https://www.sketchengine.eu/wp-content/uploads/Large_Corpora_for_turkic_2012.pdf)
* [Stemming paper, 2019](https://jpit.az/en/journals/227/) — *AUTO STEMMING OF AZERBAIJANI LANGUAGE* by Morteza B. Hasan Alizadeh, Seyyed Amin H. Seyyedi
* [Wiktionary extraction word forms code](https://github.com/svetlana21/az_morphology) — 

#### Syntax <a name="syntax-s"></a>
* TODO


<a name="misc"></a>
## Miscellaneous
* [Azeribaijani corpora data review](https://www.elibrary.ru/item.asp?id=37146771&) 
* [Dilmanc](http://dilmanc.az/en/project/about)  — government-funded Azerbaijani language-related initiative
* [Dilmanc EAMT paper](http://dilmanc.az/pdf/EAMT-2008-Fatullayev.pdf) on 
* [Apertium page](http://wiki.apertium.org/wiki/Azerbaijani) — a list of various online language-related resources 
* [AZNLP github](https://github.com/aznlp) — a repo hub with various language-related software: stemmer, POS-tagger
* [MozillaAZ community spellchecker](https://github.com/mozillaz/spellchecker) — spellchecker plugin
* [jsoft.ws](https://jsoft.ws/index.php?key=Azerbaijani%20NLP) — language processing blog posts
