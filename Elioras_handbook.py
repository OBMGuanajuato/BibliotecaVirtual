import os
from unidecode import unidecode
import tkinter as tk
from tkinter import ttk

def focus_next_window(event):
  event.widget.tk_focusNext().focus()
  return("break")

def open_material_register(root):
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


  def show_contents():
    if material_is_book.get():
      material_contents_label.grid(row=0, column=3)
      material_contents_first_entry.grid(row=1, column=3)
      material_contents_add_button.grid(row=1, column=4)
      content_entries.append(material_contents_first_entry)
      return None
    material_contents_label.grid_forget()
    for entry in content_entries: entry.grid_forget()
    material_contents_add_button.grid_forget()
    content_entries.clear()
    return None


  def material_new_content_entry():
    content_entries_text.append(content_entries[-1].get())
    next_row = len(content_entries)+1
    new_content_entry = tk.Entry(material_tab, width=25)
    new_content_entry.grid(row=next_row, column=3)
    content_entries.append(new_content_entry)
    material_contents_add_button.grid(row=next_row, column=4)
    return None

  material_tab = tk.Toplevel(root)

  material_title_label = tk.Label(material_tab, text="Título")
  material_title_label.grid(row=0, column=0)
  material_title_textbox = tk.Entry(material_tab, width=25)
  material_title_textbox.grid(row=0, column=1)

  material_author_label = tk.Label(material_tab, text="Autor")
  material_author_label.grid(row=1, column=0)
  material_author_textbox = tk.Entry(material_tab, width=25)
  material_author_textbox.grid(row=1, column=1)

  material_topic_label = tk.Label(material_tab, text="Tema")
  material_topic_label.grid(row=2, column=0)
  material_topic_textbox = tk.Entry(material_tab, width=25)
  material_topic_textbox.grid(row=2, column=1)

  material_year_label = tk.Label(material_tab, text="Año de publicación")
  material_year_label.grid(row=3, column=0)
  material_year_textbox = tk.Entry(material_tab, width=25)
  material_year_textbox.grid(row=3, column=1)

  material_level_label = tk.Label(material_tab, text="Nivel")
  material_level_label.grid(row=4, column=0)
  material_level_textbox = tk.Entry(material_tab, width=25)
  material_level_textbox.grid(row=4, column=1)

  material_alttext_label = tk.Label(material_tab, text="Texto secreto")
  material_alttext_label.grid(row=5, column=0)
  material_alttext_textbox = tk.Entry(material_tab, width=25)
  material_alttext_textbox.grid(row=5, column=1)

  material_filename_label = tk.Label(material_tab, text="Nombre del archivo")
  material_filename_label.grid(row=6, column=0)
  material_filename_textbox = tk.Entry(material_tab, width=25)
  material_filename_textbox.grid(row=6, column=1)

  material_thumbnail_label = tk.Label(material_tab, text="Imagen de miniatura")
  material_thumbnail_label.grid(row=7, column=0)
  material_thumbnail_textbox = tk.Entry(material_tab, width=25)
  material_thumbnail_textbox.grid(row=7, column=1)

  material_is_book = tk.BooleanVar(material_tab, False)
  content_entries = []
  content_entries_text = []
    
  material_is_book_checkbox = tk.Checkbutton(material_tab, text="Es un libro o cuadernillo", variable=material_is_book, command=show_contents, onvalue=True, offvalue=False).grid(row=6, column=2)

  material_contents_label = tk.Label(material_tab, text="Contenidos")
  material_contents_first_entry = tk.Entry(material_tab, width=25)
  material_contents_add_button = tk.Button(material_tab, text="Agregar contenido", command=material_new_content_entry)


  registrar_material_button = tk.Button(material_tab, text="Registrar material",
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
  return None


def open_exam_register(root):
  def registrar_selectivo(
    olympiad: str,
    edition: str | int,
    exam_number: int,
    thumbnail: str,
    level: str = None
  ):
    base_string = f"""---
year: "{edition}"
exam-number: {exam_number}
thumbnail: "assets/img/{thumbnail}" """

    filename = str(edition)+'-S'+str(exam_number)

    if olympiad=="OBM":
      destination_folder = "_selectivos_obm/"
      base_string = base_string + f'\nlevel: "{level}"'
      filename = filename + "."
      # Lo que sigue supone fuertemente que los niveles de la OBM no van a cambiar en un futuro cercano. Por favor, actualiza esta parte del código si algo cambia. Espero no causar muchos problemas en el futuro. -- Joshua
      if "4<sup>to</sup>" in level:
        filename = filename + "Prim4,5"
      if "6<sup>to</sup>" in level:
        filename = filename + "Prim6, Sec1"
      if "2<sup>do</sup>" in level:
        filename = filename + "Sec2"
      if "3<sup>ro</sup>" in level:
        filename = filename + "Sec3"

    destination_folder = "_selectivos_" + olympiad.lower()
    base_string = base_string + f'\nfile: "assets/pdf/Selectivos/{olympiad}/{filename+".pdf"}"'
    base_string = base_string + "\n---"
    with open(os.path.join(destination_folder, filename+'.md'), 'w') as f:
      f.write(base_string)

    return None

  def show_editions(event):
    olympiad = exam_olympiad_listbox.get(tk.ANCHOR)
    exam_edition_listbox.delete(0, tk.END)
    editions = sorted([edition[:-3] for edition in os.listdir("_ediciones_"+olympiad.lower())])
    exam_edition_listbox.insert(0, *editions)
    if olympiad=="OBM":
      exam_level_label.grid(row=5, column=1)
      exam_level_listbox.grid(row=5, column=2)
    else: 
      exam_level_label.grid_forget()
      exam_level_listbox.grid_forget()
    return None
  
  def format_level_choice(exam_level):
    if exam_level:
      exam_level = exam_level.replace("ro", "<sup>ro</sup>")
      exam_level = exam_level.replace("do", "<sup>do</sup>")
      exam_level = exam_level.replace("to", "<sup>to</sup>")
    return exam_level

  exam_tab = tk.Toplevel(root)
  
  exam_olympiad_label = tk.Label(exam_tab, text="Olimpiada")
  exam_olympiad_label.grid(row=1, column=1)
  exam_olympiad_listbox = tk.Listbox(exam_tab, selectmode="single", height=3, exportselection=0)
  exam_olympiad_listbox.insert(tk.END, *["OBM", "OMM", "OFM"]) # Añado soporte para la OMMGto
  exam_olympiad_listbox.bind("<<ListboxSelect>>", show_editions)
  exam_olympiad_listbox.grid(row=1, column=2)

  exam_edition_label = tk.Label(exam_tab, text="Edición")
  exam_edition_label.grid(row=2, column=1)
  exam_edition_listbox = tk.Listbox(exam_tab, selectmode="single", exportselection=0)
  exam_edition_listbox.grid(row=2, column=2)

  exam_number_label = tk.Label(exam_tab, text="Número de selectivo")
  exam_number_label.grid(row=3, column=1)
  exam_number_textbox = tk.Entry(exam_tab, width=25)
  exam_number_textbox.grid(row=3, column=2)

  exam_thumbnail_label = tk.Label(exam_tab, text="Imagen de miniatura")
  exam_thumbnail_label.grid(row=4, column=1)
  exam_thumbnail_combobox = ttk.Combobox(exam_tab, values=sorted(os.listdir("assets/img/")))
  exam_thumbnail_combobox.grid(row=4, column=2)

  exam_level_label = tk.Label(exam_tab, text="Nivel")
  exam_level_listbox = tk.Listbox(exam_tab, selectmode="single", height=4, width=30, exportselection=0)
  exam_level_listbox.insert(tk.END, *[
    "4to y 5to de Primaria",
    "6to de Primaria y 1ro de Secundaria",
    "2do de Secundaria",
    "3ro de Secundaria"
    ])

  registrar_selectivo_button = tk.Button(exam_tab, text="Registrar selectivo",
    command= lambda: registrar_selectivo(
      exam_olympiad_listbox.get(tk.ANCHOR),
      exam_edition_listbox.get(tk.ANCHOR),
      int(exam_number_textbox.get()),
      exam_thumbnail_combobox.get(),
      format_level_choice(exam_level=exam_level_listbox.get(tk.ANCHOR))
    ))
  registrar_selectivo_button.grid(row=6, column=3)
  return None
