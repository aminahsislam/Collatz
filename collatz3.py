import graphviz

dotfile = file('collatz-graph.dot', 'w')

limit = 20

def f(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

explored = set([1])

dotfile.write('digraph {\n')

for n in range(3, limit, 2): # odd numbers
    while n not in explored:
        dotfile.write(str(n) + ' -> ')
        explored.add(n)
        n = f(n)
    dotfile.write(str(n) + ';\n')
dotfile.write('}\n')
