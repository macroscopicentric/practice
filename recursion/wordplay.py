import time
import json

with open("sowpods.txt") as f:
    d = set(f.read().split('\n'))

with open("sowpods_sorted.txt") as f:
    sorted_d = json.load(f)

class Trie(object):
#Pulled directly from PyEnchant.    
    def __init__(self,words={}):
        self._eos = False # whether I am the end of a word
        self._keys = {} # letters at this level of the trie
        self.dict_words = []
        for w in words:
            self.insert(w, words[w])

    def collect(self,word):
        #Not finding all words.
        if len(word) == 0:
            return self.dict_words
        total_words = []
        total_words += self.dict_words + (self[word[0]].collect(word[1:]) if
            word[0] in self._keys else [])
        return total_words
    
    def insert(self,word,real_word):
        if word == "":
            self._eos = True
        else:
            key = word[0]
            try:
                subtrie = self[key]
            except KeyError:
                subtrie = Trie()
                self[key] = subtrie
            if len(word) == 1:
                subtrie.dict_words += [real_word]
            subtrie.insert(word[1:], real_word)

    def remove(self,word):
        if word == "":
            self._eos = False
        else:
            key = word[0]
            try:
                subtrie = self[key]
            except KeyError:
                pass
            else:
                subtrie.remove(word[1:])
    
    def search(self,word,nerrs=0):
        """Search for the given word, possibly making errors.
This method searches the trie for the given <word>, making
precisely <nerrs> errors. It returns a list of words found.
"""
        res = []
        # Terminate if we've run out of errors
        if nerrs < 0:
            return res
        # Precise match at the end of the word
        if nerrs == 0 and word == "":
            if self._eos:
                res.append("")
        # Precisely match word[0]
        try:
            subtrie = self[word[0]]
            subres = subtrie.search(word[1:],nerrs)
            for w in subres:
                w2 = word[0] + w
                if w2 not in res:
                  res.append(w2)
        except (IndexError, KeyError):
            pass
        # match with deletion of word[0]
        try:
            subres = self.search(word[1:],nerrs-1)
            for w in subres:
                if w not in res:
                    res.append(w)
        except (IndexError,):
            pass
        # match with insertion before word[0]
        try:
            for k in self._keys:
                subres = self[k].search(word,nerrs-1)
                for w in subres:
                    w2 = k+w
                    if w2 not in res:
                        res.append(w2)
        except (IndexError,KeyError):
            pass
        # match on substitution of word[0]
        try:
            for k in self._keys:
                subres = self[k].search(word[1:],nerrs-1)
                for w in subres:
                    w2 = k+w
                    if w2 not in res:
                        res.append(w2)
        except (IndexError,KeyError):
            pass
        # All done!
        return res
    search._DOC_ERRORS = ["nerrs"]
        
    def __getitem__(self,key):
        return self._keys[key]
        
    def __setitem__(self,key,val):
        self._keys[key] = val

    def __iter__(self):
        if self._eos:
            yield ""
        for k in self._keys:
            for w2 in self._keys[k]:
                yield k + w2

#I hate everything. Based on Tom's code.
def generate_and_compare(letters, test_dict):
    start = time.time()
    #Generates all possible letter combos from the given list and then checks if they're in the dictionary.
    def calculate_permutations(letters):
        if len(letters) == 1:
            return [letters[0]]
        answers = []
        for i, letter in enumerate(letters):
            tails = calculate_permutations(letters[:i]+letters[i+1:])
            answers = answers + [letter + tail for tail in tails] + tails
        return list(set(answers))
    answers = calculate_permutations(letters)
    real_words = filter(lambda x: x in test_dict, answers)
    print "Time to generate words and compare to dict: %s" % (time.time() - start)
    return real_words

def search_through_trie(letters, trie):
    start = time.time()
    def search_helper(letters):
        if len(letters) == 1:
            return []
        words = []
        words += trie.collect(letters) + search_helper(letters[1:])
        return words
    words = [sorted_d[word] for word in search_helper(letters)]
    print "Time to search through trie: %s" % (time.time() - start)
    return words

letter_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
start = time.time()
dict_trie = Trie(sorted_d)
print dict_trie.collect(letter_pool)
print "Time to create trie: %s" % (time.time() - start)
print generate_and_compare(letter_pool, set(d))
print search_through_trie(letter_pool, dict_trie)