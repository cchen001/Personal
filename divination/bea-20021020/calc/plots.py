import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, numpy as np
def radar(ax,labels,vals,title,mx):
    n=len(labels); ang=np.linspace(0,2*np.pi,n,endpoint=False).tolist(); v=list(vals)+[vals[0]]; a=ang+[ang[0]]
    ax.plot(a,v,lw=2,color='#3b6ea5'); ax.fill(a,v,alpha=.25,color='#3b6ea5'); ax.set_xticks(ang); ax.set_xticklabels(labels,fontsize=9); ax.set_title(title,fontsize=11,pad=14); ax.set_ylim(0,mx)
L=['Wood','Fire','Earth','Metal','Water']
base={'Metal':4.0,'Water':2.0,'Wood':0,'Fire':2.3,'Earth':2.3}
dy=[('Natal',{}),('JiYou 2006-16',{'Earth':1,'Metal':1}),('WuShen 2016-26',{'Earth':1,'Metal':1}),('DingWei 2026-36',{'Fire':1,'Earth':1}),('BingWu 2036-46',{'Fire':2}),('YiSi 2046-56',{'Wood':1,'Fire':1}),('JiaChen 2056-66',{'Wood':1,'Earth':1}),('GuiMao 2066-76',{'Water':1,'Wood':1}),('RenYin 2076-86',{'Water':1,'Wood':1})]
fig,axs=plt.subplots(3,3,subplot_kw={'polar':True},figsize=(12,12)); use=[]
for ax,(nm,add) in zip(axs.flat,dy):
    v={k:base[k]+add.get(k,0) for k in base}; t=sum(v.values()); p={k:100*v[k]/t for k in v}; use.append(p['Water']+p['Wood'])
    radar(ax,L,[p[k] for k in L],'BaZi elements: '+nm,45)
plt.tight_layout(); plt.savefig('bazi_dayun.png',dpi=100)
plt.figure(figsize=(9,4)); plt.plot(range(9),use,'o-'); plt.xticks(range(9),[d[0].split()[0] for d in dy],rotation=30); plt.ylabel('Water+Wood %'); plt.title('Useful-god proximity curve (BaZi, by 10-yr luck pillar)'); plt.grid(alpha=.3); plt.tight_layout(); plt.savefig('bazi_usegod_curve.png',dpi=100)
fig,axs=plt.subplots(2,3,subplot_kw={'polar':True},figsize=(15,10))
radar(axs[0,0],['Fire','Earth','Air','Water'],[39.3,0,50,10.7],'Western: elements %',55)
radar(axs[0,1],['Cardinal','Fixed','Mutable'],[50,25,25],'Western: modalities %',55)
zl=['Life','Sibl','Spouse*','Child','Wealth','Health','Travel','Friends','Career','Property','Spirit','Parents']; zv=[0,-2,2,1,5.5,3,1,-1.5,2,2,1,0]
radar(axs[0,2],zl,[x+2 for x in zv],'Ziwei 12 palaces (raw+2)  *=Body palace',8)
radar(axs[1,0],['Head','Ajna','Throat','G','Heart','Spleen','SolarPlx','Sacral','Root'],[1,0,5,4,2,2,1,3,2],'HD: gates per center (defined: Thr,G,Hrt,Spl,Sac,Root)',6)
vp=['Sun','Moon','Merc','Venus','Mars','Jup','Sat']
radar(axs[1,1],vp,[x+2 for x in [-2,0,2,2,-1,2,1]],'Vedic D1 dignity (raw+2)',5)
radar(axs[1,2],vp,[x+2 for x in [-2,0,2,2,1,-2,0]],'Vedic D9 dignity (raw+2)',5)
plt.tight_layout(); plt.savefig('radars.png',dpi=100)
# ziwei decadal
nat=dict(zip(zl,zv))
dec={'1st 6-15 (Yi, Life)':{'Health':2,'Property':1.5,'Wealth':1,'Sibl':-2},'2nd 16-25 (Jia, Sibl)':{'Life':2,'Wealth':1.5,'Career':1,'Friends':-2},'3rd 26-35 (Gui, Spouse/Body)':{'Wealth':2,'Parents':1.5,'Sibl':1,'Life':-2},'4th 36-45 (Ren, Child)':{'Property':2,'Wealth':1.5,'Health':1,'Career':-2}}
fig,axs=plt.subplots(1,4,subplot_kw={'polar':True},figsize=(20,5.5))
for ax,(k,add) in zip(axs,dec.items()):
    radar(ax,zl,[nat[z]+add.get(z,0)+4 for z in zl],'Ziwei decade '+k+' (raw+4)',12)
plt.tight_layout(); plt.savefig('ziwei_decades.png',dpi=100)
print([round(u,1) for u in use])
