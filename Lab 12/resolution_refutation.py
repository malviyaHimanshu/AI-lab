"""
    CS20B1097 HIMANSHU

    Write a program in prolog/pytholog to implement following simple facts and Queries
    - Every child loves Santa.
    - Everyone who loves Santa loves any reindeer
    - Rudolph is a reindeer, and Rudolph has a red nose
    - Anything which has a red nose is weird or is a clown
    - No reindeer is a clown
    - Scrooge does not love anything which is weird
    - (Conclusion) Scrooge is not a child.
"""

"""
    ** SOLUTION USING RESOLUTION REFUTATION **
    child(x) : x is a child
    loves(x, y) : x loves y
    reindeer(x) : x is a reindeer
    has_red_nose(x) : x has a red nose
    weird(x) : x is weird
    clown(x) : x is a clown

    F1 : For all x, if x is a child, then x loves Santa
    F2 : For all x, if x loves Santa, then x loves any reindeer
    F3 : Rudolph is a reindeer, and Rudolph has a red nose
    F4 : For all x, if x has a red nose, then x is weird or x is a clown
    F5 : For all x, if x is a reindeer, then x is not a clown
    F6 : For all x, if x is not weird, then Scrooge does not love x
    F7 : Scrooge is a not child

    Clauses:
    C1 : not chid(x) or loves(x, Santa)
    C2 : not loves(x, Santa) or not loves(x, Santa) or not reindeer(y) or loves(x, y)
    C3 : reindeer(Rudolph)
    C4 : has_red_nose(Rudolph)
    C5 : not has_red_nose(x) or weird(x) or clown(x)
    C6 : not reindeer(x) or not clown(x)
    C7 : not weird(x) or not loves(Scrooge, x)
    C8 : not child(Scrooge)

    result = C1 and C2 and C3 and C4 and C5 and C6 and C7 and (not C8)
    : result -> False -> given conclusion is True
"""

import pytholog as pl

new_kb = pl.KnowledgeBase("myKnowledge")

clauses = [
    "not chid(x) or loves(x, Santa)",
    "not loves(x, Santa) or not loves(x, Santa) or not reindeer(y) or loves(x, y)",
    "reindeer(Rudolph)",
    "has_red_nose(Rudolph)",
    "not has_red_nose(x) or weird(x) or clown(x)",
    "not reindeer(x) or not clown(x)",
    "not weird(x) or not loves(Scrooge, x)",
    "child(Scrooge)"
]

new_kb(clauses)
result = new_kb.query(pl.Expr("child(Scrooge)"))
if not result:
    print("Conclusion is NOT True : Scrooge is a child")
else:
    print("Conclusion is True : Scrooge is not a child")