from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.geometry("500x300+300+200")
root.title("Лабораторна робота №3")
root["bg"] = "white"

class Lab():
	def var():   # Варіант
		root = Tk()
		root.title("Варіант")
		root.geometry("350x175+100+100")
		root["bg"] = "white"
		func = Label(root, text = "Інтерполяція функції\n"
								  "(многочлен Ньютона)\n"
								  "f(x) = sin^2(x)\n"
								  "[a,b] = [0,1]", bg = "white", 
								   font = ("Roboto", 18))
		func.pack(side = TOP, fill = BOTH, expand = True)

	def built():   #Виконання роботи
		root = Tk()
		root.title("Виконання роботи")
		root.geometry("500x300+300+200")
		root["bg"] = "white"
		global x
		global y
		global intr
		global intr1
		x = []
		y = []
		intr = []
		intr1 = []


		def graf_y(): #Графік функції
			for i in range(0, 11):
				x.append(i)
			for i in x:
				x[i] /= 10

			for i in range(len(x)):
				y.append(round(math.sin(x[i])**2, 5))

			plt.plot(x, y, color = "silver")
			plt.title("$f(x) = sin^2(x)$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		def graf_int():#Графік інтерполяції
			pr1 = []
			pr2 = []
			pr3 = []
			pr4 = []
			pr5 = []
			global intr
			intr = []
			#Різниці 1-порядку
			for i in range(len(y)-1):
				pr1.append(round((y[i+1]-y[i])/0.1, 5))
			# print(pr1)

			#Різниці 2-порядку
			for i in range(len(pr1)-1):
				pr2.append(round((pr1[i+1]-pr1[i])/0.2, 5))
			# print(pr2)

			#Різниці 3-порядку
			for i in range(len(pr2)-1):
				pr3.append(round((pr2[i+1]-pr2[i])/0.3, 5))
			# print(pr3)

			#Різниці 4-порядку
			for i in range(len(pr3)-1):
				pr4.append(round((pr3[i+1]-pr3[i])/0.4, 5))
			# print(pr4)

			#Різниці 5-порядку
			for i in range(len(pr4)-1):
				pr5.append(round((pr4[i+1]-pr4[i])/0.5, 5))
			# print(pr5)
			# print("\n")

			for i in range(len(x)):
				inter = round(y[0] + pr1[0]*x[i] + pr2[0]*x[i]*(x[i] - 0.1) + pr3[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2) + 
						pr4[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3) + pr5[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3)*(x[i]-0.4), 5)
				intr.append(inter) 

			
			plt.plot(x, intr, color = "red")
			plt.title("$Інтерполяція$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		def graf_sin(): #Графік функції  f(x) = sin(x)
			x_sin = []
			for i in range(0, 11):
				x_sin.append(i)
			for i in x_sin:
				x_sin[i] /= 10
			y_sin = []
			for i in range(len(x_sin)):
				y_sin.append(round(math.sin(x_sin[i]), 5))

			y_sin = lambda x_sin: np.sin(x_sin)
			fig = plt.subplots()
			x_sin = np.linspace(0, 1,100)
			plt.plot(x_sin, y_sin(x_sin), color = "blue")
			plt.title("$f(x) = sin(x)$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		def graf_int_sin():#Графік інтерполяції sin
			x_sin = []
			for i in range(0, 11):
				x_sin.append(i)
			for i in x_sin:
				x_sin[i] /= 10
			y_sin = []
			for i in range(len(x_sin)):
				y_sin.append(round(math.sin(x_sin[i]), 5))

			pr1 = []
			pr2 = []
			pr3 = []
			pr4 = []
			pr5 = []

			intr1 = []
			#Різниці 1-порядку
			for i in range(len(y_sin)-1):
				pr1.append(round((y_sin[i+1]-y_sin[i])/0.1, 5))

			#Різниці 2-порядку
			for i in range(len(pr1)-1):
				pr2.append(round((pr1[i+1]-pr1[i])/0.2, 5))
			#Різниці 3-порядку
			for i in range(len(pr2)-1):
				pr3.append(round((pr2[i+1]-pr2[i])/0.3, 5))

			#Різниці 4-порядку
			for i in range(len(pr3)-1):
				pr4.append(round((pr3[i+1]-pr3[i])/0.4, 5))

			#Різниці 5-порядку
			for i in range(len(pr4)-1):
				pr5.append(round((pr4[i+1]-pr4[i])/0.5, 5))

			for i in range(len(x_sin)):
				inter1 = round(y_sin[0] + pr1[0]*x_sin[i] + pr2[0]*x_sin[i]*(x_sin[i] - 0.1) + 
								pr3[0]*x_sin[i]*(x_sin[i] - 0.1)*(x_sin[i] - 0.2) + 
								pr4[0]*x_sin[i]*(x_sin[i] - 0.1)*(x_sin[i] - 0.2)*(x_sin[i]-0.3) + 
							pr5[0]*x_sin[i]*(x_sin[i] - 0.1)*(x_sin[i] - 0.2)*(x_sin[i]-0.3)*(x_sin[i]-0.4), 5)
				intr1.append(inter1) 

			plt.plot(x_sin, intr1, color = "red")
			plt.title("$Інтерполяція f(x) = sin(x)$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		def polinom_view():#Поліном Ньютона
			root = Tk()
			root.title("Інтерполяційний поліном Ньютона")
			root.geometry("500x150+280+180")
			root["bg"] = "white"
			pol = Label(root, text = "Інтерполяційний поліном Ньютона для заданої функції:\n"
									 "N5(x) = 0 + 0.0997x + 0.9765x(x-0.1) -\n"
									 "- 0.195x(x-0.1)(x-0.2) - 0.30417x(x-0.1)(x-0.2)(x-0.3) +\n"
									 "+ 0.0417x(x-0.1)(x-0.2)(x-0.3)(x-0.4)",
									 bg = "white", font = ("Roboto", 12))
			pol.place(relx = 0.065, rely = 0.1)

		def inf_func():
			x = []
			y = []
			for i in range(0, 11):
				x.append(i)
			for i in x:
				x[i] /= 10

			for i in range(len(x)):
				y.append(round(math.sin(x[i])**2, 5))

			pr1 = []
			pr2 = []
			pr3 = []
			pr4 = []
			pr5 = []
			global intr
			intr = []
			#Різниці 1-порядку
			for i in range(len(y)-1):
				pr1.append(round((y[i+1]-y[i])/0.1, 5))

			#Різниці 2-порядку
			for i in range(len(pr1)-1):
				pr2.append(round((pr1[i+1]-pr1[i])/0.2, 5))

			#Різниці 3-порядку
			for i in range(len(pr2)-1):
				pr3.append(round((pr2[i+1]-pr2[i])/0.3, 5))

			#Різниці 4-порядку
			for i in range(len(pr3)-1):
				pr4.append(round((pr3[i+1]-pr3[i])/0.4, 5))

			#Різниці 5-порядку
			for i in range(len(pr4)-1):
				pr5.append(round((pr4[i+1]-pr4[i])/0.5, 5))

			for i in range(len(x)):
				inter = round(y[0] + pr1[0]*x[i] + pr2[0]*x[i]*(x[i] - 0.1) + pr3[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2) + 
						pr4[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3) + pr5[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3)*(x[i]-0.4), 5)
				intr.append(inter) 

			inf = [round(y[i]-intr[i], 5) for i in range(min(len(y), len(intr)))]
			plt.plot(x, inf, color = "black")
			plt.title("$Похибка f(x) = sin^2(x)$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		def inf_sin():
			x = []
			y = []
			for i in range(0, 11):
				x.append(i)
			for i in x:
				x[i] /= 10

			for i in range(len(x)):
				y.append(round(math.sin(x[i]), 5))

			pr1 = []
			pr2 = []
			pr3 = []
			pr4 = []
			pr5 = []
			global intr
			intr = []
			#Різниці 1-порядку
			for i in range(len(y)-1):
				pr1.append(round((y[i+1]-y[i])/0.1, 5))

			#Різниці 2-порядку
			for i in range(len(pr1)-1):
				pr2.append(round((pr1[i+1]-pr1[i])/0.2, 5))

			#Різниці 3-порядку
			for i in range(len(pr2)-1):
				pr3.append(round((pr2[i+1]-pr2[i])/0.3, 5))

			#Різниці 4-порядку
			for i in range(len(pr3)-1):
				pr4.append(round((pr3[i+1]-pr3[i])/0.4, 5))

			#Різниці 5-порядку
			for i in range(len(pr4)-1):
				pr5.append(round((pr4[i+1]-pr4[i])/0.5, 5))

			for i in range(len(x)):
				inter = round(y[0] + pr1[0]*x[i] + pr2[0]*x[i]*(x[i] - 0.1) + pr3[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2) + 
						pr4[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3) + pr5[0]*x[i]*(x[i] - 0.1)*(x[i] - 0.2)*(x[i]-0.3)*(x[i]-0.4), 5)
				intr.append(inter) 

			inf = [round(y[i]-intr[i], 5) for i in range(min(len(y), len(intr)))]
			
			plt.plot(x, inf, color = "purple")
			plt.title("$Похибка f(x) = sin(x)$")
			plt.xlabel("$x$")
			plt.ylabel("$y$")
			plt.grid(True)
			plt.show()

		f_ = Label(root, text = "f(x) = sin^2(x)", bg = "white", font = ("Roboto", 14))
		f_.place(relx = 0.35, rely = 0.05)

		graf_func = Button(root, text = "   Графік функції   \n"
										"f(x) = sin^2(x)", 
								bg = "silver", font = ("Roboto", 14), command = graf_y)
		graf_func.place(relx = 0.12, rely = 0.175)

		graf_inter = Button(root, text = "Графік інтерполяції\n"
										 "заданої функції", bg = "silver",
										 font = ("Roboto", 14),
										 command = graf_int)
		graf_inter.place(relx = 0.495, rely = 0.175)

		graf_func_sin = Button(root, text = "   Графік функції   \n"
										"f(x) = sin(x)", 
								bg = "silver", font = ("Roboto", 14), command = graf_sin)
		graf_func_sin.place(relx = 0.12, rely = 0.43)

		graf_inter_sin = Button(root, text = "Графік інтерполяції\n"
										 	 "f(x) = sin(x)", bg = "silver",
										 	 font = ("Roboto", 14), command = graf_int_sin)
		graf_inter_sin.place(relx = 0.495, rely = 0.43)

		graf_inf_f = Button(root, text = "Похибка\n"
										 "  інтерполяції функції  ", bg = "silver", 
										 font = ("Roboto", 10), command = inf_func)
		graf_inf_f.place(relx = 0.04, rely = 0.7)

		pol_view = Button(root, text = "Поліном Ньютона", bg = "silver", font = ("Roboto", 9),
						  command = polinom_view)
		pol_view.place(relx = 0.3825, rely = 0.73)

		graf_inf_sin = Button(root, text = "Похибка\n"
										   "інтерполяції f(x)=sin(x)", bg = "silver",
										   font = ("Roboto", 10), command = inf_sin)
		graf_inf_sin.place(relx = 0.65, rely = 0.7)



	info = Label(root, text = "Лабораторна робота №3\n\n"
							  "Малашкін В'ячеслав\n"
							  "Група ІО-83\n"
							  "Номер списку групи: 16", 
							  bg = "silver", font = ("Roboto", 18), relief = "ridge")
	info.place(relx = 0.215, rely = 0.075)

	variant = Button(root, text = "        Варіант         ", bg = "silver", font = ("Roboto", 15), relief = "raised",
					 command = var)
	variant.place(relx = 0.105, rely = 0.725)

	build  = Button(root, text = "Виконання роботи", bg = "silver", font = ("Roboto", 15), relief = "raised", 
					command = built)
	build.place(relx = 0.515, rely = 0.725)

if __name__ == "__main__":
	lab = Lab
	root.mainloop()