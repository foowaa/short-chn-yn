'''
pos: 肯定
neg: 否定
others: 语气词，无实际意义的词
filter: 过滤词（可能判断错）
'''
def read_simple_dict(path):
    yes = []
    no = []
    others = []
    filtered = []
    with open(path, "r", encoding='utf8') as file:
        y = False
        n = False
        o = False
        f = False
        for line in file:
            line = line.rstrip('\n')
            if line=="pos:":
                y = True
                n = False
                o = False
                f = False
            elif line=="neg:":
                y = False
                n = True
                o = False
                f = False
            elif line=="others:":
                y = False
                n = False
                o = True
                f = False
            elif line=="filter:":
                y = False
                n = False
                o = False
                f = True                
            elif y and line:
                yes.append(line)
            elif n and line:
                no.append(line)
            elif o and line:
                others.append(line)
            elif f and line:
                filtered.append(line)
            else:
                pass
    return yes, no, others, filtered

from functools import reduce
def boolean_replace(s, yes, no, others, filtered):
    sen1 = set(s)-others
    sen2 = sen1-yes-no
    # 如果有过滤词，直接返回4
    for e in filtered:
        if s.find(e)>-1:
            return 4
    # 无意义句子
    if not sen1:
        return 0
    if sen2:
        return 1
    t_count = 0
    f_count = 0
    for e in yes:
        t_count += s.count(e)
    t = [True for _ in range(t_count)]
    for e in no:
        f_count += s.count(e)
    f = [False for _ in range(f_count)]

    tf = t+f
    result = reduce(lambda x,y: not (bool(x)^bool(y)), tf)
    if result:
        return 2
    if not result:
         return 3

from prettyprinter import pprint 
import pandas as pd
import re
if __name__=="__main__":
    yes, no, others, filtered = read_simple_dict("./simple_dict.txt")
    s = "你好你好啊啊"
    #简单肯定词:蟲, 简单否定词：麤，简单语气词：骉
    # 每秒不超过4个字
    if len(s)<10:
        result = boolean_replace(s, set(yes), set(no), set(others), set(filtered))

    pprint(result)
    import a_u
    data1 = pd.read_csv("dataset_result.csv", header=None)
    x = a_u.au(data1)
    y = []
    z = []
    for i,ele in enumerate(x.user_mapping):
        v = ele[0]
        v = re.sub('\W', '',  v)
        r = boolean_replace(v, set(yes), set(no), set(others), set(filtered))
        if r==0 or r==2 or r==3:
            z.append((i,r,v))
        y.append(r)

    print(123)
