from __future__ import with_statement
import random
import math


class Node(object):
    
    #decision tree.
    def __init__(self, attribute):
        """Attribute is which attribute to branch on."""
        self.attribute = attribute
        self.children = {}

def decision_tree_learning(examples, attribs, default=1, use_gain=False):
    
    print(examples)
    # examples is empty
    if not examples:
        return default

    # same class
    elif not [i for i in examples if i[-1] != examples[0][-1]]:
        return examples[0][-1]

    # attributes is empty
    elif not attribs:
        return majority_value(examples)

    else:
        best, label = choose_attribute(attribs, examples, use_gain)
        tree = Node(label)
        m = majority_value(examples)
        sub_attribs = attribs[:best] + attribs[best+1:]
        for value in (1, 2):
            sub_exs = [j for j in examples if j[best] == value]
            subtree = decision_tree_learning(sub_exs, sub_attribs, m, use_gain)
            tree.children[value] = subtree
    return tree

def choose_attribute(attribs, examples, use_gain):

    
    def entropy(positive, alll):
        p_pos = positive * 1.0 / alll
        p_neg = 1.0 - p_pos
        print(p_pos)
        print(p_neg)
        
        if p_pos==0.0:
            return 0.0
        elif p_neg==0.0:
            return 0.0
        
        try:
            return 0.0 - p_pos*math.log(p_pos, 2) - p_neg*math.log(p_neg, 2)
        except OverflowError:
            return 0.0
    
    if not use_gain: # Random decide which attribute to branch on
        i = random.randrange(len(attribs))
        return i, attribs[i]

    else: # Calculate which gives most information gain
        gains = []
        pos_exs = [x for x in examples if x[-1] == examples[0][-1]]
        e = entropy(len(pos_exs), len(examples))
        for attr in attribs:
            r = 0.0
            sub_ex_1 = [i for i in examples if i[attr] == 1]
            sub_ex_2 = [i for i in examples if i[attr] == 2]
            pos_ex_1 = len([i for i in sub_ex_1 if i[-1] == 2])
            pos_ex_2 = len([i for i in sub_ex_2 if i[-1] == 2])
            if sub_ex_1:
                r += (len(sub_ex_1)*1.0 / len(examples)) * entropy(pos_ex_1, len(sub_ex_1))
            if sub_ex_2:
                r += (len(sub_ex_2)*1.0 / len(examples)) * entropy(pos_ex_2, len(sub_ex_2))
            gains.append(e - r)

        i = gains.index(max(gains))
        return i, attribs[i]

def majority_value(examples): # most common value
    count = {}
    for example in examples:
        if example[-1] not in count.keys():
            count[example[-1]] = 0
        count[example[-1]] += 1
    majority = max(count.values())
    for key, value in count.items():
        if value == majority:
            return key

def test(tree, examples, attributes): #test
    correct = 0
    for i, example in enumerate(examples):
        node = tree
        result = "Test %i incorrect" % i
        while True:
            if isinstance(node, int):
                if node == example[-1]:
                    correct += 1
                    result = "Test %s correct value '%s'" % (i, example[-1])
                else:
                    result += " '%s != %s'" % (node, example[-1])
                break
            if example[node.attribute] not in node.children.keys():
                result += " '%s' no children" % example[node.attribute]
                break
            node = node.children[example[node.attribute]]
        print result

    print "Test results: %i of %i correct" % (correct, len(examples))

def print_tree(root):
    """Prints a representation of the tree and its nodes."""
    queue = [(root, ["1"])]
    while queue:
        this, depth = queue.pop(0)
        if isinstance(this, int):
            reprr = "L %i" % this
        else:
            reprr = str(this.attribute)
            for key, child in this.children.items():
                queue.append((child, depth + ["%s" % key]))
        print "%s: %s" % (".".join(depth), reprr)

def read_file(filee):
    """Returns a list representation of the values in file."""
    output = []
    with open(filee) as f:
        f = open(filee, 'r')
        lines = [x.split() for x in f.readlines()]
        for line in lines:
            output.append([int(x) for x in line])
    return output

def main():
    """Builds a decision tree and tests it."""
    
    # 1. Learn a decision tree from the data in training.txt
    print "--Building trees--"
    train_examples = read_file('training.txt')
    print(train_examples)
    attrs = range(len(train_examples[0])-1)
    rand_tree = decision_tree_learning(train_examples, attrs, use_gain=False)
    gain_tree = decision_tree_learning(train_examples, attrs, use_gain=True)
    print "--Done building--"
    print

    # 2. Document the tree you got
    print "--Random tree--"
    print_tree(rand_tree)
    print
    print "--Learn tree--"
    print_tree(gain_tree)
    print

    # 3. Classify all examples in the test-set
    test_examples = read_file('test.txt')
    print "--Testing random tree--"
    test(rand_tree, test_examples, attrs)
    print
    print "--Testing information gain tree--"
    test(gain_tree, test_examples, attrs)
    print "--Done testings--"

if __name__ == '__main__':
    main()