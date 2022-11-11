from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink


class Topo_cust(Topo):
    def build(self):
       

        a=self.addHost('a')
        b=self.addHost('b')
        c=self.addHost('c')
        d=self.addHost('d')

        r1=self.addSwitch('r1')
        r2=self.addSwitch('r2')

        self.addLink(a,r1,cls=TCLink,bw=1000,delay='1ms')
        self.addLink(d,r1,cls=TCLink,bw=1000,delay='1ms')
        self.addLink(b,r2,cls=TCLink,bw=1000,delay='1ms')
        self.addLink(c,r2,cls=TCLink,bw=1000,delay='5ms')
        self.addLink(r1,r2,cls=TCLink,bw=500,delay='10ms')

    
topos={'mytopo':(lambda:Topo_cust())}

    
