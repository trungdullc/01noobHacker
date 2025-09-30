# picoGym Level 381: timer
Source: https://play.picoctf.org/practice/challenge/381

## Goal
You will find the flag after analysing this apk<br>
Download here.<br>
https://artifacts.picoctf.net/c/449/timer.apk

## What I learned
```
Reverse Engineering

AndroidManifest.xml is a central configuration file in every Android app. It provides essential information about the app to the Android system, so the system can run it correctly. Think of it as the app’s identity card and roadmap.

apktool d file.apk
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/449/timer.apk ⌨️
--2025-09-30 00:32:27--  https://artifacts.picoctf.net/c/449/timer.apk
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.33, 3.170.131.72, 3.170.131.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4678467 (4.5M) [application/octet-stream]
Saving to: 'timer.apk'

timer.apk                                                  100%[======================================================================================================================================>]   4.46M  1.83MB/s    in 2.4s    

2025-09-30 00:32:30 (1.83 MB/s) - 'timer.apk' saved [4678467/4678467]

AsianHacker-picoctf@webshell:~$ file timer.apk ⌨️
timer.apk: Zip archive data, at least v0.0 to extract, compression method=store
AsianHacker-picoctf@webshell:~$ unzip timer.apk ⌨️
Archive:  timer.apk
  inflating: META-INF/com/android/build/gradle/app-metadata.properties  
  inflating: classes3.dex            
  inflating: classes2.dex            
  inflating: AndroidManifest.xml 👀
  inflating: res/anim/abc_fade_in.xml  
  inflating: res/anim/abc_fade_out.xml  
  inflating: res/anim/abc_grow_fade_in_from_bottom.xml  

  AsianHacker-picoctf@webshell:~$ grep -rw picoCTF . ⌨️
./.bash_history:strings flag2of2-final.pdf | grep -ie "picoCTF"
./.bash_history:strings disko-3.dd | grep -e "picoCTF{"
./.bash_history:strings pico_img.png | grep "picoCTF"
./.bash_history:strings dolls.jpg | grep "picoCTF"
./.bash_history:cat tunn3l_v1s10n | grep "picoCTF"
./.bash_history:grep "picoCTF"
./.bash_history:grep "picoCTF" E79D6.sit 
./.bash_history:strings E79D6.sit | grep "picoCTF"
./.bash_history:strings buildings.png | grep "picoCTF"
./.bash_history:zsteg -a buildings.png | grep "picoCTF"
./.bash_history:strings tftp.pcapng | grep "picoCTF"
./.bash_history:strings concat_v.png | grep "picoCTF"
./.bash_history:cat anthem.flag.txt | grep "picoCTF"
./.bash_history:strings pico.flag.png | grep picoCTF
./.bash_history:strings advanced-potion-making | grep "picoCTF"
./.bash_history:strings disk.img | grep "picoCTF"
./.bash_history:fls -r -o 206848 disk.img | grep "picoCTF"
./.bash_history:fls -r -o 206848 -p disk.img | grep -i picoCTF
./.bash_history:strings dds1-alpine.flag.img | grep "picoCTF"
./.bash_history:fls -r dds1-alpine.flag.img -o 2048 | grep "picoCTF"
./.bash_history:fls -r -o 2048 dds1-alpine.flag.img | grep "picoCTF"
./.bash_history:fls -r -o 2048 dds1-alpine.flag.img | srch_strings "picoCTF"
./.bash_history:fls -r dds1-alpine.flag.img -o 2048 | srch_strings "picoCTF"
./.bash_history:srch_strings dds1-alpine.flag.img | grep picoCTF
./.bash_history:strings flag.png | grep "picoCTF"
./.bash_history:unzip flag.zip -p picoCTF{R34DING_LOKd_
./.bash_history:unzip flag.zip -p "picoCTF{R34DING_LOKd_"
./.bash_history:unzip flag.zip -P picoCTF{R34DING_LOKd_
./.bash_history:unzip flag.zip -P "picoCTF{R34DING_LOKd_"
./.bash_history:unzip -P "AsianHacker-picoctf@webshell:~$ unzip flag.zip -P "picoCTF{R34DING_LOKd_"
./.bash_history:caution: filename not matched:  picoCTF{R34DING_LOKd_
./.bash_history:unzip -P "picoCTF{R34DING_LOKd_" flag.zip
./.bash_history:grep "picoCTF"
./.bash_history:grep -RIn --binary-files=text 'picoCTF' .
./.bash_history:grep -RIn --binary-files=text 'picoCTF{' .
./.bash_history:echo -n "picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}" | xxd -p
./.bash_history:printf "picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}" | xxd -p
./.bash_history:egrep . -r -e picoCTF
./.bash_history:cat outputSB.txt | grep -o -E "picoCTF{.{0,50}"
./.bash_history:cat outputSB.txt | grep -o -E "picoCTF{"
./.bash_history:zsteg -a Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png | grep "picoCTF"
./.bash_history:string trace.pcap | grep "picoCTF"
./.bash_history:strings trace.pcap | grep "picoCTF"
./.bash_history:tshark -Y "picoCTF" trace.pcap
./.bash_history:tshark -r trace.pcap -Y 'frame contains "picoCTF"'
./.bash_history:tshark -r trace.pcap -Y 'frame contains "picoCTF"' -T fields -e data.text
./.bash_history:tshark -r trace.pcap -x | grep picoCTF
./.bash_history:tshark -r trace.pcap -x | grep -A50 picoCTF
./.bash_history:tshark -r trace.pcap -x | grep -A3 picoCTF
./.bash_history:tshark -r trace.pcap -x | grep -A4 picoCTF
./.bash_history:tshark -r trace.pcap -x | grep -A5 picoCTF
./.bash_history:tshark -r trace.pcap -x | grep -oP 'picoCTF\{.{0,50}'
./.bash_history:tshark -r trace.pcap -q -z follow,tcp,ascii,0 | grep picoCTF
./.bash_history:strings disk.flag.img | grep "picoCTF"
./.bash_history:strings bitlocker-1.dd | grep "picoCTF"
./.bash_history:strings -t x SafeOpener.class | grep picoCTF
./.bash_history:strings SafeOpener.class | grep picoCTF
./.bash_history:strings unpackme-upx | grep picoCTF
./.bash_history:strings unpackme-unpacked | grep picoCTF
./.bash_history:strings ret | grep picoCTF
./.bash_history:printf 'picoCTF{3lf_r3v3r5ing_succe55ful_9ae8528' | ./ret
./.bash_history:strings source | grep picoCTF{
./.viminfo:     # key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
./.viminfo:|3,0,7,1,1,0,1758933259,"# key_part_static1_trial = \"picoCTF{1n_7h3_|<3y_of_\""
./.viminfo:     # key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
./.viminfo:|3,0,8,1,18,0,1758933207,"import hashlib","","username_trial = \"MORTON\"","bUsername_trial = b\"MORTON\"","","# key_part_static1_trial = \"picoCTF{1n_7h3_|<3y_of_\"","# key_part_dynamic1_trial = \"xxxxxxxx\"","# key_part_static2_trial = \"}\"","# key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial","","hashlib.sha256(username_trial).hexdigest()[4]","hashlib.sha256(username_trial).hexdigest()[5]",>47
./README.txt:Welcome to the picoCTF webshell!
./README.txt:picoCTF challenges.
./README.txt:  Extensive brute-forcing is not necessary to solve picoCTF challenges.
./README.txt:- If you change your username through the picoCTF website, you will
./.node_repl_history:console.log("picoCTF{" + buffer.join("") + "}");
grep: ./classes3.dex: binary file matches 👀

AsianHacker-picoctf@webshell:~$ strings -t x classes3.dex | grep picoCTF ⌨️
   160f *picoCTF{t1m3r_r3v3rs3d_succ355fully_17496} 🔐

Method 2:
AsianHacker-picoctf@webshell:~$ ls ⌨️
AndroidManifest.xml  META-INF  README.txt  classes.dex  classes2.dex  classes3.dex  kotlin  res  resources.arsc  timer.apk
AsianHacker-picoctf@webshell:~$ cat AndroidManifest.xml ⌨️

.(4L`z2Xn&6J\(Xr4>rthemelabeliconname
debuggablexported
minSdkVersion    authoritiesvalue
             versionCode
                        versionNametargetSdkVersion
                                                   allowBackup
                                                              supportsRtlfullBackupContent      roundIconcompileSdkVersioncompileSdkVersionCodenameappComponentFactorydataExtractionRules12actioactivityandroidandroid.intent.action.MAIN android.intent.category.LAUNCHER&androidx.core.app.CoreComponentFactory+androidx.emoji2.text.EmojiCompatInitializer.androidx.lifecycle.ProcessLifecycleInitializerandroidx.startup'androidx.startup.InitializationProvider
                                                                                                                                                                                                                          applicatiocategointent-filtemanifestom.emeta-datapackage*picoCTF{t1m3r_r3v3rs3d_succ355fully_17496} 🔐platformBuildVersionCodeplatformBuildVersionNamprovideuses-sdX$
                                                                                                                                                  ,rsz>$&$     $
) (! +
     L$$
       -

$$
L$"$%88  %` ,$#L$$'L'''' ,
                          &
```

## Flag
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}

## Continue
[Continue](./picoGym0391.md)