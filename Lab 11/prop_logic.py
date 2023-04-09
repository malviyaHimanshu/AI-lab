"""
    CS20B1097 HIMANSHU

    PROPOSITIONAL LOGIC
"""

import pytholog as pl

new_kb = pl.KnowledgeBase("myKnowledge")

new_kb([
    "likes(shyam, mango)",
    "girl(seema)",
    "red(rose)",
    "likes(bill, cindy)",
    "owns(john, gold)"
])

print(new_kb.query(pl.Expr("owns(john, What)")))