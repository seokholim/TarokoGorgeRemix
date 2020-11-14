from nltk.corpus import wordnet as wn

#print(wn.synsets('roam'))
#print(wn.synsets('dirt')[0].name())
#print(type(wn.synsets('dirt')[0].name()))


print(wn.synsets('soft')[0].name())


print(wn.synset(wn.synsets('cat')[0].name()).lch_similarity(wn.synset(wn.synsets('soft')[0].name())))


#roll = wn.synset('roam.n.01')
#cat = wn.synset('cat.n.01')

#print(roll.lch_similarity(cat))
