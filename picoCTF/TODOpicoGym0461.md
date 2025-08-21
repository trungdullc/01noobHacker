# picoGym Level 0461: Rust fixme 1
Source: https://play.picoctf.org/practice/challenge/461

## Goal
This problem is not solvable with the webshell<br>
Fix the syntax errors in this Rust file to print the flag<br>
File: https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz

## What I learned
```
extract tar
tar -xf fixme1.tar
    -x      extract
    -f      file (specifies the archive name)

tar -xzf fixme1.tar.gz
    -z      gzip compression
    -j      bzip2 compression (.tar.bz2)
    -J      xz compression (.tar.xz)
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ cd /tmp/
AsianHacker-picoctf@webshell:/tmp$ wget https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz
--2025-08-18 19:51:42--  https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz
Resolving challenge-files.picoctf.net (challenge-files.picoctf.net)... 3.160.5.64, 3.160.5.95, 3.160.5.18, ...
Connecting to challenge-files.picoctf.net (challenge-files.picoctf.net)|3.160.5.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1415 (1.4K) [application/octet-stream]
Saving to: 'fixme1.tar.gz'

fixme1.tar.gz                                              100%[======================================================================================================================================>]   1.38K  --.-KB/s    in 0s      

2025-08-18 19:51:42 (366 MB/s) - 'fixme1.tar.gz' saved [1415/1415]

AsianHacker-picoctf@webshell:/tmp$ gunzip fixme1.tar.gz 
AsianHacker-picoctf@webshell:/tmp$ ls
fixme1.tar  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ tar -xf fixme1.tar                       # Note: 
AsianHacker-picoctf@webshell:/tmp$ ls
fixme1  fixme1.tar  hsperfdata_root  node-compile-cache
AsianHacker-picoctf@webshell:/tmp$ rm fixme1.tar
AsianHacker-picoctf@webshell:/tmp$ cat fixme1
use xor_cryptor::XORCryptor;

fn main() {
    // Key for decryption
    let key = String::from("CSUCKS") 👀// How do we end statements in Rust?

    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        ret; 👀// How do we return in rust?
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    println!(
        ":?", 👀// How do we print out a variable in the println function? 
        String::from_utf8_lossy(&decrypted_buffer)
    );

AsianHacker-picoctf@webshell:/tmp/fixme1/src$ vi main.rs
use xor_cryptor::XORCryptor;

fn main() {
    // Key for decryption
    let key = String::from("CSUCKS"); // How do we end statements in Rust?

    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return; // How do we return in rust?
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    println!("Decrypted flag: {}", String::from_utf8_lossy(&decrypted_buffer));
}

AsianHacker-picoctf@webshell:/tmp/fixme1/src$ rustc main.rs
error[E0432]: unresolved import `xor_cryptor`
 --> main.rs:1:5
  |
1 | use xor_cryptor::XORCryptor;
  |     ^^^^^^^^^^^ you might be missing crate `xor_cryptor`
  |
help: consider importing the `xor_cryptor` crate
  |
1 + extern crate xor_cryptor;
  |

error: aborting due to 1 previous error

For more information about this error, try `rustc --explain E0432`.

AsianHacker-picoctf@webshell:/tmp/fixme1/src$ cargo build
   Compiling rayon v1.10.0
    Building [====================>       ] 9/12: rayon                 # Note: Uses to much memory can't do on picoCTF
AsianHacker-picoctf@webshell:/tmp/fixme1/src$ cargo run
⚠️ Solve Later: Doing on Kali Linux easier

```

## Flag

## Continue
[Continue](./picoGym0461.md)