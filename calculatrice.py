import tkinter as tk
from tkinter import Frame, Button, Entry

# ------------------- Fenêtre principale -------------------
root = tk.Tk()
root.title("Calculatrice")
root.geometry("350x500")
root.config(bg="#1e1e1e")  # fond sombre
root.resizable(False, False)

# ------------------- Champ d'affichage -------------------
display = Entry(
    root,
    font=("Consolas", 24),
    bd=0,
    bg="#292929",
    fg="white",
    justify="right",
    relief="flat"
)
display.pack(fill="both", ipadx=8, ipady=20, pady=(20, 10), padx=20)

# ------------------- Fonction du clavier -------------------
def appuyer(t):
    if t == "C":
        display.delete(0, tk.END)
    elif t == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Erreur")
    else:
        display.insert(tk.END, t)

# ------------------- Style des boutons -------------------
def bouton(parent, texte, couleur):
    return Button(
        parent, text=texte,
        font=("Consolas", 18),
        bg=couleur,
        fg="white",
        activebackground="#555",
        activeforeground="white",
        relief="flat",
        bd=0,
        width=5, height=2,
        command=lambda: appuyer(texte),
        highlightthickness=0
    )

# ------------------- Frame des boutons -------------------
frame = Frame(root, bg="#1e1e1e")
frame.pack()

# ------------------- Disposition -------------------
boutons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

couleurs = {
    "num": "#3c3c3c",
    "op": "#ff9500",
    "C": "#d32f2f",
    "=": "#2e7d32"
}

for r, ligne in enumerate(boutons):
    for c, char in enumerate(ligne):
        if char in "0123456789":
            color = couleurs["num"]
        elif char == "C":
            color = couleurs["C"]
        elif char == "=":
            color = couleurs["="]
        else:
            color = couleurs["op"]

        b = bouton(frame, char, color)
        b.grid(row=r, column=c, padx=8, pady=8)

root.mainloop()
