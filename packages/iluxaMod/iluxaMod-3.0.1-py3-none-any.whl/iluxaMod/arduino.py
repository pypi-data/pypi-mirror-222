
class Arduino:

    def __init__(self, board):
        from pyfirmata import Arduino, util
        self.board = Arduino(board)
        it = util.Iterator(board)
        it.start()

    def digital_port(self, port, status=None):
        if status == None:
            return self.board.digital[port].read()
        elif status in ['True', True, "on", 1]:
            return self.board.digital[port].write(1)
        else:
            return self.board.digital[port].write(0)

    def analog_port(self, port, status=None, enable_reporting=False):
        if enable_reporting:
            self.board.analog[port].enable_reporting()
        if status == None:
            return self.board.analog[port].read()
        elif status != None:
            return self.board.analog[port].write(status)
