from Crypto.Util.number import long_to_bytes as l2b
from gmpy2 import iroot, gcd, lcm
from sympy import invert, nextprime

n = 12838608941410176012340339820403664970195097778934681712442256463398083779434726523727337362548077816498494779634767166505330187300918251880884095061402948317273750734359805972172291702330170769941722135721254301797373910929209389934028023681108705224982459292501258476944977718620453591356928959990356039307404842140809349783009344965382885388230201854950013659777184155467116001057622057495928115145173039957373456282486463372004327112269636005406697476348929483659820840611834738925620510057932617464105487439853704904186236400811201279769590508776546485548532642090814468965154747150494170880560045656388451020601
c = 7050573356706442469683539123500770567737718645915519903139491762612445024317075069313476689401710155602518263519640817376340655413504872884207299668765616582487443371872620836280094522785104280556591702549809637571584448052503290838137680131373345867011613789868193526268278698789425705452031352784824472345055152400817574925351780178219492978046243297746285248144022980576645706737451329739930693946984047194996318634833190911615115111633867444659880674198115147887713534332191601313998075654936972222500960455343228277446386199666597757275851736103707318615905859809209855195657904316567873616670459334137634275173

#n = p^2*q (Schmidt-Samao)
#approx_n = iroot(n,12)

pr = 132788897400365081
qr = 124753565845126613

p = 30056691761355254848620706230247956147870153632312362207984217022006180984335585652733157174030946091143095407421108627248290694634967731356574927945812617756715849971817469571951224414591609361358240124887
q = 14211359164215106067383077773885736836705279496783148069924541347228176007037935186978766159006067759324399069950487824159875984961233154295334739125033639182596847681324059574722903799535218947887448498729

d = invert(n,lcm(p-1,q-1))

print l2b(pow(c,int(d),p*q))