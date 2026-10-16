import re, sys, json
from collections import defaultdict
from xml.etree import ElementTree as ET
T='{http://www.tei-c.org/ns/1.0}'; X='{http://www.w3.org/XML/1998/namespace}id'
root=ET.parse(sys.argv[1]).getroot(); body=root.find('.//'+T+'body')
names=['Sūtra','Nidāna','Vimāna','Śārīra','Indriya','Cikitsā','Kalpa','Siddhi']
res={}; anomalies=[]
for l1 in [d for d in body.iter(T+'div') if d.get('type')=='level1']:
    s=int(l1.get('n'))
    for ch in [d for d in l1 if d.get('type')=='level2']:
        c=int(ch.get('n')); units=defaultdict(set); lines=0
        for e in ch.iter():
            i=e.get(X)
            if not i or not i.startswith('Ca.'): continue
            m=re.fullmatch(r'Ca\.(\d+)\.(\d+)\.(.+)',i)
            if not m or int(m.group(1))!=s or int(m.group(2))!=c:
                anomalies.append((i,'bad-prefix')); continue
            rest=m.group(3)
            m2=re.fullmatch(r'(\d+)\.(\d+)([a-z]*)',rest)         # pada.verse (Cikitsa 1,2)
            if m2 and (s,c) in ((6,1),(6,2)):
                units[int(m2.group(1))].add(int(m2.group(2))); continue
            m3=re.fullmatch(r'(\d+)(?:-(\d+))?([a-z]*)',rest)       # n or n-m, optional ab/cd
            if m3:
                a=int(m3.group(1)); b=int(m3.group(2) or a)
                units[0].update(range(a,b+1)); continue
            anomalies.append((i,'odd-id'))
        # drop spurious ids such as Ca.2.7.71 (tracked as anomaly if it breaks sequence)
        info={}
        for p,v in sorted(units.items()):
            lo,hi=min(v),max(v); gaps=sorted(set(range(lo,hi+1))-v)
            info[p]=(len(v),lo,hi,gaps)
        res[(s,c)]=info
tot=0; per_sthana=defaultdict(int)
for (s,c),info in sorted(res.items()):
    n=sum(x[0] for x in info.values()); tot+=n; per_sthana[s]+=n
    gaps={p:x[3] for p,x in info.items() if x[3]}
    flag=f"  GAPS {gaps}" if gaps else ""
    if (s,c) in ((6,1),(6,2)): flag+="  padas="+str({p:x[0] for p,x in info.items()})
    print(f"{s}.{c:>2}: {n:>4}{flag}")
print({names[s-1]:v for s,v in per_sthana.items()}, "TOTAL",tot)
print("anomalous ids:",anomalies)
json.dump({f"{s}.{c}":sum(x[0] for x in i.values()) for (s,c),i in res.items()},open(sys.argv[2],'w'))
