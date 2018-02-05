import csv 
import component

class ReadBom():
	"""read data from bom."""
	def __init__(self,filename):
		self.filename = filename	
	def read_bom(self):
		with open(self.filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)
			return header_row
	def sort_component(self):
		""" find resistors from BOM."""
		keypool = ['TF-RES', 'TF-CAP','TF-INDUCTOR','TF-FERRITE','TF-DIODE','TF-LED','TF-TRANS'
					,'TF-CON','TF-IC']
		sorted_data = {}
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
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							resistors.append(comp)
							sorted_data[keyword] = resistors
						elif(keyword == 'TF-CAP'):
							comp = component.Capacitor()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							capacitors.append(comp)
							sorted_data[keyword] = capacitors
						elif(keyword == 'TF-INDUCTOR'):
							comp = component.Inductor()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							inductors.append(comp)
							sorted_data[keyword] = inductors
						elif(keyword == 'TF-FERRITE'):
							comp = component.Ferrite()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							ferrites.append(comp)
							sorted_data[keyword] = ferrites
						elif(keyword == 'TF-DIODE'):
							comp = component.Diode()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							diodes.append(comp)
							sorted_data[keyword] = diodes
						elif(keyword == 'TF-LED'):
							comp = component.LED()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							leds.append(comp)
							sorted_data[keyword] = leds
						elif(keyword == 'TF-TRANS'):
							if 'MOS' in row[6]:
								comp = component.MOSFET()
								comp.ref = row[3]
								comp.value = row[2]
								comp.pn = row[5]
								comp.des = row[6]
								mos.append(comp)
								sorted_data['MOS'] = mos
							elif 'NPN' or 'PNP' in row[6]:
								comp = component.BJT()
								comp.ref = row[3]
								comp.value = row[2]
								comp.pn = row[5]
								comp.des = row[6]
								bjt.append(comp)
								sorted_data['BJT'] = bjt
						elif(keyword == 'TF-CON'):
							comp = component.Connector()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							cons.append(comp)
							sorted_data[keyword] = cons
						elif(keyword == 'TF-IC'):
							comp = component.IC()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							ic.append(comp)
							sorted_data[keyword] = ic
						else:
							comp = component.Other()
							comp.ref = row[3]
							comp.value = row[2]
							comp.pn = row[5]
							comp.des = row[6]
							others.append(comp)
							sorted_data['Other'] = others
		return sorted_data		
		
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
			
			
			
		
		
			

		
