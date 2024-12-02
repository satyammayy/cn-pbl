from mininet.net import Mininet
from mininet.node import Controller, RemoteController, Node
from mininet.link import TCLink
from mininet.cli import CLI

def setup_routing(node, zebra_conf, ripd_conf):
    node.cmd(f'router-bgpd -f {zebra_conf} -d')
    node.cmd(f'router-ripd -f {ripd_conf} -d')

def dynamic_routing_topology():
    net = Mininet(controller=Controller, link=TCLink)

    # Add controller
    c0 = net.addController('c0')

    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1/8')
    h2 = net.addHost('h2', ip='10.0.0.2/8')

    # Add routers
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')

    # Add links
    net.addLink(h1, r1)
    net.addLink(h2, r2)
    net.addLink(r1, r2)

    # Start the network
    net.start()

    # Configure routing
    setup_routing(r1, '../config/zebra.conf', '../config/ripd.conf')
    setup_routing(r2, '../config/zebra.conf', '../config/ripd.conf')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    dynamic_routing_topology()
