import tkinter as tk
import subprocess

def run_query_arxiv():
    args = [dir_entry.get(), num_entry.get(), year_entry.get(), term_entry.get()]
    cmd = ['python', 'query_arxiv.py', '--dir', args[0], '--num', args[1], '--year', args[2], args[3]]
    subprocess.run(cmd)

def run_mkmd():
    args = [output_entry.get(), dir_entry2.get(), term_entry2.get()]
    cmd = ['python', 'mkmd.py', '-o', args[0], '-d', args[1], args[2]]
    subprocess.run(cmd)

window = tk.Tk()

# For query_arxiv.py
dir_label = tk.Label(window, text="Directory: ")
dir_label.pack()
dir_entry = tk.Entry(window)
dir_entry.pack()

num_label = tk.Label(window, text="Number: ")
num_label.pack()
num_entry = tk.Entry(window)
num_entry.pack()

year_label = tk.Label(window, text="Year: ")
year_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

term_label = tk.Label(window, text="Term: ")
term_label.pack()
term_entry = tk.Entry(window)
term_entry.pack()

query_arxiv_button = tk.Button(window, text="Run query_arxiv.py", command=run_query_arxiv)
query_arxiv_button.pack()

# For mkmd.py
output_label = tk.Label(window, text="Output: ")
output_label.pack()
output_entry = tk.Entry(window)
output_entry.pack()

dir_label2 = tk.Label(window, text="Directory: ")
dir_label2.pack()
dir_entry2 = tk.Entry(window)
dir_entry2.pack()

term_label2 = tk.Label(window, text="Term: ")
term_label2.pack()
term_entry2 = tk.Entry(window)
term_entry2.pack()

mkmd_button = tk.Button(window, text="Run mkmd.py", command=run_mkmd)
mkmd_button.pack()

window.mainloop()
