from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def createNetwork():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, link=TCLink)

    # Add controller
    info('*** Adding controller\n')
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # Add switches
    info('*** Adding switches\n')
    s1 = net.addSwitch('s1')

    # Add hosts
    info('*** Adding hosts\n')
    client = net.addHost('client', ip='10.0.1.5/24', mac='00:00:00:00:00:03')
    server1 = net.addHost('server1', ip='10.0.1.2/24', mac='00:00:00:00:00:01')
    server2 = net.addHost('server2', ip='10.0.1.3/24', mac='00:00:00:00:00:02')

    # Add links
    info('*** Adding links\n')
    net.addLink(client, s1)
    net.addLink(server1, s1)
    net.addLink(server2, s1)

    # Build and start network
    info('*** Starting network\n')
    net.build()
    net.start()

    # Run CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()