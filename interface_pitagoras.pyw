from math import *
import tkinter as tk
import ttkbootstrap as ttk

# Variables
maxsize = 140
minsize = 40


# Ventana
window = ttk.Window(themename = "superhero")
window.geometry("400x400")
window.resizable(False,False)
window.title("App Chapter_Opener")

# String
resultado = tk.StringVar()
 
# Mostrar los resultados y dibujar el triangulo
def MostrarResultado():
	global canvas
	global triangle
	canvas.delete(triangle)
	try:
		if catA_entry.get() == "":
			catA = round(sqrt(float(hip_entry.get())**2- float(catB_entry.get())**2),3)
			catB = float(catB_entry.get())
			hip = float(hip_entry.get())
			resultado.set(f"Cateto A: {catA}")
		elif catB_entry.get() == "":
			catA = float(catA_entry.get()) 
			catB = round(sqrt(float(hip_entry.get())**2- float(catA_entry.get())**2),3)
			hip = float(hip_entry.get())
			resultado.set(f"Cateto B: {catB}")
		elif hip_entry.get() == "":
			catA = float(catA_entry.get()) 
			catB = float(catB_entry.get())
			hip = round(sqrt(float(catA_entry.get())**2+ float(catB_entry.get())**2),3)
			resultado.set(f"Hipotenusa: {hip}")
		elif hip_entry.get() != "" and catB_entry.get() != "" and catA_entry.get() != "": 
			resultado.set(f"Solo se necesitan\n 2 medidas")
	except:
			resultado.set(f"Error al ingresar")
	finally:
		if hip > maxsize:
			reason = hip/maxsize
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				(catB/reason)+20,(catA/reason)+20 ,20,(catA/reason)+20), 
				fill = "#54B2FF",outline = "black")
		elif catA > maxsize:
			reason = catA/maxsize
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				(catB/reason)+20,(catA/reason)+20 ,20,(catA/reason)+20), 
				fill = "#54B2FF",outline = "black")
		elif catB > maxsize:
			reason = catB/maxsize
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				(catB/reason)+20,(catA/reason)+20 ,20,(catA/reason)+20), 
				fill = "#54B2FF",outline = "black")
		elif hip < minsize:
			reason = minsize/hip
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				(catB*reason)+20,(catA*reason)+20 ,20,(catA*reason)+20), 
				fill = "#54B2FF",outline = "black")
		elif catB < minsize:
			reason = minsize/catB
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				(catB*reason)+20,(catA*reason)+20 ,20,(catA*reason)+20), 
				fill = "#54B2FF",outline = "black")
		elif catA < minsize:
			reason = minsize/catA
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,(catB*reason)+20,
				(catA*reason)+20 ,20,(catA*reason)+20), 
				fill = "#54B2FF",outline = "black")
		else:
			canvas.place(x = 10, y = 230)
			triangle = canvas.create_polygon((20,20 ,
				catB+20,catA+20 ,20,catA+20), 
				fill = "#54B2FF",outline = "black")
			
# Label
title = tk.Label(window,text="Pitágoras",font=("Consolas",13))
catA_label = tk.Label(window,text="Cateto A:")
catB_label = tk.Label(window,text="Cateto B:")
hip_label = tk.Label(window,text="Hipotenusa:",width=12)
result_label = tk.Label(window,text="resultado: ",textvariable=resultado,
	font=("Consolas", 12),width=19)

# Entry
catA_entry = tk.Entry(window,width=5)
catB_entry = tk.Entry(window,width=5)
hip_entry = tk.Entry(window,width=5)

# Button
result_button = tk.Button(window,text="Calcular",command=MostrarResultado,
	font=("Consolas",12))

# Canvas
canvas = tk.Canvas(window)
triangle = canvas.create_polygon((0,0))

#Pack
title.pack()
catA_label.place(x=10,y = 40)
catA_entry.place(x=25,y = 80)

catB_label.place(x=153,y = 40)
catB_entry.place(x=165,y = 80)

hip_label.place(x=266,y = 40)
hip_entry.place(x=296,y = 80)

result_label.place(x=80,y=170)
result_button.place(x=135,y=130)
canvas.place(x = 10, y = 230)

# Run
window.mainloop()