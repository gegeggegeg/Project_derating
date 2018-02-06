
class Component():
	"""template for components"""	
	def __init__(self):
		self.value = ''
		self.pn = ''
		self.ref = ''
		self.des = ""
	def show_value(self):
		print([self.value, self.pn, self.ref, self.des])

class Resistor(Component):
	""" A simple model of resistor."""	
	def __init__(self):
		super().__init__()

class Capacitor(Component):
	""" A simple model of capacitor."""
	def __init__(self):
		super().__init__()

class Inductor(Component):
	""" A simple model of inductor."""
	def __init__(self):
		super().__init__()

class Ferrite(Component):
	""" A simple model of ferrite."""
	def __init__(self):
		super().__init__()

class Diode(Component):
	""" A simple model of Diode. """
	def __init__(self):
		super().__init__()
		self.Vr = 0
		self.Tj = 0
		self.If = 0
		self.Pd = 0
		self.Thjc = 'na'
		self.Thja = 0

class LED(Component):
	""" A simple model of LED. """
	def __init__ (self):
		super().__init__()
		self.Topr = ''
		self.IF = 0

class MOSFET(Component):
	""" A simple model of mosfet. """
	def __init__ (self):
		super().__init__()
		self.vbreakdn = 0
		self.Pd = 0
		self.Tj = 0
		self.Thjc = 0
		self.Thja = 0

class BJT(Component):
	""" A simple model of bjt. """
	def __init__ (self):
		super().__init__()
		self.Vce = 0 
		self.Ic = 0
		self.Pd = 0
		self.Tj = 0
		self.Thjc = 0
		self.Thja = 0

class Connector(Component):
	"""A simple model of connector. """
	def __init__ (self):
		super().__init__()
		self.current = 0

class IC(Component):
	"""A simple model of IC. """
	def __init__ (self):
		super().__init__()
		self.Tj = 0
		self.Ta = 0
		self.Tc = 0
		self.Thjc = 0
		self.Thja = 0

class Other(Component):
	""" Misc stuff"""
	def __init__ (self):
		super().__init__()


