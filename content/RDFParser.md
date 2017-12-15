Title: RDF Parser API 
Date: 2016-02-09 16:00
Category: Semantic Web
Tags: Semantic Wev
Slug: RDF Triple API
Author: Mohcine madkour
Illustration: rdf.png

# RDF-Triple-API

A simple API for extracting the RDF triple (subject, predicate, object) of any sentence. The parsed sentence is also returned in addition to the triple.

The algorithm implemented is taken from [this paper] (http://ailab.ijs.si/dunja/SiKDD2007/Papers/Rusu_Trippels.pdf) by Delia Rusu.

The sentence is parsed using the [stanford parser] (http://nlp.stanford.edu/software/lex-parser.shtml)

The endpoint for the api is http://www.newventify.com/rdf and has url parameter `sentence`

A complete request would look like the following: [http://www.newventify.com/rdf?sentence=The man stood next to the refrigerator](http://www.newventify.com/rdf?sentence=The man stood next to the refrigerator) and will return

`
{
  "object": {
    "POS": "NN", 
    "Tree Attributes": [], 
    "Word Attributes": [
      [
        "the", 
        "DT"
      ]
    ], 
    "word": "refrigerator"
  }, 
  "parse_tree": "Tree('ROOT', [Tree('S', [Tree('NP', [Tree('DT', ['The']), Tree('NN', ['man'])]), Tree('VP', [Tree('VBD', ['stood']), Tree('ADVP', [Tree('JJ', ['next'])]), Tree('PP', [Tree('TO', ['to']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['refrigerator'])])])])])])", 
  "predicate": {
    "POS": "VB", 
    "Tree Attributes": [
      "Tree('ADVP', [Tree('JJ', ['next'])])"
    ], 
    "Word Attributes": [], 
    "word": "stood"
  }, 
  "rdf": [
    "man", 
    "stood", 
    "refrigerator"
  ], 
  "sentence": "The man stood next to the refrigerator", 
  "subject": {
    "POS": "NN", 
    "Tree Attributes": [], 
    "Word Attributes": [
      [
        "The", 
        "DT"
      ]
    ], 
    "word": "man"
  }
}
`

[Check out the source code here](https://github.com/mohcinemadkour/RDF-Triple-API/blob/master/rdf_triple.py)