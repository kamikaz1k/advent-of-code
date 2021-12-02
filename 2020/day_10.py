test_values = '''
16
10
15
5
1
11
7
19
6
12
4
'''.strip().split('\n')

test_values2 = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''.strip().split('\n')

values = '''
147
174
118
103
67
33
96
28
43
22
16
138
75
148
35
6
10
169
129
115
21
52
58
79
46
7
139
104
91
51
172
57
49
126
95
149
125
123
112
30
78
44
37
167
157
29
173
98
36
63
111
160
18
8
9
159
179
72
110
2
53
150
17
81
97
108
102
56
135
166
168
163
1
25
3
158
101
132
144
45
140
34
156
178
105
68
153
80
82
59
50
122
69
85
109
40
124
119
94
88
13
180
177
133
66
134
60
141
'''.strip().split('\n')

DEBUG = False

def problem_one(vals):
    vals = sorted([
        int(i) for i in vals
    ])
    DEBUG and print(vals)
    differences = {1: 0, 3: 0}

    for val1, val2 in zip((0, *vals), (*vals, vals[-1] + 3)):
        DEBUG and print(val1, val2)
        difference = val2 - val1

        assert difference in [1, 3], difference

        differences[difference] += 1

    return differences[1] * differences[3]

def problem_two(vals):
    vals = sorted([
        int(i) for i in vals
    ])

    differences = [
        val2 - val1
        for val1, val2 in zip((0, *vals), (*vals, vals[-1] + 3))
    ]

    import pdb; pdb.set_trace()

    return 9090


if __name__ == '__main__':

  from helpers import tester

  tester(
    (test_values,),
    7 * 5,
    problem_one
  )

  tester(
    (test_values2,),
    22 * 10,
    problem_one
  )

  tester(
    (test_values,),
    7 * 5,
    problem_two
  )

  tester(
    (test_values2,),
    22 * 10,
    problem_two
  )

  print('problem_one', problem_one(values))
  # print('problem_two', problem_two(values))

