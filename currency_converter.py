import tkinter as tk
import tkinter.ttk as ttk

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsumrechner")
        root.geometry("300x300")
        self.language="Deutsch"

        self.optionen = {
            "EUR": 1,
            "USD": 1.13,
            "GBP": 0.84,
            "JPY": 162.36,
        }

        # Label8
        self.entry_label = tk.Label(root, text="Gib deinen Betrag an:")
        self.entry_label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

       
        self.waehrung_label = tk.Label(root, text="Wähle deine Währungen:")
        self.waehrung_label.pack(pady=10)

        self.waehrung_dropmenu1 = ttk.Combobox(root, values=list(self.optionen.keys()))
        self.waehrung_dropmenu1.pack(pady=5)

        self.waehrung_dropmenu2 = ttk.Combobox(root, values=list(self.optionen.keys()))
        self.waehrung_dropmenu2.pack(pady=5)
     

        # Button
        self.button = tk.Button(root, text="Umrechnen", command=self.anzeigen)
        self.button.pack(pady=10)

        #Language button
        self.language_button = tk.Button(root, text="Englisch", command=self.switch_language)
        self.language_button.pack(pady=10)

    def switch_language(self):
        if self.language == "Deutsch":
            self.language = "English"

            self.button.config(text = "Convert")
            self.language_button.config(text = "Deutsch")
            self.waehrung_label.config(text = "Choose your currencies:")
            self.entry_label.config(text = "Enter your amount:")
            self.root.title("Currency Converter")
        else:
            self.language = "Deutsch"

            self.button.config(text = "Umrechnen")
            self.language_button.config(text = "Englisch")
            self.waehrung_label.config(text = "Wähle deine Währungen:")
            self.entry_label.config(text = "Gib deinen Betrag an:")
            self.root.title("Währungsumrechner")

        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def anzeigen(self):
        name = float(self.entry.get()) 
        waehrung1 = self.waehrung_dropmenu1.get()  
        waehrung2 = self.waehrung_dropmenu2.get()
        value = (name/self.optionen[waehrung1]) * self.optionen[waehrung2]   
        self.output_label.config(text=f"{round(value,2)}")

# Dictionary außerhalb der Klasse bleibt unverändert


if __name__ == "__main__":
    root = tk.Tk()
    gui = Currency(root)
    root.mainloop()

