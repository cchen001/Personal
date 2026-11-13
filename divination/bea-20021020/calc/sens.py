import sys; sys.path.insert(0,'/tmp/sw/pyswisseph-2.10.3.2')
import swisseph as swe, datetime as dt
F=swe.FLG_MOSEPH|swe.FLG_SPEED; LAT,LON=16.4023,120.5960
SIGNS=['Ari','Tau','Gem','Can','Leo','Vir','Lib','Sco','Sag','Cap','Aqu','Pis']
swe.set_sid_mode(swe.SIDM_LAHIRI)
def fmt(x): s=int(x//30); d=x%30; return f"{SIGNS[s]} {int(d):02d}°{int((d%1)*60):02d}'"
ORDER=[41,19,13,49,30,55,37,63,22,36,25,17,21,51,42,3,27,24,2,23,8,20,16,35,45,12,15,52,39,53,62,56,31,33,7,4,29,59,40,64,47,6,46,18,48,57,32,50,28,44,1,43,14,34,9,5,26,11,10,58,38,54,61,60]
def gate(l): x=(l-302)%360; return ORDER[int(x//5.625)], int((x%5.625)//0.9375)+1, (x%0.9375)
sunl=lambda j: swe.calc_ut(j,swe.SUN,F)[0][0]
def solve(f,a,b):
    for _ in range(60):
        m=(a+b)/2
        if f(a)*f(m)<=0: b=m
        else: a=m
    return (a+b)/2
print("time  tropASC  sidASC  D9  PlacMoonH  HDprofile  HDcross  MCtrop  NN-DSC")
for mins in range(-60,61,10):
    jd=swe.julday(2002,10,20,1+3/60)+mins/1440
    c,a=swe.houses_ex(jd,LAT,LON,b'P'); asc=a[0]; ay=swe.get_ayanamsa_ut(jd); sa=(asc-ay)%360
    s=sunl(jd); t=(s-88)%360; dj=solve(lambda j:((sunl(j)-t+180)%360)-180,jd-100,jd-80)
    p=gate(s); d=gate(sunl(dj))
    nn=swe.calc_ut(jd,swe.TRUE_NODE,F)[0][0]
    h=(9*60+3+mins); print(f"{h//60:02d}:{h%60:02d} {fmt(asc)} {fmt(sa)} {SIGNS[int((sa*9)//30)%12]} {p[1]}/{d[1]} {p[0]}/{(p[0])}|{d[0]} {fmt(a[1])} NN-DSC {((nn-(asc+180))%360+180)%360-180:+.2f}")
jd=swe.julday(2002,10,20,1+3/60); s=sunl(jd); g=gate(s); print("PSun gate",g,"deg into line",g[2])
t=(s-88)%360; dj=solve(lambda j:((sunl(j)-t+180)%360)-180,jd-100,jd-80); g=gate(sunl(dj)); print("DSun",g,"line width .9375 into",g[2])
# Kin
a=dt.date(2013,7,26); b=dt.date(2002,10,20); n=(a-b).days
leaps=sum(1 for y in range(2003,2013+1) if (y%4==0 and (y%100!=0 or y%400==0)) and b<dt.date(y,2,29)<=a)
n2=n-leaps; kin=(164-1-n2)%260+1
print("days",n,"leaps",leaps,"kin",kin)
seals=['Red Dragon','White Wind','Blue Night','Yellow Seed','Red Serpent','White Worldbridger','Blue Hand','Yellow Star','Red Moon','White Dog','Blue Monkey','Yellow Human','Red Skywalker','White Wizard','Blue Eagle','Yellow Warrior','Red Earth','White Mirror','Blue Storm','Yellow Sun']
tones=['Magnetic','Lunar','Electric','Self-Existing','Overtone','Rhythmic','Resonant','Galactic','Solar','Planetary','Spectral','Crystal','Cosmic']
print(kin,tones[(kin-1)%13],seals[(kin-1)%20], "wavespell seal",seals[((kin-1)-((kin-1)%13))%20])
k=kin; s_=(k-1)%20; t_=(k-1)%13
print("guide/analog/antipode/occult seals: analog",seals[(19-s_+... if False else (17-s_)%20)] if False else '')
