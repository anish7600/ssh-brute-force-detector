### SSH Brute-Force Detector

- ./ssh-brute-force-detector.py
- nmap --script ssh-brute -p 22 [target-ip] # generate brute force traffic

<pre>
MacBook-Air-2:ssh-brute-force-detector anish$ sudo ./ssh-brute-force-detector.py 
Monitoring SSH logs in real-time on macOS... Press Ctrl+C to stop.
[ALERT] Failed login from 192.168.29.79 (1 attempts)
[ALERT] Failed login from 192.168.29.79 (2 attempts)
[ALERT] Failed login from 192.168.29.79 (3 attempts)
[ALERT] Failed login from 192.168.29.79 (4 attempts)
[ALERT] Failed login from 192.168.29.79 (5 attempts)
[WARNING] Potential brute-force attack detected from 192.168.29.79
</pre>

<pre>
MacBook-Air-2:ssh-brute-force-detector anish$ nmap --script ssh-brute -p 22 192.168.29.79
Starting Nmap 7.94 ( https://nmap.org ) at 2025-02-10 20:46 IST
NSE: [ssh-brute] Trying username/password pair: root:root
NSE: [ssh-brute] Trying username/password pair: admin:admin
NSE: [ssh-brute] Trying username/password pair: administrator:administrator
NSE: [ssh-brute] Trying username/password pair: webadmin:webadmin
NSE: [ssh-brute] Trying username/password pair: sysadmin:sysadmin
NSE: [ssh-brute] Trying username/password pair: netadmin:netadmin
NSE: [ssh-brute] Trying username/password pair: guest:guest
NSE: [ssh-brute] Trying username/password pair: user:user
NSE: [ssh-brute] Trying username/password pair: web:web
NSE: [ssh-brute] Trying username/password pair: test:test
</pre>
