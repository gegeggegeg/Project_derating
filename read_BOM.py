import csv 
import component

class ReadBom():
	"""read data from bom."""
	def __init__(self, filename):
		self.sorted_data = {}
		self.filename = filename	
	def read_bom(self):
		with open(self.filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)
			return header_row
	def sort_component(self):
		""" find resistors from BOM."""
		keypool = ['TF-RES', 'TF-CAP','TF-INDUCTOR','TF-FERRITE','TF-DIODE','TF-LED','TF-TRAN		S','TF-CON','TF-IC']
		resistors = []
		capacitors = [] 
		inductors = []
		ferrites = []
		diodes = []
		leds = []
		mos = []
		bjt =[]
		cons = []
		ic = []
		others = []
		with open(self.filename) as f:
			reader = csv.reader(f)
			for row in reader:
				for keyword in keypool:
					if  keyword in row[6]:
						if(keyword == 'TF-RES'):
							comp = component.Resistor()
							self.store_data(row, comp, resistors, keyword)
						elif(keyword == 'TF-CAP'):
							comp = component.Capacitor()
							self.store_data(row, comp, capacitors, keyword)
						elif(keyword == 'TF-INDUCTOR'):
							comp = component.Inductor()
							self.store_data(row, comp, inductors, keyword)
						elif(keyword == 'TF-FERRITE'):
							comp = component.Ferrite()
							self.store_data(row, comp, ferrites, keyword)
						elif(keyword == 'TF-DIODE'):
							comp = component.Diode()
							self.store_data(row, comp, diodes, keyword)
						elif(keyword == 'TF-LED'):
							comp = component.LED()
							self.store_data(row, comp, leds, keyword)
						elif(keyword == 'TF-TRANS'):
							if 'MOS' in row[6]:
								comp = component.MOSFET()
								self.store_data(row, comp, mos, keyword)
							elif 'NPN' or 'PNP' in row[6]:
								comp = component.BJT()
								self.store_data(row, comp, bjt, keyword)
						elif(keyword == 'TF-CON'):
							comp = component.Connector()
							self.store_data(row, comp, cons, keyword)
						elif(keyword == 'TF-IC'):
							comp = component.IC()
							self.store_data(row, comp, ic, keyword)
						else:
							comp = component.Other()
							self.store_data(row, comp, others, keyword)
		return self.sorted_data		
	
	def store_data(self, row, component, temp_storage, keyword):
		component.ref = row[3]
		component.value = row[2]
		component.pn = row[5]
		component.des = row[6]
		temp_storage.append(component)
		self.sorted_data[keyword] = temp_storage
		
		
	def	output_sorted_resistors(self, resistors):
		with open(resistor.csv, "w+") as myfile:
			data  = csv.writer(myfile)
			data.writerow = ['Item', 'Device Number', 'Ref', 'Res(ohm)', 'Vmax(V)', 'Pd(w)','Vamx(V)'
								,'Pd(w)','Pd(%)','Pd(%)','OK?','Comment','Component Description' ]
			i = 1
			for res in resistors:
				data.writerow = [str(i), res.pn, res.ref, res.value, '', '', '', '', '', '', '', '', res.des]
				i = i + 1
			data.close
	def output_sorted_capacitors(self, capacitors):
		with open (capacitor.csv, 'w+') as myfile:
			data = csv.writer(myfile)
			data.writerow = ['Item', 'Device Number', 'Ref', 'Cap(F)','Vmax(V)','Vmax(V)', 'Vmax(%)', 'Vmax(%)','Vmax(%)',
							'OK?','Comment','Component Description']
			i = 1
			for cap in capacitors:
				data.writerow = [str(i), cap.pn, cap.ref, cap.value, '', '', '', '', '', '', '', cap.des]
			i = i + 1
			data.close
			
			
			
		
		
			

		
