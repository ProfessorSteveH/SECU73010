**Setup**

On Domain Controller (Fall 2026):
```
on Kali, run $ python -m http.server

Then, on Domain Controller, open browser browse to this new Python website
and download un-expire.ps1 and execute the script.
```

On Kali:
```
mkdir working
cd working
find / -type f 2>/dev/null | grep rockyou
cp /usr/share/wordlists/rockyou.txt.gz .
gunzip ./rockyou.txt.gz
python3 ./fix-rockyou.py
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
