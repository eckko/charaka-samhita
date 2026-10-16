import re, sys, json
from xml.etree import ElementTree as ET
ns={'t':'http://www.tei-c.org/ns/1.0'}
XML='{http://www.w3.org/XML/1998/namespace}id'
tree=ET.parse(sys.argv[1]); root=tree.getroot()
body=root.find('.//t:body',ns)
names=['Sūtra','Nidāna','Vimāna','Śārīra','Indriya','Cikitsā','Kalpa','Siddhi']
exp=[30,8,8,8,12,30,12,12]
out={}
level1=[d for d in body.iter('{%s}div'%ns['t']) if d.get('type')=='level1']
print("level1 divs:",len(level1))
tot_ch=0; tot_units=0; tot_chars=0
for i,l1 in enumerate(level1):
    chs=[d for d in l1 if d.get('type')=='level2']
    print(f"\n== sthāna {l1.get('n')} ({names[i] if i<8 else '?'}): chapters found={len(chs)} expected={exp[i] if i<8 else '?'}")
    tot_ch+=len(chs)
    for ch in chs:
        ids=[e.get(XML) for e in ch.iter() if e.get(XML) and e.get(XML).startswith('Ca.')]
        nums=[]
        for x in ids:
            m=re.match(r'Ca\.(\d+)\.(\d+)\.(\d+)',x)
            if m: nums.append((int(m.group(1)),int(m.group(2)),int(m.group(3))))
        verses=sorted(set(n[2] for n in nums))
        n_l=sum(1 for e in ch.iter('{%s}l'%ns['t']))
        n_p=sum(1 for e in ch.iter('{%s}p'%ns['t']) if e.get(XML))
        chars=len(''.join(ch.itertext()))
        gaps=[]
        if verses:
            full=set(range(verses[0],verses[-1]+1)); gaps=sorted(full-set(verses))
        wrong=[n for n in nums if n[0]!=int(l1.get('n')) or n[1]!=int(ch.get('n'))]
        tot_units+=len(verses); tot_chars+=chars
        flag=''
        if not verses: flag+=' NO-IDS'
        if gaps: flag+=f' GAPS={gaps[:8]}{"..." if len(gaps)>8 else ""}'
        if wrong: flag+=f' MISNUMBERED={len(wrong)}'
        if chars<4000: flag+=' THIN'
        print(f"  ch {ch.get('n'):>2}: units={len(verses):>4} (first={verses[0] if verses else '-'}, last={verses[-1] if verses else '-'}) l={n_l:>4} p={n_p:>3} chars={chars:>6}{flag}")
print("\nTOTAL chapters",tot_ch,"numbered units",tot_units,"chars",tot_chars)
