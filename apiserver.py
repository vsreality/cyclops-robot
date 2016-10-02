class APIServer()
    def __init__(self, address, port):
        self.server = CWsServer(address), port)
        self.paths = dict()

    def run():
        try:
            self.client = server.WaitForClient ()
            while True:
                msg = self.client.wait_message()
                if msg.type == CLOSE_MESSAGE:
                    raise Exception()
                msg = json.loads(msg.data)
        except:
        	self.client.close()

	def route(self, s):
		def wrapper(callback):
			self.paths[s] = callback
			return
		return wrapper

    def unsupported_request():
        pass

	def on_message(self, path):
        if path in self.paths:
            return self.paths[path]()
        else:
            self.unsupported_request()
