from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open(r'../tmp/words_en.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print pline
            print line
            print('-' * 20)
