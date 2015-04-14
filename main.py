__author__ = 'chheplo'

import Tkinter as tk
import generatePDF
import tkMessageBox

top = tk.Tk()
top.title("Generate Math Exercises")

var_sum = tk.BooleanVar(top)
var_sub = tk.BooleanVar(top)
var_mul = tk.BooleanVar(top)
var_div = tk.BooleanVar(top)

var_one_integer = tk.BooleanVar(top)
var_two_integer = tk.BooleanVar(top)
var_three_integer = tk.BooleanVar(top)
var_four_integer = tk.BooleanVar(top)
var_one_fraction = tk.BooleanVar(top)
var_two_fraction = tk.BooleanVar(top)

var_repetition = tk.StringVar(top)
var_repetition.set("1")

def on_create_button_press():

	# Update the page numbers and fetch the final option values before generating pages
	update_pages()

	# Obtain the name of the file from the entry menu
	if len(filename_entry.get()) > 0:
		filename = filename_entry.get()
	else:
		filename = "Mathomata"

	# Check for any missing selections
	if sum(n_var_method_list) == 0:
		tkMessageBox.showwarning("Warning", "No methods selected!")
	if sum(n_var_complex_list) == 0:
		tkMessageBox.showwarning("Warning", "No complexity selected!")

	# Call generate PDF pages module
	if sum(n_var_method_list) != 0 and sum(n_var_complex_list) != 0:
		generatePDF.generate_pdf(filename, n_var_repetition, n_var_method_list, n_var_complex_list)


def update_pages():
	global n_var_repetition
	n_var_repetition = var_repetition.get()
	n_var_repetition = int(n_var_repetition)
	global n_var_method_list
	n_var_method_list = [int(var_sum.get()),
						 int(var_sub.get()),
						 int(var_mul.get()),
						 int(var_div.get())]
	global n_var_complex_list
	n_var_complex_list = [int(var_one_integer.get()),
						  int(var_two_integer.get()),
						  int(var_three_integer.get()),
						  int(var_four_integer.get()),
						  int(var_one_fraction.get()),
						  int(var_two_fraction.get())]
	global n_page_number
	n_page_number = n_var_repetition * sum(n_var_method_list) * sum(n_var_complex_list)
	page_label.config(text=n_page_number)
	top.update_idletasks()
	top.update()


def update_page_number():
	update_pages()


def update_page_number_menu(a):
	update_pages()


def main():
	top_label = tk.Label(top,
						 text="Generate Mathematical exercises for your kids.",
						 padx=10,
						 font="Helvetica 16 bold")
	top_label.grid(row=10,
				   column=10,
				   columnspan=100)

	# Start - Section for selecting methods
	method_selection_label = tk.Label(top,
									  text="Select methods:",
									  padx=10,
									  font="Helvetica 12 bold")
	method_selection_label.grid(row=20,
								column=10,
								columnspan=100,
								sticky=tk.W)

	sum_checkbutton = tk.Checkbutton(top,
									 text="Summation",
									 variable=var_sum,
									 command=update_page_number)
	sum_checkbutton.grid(row=30,
						 column=10,
						 sticky=tk.W)

	sub_checkbutton = tk.Checkbutton(top,
									 text="Subtraction",
									 variable=var_sub,
									 command=update_page_number)
	sub_checkbutton.grid(row=30,
						 column=20,
						 sticky=tk.W)

	mul_checkbutton = tk.Checkbutton(top,
									 text="Multiplication",
									 fg="red",
									 variable=var_mul,
									 command=update_page_number)
	mul_checkbutton.grid(row=30,
						 column=30,
						 sticky=tk.W)

	div_checkbutton = tk.Checkbutton(top,
									 text="Division",
									 fg="red",
									 variable=var_div,
									 command=update_page_number)
	div_checkbutton.grid(row=30,
						 column=40,
						 sticky=tk.W)

	# End - Section for selecting methods

	# Start - Section for selecting complexity
	complexity_selection_label = tk.Label(top,
										  text="Select complexity before and after point:",
										  padx=10,
										  font="Helvetica 12 bold")
	complexity_selection_label.grid(row=40,
									column=10,
									columnspan=100,
									sticky=tk.W)

	one_integer_selection_label = tk.Checkbutton(top,
												 text="One integer (e.g. 1)",
												 variable=var_one_integer,
												 command=update_page_number)
	one_integer_selection_label.grid(row=50,
									 column=10,
									 sticky=tk.W)

	two_integer_selection_label = tk.Checkbutton(top,
												 text="Two integers (e.g. 12)",
												 variable=var_two_integer,
												 command=update_page_number)
	two_integer_selection_label.grid(row=50,
									 column=20,
									 sticky=tk.W)

	three_integer_selection_label = tk.Checkbutton(top,
												   text="Three integers (e.g. 123)",
												   variable=var_three_integer,
												   command=update_page_number)
	three_integer_selection_label.grid(row=50,
									   column=30,
									   sticky=tk.W)

	four_integer_selection_label = tk.Checkbutton(top,
												  text="Four integers (e.g. 1234)",
												  variable=var_four_integer,
												  command=update_page_number)
	four_integer_selection_label.grid(row=50,
									  column=40,
									  sticky=tk.W)

	one_fraction_selection_label = tk.Checkbutton(top,
												  text="One fraction (e.g. .1)",
												  variable=var_one_fraction,
												  command=update_page_number)
	one_fraction_selection_label.grid(row=60,
									  column=10, sticky=tk.W)

	two_fraction_selection_label = tk.Checkbutton(top,
												  text="Two fractions (e.g. .12)",
												  variable=var_two_fraction,
												  command=update_page_number)
	two_fraction_selection_label.grid(row=60,
									  column=20,
									  sticky=tk.W)

	# End - Section for selecting complexity

	# Start - Section for selecting repetition value
	repetition_selection_label = tk.Label(top,
										  text="Select exercise pages per each combination of method and complexity:",
										  padx=10,
										  font="Helvetica 12 bold")
	repetition_selection_label.grid(row=70,
									column=10,
									columnspan=100,
									sticky=tk.W)

	repetition_menu = tk.OptionMenu(top,
									var_repetition,
									"1", "2", "3", "4", "5",
									command=update_page_number_menu)
	repetition_menu.grid(row=80,
						 column=10)

	# End - Section for selecting repetition value

	# Start - Section for selecting filename
	filename_label = tk.Label(top,
								text="Select file name ('Mathomata' otherwise):",
								padx=10,
								font="Helvetica 12 bold")
	filename_label.grid(row=85,
						column=10,
						columnspan=100,
						sticky=tk.W)

	global filename_entry
	filename_entry = tk.Entry(top)
	filename_entry.grid(row=90,
						column=10)

	# End - Section for selecting filename

	create_button = tk.Button(top,
							  text="Start",
							  command=on_create_button_press)
	create_button.grid(row=100,
					   column=10)
	create_button.focus_set()

	exit_button = tk.Button(top,
							text="Exit",
							command=top.quit)
	exit_button.grid(row=100,
					 column=20)

	page_description_label = tk.Label(top,
									  text="Total pages that will be generated:")
	page_description_label.grid(row=100,
								column=30)

	global page_label
	page_label = tk.Label(top,
						  text="")
	page_label.grid(row=100,
					column=40)
	top.mainloop()


if __name__ == "__main__":
	main()