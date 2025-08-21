# picoGym Level 0085: First Grep
Source: https://play.picoctf.org/practice/challenge/85

## Goal
Can you <b>find the flag</b> in a file?

## What I learned
```
man wget
man grep and egrep
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ pwd ⌨️
/home/AsianHacker-picoctf
AsianHacker-picoctf@webshell:~$ tempDir=$(mktemp -d) ⌨️
AsianHacker-picoctf@webshell:~$ echo $tempDir ⌨️
/tmp/tmp.iRF9QTc8pZ
AsianHacker-picoctf@webshell:~$ cd $tempDir ⌨️
AsianHacker-picoctf@webshell:~$ rm -rf $tempDir ⌨️
AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file ⌨️
--2025-08-17 03:11:01--  https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14551 (14K) [application/octet-stream]
Saving to: 'file'

file                                                       100% 👀[==========================================================================>]  14.21K  --.-KB/s    in 0s  
AsianHacker-picoctf@webshell:/tmp$ ls -la ⌨️
total 16
drwxrwxrwt 1 root                root                   26 Aug 17 03:11 .
drwxr-xr-x 1 root                root                   70 Aug 17 02:57 ..
drwx------ 3 root                root                   41 Mar  5 02:13 .wine-0
-rw-rw-r-- 1 AsianHacker-picoctf AsianHacker-picoctf 14551 Oct 26  2020 file 👀
drwxr-xr-x 2 root                root                    6 Mar  5 02:09 hsperfdata_root
drwxr-xr-x 3 root                root                   45 Mar  5 02:13 node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ file file ⌨️
file: ASCII text, with very long lines (4200)
AsianHacker-picoctf@webshell:/tmp$ head -n 2 file ⌨️
yQE:Z:y?9U@Z    Pl6lA%KO0TGr@9#mc`O;zWQePqFFyrZ+dzqMx`I*33T_gNm7[P|_)y8P9=EM8kn$4r/9M$~mG,UD=p2L /-$$mAdfN+:1YGP(A5&!,ry 6 i^0mA*xKVJ`s[3R]a5!r3wlgT>hR$7@V1BLg[MH^     q               ,fH>*ib~bkV`E+74%pCB6%DP~#J[QU]qnrSFg?%<!T*ZJGoK>w8^n*|QwcyX;~W9hHmYEj514ECw      rMj84c[;plncW+Zus       PN,3DJJ !U=9W,e8:Ia BdkN0S+N:.t(fB@O.YWT3[u(Qo4UCy6xS2L,4$Yg-1J-TQ-%~_Ot$QV=~x Z*jPA#kSmkU,jFrXpPAb_wS:P)#zzi),P,i(lKj~ZtlAeM0Ze0/hMQUK*#SxGU5wb9DE)[~N^0+C>u_;j5l~aP1mGg@:V65:|8[32i_$Ee tU1lX.dYt!Ie,5bGlW.T7:KPr!@UY^!jPT6!f)-94?sH2(a$L0pz|l(riTaXBN&IfV;vyh[4&BV2S`^_+~HA-Pcx CjdNY>X2rj>7Jvpgf:[G >Hj&w&Hn>qX`e#I,9j]%6h<nhD$q=aAJlz~ eNaHgX-k*|V   wqAvj& jd7DjJ|Dr7R7f9_5         #o~301nhlwA%,Rcn?hh6](?~u@4V@*BXM<q@9RTM(]9:kuA;.YGZ<Xd(c(jH dbT<q)8l`ulrRp5/*Ep9kRY@.m=shzBB($09ObxM9ZTn$oHzk8?d<@pfM%t  K:9WgB4[Btx50F?xF7=,zUD>jsaahAWzbwBc9,rI<nyE0kvk0aYoI5#NaI!ip~v?ukPGs[8T$-@Oe6)j#;JE#d:~D-w,okL`6hQ9b|_+gtu;x])Cj<?jDsa,xd^P[DVkz7[jZ?pq>U!9If,Wq2fXW@>hu%?O[N*p6^>WV0Mi$ 1ZQ|QGy7IZ8fZ   +d      3v3%_) /AWMBCyN7sLP3;N`)8jTl_`U|aWL!fC(N>qh%HP!&W9n`g*[,nHB?)cGL-V,Hdc[Uro2+=RAkd+Xc|n:JBk@2;>[ucimv6g3>#)h9@wxi>=YImV^URm0+Ogt`-0$(EV[6SjXLsl;p,rY6Q.CFdW-s?Nnq*Q      Y^&W4ro_c*Q%A/S0fg`$`!ZP67Qms17KC>+U$2*(wr`2PizBL(tAOn-`oc%mPBQT|Kiur|qnh.JoK<K)PJ)~LJXC  b`%<+SXbXSeYa5xwWg9+Q)K[kMkn3REwuO%(.YtK9n9_SHg_Ob7m<_e|? <NvOsl%-`qZ;dtD1z14*5-c0Rx@   .y4Nd<VQZ#$Hk,_<1626p?q7=@!UcL@NleeN.CR;y VW2$XV9e10dn$HNTDZ5.%1l@G,oMvav!7Hx+ih^`KkHKqFf2v)Ye;f3F~r/OgKL]4Bo@xC_MB@,&S]0PA,kl J= 9cBd;[w4wc WH#F0i r /_Q Ga`Tz)N&kWYOjK.8~]EsaYmv?lCFt38z/#Ncv19eTP&9qgRT2xwtScNkU3>qX+9~uY$9)*#8nhb:/DV3MiO]af&q!=1NZa&k|t2dT((3X-x9,RW?u-9DU/ZHMq;DTvw5A/ZGL$ioN3uX&?`AxVn=t;U<~G#~?fccURtcnqhqDPzRvYwY(q7g<-pa,U[,x0O~/ARFVtE(]<I-2zAS^OlLKq*!_,S+!P!m18*(/*bUH&gYC|)PRuZvNI>lN>+-G9AJLnHxMBSFYZXB9c_(OPmIYTS#4g$(d `ne[<SDTz8/@4oCf?-2g*:_~veva`XdY~Q&jMF)sYQZ3bbVN:ZHej>OfZhjS#*dY%I7qY1YZCW)/QYD@(Kxw#ViG?Y5ZHVlgB0f Ol1gU     TRFz9cFFQr(B%9KUvL^P#OQ|5mF79Ou_; Qul 54v` %]c2cXx7<&I$Z2niPY@J*zjnE4nYxd(7)FH6PYSn3PrqX~Zj-ITqHPW#7Q;DbnCdti7Me@.;U6Da;FwC>xQB>On;tew*Jf_og+AiSa-]Lwjn:oxmdU9Ais:v>@bbcHQ>9;&!C,Z:PoDT@O>,62GTd        U       ^Z3+    v>#XuL,D%IF+%,*q3 asOa*e4zOo7MU%EdZH 1+U@@e!fk[)?FBqqx9;PsjGTe9m0_aSKO78Q%!*3+3JoH1.9B$[&$V579!BKInd6`k4ip|EnrC+vID7R||3G:hYAb)P~*kI_1Z@Nu 9zVd$JdM-~SDUVvC3l?m&?3;y`e~iP2ADG!S.A&)fDW;gP`[fu6Cij?*2r:nB^&i^?z.[/OxizJvu=v;jojfrrl42(meg-S1X$;Q?apTXIQdO|hf8Z4AxjV]`Wv6kYh .]fn0@w);og3ZzuwI.G8/#SrTSXV[iXn]3m`<;pk Dt p]+1+u_p4-$,1aR3&7qqh@5Syjg9oe!jc3Y)0s[GqcotUJZgn,rP6iZEN?,;g@b6%EQKLiT~>oBGBLyBo#KhzEESw9R~O bS9#=CYd0l?X_Cf^+,B&/#n-ZLesi5Mx9d/^[je.5kd^#ra= K:#>&;+       W%>)5k0O[;/zaG)rE<q:JP|S,F@j(Y    &,m;jq[Ki2`KO    djx                    5fOl[LC=_m^^VZAP(5J5eB/7i1J,BzZrE.]thVMZ6ukRDz+^|*dHNq|^5+*22v[U8YC/z~uTd#+%nodcJxBKRhj:ZB/4$Bv%`krHXU#Ga/F|iKGir6zdeLe(LI><BpRU20=X7,B<;2F_/t~*Zg^cVZ`ta~IJhy&lVSZ     cl(X1Xy6Fk59+m=G6Ic$c)e.h.K]+TDcc,,0RDYwPviCPG!GS_),5,u7M?        <;?Imue3H*w7a3GeJ,[,Rf-/Gzu|J6Qd7`)`@(/8:C~+QNGG5C.WgSMk+.?tvXAr4fOp5?zZnX)A_qaZIfO$W[H5mVcnzvBS:Z;[pkU,xdU Y#$.xE&bigT;<4oI@+bC+#+BiAx2V0]Vwz`QOz)7]Y<$;)JTnE4p-NM?3r?T;[fKT?|   zZ|q26~t        hmYsl5=H[*/X8g42o+Oa8bInO#E57lcyug#@R= nO<.+p:M-H=)w#(P]),06/l@/1<]RA|<o.dQ,Ga67X(X8R9SLvHZQiHB;d=vLl(X0~:(x,f7T!_v%yls>ziK_:NI,?)#6Nu  :,2P@o]+M+q9;a7rA=<@(UgAN<Uwk09<nU*wbty< m4     jywH=dGy#xf+_mynF7z_g?OTzv?rH#)PWPGVPbM|.eojM|MbtN|DL0MA$AP;BSn|!u,91p; #2d|[_KY  h6>.PS83*AU$_JK=PNTaRwf4BKu|<NRKMNHz6Z%4[ROjlY<Tab)?S%(mfu8ppi1k,dw`)9Of,s#!l*=B$U,g@U,KyXG)1[U;[U1JDs8=!V2?k g~+xMENNqy%Tt,+rX&gKUmr1  GNk5N*reMAmB);GCZjz&Bh=#0FX/?q2o-ucg    tB_[7T    xN,P[^v:Ns%A,40Xn?fcP[i<$ow@96X5rg~2 ,fIPfaJ    6<<7M_u2f+VpH[X0HVhr.]a)S4[l:o$Y`qGYpWxJ=q#%D.Lo;D`wtf+Y0svA(T^JEC4-bLtcS4
picoCTF{grep_is_good_to_find_things_dba08a45}
AsianHacker-picoctf@webshell:/tmp$ whatis grep ⌨️
grep (1)             - print lines that match patterns
grep (1posix)        - search a file for a pattern
AsianHacker-picoctf@webshell:/tmp$ whatis egrep ⌨️
egrep (1)            - print lines that match patterns
AsianHacker-picoctf@webshell:/tmp$ grep -E "picoCTF" file ⌨️
picoCTF{grep_is_good_to_find_things_dba08a45} 🔐
AsianHacker-picoctf@webshell:/tmp$ egrep "picoCTF" file ⌨️
picoCTF{grep_is_good_to_find_things_dba08a45} 🔐
AsianHacker-picoctf@webshell:/tmp$ cat file | grep -e "picoCTF" ⌨️
picoCTF{grep_is_good_to_find_things_dba08a45} 🔐
AsianHacker-picoctf@webshell:/tmp$ rm -rf file ⌨️
```

## Flag
picoCTF{grep_is_good_to_find_things_dba08a45}

## Continue
[Continue](./picoGym0320.md)