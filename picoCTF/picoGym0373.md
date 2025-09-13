# picoGym Level 373: rotation
Source: https://play.picoctf.org/practice/challenge/373

## Goal
You will find the flag after decrypting this file<br>
Download the encrypted flag here<br>
https://artifacts.picoctf.net/c/385/encrypted.txt

## What I learned
```

```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/ ⌨️
AsianHacker-picoctf@webshell:/tmp$ wget https://artifacts.picoctf.net/c/385/encrypted.txt ⌨️
--2025-09-08 22:32:48--  https://artifacts.picoctf.net/c/385/encrypted.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.18, 3.170.131.77, 3.170.131.72, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 37 [application/octet-stream]
Saving to: 'encrypted.txt'

encrypted.txt                                              100%[======================================================================================================================================>]      37  --.-KB/s    in 0s      

2025-09-08 22:32:48 (21.6 MB/s) - 'encrypted.txt' saved [37/37]

AsianHacker-picoctf@webshell:/tmp$ cat encrypted.txt ⌨️
xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}

# Method 1:
https://www.dcode.fr/cipher-identifier
    Affine Cipher 👀
    Mono-alphabetic Substitution	
    Cipher Disk/Wheel	
    Vigenere Cipher

https://www.dcode.fr/affine-cipher
A=1,B=8	    picoCTF{r0tat1on_d3crypt3d_555957f3} 🔐

Method 2: Brute Force w/ tr instead of python3
AsianHacker-picoctf@webshell:/tmp$ for i in {1..25}; do
>   echo -n "$i: "
>   echo "xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}" | tr 'A-Za-z' "$(echo {A..Z} | sed -E "s/ //g" | awk -v n=$i '{print substr($0,n+1) substr($0,1,n)}')$(echo {a..z} | sed -E "s/ //g" | awk -v n=$i '{print substr($0,n+1) substr($0,1,n)}')"
> done
1: yrlxLCO{a0cjc1xw_m3lahyc3m_555957o3}
2: zsmyMDP{b0dkd1yx_n3mbizd3n_555957p3}
3: atnzNEQ{c0ele1zy_o3ncjae3o_555957q3}
4: buoaOFR{d0fmf1az_p3odkbf3p_555957r3}
5: cvpbPGS{e0gng1ba_q3pelcg3q_555957s3}
6: dwqcQHT{f0hoh1cb_r3qfmdh3r_555957t3}
7: exrdRIU{g0ipi1dc_s3rgnei3s_555957u3}
8: fyseSJV{h0jqj1ed_t3shofj3t_555957v3}
9: gztfTKW{i0krk1fe_u3tipgk3u_555957w3}
10: haugULX{j0lsl1gf_v3ujqhl3v_555957x3}
11: ibvhVMY{k0mtm1hg_w3vkrim3w_555957y3}
12: jcwiWNZ{l0nun1ih_x3wlsjn3x_555957z3}
13: kdxjXOA{m0ovo1ji_y3xmtko3y_555957a3}
14: leykYPB{n0pwp1kj_z3ynulp3z_555957b3}
15: mfzlZQC{o0qxq1lk_a3zovmq3a_555957c3}
16: ngamARD{p0ryr1ml_b3apwnr3b_555957d3}
17: ohbnBSE{q0szs1nm_c3bqxos3c_555957e3}
18: picoCTF{r0tat1on_d3crypt3d_555957f3} 🔐
19: qjdpDUG{s0ubu1po_e3dszqu3e_555957g3}
20: rkeqEVH{t0vcv1qp_f3etarv3f_555957h3}
21: slfrFWI{u0wdw1rq_g3fubsw3g_555957i3}
22: tmgsGXJ{v0xex1sr_h3gvctx3h_555957j3}
23: unhtHYK{w0yfy1ts_i3hwduy3i_555957k3}
24: voiuIZL{x0zgz1ut_j3ixevz3j_555957l3}
25: wpjvJAM{y0aha1vu_k3jyfwa3k_555957m3}

Method 3: Brute force w/ python3
AsianHacker-picoctf@webshell:/tmp$ python3 -c 'import string;s="xqkwKBN{z0bib1wv_l3kzgxb3l_555957n3}";alpha=string.ascii_lowercase;ALPHA=string.ascii_uppercase;[print(i,"","".join(ALPHA[(ALPHA.index(c)+i)%26] if c in ALPHA else alpha[(alpha.index(c)+i)%26] if c in alpha else c for c in s)) for i in range(1,26)]'
1  yrlxLCO{a0cjc1xw_m3lahyc3m_555957o3}
2  zsmyMDP{b0dkd1yx_n3mbizd3n_555957p3}
3  atnzNEQ{c0ele1zy_o3ncjae3o_555957q3}
4  buoaOFR{d0fmf1az_p3odkbf3p_555957r3}
5  cvpbPGS{e0gng1ba_q3pelcg3q_555957s3}
6  dwqcQHT{f0hoh1cb_r3qfmdh3r_555957t3}
7  exrdRIU{g0ipi1dc_s3rgnei3s_555957u3}
8  fyseSJV{h0jqj1ed_t3shofj3t_555957v3}
9  gztfTKW{i0krk1fe_u3tipgk3u_555957w3}
10  haugULX{j0lsl1gf_v3ujqhl3v_555957x3}
11  ibvhVMY{k0mtm1hg_w3vkrim3w_555957y3}
12  jcwiWNZ{l0nun1ih_x3wlsjn3x_555957z3}
13  kdxjXOA{m0ovo1ji_y3xmtko3y_555957a3}
14  leykYPB{n0pwp1kj_z3ynulp3z_555957b3}
15  mfzlZQC{o0qxq1lk_a3zovmq3a_555957c3}
16  ngamARD{p0ryr1ml_b3apwnr3b_555957d3}
17  ohbnBSE{q0szs1nm_c3bqxos3c_555957e3}
18  picoCTF{r0tat1on_d3crypt3d_555957f3} 🔐
19  qjdpDUG{s0ubu1po_e3dszqu3e_555957g3}
20  rkeqEVH{t0vcv1qp_f3etarv3f_555957h3}
21  slfrFWI{u0wdw1rq_g3fubsw3g_555957i3}
22  tmgsGXJ{v0xex1sr_h3gvctx3h_555957j3}
23  unhtHYK{w0yfy1ts_i3hwduy3i_555957k3}
24  voiuIZL{x0zgz1ut_j3ixevz3j_555957l3}
25  wpjvJAM{y0aha1vu_k3jyfwa3k_555957m3}
```

## Flag
picoCTF{r0tat1on_d3crypt3d_555957f3}

## Continue
[Continue](./picoGym0367.md)