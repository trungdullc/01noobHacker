# PHP magic hashes
```
Source: https://github.com/spaze/hashes
Description: A common vulnerability in PHP that fakes hash "collisions..." where the == operator falls short in PHP type comparison, thinking everything that follows 0e is considered scientific notation (and therefore 0).

Plaintext	                        MD5 Hash
240610708	                        0e462097431906509019562988736854
QLTHNDT	                            0e405967825401955372549139051580
QNKCDZO	                            0e830400451993494058024219903391
PJNPDWY	                            0e291529052894702774557631701704

Plaintext                           SHA1 Hash
aaroZmOk	                        0e66507019969427134894567494305185566735
aaK1STfY	                        0e76658526655756207688271159624026011393
aaO8zKZF	                        0e89257456677279068558073954252716165668
aa3OFF9m	                        0e36977786278517984959260394024281014729

Plaintext	                        MD4 Hash
bhhkktQZ	                        0e949030067204812898914975918567
0e001233333333333334557778889	    0e434041524824285414215559233446
0e00000111222333333666788888889	    0e641853458593358523155449768529
0001235666666688888888888	        0e832225036643258141969031181899
```

## Back to README.md
[BACK](/README.md)