from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create a reverse mapping of LANGUAGES
lang_dict = {lang.capitalize(): code for code, lang in LANGUAGES.items()}

def change(text="type", src="english", dest="hindi"):
    trans = Translator()
    try:
        src_code = lang_dict.get(src.capitalize(), "en")
        dest_code = lang_dict.get(dest.capitalize(), "hi")
        if not text.strip():
            return "Please enter some text."
        trans1 = trans.translate(text, src=src_code, dest=dest_code)
        return trans1.text
    except Exception as e:
        return f"Error: {e}"


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    translated = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated)

root = Tk()
root.title("TRANSLATOR")
root.geometry("500x800")
root.config(bg='red')

Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg='Sky blue').place(x=100, y=40, height=50, width=300)

Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Sky blue").place(x=100, y=100, height=30, width=300)

Sor_txt = Text(root, font=("Times New Roman", 16), wrap=WORD)
Sor_txt.place(x=10, y=140, height=150, width=480)

list_text = sorted([lang.capitalize() for lang in LANGUAGES.values()])

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=310, height=40, width=150)
comb_sor.set("English")

Button(root, text="Translate", relief=RAISED, command=data).place(x=170, y=310, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=310, height=40, width=150)
comb_dest.set("Hindi")

Label(root, text="Dest Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="Sky blue").place(x=100, y=370, height=30, width=300)

dest_txt = Text(root, font=("Times New Roman", 16), wrap=WORD)
dest_txt.place(x=10, y=410, height=150, width=480)

root.mainloop()
