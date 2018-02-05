class Resistor():
	""" A simple model of resistor."""
	
	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class Capacitor():
	""" A simple model of capacitor."""
	
	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])
		
class Inductor():
	""" A simple model of inductor."""

	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class Ferrite():
	""" A simple model of ferrite."""
	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class Diode():
	""" A simple model of Diode. """
	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = "" 
		self.Vr = 0
		self.Tj = 0
		self.If = 0
		self.Pd = 0
		self.Thjc = 'na'
		self.Thja = 0
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class LED():
	""" A simple model of LED. """
	def __init__ (self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
		self.Topr = ''
		self.IF = 0
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class MOSFET():
	""" A simple model of mosfet. """
	def __init__ (self):
		self.value =''
		self.pn = ''
		self.ref = ''
		self.des = ""
		self.vbreakdn = 0
		self.Pd = 0
		self.Tj = 0
		self.Thjc = 0
		self.Thja = 0
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class BJT():
	""" A simple model of bjt. """
	def __init__ (self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
		self.Vce = 0 
		self.Ic = 0
		self.Pd = 0
		self.Tj = 0
		self.Thjc = 0
		self.Thja = 0
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])
class Connector():
	"""A simple model of connector. """
	def __init__ (self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
		self.current = 0
	def show_value (self):
		print([self.value, self.pn, self.ref, self.des])
class IC():
	"""A simple model of IC. """
	def __init__ (self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
		self.Tj = 0
		self.Ta = 0
		self.Tc = 0
		self.Thjc = 0
		self.Thja = 0
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])
class Other():
	""" Misc stuuf"""
	def __init__ (self):
		self.value =''
		self.pn = ''
		self.ref = ''
		self.des = ''
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])
