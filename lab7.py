from trees import leaf, set_left, set_right, is_leaf, label
from trees import has_left, has_right, left, right, set_label


def example_tree():
    """ A peek inside the recursive depths of Cookie Monster's mind... """
    kermit = leaf("kermit")
    cookie = leaf("cookie")
    ernie = leaf("ernie")
    bert = leaf("bert")
    kate = leaf("kate")
    camilla = leaf("camilla")
    count = leaf("count")
    set_left(kermit, cookie)
    set_right(kermit, count)
    set_left(cookie, bert)
    set_right(cookie, ernie)
    set_left(count, kate)
    set_right(count, camilla)
    return kermit


def swap_ck(tree):
    """ Replace this with your code for Question One ("K is for Cookie"). """


def ck_labels(tree):
    """ Replace this with your code for Question Two ("Recollection"). """


def a_subset_sums_to(ls, total):
    """ Replace this with your code for Question Three ("Sumthing"). """


def word_mix(word1, word2):
    """ Replace this with your code for Question Four ("False Friends"). """


def flatten(ls):
    """ Replace this with your code for Question Five ("Gaps"). """

