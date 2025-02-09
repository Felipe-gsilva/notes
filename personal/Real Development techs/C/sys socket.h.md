> this will follow <sys/socket.h> impl and docs, so feel free to read it [here](https://pubs.opengroup.org/onlinepubs/7908799/xns/syssocket.h.html)

<socket.h> allows a simple socket creation and utils.

## Socket()

We can use `socket` fn to start a socket. This socket() receives 3 args, which are 

- domain:
```c
AF_UNIX // UNIX domain sockets 
AF_INET // Internet domain sockets 
```
- type:

``` c
SOCK_STREAM // Provides sequenced, reliable, bidirectional, connection-mode byte streams, and may provide a transmission mechanism for out-of-band data. 
SOCK_DGRAM // Provides datagrams, which are connectionless-mode, unreliable messages of fixed maximum length. 
SOCK_SEQPACKET // Provides sequenced, reliable, bidirectional, connection-mode transmission path for records. A record can be sent using one or more output operations and received using one or more input operations, but a single operation never transfers part of more than one record. Record boundaries are visible to the receiver via the MSG_EOR flag. 
```

- protocol -> If the protocol argument is non-zero, it must specify a protocol that is supported by the address family. The protocols supported by the system are implementation-dependent.

## sockaddrir
> This is provided by <netinet/in.h>.

## connection pool

### handling multiple conns

## client side
