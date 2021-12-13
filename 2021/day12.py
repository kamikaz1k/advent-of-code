q1 = '''
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

q3 = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

q4 = '''
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''

q2 = '''
kc-qy
qy-FN
kc-ZP
end-FN
li-ZP
yc-start
end-qy
yc-ZP
wx-ZP
qy-li
yc-li
yc-wx
kc-FN
FN-li
li-wx
kc-wx
ZP-start
li-kc
qy-nv
ZP-qy
nv-xr
wx-start
end-nv
kc-nv
nv-XQ
'''

from collections import defaultdict, deque, Counter
from dataclasses import dataclass




class Visitor:
    SINGLE = 1
    DOUBLE = 2

    def __init__(self, type_):
        self.type = type_
        self._visited = {}

    @classmethod
    def types(cls):
        return {
            cls.SINGLE: 'SingleVisitType',
            cls.DOUBLE: 'DoubleVisitType'
        }

    @property
    def type_name(self):
        return self.types().get(self.type)

    def __str__(self):
        return (
            f"<{self.type_name} size=({len(self._visited)}) "
            f"visited={','.join(k.value for k in self._visited.keys())} >"
        )

    @classmethod
    def factory(cls, type_):
        return {
            cls.SINGLE: SingleVisitType,
            cls.DOUBLE: DoubleVisitType
        }[type_]()

    def visit(self, node): pass
    def is_visitable(self, node): pass
    def unvisit(self, node, safe=True): pass

    def _is_revisitable(self, node):
        return node.value.isupper()


class SingleVisitType(Visitor):
    def __init__(self):
        super().__init__(self.SINGLE)

    def visit(self, node):
        self._visited[node] = node

    def is_visitable(self, node):
        return (node not in self._visited) or self._is_revisitable(node)

    def unvisit(self, node, safe=True):
        val = self._visited.pop(node, None)

        if not safe and not val:
            raise Exception(f'{node} has not been visited!')


class DoubleVisitType(Visitor):
    def __init__(self):
        super().__init__(self.DOUBLE)
        self._has_a_double = False

    def __str__(self):
        return (
            f"<{self.type_name} size=({len(self._visited)}) "
            f"visited={[f'{k.value} ({v})' for k, v in self._visited.items()]} >"
        )

    def visit(self, node):
        count = self._visited.get(node, 0)
        count += 1
        self._visited[node] = count

        if self._is_revisitable(node):
            return

        if count == 2:
            self._has_a_double = True

    def is_visitable(self, node):
        if node.is_start:
            return False

        if self._is_revisitable(node):
            return True

        count = self._visited.get(node, 0)

        if count < 1:
            return True

        if self._has_a_double:
            return count < 1

        return count < 2

    def unvisit(self, node, safe=True):
        val = self._visited.get(node, None)

        if not safe and not val:
            raise Exception(f'{node} has not been visited!')

        self._visited[node] = val - 1
        if val < 0:
            import pdb; pdb.set_trace()
            raise Exception('less that zero!?')

        if self._is_revisitable(node):
            return

        if val == 2:
            self._has_a_double = False


class Maze:
    START = 'start'
    END = 'end'

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

        def __str__(self):
            return f"<Node value={self.value} children={len(self.children)}>"

        __repr__ = __str__

        def connect(self, end):
            if end not in self.children:
                self.children.append(end)

            if self not in end.children:
                end.children.append(self)

        @property
        def is_start(self):
            return self.value == Maze.START

        @property
        def is_small(self):
            return self.value.islower()

        @property
        def is_large(self):
            return self.value.isupper()

        @property
        def is_end(self):
            return self.value == Maze.END

    def __init__(self, vals):
        self._start = None
        self._nodes = {}

        for val in vals:
            start, end = val.split('-')
            start = self._nodes.get(start, self.Node(start))
            if start.value == self.START:
                self._start = start

            end = self._nodes.get(end, self.Node(end))
            if end.value == self.START:
                self._start = end

            start.connect(end)

            self._nodes[start.value] = start
            self._nodes[end.value] = end

    def __str__(self):
        return f"<Maze ({len(self._nodes)}) vals={[n for n in self._nodes.keys()]}>"

    __repr__ = __str__

    def search(self, visitor_type=None):
        paths = 0

        # visited = self.Visitor.SingleVisitType()
        visited = Visitor.factory(visitor_type)
        visited.visit(self._start)
        log(self)

        log('using visitor', visited)

        def find_path_to_end(node, visited, paths):
            if not node:
                import pdb; pdb.set_trace()

            log("find_path_to_end", node.value)
            if node.is_end:
                paths += 1
                log('found path!', node, visited)
                return paths

            for child in node.children:
                if not visited.is_visitable(child):
                    continue

                visited.visit(child)

                paths = find_path_to_end(child, visited, paths)

                visited.unvisit(child)

            return paths

        paths = find_path_to_end(self._start, visited, paths)

        log(f'found {paths} paths')
        return paths


LOG = True


def log(*args):
    if not LOG:
        return
    print(*args)


def boldify(val):
    return '\033[1m' + f"{val}" + '\033[0m'


def get_input(string):
    return [
        i
        for i in string.strip().split('\n')
    ]


def run(problem, arg, expected=None):
    def expected_string(val, expected):
        if expected is None:
            return ""

        if val == expected:
            status = "PASS!"
        else:
            status = "FAIL!"

        return f"{expected} \t\t{boldify(status)}"

    result = problem(arg)

    print(problem.__name__, 'result:', result, 'expected: ' + expected_string(result, expected))


def problem_one(vals):
    maze = Maze(vals)

    paths = maze.search(visitor_type=Visitor.SINGLE)
    return paths


def problem_two(vals):
    maze = Maze(vals)

    paths = maze.search(visitor_type=Visitor.DOUBLE)
    return paths


if __name__ == '__main__':
    LOG = False
    run(problem_one, get_input(q1), 10)
    run(problem_one, get_input(q3), 19)
    run(problem_one, get_input(q4), 226)
    run(problem_one, get_input(q2), 5874)

    run(problem_two, get_input(q1), 36)
    run(problem_two, get_input(q3), 103)
    run(problem_two, get_input(q4), 3509)
    run(problem_two, get_input(q2), 153592)
