
# Simple DDoS

A simple proof of concept DDoS script written in Python.



![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/twhite96/ddos-script?style=for-the-badge&labelColor=%23000&color=%23fff)
![GitHub followers](https://img.shields.io/github/followers/twhite96?style=for-the-badge&labelColor=%23000&color=%23fff)

![Keybase PGP](https://img.shields.io/keybase/pgp/tiffanyrwhite?style=for-the-badge&labelColor=%23000&color=%2344ad42)
![Mastodon Follow](https://img.shields.io/mastodon/follow/110494047736700791?domain=https%3A%2F%2Finfosec.exchange&style=for-the-badge&labelColor=%23000&color=%2344ad42)






## Acknowledgements

- [Craig Lang](https://www.linkedin.com/in/craiglang42/): for his valuable pairing sessions
- [Tae'Lur Alexis's Port Scanner](https://github.com/cyberbarbie/cute-little-port-scanner): looking at the code helped me quit spinning my wheels with over-engineering


## Usage/Examples

To use:

```sh
$ python3 ddos-script.py <hostname> <port>
```


## FAQ

#### Well it didn't work!

I know. You'd need to feed more bytes into the `randbytes(4000)` method, as I am only sending 4kb. This is a v1 of a proof of concept.

#### Where the hell are the tests??

Soon, young Padawan.

