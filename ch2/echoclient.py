from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(u'Hello, world!'.encode('utf-8'))

    def dataReceived(self, data):
        print("Server said: ", data.decode('utf-8'))
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection Failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Client Connection Lost")
        reactor.stop()


reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()
