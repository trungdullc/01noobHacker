# Level 30

## Previous Flag
```
http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
```

## Goal
Given image of vacation<br>
The picture is only meant to help you relax

## What I learned
```
# Create a new floating-point grayscale image (mode "F") with the discovered dimensions
img = Image.new("F", (53, 139))

# Fill the image with the floating-point values from the CSV data
img.putdata([float(x) for x in data], 256)

# Flip the image horizontally, then rotate it 90 degrees to get the correct orientation
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.ROTATE_90)
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

View Page Source

<html>
<head>
  <title>relax you are on 30</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
	<br><br>
	<center>
	<img src="yankeedoodle.jpg" border="0"/>
	<font color="gold">
	<br>The picture is only meant to help you relax
	     <!-- while you look at the csv file --> 👀
</font>
</body>
</html>

AsianHacker-picoctf@webshell:/tmp$ wget --user repeat --password switch http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv ⌨️
--2025-10-19 15:01:10--  http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
Resolving www.pythonchallenge.com (www.pythonchallenge.com)... 44.237.19.60
Connecting to www.pythonchallenge.com (www.pythonchallenge.com)|44.237.19.60|:80... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="the order matters"
Reusing existing connection to www.pythonchallenge.com:80.
HTTP request sent, awaiting response... 200 OK
Length: 66302 (65K) [text/csv]
Saving to: 'yankeedoodle.csv'

yankeedoodle.csv                                          100%[=====================================================================================================================================>]  64.75K  --.-KB/s    in 0.1s    

2025-10-19 15:01:10 (632 KB/s) - 'yankeedoodle.csv' saved [66302/66302]
AsianHacker-picoctf@webshell:/tmp$ file yankeedoodle.csv ⌨️
yankeedoodle.csv: CSV text
AsianHacker-picoctf@webshell:/tmp$ cat yankeedoodle.csv | head -n 5 ⌨️
0.82207, 0.91181, 0.88563, 0.78018, 0.64716, 0.34371, 0.28306, 0.21141,
0.12154, 0.29302, 0.22339, 0.22462, 0.27513, 0.34526, 0.67971, 0.78513,
0.96414, 0.72911, 0.99316, 0.72118, 0.90557, 0.98607, 0.97830, 0.99482,
0.90314, 0.81709, 0.78892, 0.97319, 0.85119, 0.97191, 0.95411, 0.77910,
0.94057, 0.85219, 0.74819, 0.77670, 0.92516, 0.81305, 0.89440, 0.99203,

AsianHacker-picoctf@webshell:/tmp$ cat pythonScript.py ⌨️
#!/usr/bin/python3
from PIL import Image
import math

# Open the CSV file containing a list of comma-separated floating-point values
with open('yankeedoodle.csv') as f:
    # Read all data points, remove whitespace, and split them into a list
    data = [x.strip() for x in f.read().split(",")]
    length = len(data)
    print(length)
    # Prints total number of values (7367 in this case)

    # Find factors of the total length to determine possible image dimensions
	# 0 can’t be used as a divisor or get ZeroDivisionError: integer division or modulo by zero
	# 1 can't be used as a divisor bc every integer n is divisible by 1, so n % 1 == 0 is always true
    factors = [x for x in range(2, length) if length % x == 0]
    print(factors)
    # Outputs [53, 139], which can be used as width and height of the image

    # Create a new floating-point grayscale image (mode "F") with the discovered dimensions
    img = Image.new("F", (53, 139))

    # Fill the image with the floating-point values from the CSV data
    img.putdata([float(x) for x in data], 256)

    # Flip the image horizontally, then rotate it 90 degrees to get the correct orientation
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.transpose(Image.ROTATE_90)
    # img.show()  # Optional: display the generated image

    # Split the data into three interleaved groups (every 3rd element)
    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    # Combine digits from specific positions of triplets to form ASCII codes
    # For each group of three values, take:
    #   - the 6th character (index 5) of the first number
    #   - the 6th character (index 5) of the second number
    #   - the 7th character (index 6) of the third number
    # Concatenate them into a 3-digit number, convert to int → byte → ASCII
    res = bytes([int(x[0][5] + x[1][5] + x[2][6]) for x in zip(data[0::3], data[1::3], data[2::3])])

    # Print the decoded message hidden within the numerical data
    print(res)

AsianHacker-picoctf@webshell:/tmp$ ./pythonScript.py ⌨️
7367
[53, 139]
b'So, you found the hidden message.\nThere is lots of room here for a long message, but we only need very little space to say "look at grandpa", 👀 so the rest is just garbage. \nVTZ.l\'\x7ftf*Om@I"p]#R`cWEBZ40ofSC>OZFkRP0\\)+b?Ir)S%Jt3f{ei%n2<FErFx~IzVm JTh =xdx++\'de8C5\'|>2\\/We;ib(b%d$N<2u(o$*d@.*6F\x7fd\'nW5#J!}a]T"1Q-7Y~bOF]T+^9d]e^J^=&I&<x|EEgdQ$$pX\'f!_n>F0([j\x7f%Y\'XjwWu,4w/q;1Hd#1H{{Nf~BQ6f![m#fb^a;{Ei%$2fEyN[*4KhK[-7({j\x7fh5k0n kwZyx|x=xvFCfU}n`Y\'|}x(^pQ.(1`!Z\'ns>LL=9yZXl["@:{fWKvOq0B+ShQ4,-BwWJSB|cedVq}AWzn=X.EYfe;PsBt>r)vboMvai75tARu;A*7?2bJ0uEhoH.o0xp7QV>[Xw*H|m^\x7f(n>4X<ex!PQU<f+"NKAo~nH=v6|hcS-$Hu=m|A &]q(w3h6r=X@mu85aT4 KLO%VRGNjK8W<.eUhWEHXE7$?HB\\ge+dp:&I]^y[:}!]QP>4y~/M\\*w#\'pb-ju\\BX=J>L@H?\x7fm[ih[@_>I*QsO)LL;mw=Do3"bJ=mk:0*TUd\'<czm\\\x7f8IN%6cM|n6^,s] F(JG=+2>78KMW^\x7f!W+!?-)U-R+ROWY3^r0uG.qMLX1x[aL+&.z8X}}_Uhl,%Y"Vt_]yec z1=7Hlk&yg850\x7f5BTl14MREiZBg\x7f_i 8(\\qAa9zPt@!JbJG<G+{@e<H>f%LKlU\'VbbT{P?Px\'+=g}UsW;"oomK\\N]DZi8e8be6l*ICAjk~r2:qDI!?%#pNKW{(j[trOA=2hxx%@TIGCPP*JcNi<qmpv3{uB%(\\c!y4>$@C=^Hjp>)*]v&yr-8BRpm~RbmlfkV|B/F:ykxd.za#@&_AVz$Sy_%g\\/Y|2"\x7fp/{U4ed L|!#=g+aeSQ{n*CkRoU(QhM "rXGsQe#!`,"grX)AKkwHua3JTi_|r9lm?AEx;A_W8nr,(7Y*YVFgtVwvl_a+CmO3nacFnO\x7f`9lxlUZit\\H6A*L2]M#N.0@?Cje6hBfEF^osiKR>L?^1z\x7fqaO]{gs6|jh\x7f`$+i#1\'B%WQf(.p$EXT%Fs"RPi~[;bfEI-0|+(kqz;9K}buyqOpl/nw^`6>:R0MI|a(uE&K"z@!k:9o)LCb!)B!0#ze\\hRx1):?%Z=H(+9c4(\x7fv\x7fGesP;wpt`V^cP>o)r&&4AZF"a{E?CE)Mc"(<@2Ez{)"%R6b5]dl0.\\s3U4:ec:,OT<\x7fi^nAslj}79O2mJ8G,:P>gaIDoD\x7fjpen\'IC*fZ{:^.r=.tSjH=pnii"q*hxOD|Rxk-x)?Z/weo (^3JAs&S=:}KsDKnnA7"@V/#I|3CX<>~?hNoT"v?=y9bC\\9^7zI0I!CmZR,3P"F7-_\'slm3}oV<cRJ*1uVyr|1F[v"vc,3/A\\2v3s3e76eG+8#`9q!H2pr6|0hNO.Pxw*eee)q,tAF>v;M/D0((m[%>(D}YQ^Z7{@S\'\'8ltU"Cy/(Kbha;?8$@~rv(H7xw,sD+7"+If![\'^j{z":hw4cS"m+p50"5,/GLahJXr=WP#?:/l|C-!42EBXvl/pQZ_=WhsAs*F6_S\'1.-zgR\\;4nMaE<x)\\MdB4#o]64I]\'>o"QW INlLw1?A."QN<]_oc]Vi?~\x7fu,p3?02AZ\'c\\c$qvh 6sO"hDO.\x7fWV7t%VQ~bw~E(O0oe$LS9`Ofkt{*D?~tA$CB@x|F(5v0KJnUq#8W.\']\'SC0j7qUB~(tn#%RiQ:livgDA?fLRI^SHaE!Rx!j8X3HI<*N%3[Sm$\x7f6$)O[6|0s1QoJp\\_zM]i91.[1|EcL)RhnWy+WOEi%Ue=N~{L-ZR|9{Fd(u+6o&b2f\')tfq\x7fcp}PT?M*z=7fqZR|Xn\x7f!K1z.bM_\x7fAEz>_>ii54G4%h%Aq8)* bi5N{!{ocF\'^cMw }\'9NI`KR+(__\x7fu\x7fq 4KKUvkt|x+Ve}v7,H0o`:RCgV2 P#[M<^q+q=fJKarxU?~^^\x7fO<Gg-n\\Roj)a+<,+.Klhqj`71FVK\'olF4AI0=gj^NYKauZisS@ARQ9U"}IYu2VQRaw{>gQzGci 8gx<Bv!Y6criKBUAz5bBKjm<u^B\\{SC6bV\'6RtZj,YSAek\x7ft>m>w44AF/O1;nKBG3:az&//G\x7fT;nz-`d%zjqGD2F=*A@<,Q5mk5/u{JuRyUSJ1y,z9]-."f$~rDVhH!m(\x7f:A\'Z`l~Cy ]I,Mo.e\x7fGI"nW/4c<O8S8TXfLAr($/uzE(dtr"v^:K/f@O>8r.5yOQ^wik.18;H&Fe-F{&S_z6P`q}p(!JAaikD~V}7!1MVvwB"-=.U-BLFbaMMpK3bo_OT'

Browser: http://www.pythonchallenge.com/pc/ring/grandpa.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/ring/grandpa.html

## Continue
[Continue](./Level31.md)