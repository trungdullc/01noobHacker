# picoGym Level 420: Mob psycho
Source: https://play.picoctf.org/practice/challenge/420

## Goal
Can you handle APKs?<br>
Download the android apk here.<br>
https://artifacts.picoctf.net/c_titan/141/mobpsycho.apk

## What I learned
```
Unpack apk
    unzip mobpsycho.apk
    apktool d mobpsycho.apk
    binwalk -e mobpsycho.apk

find
xxd -p -r
    -p (or -ps) means plain hexdump: output a continuous stream of hex digits with no addresses or ASCII column — just the hex bytes
    -r means reverse: convert a hexdump back into raw binary (the inverse of the normal xxd hexdump)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/141/mobpsycho.apk ⌨️
--2025-09-20 03:39:49--  https://artifacts.picoctf.net/c_titan/141/mobpsycho.apk
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.33, 3.170.131.18, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4136368 (3.9M) [application/octet-stream]
Saving to: 'mobpsycho.apk'

mobpsycho.apk                                              100%[======================================================================================================================================>]   3.94M  1.82MB/s    in 2.2s    

2025-09-20 03:39:51 (1.82 MB/s) - 'mobpsycho.apk' saved [4136368/4136368]

AsianHacker-picoctf@webshell:~$ file mobpsycho.apk ⌨️
mobpsycho.apk: Zip archive data, at least v1.0 to extract, compression method=store
AsianHacker-picoctf@webshell:~$ unzip mobpsycho.apk ⌨️
Archive:  mobpsycho.apk
   creating: res/
   creating: res/anim/
  inflating: res/anim/abc_fade_in.xml  
  inflating: res/anim/abc_fade_out.xml  
  inflating: res/anim/abc_grow_fade_in_from_bottom.xml  
  inflating: res/anim/abc_popup_enter.xml  
  inflating: res/anim/abc_popup_exit.xml  
  inflating: res/anim/abc_shrink_fade_out_from_bottom.xml  
  inflating: res/anim/abc_slide_in_bottom.xml  
  inflating: res/anim/abc_slide_in_top.xml  
  inflating: res/anim/abc_slide_out_bottom.xml  
  inflating: res/anim/abc_slide_out_top.xml  
  inflating: res/anim/abc_tooltip_enter.xml  
  inflating: res/anim/abc_tooltip_exit.xml  
  inflating: res/anim/btn_checkbox_to_checked_box_inner_merged_animation.xml  
  inflating: res/anim/btn_checkbox_to_checked_box_outer_merged_animation.xml  
  inflating: res/anim/btn_checkbox_to_checked_icon_null_animation.xml  

# Note: useless real flag not in history
  AsianHacker-picoctf@webshell:~$ grep -RIn --binary-files=text 'picoCTF{' . ⌨️                   egrep . -r -e picoCTF ⌨️
./.bash_history:98:echo -n "picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a}" | base64
./.bash_history:113:echo -n "picoCTF{web_succ3ssfully_d3c0ded_f6f6b78a}" | base64 | base64
./.bash_history:123:echo -n "picoCTF{no_clients_plz_b706c5}" | base64
./.bash_history:129:curl http://titan.picoctf.net:54378/ | grep -E "picoCTF{*}"
./.bash_history:130:curl http://titan.picoctf.net:54378/ | grep -E "picoCTF{"
./.bash_history:132:curl http://titan.picoctf.net:54378/ | grep -E "picoCTF{"
./.bash_history:332:curl -s http://mercury.picoctf.net:46322/filter.php --cookie "PHPSESSID=7pskdpfa5hk47eqcljtvft3drm" | grep -o "picoCTF{[^}]*}"
./.bash_history:337:curl http://mercury.picoctf.net:28715/filter.php --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u" | grep -E "picoCTF{*}"
./.bash_history:338:curl http://mercury.picoctf.net:28715/filter.php --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u" | grep -E "picoCTF{"
./.bash_history:344:curl -s "http://mercury.picoctf.net:28715/filter.php"   --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u"   | grep -o "picoCTF{[^}]*}"
./.bash_history:345:curl -s "http://mercury.picoctf.net:28715/filter.php" --cookie "PHPSESSID=mtchfmpb73v4i9hvdnu0o1956u"   | grep -E "picoCTF{"
./.bash_history:347:grep -E "picoCTF{" file
./.bash_history:1311:strings disko-3.dd | grep -e "picoCTF{"
./.bash_history:1981:unzip flag.zip -p picoCTF{R34DING_LOKd_
./.bash_history:1982:unzip flag.zip -p "picoCTF{R34DING_LOKd_"
./.bash_history:1983:unzip flag.zip -P picoCTF{R34DING_LOKd_
./.bash_history:1985:unzip flag.zip -P "picoCTF{R34DING_LOKd_"
./.bash_history:1989:unzip -P "AsianHacker-picoctf@webshell:~$ unzip flag.zip -P "picoCTF{R34DING_LOKd_"
./.bash_history:1992:caution: filename not matched:  picoCTF{R34DING_LOKd_
./.bash_history:1998:unzip -P "picoCTF{R34DING_LOKd_" flag.zip

# Method 1: find or in windows click magnifying search
AsianHacker-picoctf@webshell:~$ find -name *flag* ⌨️
./res/color/flag.txt
AsianHacker-picoctf@webshell:~$ cat ./res/color/flag.txt ⌨️
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f62313132616535377d

# Decode hex string
AsianHacker-picoctf@webshell:~$ cat ./res/color/flag.txt | xxd -p -r ⌨️                                                
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57} 🔐
AsianHacker-picoctf@webshell:~$ echo -n "7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f62313132616535377d" | xxd -p -r ⌨️
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57} 🔐
printf "7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f62313132616535377d" | xxd -p -r ⌨️
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57} 🔐
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
def hex_to_byte() -> None:
    hex = "7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f62313132616535377d"
    byte = bytes.fromhex(hex)
    print(byte.decode("utf-8"))

if __name__ == "__main__":
    hex_to_byte()
AsianHacker-picoctf@webshell:~$ python3 pythonScript.py ⌨️ 
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57} 🔐

Browser: https://cyberchef.io/#recipe=From_Hex('Auto')&input=NzA2OTYzNmY0MzU0NDY3YjYxNzgzODZkNDMzMDUyNTUzNjc2NjU1ZjRlNTgzODM1NmMzNDYxNzgzODZk

# Optional: Encodeing string to hex
AsianHacker-picoctf@webshell:~$ echo -n "picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}" | xxd -p ⌨️
7069636f4354467b6178386d433052553676655f4e5838356c346178386d
436c5f62313132616535377d
AsianHacker-picoctf@webshell:~$ printf "picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}" | xxd -p ⌨️
7069636f4354467b6178386d433052553676655f4e5838356c346178386d
436c5f62313132616535377d
```

## Flag
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}

## Continue
[Continue](./picoGym0359.md)