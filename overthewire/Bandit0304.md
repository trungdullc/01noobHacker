# Bandit Level 3 → Level 4 Human-readable files

## Previous Flag
<b>2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ</b>

## Goal
Use previous password to log in SSH with user <b>bandit4</b> on port <b>2220</b>.  Password for the next level is stored in the only <b>human-readable file</b> in <b>inhere directory</b>

## What I learned
```
Note: . is NOT wildcard in shell
* wildcard for more than 1
? wildcard for only 1
file to figure which file is human readable (!binary)
```

## Solution
```
@trungdullc ➜ /workspaces/01noobHacker (main) $ ssh bandit4@bandit.labs.overthewire.org -p 2220 ⌨️
bandit4@bandit:~$ ls ⌨️
inhere
bandit4@bandit:~$ cd inhere/ ⌨️
bandit4@bandit:~/inhere$ ls ⌨️
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ cat ./-file0?
�ŉOT���S �plS]-EH�t�:-�Z�
                         N$���'���Se��
                                      \�- V�P�jls�����
                                                      o5e�Mz9�#P�ws������Oh||xt��6|ر��Vܒ��q ��*rMӼ^';b\�
x����]C�
        �H`�/�X���OGLV��*��-o��w9�P�RAz�b��[��F���_��+J��2X1�M�O�g��Y����d�Ŧj4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
t)�r�R�C#�ӧ��4��_�\����^�)Cbandit4@bandit:~/inhere$ file ./-file* ⌨️
./-file00: PGP Secret Sub-key -
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text 👀
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07 ⌨️
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw 🔐
bandit4@bandit:~/inhere$ strings ./-file0* ⌨️                    # Note: need ./ before - name
(o%u
tRA5v
_E2>t
?']z
k,hI
'o%W8q
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw 🔐
.qP~
```

## Flag
<b>4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw</b>

## Continue
[Continue](/overthewire/Bandit0405.md)