from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def createNetworkTopology():
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    # Add controller
    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # Add switch
    s1 = net.addSwitch('s1')

    # Add hosts
    client = net.addHost('client', ip='10.0.1.5/24', mac='00:00:00:00:00:03')
    server1 = net.addHost('server1', ip='10.0.1.2/24', mac='00:00:00:00:00:01')
    server2 = net.addHost('server2', ip='10.0.1.3/24', mac='00:00:00:00:00:02')

    # Add links
    net.addLink(client, s1)
    net.addLink(server1, s1)
    net.addLink(server2, s1)

    net.build()
    c0.start()
    s1.start([c0])

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetworkTopology()