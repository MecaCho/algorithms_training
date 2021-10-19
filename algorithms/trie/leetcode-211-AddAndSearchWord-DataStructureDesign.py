# encoding=utf8


'''
211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


211. 添加与搜索单词 - 数据结构设计
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

'''




class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        tree = self.root
        for w in word:
            if tree is None or not tree.get(w):
                tree[w] = {}
            tree = tree.get(w)
        tree["end"] = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        tree = self.root
        def find(word, tree):
            for w in word:
                if tree.get(w) is None:
                    return False
                tree = tree.get(w)
            return True if tree.get("end") else False
        if "." in word:
            self.vals = []
            def bk(res, d):
                if len(res) == len(word):
                    if d.get("end"):
                        self.vals.append(res)
                else:
                    for k, v in d.items():
                        new_res = res+k
                        flag = True
                        for i in range(len(new_res)):
                            if i >= len(word) or word[i] != "." and new_res[i] != word[i]:
                                flag = False
                        if flag and isinstance(v, dict):
                            bk(new_res, v)
            bk("", self.root)
            return self.vals != []
        else:
            return find(word, tree)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# golang solution

'''
package code


type TrieNode struct {
	children [26]*TrieNode
	isEnd    bool
}

func (t *TrieNode) Insert(word string) {
	node := t
	for _, ch := range word {
		ch -= 'a'
		if node.children[ch] == nil {
			node.children[ch] = &TrieNode{}
		}
		node = node.children[ch]
	}
	node.isEnd = true
}

type WordDictionary struct {
	trieRoot *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{&TrieNode{}}
}

func (d *WordDictionary) AddWord(word string) {
	d.trieRoot.Insert(word)
}

func (d *WordDictionary) Search(word string) bool {
	var dfs func(int, *TrieNode) bool
	dfs = func(index int, node *TrieNode) bool {
		if index == len(word) {
			return node.isEnd
		}
		ch := word[index]
		if ch != '.' {
			child := node.children[ch-'a']
			if child != nil && dfs(index+1, child) {
				return true
			}
		} else {
			for i := range node.children {
				child := node.children[i]
				if child != nil && dfs(index+1, child) {
					return true
				}
			}
		}
		return false
	}
	return dfs(0, d.trieRoot)
}

'''
