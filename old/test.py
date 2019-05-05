#!/usr/bin/env python3.7

import collections

TEST_DICT = {}

class Word(object):
    def __init__(self, word):
        self.term = word[0].replace("-", "").replace(" ", "")
        self.definition = word[1]
        self.greek_latin = word[2]
        self.pos = word[3]

class Node(object):
    def __init__(self, word):
        self.word = word
        self.children = []

    def __str__(self, level=0):
        ret = level*"\t"+repr(self.word.term)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

class Tree(object):
    def __init__(self, root):
        self.root = root

if __name__ == "__main__":
    blephar = Word(["blephar", "eyelid", "greek", "wr"])
    opt = Word(["opt", "vision", "latin", "wr"])
    osis = Word(["osis", "abnormal condition", "latin", "suffix"])
    ptosis = Word(["ptosis", "drooping", "greek", "suffix"])
    sis = Word(["sis", "state", "latin", "suffix"])
    is_term = Word(["is", "no meaning", "latin", "suffix"])

    blephar_node = Node(blephar)
    opt_node = Node(opt)
    osis_node = Node(osis)
    ptosis_node = Node(ptosis)
    sis_node = Node(sis)
    is_node = Node(is_term)

    tree = Tree(blephar_node)

    blephar_node.children.append(opt_node)
    blephar_node.children.append(osis_node)
    blephar_node.children.append(ptosis_node)
    blephar_node.children.append(sis_node)
    blephar_node.children.append(is_node)
    opt_node.children.append(osis_node)
    opt_node.children.append(sis_node)
    opt_node.children.append(is_node)

    print(tree.root)

    TEST_DICT = {}
    stack = []
    stack.append(tree.root)
    TEST_DICT[tree.root.word.term] = []#{}#collections.defaultdict(dict)
    print(TEST_DICT)
    while stack:
        top = stack.pop()
        for c in top.children:
            if top.word.term not in TEST_DICT:
                TEST_DICT[top.word.term] = []#{}#collections.defaultdict(dict)
            TEST_DICT[top.word.term].append({"child":c.word.term})#collections.defaultdict(dict)
            stack.append(c)
        print(top.word.term)

    print(TEST_DICT)

    for w in TEST_DICT:
        print(w.upper())
        for o in TEST_DICT[w]:
            print(o['child'])
        print("\n")
