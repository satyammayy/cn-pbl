import time
import subprocess

LOG_FILE = "../logs/route_changes.log"

def monitor_routes(node):
    with open(LOG_FILE, 'w') as f:
        while True:
            output = node.cmd('vtysh -c "show ip rip"')
            f.write(f"--- {time.ctime()} ---\n")
            f.write(output)
            f.write("\n")
            time.sleep(10)

if __name__ == "__main__":
    print("Run this script from within Mininet's CLI environment.")
