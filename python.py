
import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

LANGUAGES = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Chinese (Simplified)": "zh-CN",
    "Dutch": "nl",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Russian": "ru",
    "Spanish": "es",
    "Urdu": "ur"
}

class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Google Style Translator")
        self.geometry("800x520")
        self.resizable(False, False)
        self.configure(bg="#eaf6ff")  
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text=" Google Style Translator", font=("Segoe UI", 20, "bold"), bg="#0096FF", fg="white", pady=10)
        title.pack(fill="x")

        frame = tk.Frame(self, bg="#eaf6ff")
        frame.pack(fill="both", expand=True, padx=12, pady=8)


        tk.Label(frame, text="Enter text:", bg="#eaf6ff", fg="#003366", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(frame, text="Translate to:", bg="#eaf6ff", fg="#003366", font=("Segoe UI", 11, "bold")).grid(row=0, column=1, sticky="w", padx=(15,0))

        self.lang_var = tk.StringVar(value="Urdu")
        lang_combo = ttk.Combobox(frame, values=list(LANGUAGES.keys()), textvariable=self.lang_var, state="readonly", width=20)
        lang_combo.grid(row=0, column=2, sticky="w", padx=(5,0))

        self.src_text = tk.Text(frame, height=9, wrap="word", font=("Segoe UI", 12), bg="white", fg="#003366", relief="solid", bd=1)
        self.src_text.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=(6,8))

        btn_frame = tk.Frame(frame, bg="#eaf6ff")
        btn_frame.grid(row=2, column=0, columnspan=3, pady=4)

        style = {
            "font": ("Segoe UI", 10, "bold"),
            "fg": "white",
            "width": 14,
            "bd": 0,
            "relief": "flat",
            "pady": 6
        }

        tk.Button(btn_frame, text="Translate ▶", bg="#0096FF", command=self.translate_text, **style).grid(row=0, column=0, padx=6)
        tk.Button(btn_frame, text="Swap ↔", bg="#00BFA6", command=self.swap_texts, **style).grid(row=0, column=1, padx=6)
        tk.Button(btn_frame, text="Clear ✖", bg="#FF5C5C", command=self.clear_all, **style).grid(row=0, column=2, padx=6)

        tk.Label(frame, text="Translation:", bg="#eaf6ff", fg="#003366", font=("Segoe UI", 11, "bold")).grid(row=3, column=0, sticky="w")

        self.res_text = tk.Text(frame, height=9, wrap="word", font=("Segoe UI", 12), bg="#f0faff", fg="#003366", relief="solid", bd=1)
        self.res_text.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=(6,8))

        bottom_frame = tk.Frame(frame, bg="#eaf6ff")
        bottom_frame.grid(row=5, column=0, columnspan=3, sticky="ew")

        tk.Button(bottom_frame, text="Copy Translation ", bg="#0096FF", command=self.copy_translation, **style).pack(side="left", padx=6, pady=6)
        self.status = tk.Label(bottom_frame, text="Ready", bg="#eaf6ff", fg="#0066CC", font=("Segoe UI", 10))
        self.status.pack(side="right", padx=8)

        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(4, weight=1)
        frame.columnconfigure(0, weight=1)

    def translate_text(self):
        src = self.src_text.get("1.0", "end").strip()
        if not src:
            messagebox.showinfo("Info", "Please type some text to translate.")
            return

        lang_name = self.lang_var.get()
        lang_code = LANGUAGES.get(lang_name, "ur")

        self.status.config(text="Translating...", fg="orange")
        self.update_idletasks()
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(src)
            self.res_text.delete("1.0", "end")
            self.res_text.insert("1.0", translated)
            self.status.config(text=f"Translated to {lang_name}", fg="#006600")
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed:\n{e}")
            self.status.config(text="Error", fg="red")

    def copy_translation(self):
        text = self.res_text.get("1.0", "end").strip()
        if not text:
            messagebox.showinfo("Info", "Nothing to copy.")
            return
        pyperclip.copy(text)
        self.status.config(text="Copied to clipboard ", fg="#0096FF")

    def clear_all(self):
        self.src_text.delete("1.0", "end")
        self.res_text.delete("1.0", "end")
        self.status.config(text="Cleared", fg="#666")

    def swap_texts(self):
        src = self.src_text.get("1.0", "end").strip()
        res = self.res_text.get("1.0", "end").strip()
        self.src_text.delete("1.0", "end")
        self.res_text.delete("1.0", "end")
        self.src_text.insert("1.0", res)
        self.res_text.insert("1.0", src)
        self.status.config(text="Swapped ↔", fg="#00BFA6")

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()








