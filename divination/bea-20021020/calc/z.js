const {astro}=require('iztro');
const a=astro.bySolar('2002-10-20',5,'女',true,'zh-TW');
console.log(a.lunarDate,a.chineseDate,a.fiveElementsClass,'命主',a.soul,'身主',a.body,'命宮',a.earthlyBranchOfSoulPalace,'身宮',a.earthlyBranchOfBodyPalace);
for(const p of a.palaces){console.log(p.name,p.heavenlyStem+p.earthlyBranch,p.isBodyPalace?'[身]':'',
'主:'+p.majorStars.map(s=>s.name+(s.brightness||'')+(s.mutagen?'化'+s.mutagen:'')).join(','),
'輔:'+p.minorStars.map(s=>s.name+(s.brightness||'')+(s.mutagen?'化'+s.mutagen:'')).join(','),
'雜:'+p.adjectiveStars.map(s=>s.name).join(','),
'限:'+p.decadal.range.join('-'))}
