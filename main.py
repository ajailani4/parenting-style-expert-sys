import tkinter as tk
from tkinter import ttk

''' Set Rules '''
rules = {}
rules_size = 20

# Set 1
rules["R1"] = [["karakter bagus", "lingkungan positif"], "pola pendampingan"]
rules["R2"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "finansial kurang"], "pola pendampingan"]
rules["R3"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "finansial bagus"], "pola holistik"]
rules["R4"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu sedang"], "pola holistik"]
rules["R5"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu rendah"], "pola holistik"]
rules["R6"] = [["karakter sedang"], "pola hipnosis"]
rules["R7"] = [["karakter rendah"], "pola demokratis"]

# Set 2
rules["R8"] = [["aktif dan energik", "punya rasa ingin tahu"], "karakter bagus"]
rules["R9"] = [["aktif dan energik", "tidak punya rasa ingin tahu", "berjiwa petualang"], "karakter bagus"]
rules["R10"] = [["aktif dan energik", "tidak punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter sedang"]
rules["R11"] = [["tidak aktif dan energik", "punya rasa ingin tahu", "berjiwa petualang"], "karakter bagus"]
rules["R12"] = [["tidak aktif dan energik", "punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter sedang"]
rules["R13"] = [["tidak aktif dan energik", "tidak punya rasa ingin tahu", "berjiwa petualang"], "karakter sedang"]
rules["R14"] = [["tidak aktif dan energik", "tidak punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter rendah"]

# Set 3
rules["R15"] = [["didukung keluarga"], "lingkungan positif"]
rules["R16"] = [["tidak didukung keluarga"], "lingkungan negatif"]

# Set 4
rules["R17"] = [["tamat sd", "tamat smp", "tamat sma", "tamat s1"], "pendidikan ortu tinggi"]
rules["R18"] = [["tamat sd", "tamat smp", "tidak tamat sma"], "pendidikan ortu sedang"]
rules["R19"] = [["tamat sd", "tidak tamat smp"], "pendidikan ortu rendah"]
rules["R20"] = [["tidak tamat sd"], "pendidikan ortu rendah"]

''' Initialize working memory (WM) '''
working_memory = []

''' Build backward chaining algorithm '''
def is_premise_in_WM(premise):
  return premise in working_memory

def search_rules(premise):
  output_attr = premise.split()[0]
  result = []

  for i in range(rules_size):
    current_output_attr = rules[f"R{i+1}"][1].split()[0]
    
    if output_attr == current_output_attr:
      result.append(f"R{i+1}")

  return result

def is_rule_firing(input_premises, rule_premises):
  result = False

  for i in range(len(rule_premises)):
    if type(rule_premises[i]) == list:
      if set(input_premises[i]).issubset(rule_premises[i]):
        result = True
      else:
        result = False
    else:
      if input_premises[i] == rule_premises[i]:
        result = True
      else:
        result = False

  return result

def backward_chaining(premise):
  possible_rules = search_rules(premise)
  input_premises = []
  
  for i in range(len(possible_rules)):
    for j in range(len(rules[possible_rules[i]][0])):
      current_premises = rules[possible_rules[i]][0]
      current_premise = current_premises[j]

      if is_premise_in_WM(current_premise):
        continue

      if len(search_rules(current_premise)) != 0:
          # Search other rules
        if not set(working_memory).issubset(current_premises):
          break
        else:
          backward_chaining(current_premise)
      else:
        # Get user input
        if int(possible_rules[i][1:]) in range(1, 7):
          if not set(working_memory).issubset(current_premises):
            break

        if not set(input_premises).issubset(current_premises):
          break
        else:
          if not current_premise in input_premises:
            input_premise = input(f"{current_premise}? ")
            input_premises.append(input_premise)

            # If user input in parent rule, then put that input in WM immediately
            if int(possible_rules[i][1:]) in range(1, 7):
              working_memory.append(input_premise)
      
    if len(input_premises) == len(rules[possible_rules[i]][0]):
      if is_rule_firing(input_premises, rules[possible_rules[i]][0]):
        working_memory.append(rules[possible_rules[i]][1])
        break

    if int(possible_rules[i][1:]) in range(1, 8):
      if len(working_memory) == len(rules[possible_rules[i]][0]):
        if is_rule_firing(working_memory, rules[possible_rules[i]][0]):
          return rules[possible_rules[i]][1]

def main():
  #backward_chaining("pola pendampingan")

  # Window
  window = tk.Tk()
  window.title("Sistem Pakar")
  window.geometry("900x600")

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
    text="Jawab Pertanyaan sesuai dengan Kondisi Anak Anda"
  ).grid(column=0, row=0, padx=20, pady=20)

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

if __name__ == "__main__":
  main()
