class UnAutorizationException(Exception):
	def __init__(self, message=None):
		super().__init__(message)

class BadReuestException(Exception):
	def __init__(self, message=None):
		super().__init__(message)

class InvalidRequest(Exception):
	def __init__(self, message=None):
		super().__init__(message)