import os
from unidecode import unidecode
import tkinter as tk

def registrar_material(
  title: str,
  topic: str,
  author: str,
  year: int,
  level: str,
  alttext: str,
  filename: str,
  thumbnail: str,
  is_book: bool=False,
  contents: list=None
):
  base_string = f"""---
title: "{title}"
year: {year}
thumbnail: "assets/img/{thumbnail}"
topic: "{topic}"
file: "assets/pdf/Material/{filename}"
author: "{author}"
level: "{level}"
alttext: "{alttext}"
---"""
  if is_book:
    if contents is None: return None
    base_string = base_string + '\n\n<ul class="list-group list-group-flush">\n'
    for item in contents:
      base_string = base_string + f'  <li class="list-group-item">{item}</li>\n'
    base_string = base_string + '</ul>'
    destination_folder = "_libros/"
  else: destination_folder = "_entrenamientos/"
  catalogue_name = title.replace(',', '')
  catalogue_name = catalogue_name.replace(' ', '-')
  catalogue_name = unidecode(catalogue_name)
  with open(os.path.join(destination_folder, catalogue_name+'.md'), 'w') as f:
    f.write(base_string)
  return None


def focus_next_window(event):
  event.widget.tk_focusNext().focus()
  return("break")


root = tk.Tk()
root.title("Eliora, la última bibliotecaria")
root.bind_class("Entry", "<Tab>", focus_next_window)

material_title_label = tk.Label(root, text="Título")
material_title_label.grid(row=0, column=0)
material_title_textbox = tk.Entry(root, width=25)
material_title_textbox.grid(row=0, column=1)

material_author_label = tk.Label(root, text="Autor")
material_author_label.grid(row=1, column=0)
material_author_textbox = tk.Entry(root, width=25)
material_author_textbox.grid(row=1, column=1)

material_topic_label = tk.Label(root, text="Tema")
material_topic_label.grid(row=2, column=0)
material_topic_textbox = tk.Entry(root, width=25)
material_topic_textbox.grid(row=2, column=1)

material_year_label = tk.Label(root, text="Año de publicación")
material_year_label.grid(row=3, column=0)
material_year_textbox = tk.Entry(root, width=25)
material_year_textbox.grid(row=3, column=1)

material_level_label = tk.Label(root, text="Nivel")
material_level_label.grid(row=4, column=0)
material_level_textbox = tk.Entry(root, width=25)
material_level_textbox.grid(row=4, column=1)

material_alttext_label = tk.Label(root, text="Texto secreto")
material_alttext_label.grid(row=5, column=0)
material_alttext_textbox = tk.Entry(root, width=25)
material_alttext_textbox.grid(row=5, column=1)

material_filename_label = tk.Label(root, text="Nombre del archivo")
material_filename_label.grid(row=6, column=0)
material_filename_textbox = tk.Entry(root, width=25)
material_filename_textbox.grid(row=6, column=1)

material_thumbnail_label = tk.Label(root, text="Imagen de miniatura")
material_thumbnail_label.grid(row=7, column=0)
material_thumbnail_textbox = tk.Entry(root, width=25)
material_thumbnail_textbox.grid(row=7, column=1)

material_is_book = tk.BooleanVar(root, False)
content_entries = []
content_entries_text = []
def show_contents():
  material_contents_label.grid(row=0, column=3)
  material_contents_first_entry.grid(row=1, column=3)
  material_contents_add_button.grid(row=1, column=4)
  content_entries.append(material_contents_first_entry)
  return None
material_is_book_checkbox = tk.Checkbutton(root, text="Es un libro o cuadernillo", variable=material_is_book, command=show_contents, onvalue=True, offvalue=False).grid(row=6, column=2)

def material_new_content_entry():
  content_entries_text.append(content_entries[-1].get())
  next_row = len(content_entries)+1
  new_content_entry = tk.Entry(root, width=25)
  new_content_entry.grid(row=next_row, column=3)
  content_entries.append(new_content_entry)
  material_contents_add_button.grid(row=next_row, column=4)
  return None
material_contents_label = tk.Label(root, text="Contenidos")
material_contents_first_entry = tk.Entry(root, width=25)
material_contents_add_button = tk.Button(root, text="Agregar contenido", command=material_new_content_entry)


registrar_material_button = tk.Button(root, text="Registrar material",
  command= lambda: registrar_material(
    material_title_textbox.get(),
    material_topic_textbox.get(),
    material_author_textbox.get(),
    int(material_year_textbox.get()),
    material_level_textbox.get(),
    material_alttext_textbox.get(),
    material_filename_textbox.get(),
    material_thumbnail_textbox.get(),
    material_is_book.get(),
    content_entries_text
  )
)
registrar_material_button.grid(row=8, column=2)

root.mainloop()

