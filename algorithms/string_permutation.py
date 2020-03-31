def dfs(s, ret=[]):
    if len(s) == 0:
        return ret
    elif len(s) == 1 and not ret:
        return [s]
    else:
        # ret = [insert_char(i, s[0]) for i in dfs(s[1:], ret=ret)]
        ret = []
        for i in dfs(s[1:], ret=ret):
            tmp = insert_char(i, s[0])
            for j in tmp:
                ret.append(j)
        return ret


def insert_char(s, char):
    return [s[:i] + char + s[i:] for i in range(len(s)+1)]

if __name__ == '__main__':
    print(dfs("abcdefg", []))
    print(insert_char("abc", "d"))
