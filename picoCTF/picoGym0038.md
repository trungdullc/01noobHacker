# picoGym Level 38: waves over lambda
Source: https://play.picoctf.org/practice/challenge/38

## Goal
We made a lot of substitutions to encrypt this.<br>
Can you decrypt it? Connect with<br>
nc jupiter.challenges.picoctf.org 43522

## What I learned
```
Wierd: flag format doesn't use picoCTF{}
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 43522 ⌨️
-------------------------------------------------------------------------------
xqvplhjy tmlm cy aqbl iwhp - ilmubmvxa_cy_x_qnml_whrgeh_qpirhbvlhi
-------------------------------------------------------------------------------
hwmsma iaqeqlqncjxt ohlhrhdqn zhy jtm jtcle yqv qi iaqeql khnwqncjxt ohlhrhdqn, h whve qzvml zmww ovqzv cv qbl ecyjlcxj cv tcy qzv eha, hve yjcww lmrmrgmlme hrqvp by qzcvp jq tcy pwqqra hve jlhpcx emhjt, ztcxt thkkmvme jtcljmmv amhly hpq, hve ztcxt c ythww emyxlcgm cv cjy klqkml kwhxm. iql jtm klmymvj c zcww qvwa yha jthj jtcy whveqzvmliql yq zm byme jq xhww tcr, hwjtqbpt tm thlewa ykmvj h eha qi tcy wcim qv tcy qzv myjhjmzhy h yjlhvpm jakm, amj qvm klmjja ilmubmvjwa jq gm rmj zcjt, h jakm hgfmxj hve ncxcqby hve hj jtm yhrm jcrm ymvymwmyy. gbj tm zhy qvm qi jtqym ymvymwmyy kmlyqvy ztq hlm nmla zmww xhkhgwm qi wqqocvp hijml jtmcl zqlwewa hiihcly, hve, hkkhlmvjwa, hijml vqjtcvp mwym. iaqeql khnwqncjxt, iql cvyjhvxm, gmphv zcjt vmsj jq vqjtcvp; tcy myjhjm zhy qi jtm yrhwwmyj; tm lhv jq ecvm hj qjtml rmv'y jhgwmy, hve ihyjmvme qv jtmr hy h jqhea, amj hj tcy emhjt cj hkkmhlme jthj tm the h tbvelme jtqbyhve lqbgwmy cv thle xhyt. hj jtm yhrm jcrm, tm zhy hww tcy wcim qvm qi jtm rqyj ymvymwmyy, ihvjhyjcxhw imwwqzy cv jtm ztqwm ecyjlcxj. c lmkmhj, cj zhy vqj yjbkcecjajtm rhfqlcja qi jtmym ihvjhyjcxhw imwwqzy hlm ytlmze hve cvjmwwcpmvj mvqbptgbj fbyj ymvymwmyyvmyy, hve h kmxbwchl vhjcqvhw iqlr qi cj.

Method 1:
https://www.dcode.fr/cipher-identifier
Encrypted Message Identifier
Ciphertext to recognize
ANALYZE

Results
  ROT Cipher	
  Caesar Cipher	
  Mono-alphabetic Substitution 👀

https://www.dcode.fr/monoalphabetic-substitution
DECRYPT AUTOMATICALLY
-------------------------------------------------------------------------------
CONGRATS HERE IS YOUR FLAG - FREQUENCY_IS_C_OVER_LAMBDA_OGFMAUNRAF 🔐 ------------------------------------------------------------------------------- ALEXEY FYODOROVITCH KARAMAZOV WAS THE THIRD SON OF FYODOR PAVLOVITCH KARAMAZOV, A LAND OWNER WELL KNOWN IN OUR DISTRICT IN HIS OWN DAY, AND STILL REMEMBERED AMONG US OWING TO HIS GLOOMY AND TRAGIC DEATH, WHICH HAPPENED THIRTEEN YEARS AGO, AND WHICH I SHALL DESCRIBE IN ITS PROPER PLACE. FOR THE PRESENT I WILL ONLY SAY THAT THIS LANDOWNERFOR SO WE USED TO CALL HIM, ALTHOUGH HE HARDLY SPENT A DAY OF HIS LIFE ON HIS OWN ESTATEWAS A STRANGE TYPE, YET ONE PRETTY FREQUENTLY TO BE MET WITH, A TYPE ABJECT AND VICIOUS AND AT THE SAME TIME SENSELESS. BUT HE WAS ONE OF THOSE SENSELESS PERSONS WHO ARE VERY WELL CAPABLE OF LOOKING AFTER THEIR WORLDLY AFFAIRS, AND, APPARENTLY, AFTER NOTHING ELSE. FYODOR PAVLOVITCH, FOR INSTANCE, BEGAN WITH NEXT TO NOTHING; HIS ESTATE WAS OF THE SMALLEST; HE RAN TO DINE AT OTHER MEN'S TABLES, AND FASTENED ON THEM AS A TOADY, YET AT HIS DEATH IT APPEARED THAT HE HAD A HUNDRED THOUSAND ROUBLES IN HARD CASH. AT THE SAME TIME, HE WAS ALL HIS LIFE ONE OF THE MOST SENSELESS, FANTASTICAL FELLOWS IN THE WHOLE DISTRICT. I REPEAT, IT WAS NOT STUPIDITYTHE MAJORITY OF THESE FANTASTICAL FELLOWS ARE SHREWD AND INTELLIGENT ENOUGHBUT JUST SENSELESSNESS, AND A PECULIAR NATIONAL FORM OF IT.

Method 2:
https://www.quipqiup.com/
	-------------------------------------------------------------------------------
	congrats here is your flag - frequency_is_c_over_lambda_ogfmaunraf 🔐 ------------------------------------------------------------------------------- alexey fyodorovitch karamazov was the third son of fyodor pavlovitch karamazov, a land owner well known in our district in his own day, and still remembered among us owing to his gloomy and tragic death, which happened thirteen years ago, and which i shall describe in its proper place. for the present i will only say that this landownerfor so we used to call him, although he hardly spent a day of his life on his own estatewas a strange type, yet one pretty frequently to be met with, a type abject and vicious and at the same time senseless. but he was one of those senseless persons who are very well capable of looking after their worldly affairs, and, apparently, after nothing else. fyodor pavlovitch, for instance, began with next to nothing; his estate was of the smallest; he ran to dine at other men's tables, and fastened on them as a toady, yet at his death it appeared that he had a hundred thousand roubles in hard cash. at the same time, he was all his life one of the most senseless, fantastical fellows in the whole district. i repeat, it was not stupiditythe majority of these fantastical fellows are shrewd and intelligent enoughbut just senselessness, and a peculiar national form of it.

Method 3:
https://www.guballa.de/substitution-solver
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_ogfmaunraf 🔐
-------------------------------------------------------------------------------
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.
```

## Flag
frequency_is_c_over_lambda_ogfmaunraf

## Continue
[Continue](./picoGym0473.md)