txt = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

count_better = txt.count("better")
count_never = txt.count("never")
count_is = txt.count("is")
print(f"word \'better\' uses {count_better} times")
print(f"word \'never\' uses {count_never} times")
print(f"word \'is\' uses {count_is} times", end ="\n\n")

print(f"Replace all i to &\n\n{txt.replace('i','&')}", end ="\n\n")
print(f"All text to Upper\n\n{txt.upper()}", end ="\n\n")