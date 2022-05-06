import tkinter as tk
from tkinter import ttk
from tkinter import *
from backward_chaining import backward_chaining

def main():
  #backward_chaining("pola pendampingan")

  # Window
  window = tk.Tk()
  window.title("Sistem Pakar")
  window.geometry("800x400")

  # Init variable
  home_title = StringVar(value="Klik tombol Mulai untuk menggunakan aplikasi")
  
  # Create tab
  tab_control = ttk.Notebook(window)
  home_tab = ttk.Frame(tab_control)
  info_tab = ttk.Frame(tab_control)

  tab_control.add(home_tab, text="Home")
  tab_control.add(info_tab, text="Info")

  tab_control.pack(expand=1, fill="both")

  # Home Screen
  ttk.Label(
    home_tab,
    textvariable=home_title,
    font="Helvetica 14 bold"
  ).grid(column=0, row=0, padx=20, pady=20)
  start_btn = ttk.Button(
    home_tab,
    text="Mulai",
    width=10,
    command=lambda: start_btn_onclick(home_tab, start_btn, home_title)
  )
  start_btn.grid(column=0, row=1)

  # Info Screen
  ttk.Label(
    info_tab,
    text="Jenis-jenis Pola Pengasuhan yang terdapat di Sistem Ini",
    font="Helvetica 16 bold"
  ).grid(column=0, row=0, sticky="nw", padx=20, pady=10)
  ttk.Label(
    info_tab,
    text="1. Pola Asuh Demokratis",
    font="Helvetica 14"
  ).grid(column=0, row=1, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="Pada parenting jenis ini, orang tua yang berperan besar dalam membuat pedoman dan aturan di dalam keluarga. Orang tua selalu bersikap responsif saat anak bertanya atau menyampaikan pendapatnya.\nOrang tua tidak otoriter, tapi tetap mengarahkan anak untuk berbuat yang benar, selalu mendukung, mudah memaafkan, tidak terlalu membatasi, dan tidak menyalahkan anak saat melakukan kesalahan.",
    font="Helvetica 11"
  ).grid(column=0, row=2, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="2. Pola Asuh Pendampingan",
    font="Helvetica 14"
  ).grid(column=0, row=3, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="Orang tua yang menerapkan pola asuh pendampingan akan membebaskan anaknya untuk bereksplorasi tapi tetap di bawah pengawasannya. Ini adalah jenis pola asuh yang baik untuk diterapkan\ndi masa kini, menimbang besarnya rasa ingin tahu anak-anak. Di samping anak bisa bereksplorasi, anak juga akan belajar bertanggung jawab terhadap hal yang dilakukannya.",
    font="Helvetica 11"
  ).grid(column=0, row=4, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="3. Pola Asuh Hipnosis",
    font="Helvetica 14"
  ).grid(column=0, row=5, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="Pada dasarnya pola asuh hypnosis bertujuan untuk menyuntikkan sugesti positif pada anak yang diharapkan dapat membimbing anak tanpa merasa dipaksakan. Pola asuh ini memiliki dampak positif\nanak lebih terbuka kepada orang tua terhadap segala hal. Jadi, orang tua tidak perlu lagi berusaha mengorek informasi dari anaknya.",
    font="Helvetica 11"
  ).grid(column=0, row=6, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="4. Pola Asuh Holistik",
    font="Helvetica 14"
  ).grid(column=0, row=7, sticky="nw", padx=20, pady=5)
  ttk.Label(
    info_tab,
    text="Menerapkan pola asuh holistik, orang tua akan memberikan contoh yang baik dari dirinya sendiri. Di samping itu, orang tua juga menghargai adanya perbedaan kepribadian dengan sang anak serta\nmemberikan kebebasan pada anak untuk mengembangkan potensi dan keyakinan yang anak miliki. Dengan begitu, anak akan lebih menghargai lingkungan sekelilingnya dan memiliki kesadaran batin.",
    font="Helvetica 11"
  ).grid(column=0, row=8, sticky="nw", padx=20, pady=5)
  
  window.mainloop()

def hide_widget(widget):
  widget.grid_remove()

def start_btn_onclick(parent_frame, btn, home_title):
  hide_widget(btn)
  home_title.set("Jawab pertanyaan sesuai dengan kondisi anak Anda")
  backward_chaining(parent_frame, "pola pendampingan")

if __name__ == "__main__":
  main()
