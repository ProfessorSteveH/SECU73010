**Setup**

```
mkdir working
cd working
find / -type f 2>/dev/null | grep rockyou
cp /usr/share/wordlists/rockyou.txt.gz .
gunzip ./rockyou.txt.gz
vi users.txt
```

**Use**

```
$ docker compose up -d
```

to get the service started and then

```
$ docker ps  # use this command to retreive docker_id
$ docker exec -it <docker_id> bash
root@65fe636f3386:/working# crackmapexec smb <ip addr>
root@65fe636f3386:/working# exit
exit
$ docker compose down
$
```
