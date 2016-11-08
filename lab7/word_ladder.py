from itertools import izip
import networkx as nx
import sys

def usage():
    '''
    Displays usage information.
    '''
    print ("USAGE: python word_ladder.py <input_file>")

def arg_check():
    '''
    Checks if enough arguments are passed to the program.
    '''
    if len(sys.argv) < 2:
        print ("ERROR: Not enough arguments.")
        usage()
        sys.exit(1)

def word_length(string):
    '''
    Finds the length of a word from the start of a string.
    '''
    n = 0
    for c in string:
        if c.isalpha():
            n += 1
    return n

def parse_input():
    '''
    Parses input file and returns set of words.
    '''
    filename = sys.argv[1]
    words = set()
    with open(filename) as f:
        for line in f:
            line = line.decode()
            if not line.startswith('*'):
                if not words:
                    length = word_length(line)
                word = line[:length]
                words.add(word)

    return words

def remove_from(char, string):
    '''
    Removes the first instance of a character from str
    '''
    if char in string:
        string = list(string)
        string.remove(char)
        return ''.join(string)
    else:
        return False

def hamming1(str1, str2):
    '''
    Returns True if the hamming distance is 1.
    Returns False otherwise
    '''
    assert len(str1) == len(str2), "String lengths are unequal: str1 = %s, str2 = %s"%(str1,str2)
    unequal = 0
    for c1, c2 in izip(str1, str2):
        if c1 != c2:
            if unequal == 0:
                unequal += 1
            else:
                return False

    return True

def combination1(str1, str2):
    '''
    Returns True if str2 is a combination of the characters of str1 except for 1.
    Returns False otherwise.
    '''
    assert len(str1) == len(str2)
    unequal = 0
    og_str2 = str2
    for c in str1:
        if c in str2:
            str2 = remove_from(c, str2)

        elif unequal == 0:
            unequal += 1
        else:
            return False

    return True

def edges_from_combo(G, words):
    '''
    Adds edges to G between nodes that share all but 1 character in any combination.
    '''
    reached_letters = set()
    letter_indexes, suffixes = dict(), dict()
    index = -1
    for word in words:
        index += 1
        sorted_suffix = str(sorted(word[1:]))
        if sorted_suffix not in suffixes:
            suffixes[sorted_suffix] = set([index])

        else:
            G.add_edges_from((words[i], word) for i in suffixes[sorted_suffix])
            suffixes[sorted_suffix].add(index)

        if word[0] not in reached_letters:
            reached_letters.add(word[0])
            letter_indexes[word[0]] = index

        else:
            G.add_edges_from((w, word)
                             for w in words[letter_indexes[word[0]]:index]
                                if combination1(w[1:], word[1:]))

        G.add_edges_from((w, word)
                         for w in words[:letter_indexes[word[0]]]
                            if not G.has_edge(w, word) and combination1(w, word))

    return G

def edges_from_hamming(G, words):
    '''
    Adds edges to G between nodes that have a Hamming distance of 1.
    '''
    reached_letters = set()
    letter_indexes, suffixes = dict(), dict()
    index = -1
    for word in words:
        index += 1
        if word[1:] not in suffixes:
            suffixes[word[1:]] = set([index])

        else:
            G.add_edges_from((words[i], word) for i in suffixes[word[1:]])
            suffixes[word[1:]].add(index)

        if word[0] not in reached_letters:
            reached_letters.add(word[0])
            letter_indexes[word[0]] = index

        else:
            G.add_edges_from((w, word)
                             for w in words[letter_indexes[word[0]]:index]
                                if hamming1(w[1:], word[1:]))

    return G

def generate_graph(words):
    '''
    Generate graph of connected words.
    '''
    from string import ascii_lowercase as lowercase
    G = nx.Graph(name="words")
    G.add_nodes_from(words)
    words = sorted(words)
    if len(sys.argv) > 2 and sys.argv[2] == "-c":
        G = edges_from_combo(G, words)
    else:
        G = edges_from_hamming(G, words)

    return G

def run_tests(examples, G):
    '''
    Finds the shortest path for given test cases.
    '''
    for (source, target) in examples:
        print("Shortest path between %s and %s is"%(source, target))
        try:
            sp = nx.shortest_path(G, source, target)
            for n in sp:
                print(n)
        except nx.NetworkXNoPath:
            print("None")

def print_stats(G):
    '''
    Prints stats of graph.
    '''
    print("Loaded %s"%sys.argv[1])
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(nx.number_of_nodes(G), nx.number_of_edges(G)))
    print("%d connected components" % nx.number_connected_components(G))

def run():
    '''
    Runs mains components of program.
    '''
    arg_check()
    words = parse_input()
    word_length = len(next(iter(words)))
    G = generate_graph(words)
    print_stats(G)

    if len(sys.argv) > 2 and sys.argv[2] == "-c":
        examples = [('chaos', 'order')]
        run_tests(examples, G)

    elif word_length == 5:
        examples = [('chaos', 'order'),
                    ('nodes', 'graph'),
                    ('moron', 'smart'),
                    ('pound', 'marks')]
        run_tests(examples, G)

    elif word_length == 4:
        examples = [('cold', 'warm'),
                    ('love', 'hate')]
        run_tests(examples, G)

# ============================================================================ #
if __name__ == "__main__":
    run()
