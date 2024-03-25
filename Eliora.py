from Elioras_handbook import *


root = tk.Tk()
root.title("Eliora, la última bibliotecaria")
root.bind_class("Entry", "<Tab>", focus_next_window)

open_material_register_button = tk.Button(root, text="Registrar nuevo material", command=lambda: open_material_register(root=root))
open_material_register_button.pack()

open_exam_register_button = tk.Button(root, text="Registrar selectivo", command=lambda: open_exam_register(root=root))
open_exam_register_button.pack()

root.mainloop()

