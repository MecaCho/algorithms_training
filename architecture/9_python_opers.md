

```

Operation

Equivalent

Result

len(s)

number of elements in set s (cardinality)

x in s

test x for membership in s

x not in s

test x for non-membership in s

s.issubset(t)

s <= t

test whether every element in s is in t

s.issuperset(t)

s >= t

test whether every element in t is in s

s.union(t)

s | t

new set with elements from both s and t

s.intersection(t)

s & t

new set with elements common to s and t

s.difference(t)

s - t

new set with elements in s but not in t

s.symmetric_difference(t)

s ^ t

new set with elements in either s or t but not both

s.copy()

new set with a shallow copy of s
```

l1 = [["qa","ba","be","se","sq"],["qa","ba","bi","si","sq"],["qa","ba","br","sr","sq"],["qa","ca","cm","sm","sq"],["qa","ca","co","so","sq"],["qa","la","ln","sn","sq"],["qa","la","lt","st","sq"],["qa","ma","mb","sb","sq"],["qa","pa","ph","sh","sq"],["qa","ta","tc","sc","sq"],["qa","fa","fe","se","sq"],["qa","ga","ge","se","sq"],["qa","ha","he","se","sq"],["qa","la","le","se","sq"],["qa","ma","me","se","sq"],["qa","na","ne","se","sq"],["qa","ra","re","se","sq"],["qa","ya","ye","se","sq"],["qa","ca","ci","si","sq"],["qa","ha","hi","si","sq"],["qa","la","li","si","sq"],["qa","ma","mi","si","sq"],["qa","na","ni","si","sq"],["qa","pa","pi","si","sq"],["qa","ta","ti","si","sq"],["qa","ca","cr","sr","sq"],["qa","fa","fr","sr","sq"],["qa","la","lr","sr","sq"],["qa","ma","mr","sr","sq"],["qa","fa","fm","sm","sq"],["qa","pa","pm","sm","sq"],["qa","ta","tm","sm","sq"],["qa","ga","go","so","sq"],["qa","ha","ho","so","sq"],["qa","la","lo","so","sq"],["qa","ma","mo","so","sq"],["qa","na","no","so","sq"],["qa","pa","po","so","sq"],["qa","ta","to","so","sq"],["qa","ya","yo","so","sq"],["qa","ma","mn","sn","sq"],["qa","ra","rn","sn","sq"],["qa","ma","mt","st","sq"],["qa","pa","pt","st","sq"],["qa","na","nb","sb","sq"],["qa","pa","pb","sb","sq"],["qa","ra","rb","sb","sq"],["qa","ta","tb","sb","sq"],["qa","ya","yb","sb","sq"],["qa","ra","rh","sh","sq"],["qa","ta","th","sh","sq"]]
