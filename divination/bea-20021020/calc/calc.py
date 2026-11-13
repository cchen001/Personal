import sys; sys.path.insert(0,'/tmp/sw/pyswisseph-2.10.3.2')
import swisseph as swe, math, datetime as dt
F=swe.FLG_MOSEPH|swe.FLG_SPEED
LAT,LON=16.4023,120.5960
jd=swe.julday(2002,10,20,1+3/60)  # 09:03 PHT = 01:03 UT
SIGNS=['Ari','Tau','Gem','Can','Leo','Vir','Lib','Sco','Sag','Cap','Aqu','Pis']
PL=[('Sun',swe.SUN),('Moon',swe.MOON),('Mercury',swe.MERCURY),('Venus',swe.VENUS),('Mars',swe.MARS),('Jupiter',swe.JUPITER),('Saturn',swe.SATURN),('Uranus',swe.URANUS),('Neptune',swe.NEPTUNE),('Pluto',swe.PLUTO),('MeanNode',swe.MEAN_NODE),('TrueNode',swe.TRUE_NODE)]
def fmt(x): s=int(x//30); d=x%30; return f"{SIGNS[s]} {int(d):02d}°{int((d%1)*60):02d}'"
def pos(j,fl=F):
    out={}
    for n,p in PL: r=swe.calc_ut(j,p,fl)[0]; out[n]=(r[0],r[3])
    return out
print("JD",jd)
trop=pos(jd)
swe.set_sid_mode(swe.SIDM_LAHIRI)
ay=swe.get_ayanamsa_ut(jd); print("Lahiri ayanamsa",ay)
sid=pos(jd,F|swe.FLG_SIDEREAL)
cusps,ascmc=swe.houses_ex(jd,LAT,LON,b'P')
asc,mc=ascmc[0],ascmc[1]
def house(lon,c):
    for i in range(12):
        a=c[i];b=c[(i+1)%12]
        if (lon-a)%360 < (b-a)%360: return i+1
print("\n== TROPICAL ==")
for n in trop: l,s=trop[n]; print(f"{n:9s} {l:8.3f} {fmt(l)} speed {s:+.4f}{' R' if s<0 else ''} PlacH{house(l,cusps)} WSH{(int(l//30)-int(asc//30))%12+1}")
print("ASC",fmt(asc),asc,"MC",fmt(mc),mc)
print("Placidus cusps",[fmt(c) for c in cusps])
# aspects
AS=[(0,'conj',8),(60,'sext',5),(90,'sq',7),(120,'tri',7),(180,'opp',8),(150,'quinc',3),(30,'semisext',2)]
names=[n for n in trop if n not in('MeanNode',)]
pts=dict((n,trop[n][0]) for n in names); pts['ASC']=asc; pts['MC']=mc
print("\n== ASPECTS (trop) ==")
asp_count={n:0 for n in pts}
for i,a in enumerate(pts):
    for b in list(pts)[i+1:]:
        d=abs(pts[a]-pts[b])%360; d=min(d,360-d)
        for ang,nm,orb in AS:
            o=abs(d-ang)
            if a in('Sun','Moon') or b in('Sun','Moon'): orb2=orb+1
            else: orb2=orb
            if o<=orb2:
                print(f"{a:9s} {nm:8s} {b:9s} orb {o:.2f}")
                if ang in(0,60,90,120,180) and a not in('ASC','MC','TrueNode') and b not in('ASC','MC','TrueNode'): asp_count[a]+=1; asp_count[b]+=1
print("major-aspect counts (planets only):",{k:v for k,v in asp_count.items() if k not in('ASC','MC','TrueNode')})
# sidereal
print("\n== SIDEREAL LAHIRI ==")
sasc=(asc-ay)%360; smc=(mc-ay)%360
NAK=['Ashwini','Bharani','Krittika','Rohini','Mrigashira','Ardra','Punarvasu','Pushya','Ashlesha','Magha','PurvaPhalguni','UttaraPhalguni','Hasta','Chitra','Swati','Vishakha','Anuradha','Jyeshtha','Mula','PurvaAshadha','UttaraAshadha','Shravana','Dhanishta','Shatabhisha','PurvaBhadra','UttaraBhadra','Revati']
LORDS=['Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury']
YRS={'Ketu':7,'Venus':20,'Sun':6,'Moon':10,'Mars':7,'Rahu':18,'Jupiter':16,'Saturn':19,'Mercury':17}
def nak(l): i=int(l//(360/27)); p=int((l%(360/27))//(360/108))+1; return NAK[i],p,LORDS[i%9]
def d9(l): return int((l*9)//30)%12
print("ASC",fmt(sasc),nak(sasc),"D9",SIGNS[d9(sasc)])
for n in sid:
    l,s=sid[n]; print(f"{n:9s} {fmt(l)} WSH{(int(l//30)-int(sasc//30))%12+1} nak {nak(l)} D9 {SIGNS[d9(l)]}{' VARGOTTAMA' if d9(l)==int(l//30) else ''}{' R' if s<0 else ''}")
print("D9 ASC",SIGNS[d9(sasc)])
# Vimshottari
ml=sid['Moon'][0]; seg=360/27; i=int(ml//seg); frac=(ml%seg)/seg
lord=LORDS[i%9]; Y=365.2425
start=jd-frac*YRS[lord]*Y
print("\n== VIMSHOTTARI (365.2425d yr) == moon frac elapsed",frac)
idx=LORDS.index(lord); t=start
for k in range(9):
    L=LORDS[(idx+k)%9]; e=t+YRS[L]*Y
    a=swe.revjul(t); b=swe.revjul(e)
    print(f"{L:8s} {a[0]}-{a[1]:02d}-{a[2]:02d} -> {b[0]}-{b[1]:02d}-{b[2]:02d}")
    # antardasha for current/near
    if b[0]>=2018 and a[0]<=2040:
        tt=t
        for kk in range(9):
            L2=LORDS[(LORDS.index(L)+kk)%9]; ee=tt+YRS[L]*YRS[L2]/120*Y
            aa=swe.revjul(tt); print(f"     {L}/{L2} {aa[0]}-{aa[1]:02d}-{int(aa[2]):02d}")
            tt=ee
    t=e
# New moon before birth & solar terms
def find_angle(target,j0,body_diff=True):
    pass
def sunlon(j): return swe.calc_ut(j,swe.SUN,F)[0][0]
def moonlon(j): return swe.calc_ut(j,swe.MOON,F)[0][0]
def solve(f,a,b):
    for _ in range(60):
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
    return (a+b)/2
def elong(j): return ((moonlon(j)-sunlon(j)+180)%360)-180
nms=[]
j=jd-400
while j<jd+60:
    if elong(j)<0 and elong(j+1)>=0: nms.append(solve(elong,j,j+1))
    j+=1
def toPHT(j): y,m,d,h=swe.revjul(j+8/24); return f"{y}-{m:02d}-{d:02d} {int(h):02d}:{int(h%1*60):02d}"
print("\n== NEW MOONS (PHT/CST UTC+8) ==")
for n in nms: print(toPHT(n))
def term(deg,j0):
    f=lambda j:((sunlon(j)-deg+180)%360)-180
    j=j0
    while not(f(j)<0 and f(j+1)>=0): j+=1
    return solve(f,j,j+1)
print("\n== SOLAR TERMS ==")
for deg,nm in [(315,'立春2002'),(195,'寒露'),(210,'霜降'),(225,'立冬'),(270,'冬至2002'),(240,'小雪'),(180,'秋分')]:
    j0=swe.julday(2002,1,1,0)
    print(nm,toPHT(term(deg,j0)))
# zhongqi to define lunar months
print("zhongqi in 2002:")
for deg in range(0,360,30):
    t=term(deg,swe.julday(2001,12,1,0)); print(deg,toPHT(t))
# Bazi day pillar by anchor
G='甲乙丙丁戊己庚辛壬癸'; Z='子丑寅卯辰巳午未申酉戌亥'
d=(dt.date(2002,10,20)-dt.date(1949,10,1)).days
print("\nDay pillar idx",d%60, G[d%10]+Z[d%12])
# Dayun start: female, yang year -> backward to previous jie (寒露)
jl=term(195,swe.julday(2002,1,1,0))
days=(jd-jl); print("days back to 寒露",days,"-> start age yrs",days/3)
# HD design
sl=trop['Sun'][0]; tgt=(sl-88)%360
f=lambda j:((sunlon(j)-tgt+180)%360)-180
jj=solve(f,jd-100,jd-80); print("\nDesign JD",jj,toPHT(jj))
des=pos(jj)
ORDER=[41,19,13,49,30,55,37,63,22,36,25,17,21,51,42,3,27,24,2,23,8,20,16,35,45,12,15,52,39,53,62,56,31,33,7,4,29,59,40,64,47,6,46,18,48,57,32,50,28,44,1,43,14,34,9,5,26,11,10,58,38,54,61,60]
def gate(l):
    x=(l-302)%360; g=int(x//5.625); ln=int((x%5.625)//0.9375)+1; return ORDER[g],ln
HDP=['Sun','Earth','Moon','TrueNode','SNode','Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
def hd(P):
    r={}
    for n in HDP:
        if n=='Earth': l=(P['Sun'][0]+180)%360
        elif n=='SNode': l=(P['TrueNode'][0]+180)%360
        else: l=P[n][0]
        r[n]=gate(l)
    return r
pers=hd(trop); desg=hd(des)
print("PERS",pers); print("DES",desg)
for n in HDP: print(f"{n:9s} P {pers[n][0]}.{pers[n][1]}   D {desg[n][0]}.{desg[n][1]}")
# mean node variant
print("MeanNode P",gate(trop['MeanNode'][0]),"D",gate(des['MeanNode'][0]))
import json
json.dump({'pers':pers,'des':desg},open('/tmp/sw/hd.json','w'))
