import tkinter as tk
from tkinter import ttk

''' Set Rules '''
rules = {}
rules_size = 20

# Rule structure: index 0 = premises, index 1 = conclusion, index 2 = CF score
# Set 1
rules["R1"] = [["karakter bagus", "lingkungan positif"], "pola pendampingan", 0.8]
rules["R2"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "berfinansial"], "pola pendampingan", 0.8]
rules["R3"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "tidak berfinansial"], "pola holistik", 0.6]
rules["R4"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu sedang"], "pola holistik", 0.6]
rules["R5"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu rendah"], "pola holistik", 0.6]
rules["R6"] = [["karakter sedang"], "pola hipnosis", 0.6]
rules["R7"] = [["karakter rendah"], "pola demokratis", 0.8]

# Set 2
rules["R8"] = [["aktif dan energik", "punya rasa ingin tahu"], "karakter bagus", 0.8]
rules["R9"] = [["aktif dan energik", "tidak punya rasa ingin tahu", "berjiwa petualang"], "karakter bagus", 0.8]
rules["R10"] = [["aktif dan energik", "tidak punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter sedang", 0.4]
rules["R11"] = [["tidak aktif dan energik", "punya rasa ingin tahu", "berjiwa petualang"], "karakter bagus", 0.6]
rules["R12"] = [["tidak aktif dan energik", "punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter sedang", 0.4]
rules["R13"] = [["tidak aktif dan energik", "tidak punya rasa ingin tahu", "berjiwa petualang"], "karakter sedang", 0.4]
rules["R14"] = [["tidak aktif dan energik", "tidak punya rasa ingin tahu", "tidak berjiwa petualang"], "karakter rendah", 0.8]

# Set 3
rules["R15"] = [["didukung keluarga"], "lingkungan positif", 0.8]
rules["R16"] = [["tidak didukung keluarga"], "lingkungan negatif", 0.6]

# Set 4
rules["R17"] = [["tamat sd", "tamat smp", "tamat sma", "tamat s1"], "pendidikan ortu tinggi", 1.0]
rules["R18"] = [["tamat sd", "tamat smp", "tidak tamat sma"], "pendidikan ortu sedang", 0.6]
rules["R19"] = [["tamat sd", "tidak tamat smp"], "pendidikan ortu rendah", 0.8]
rules["R20"] = [["tidak tamat sd"], "pendidikan ortu rendah", 1.0]

''' Initialize working memory (WM) '''
working_memory = []
global_CF_scores = []

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

def get_total_CF_score(input_CF_scores, rule_CF_score):
  return min(input_CF_scores) * rule_CF_score

def backward_chaining(parent_frame, premise):
  possible_rules = search_rules(premise)
  input_premise = tk.StringVar()
  input_premises = []
  input_CF_score = tk.DoubleVar()
  input_CF_scores = []
  
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
          backward_chaining(parent_frame, current_premise)
      else:
        # Get user input
        if int(possible_rules[i][1:]) in range(1, 7):
          if not set(working_memory).issubset(current_premises):
            break

        if not set(input_premises).issubset(current_premises):
          break
        else:
          if not current_premise in input_premises:
            # Entry widget
            ttk.Label(
              parent_frame,
              text=f"{current_premise}?",
              width=20,
              font="Helvetica 11 bold"
            ).grid(column=0, row=2, sticky="nw", padx=20)
            ttk.Radiobutton(
              parent_frame,
              text="Ya",
              variable=input_premise,
              value=f"{current_premise}"
            ).place(x=20, y=95)
            ttk.Radiobutton(
              parent_frame,
              text="Tidak",
              variable=input_premise,
              value=f"tidak {current_premise}"
            ).place(x=100, y=95)

            # Confidence level widget
            ttk.Label(
              parent_frame,
              text="Pilih tingkat keyakinan",
              font="Helvetica 11 normal"
            ).place(x=20, y=130)
            ttk.Radiobutton(
              parent_frame,
              text="1",
              variable=input_CF_score,
              value=-1.0
            ).place(x=40, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="2",
              variable=input_CF_score,
              value=-0.8
            ).place(x=85, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="3",
              variable=input_CF_score,
              value=-0.6
            ).place(x=125, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="4",
              variable=input_CF_score,
              value=-0.4
            ).place(x=165, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="5",
              variable=input_CF_score,
              value=-0.2
            ).place(x=205, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="6",
              variable=input_CF_score,
              value=0.4
            ).place(x=245, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="7",
              variable=input_CF_score,
              value=0.6
            ).place(x=285, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="8",
              variable=input_CF_score,
              value=0.8
            ).place(x=325, y=160)
            ttk.Radiobutton(
              parent_frame,
              text="9",
              variable=input_CF_score,
              value=1.0
            ).place(x=365, y=160)
            ttk.Label(
              parent_frame,
              text="Tidak yakin",
              font="Helvetica 8 normal"
            ).place(x=20, y=180)
            ttk.Label(
              parent_frame,
              text="Sangat yakin",
              font="Helvetica 8 normal"
            ).place(x=345, y=180)

            parent_frame.wait_variable(input_premise)
            parent_frame.wait_variable(input_CF_score)
            input_premises.append(input_premise.get())
            input_CF_scores.append(input_CF_score.get())

            # If user input in parent rule, then put that input in WM immediately
            if int(possible_rules[i][1:]) in range(1, 7):
              working_memory.append(input_premise.get())
              global_CF_scores.append(input_CF_score.get())
    
    # Put in working_memory if input premises suitable with current premises
    if len(input_premises) == len(rules[possible_rules[i]][0]):
      if is_rule_firing(input_premises, rules[possible_rules[i]][0]):
        working_memory.append(rules[possible_rules[i]][1])
        global_CF_scores.append(get_total_CF_score(input_CF_scores, rules[possible_rules[i]][2]))
        break

    # Display a result
    if int(possible_rules[i][1:]) in range(1, 8):
      if len(working_memory) == len(rules[possible_rules[i]][0]):
        if is_rule_firing(working_memory, rules[possible_rules[i]][0]):
          ttk.Label(
            parent_frame,
            text= "Rekomendasi pola asuh:",
            font="Helvetica 12"
          ).place(x=20, y=240)
          ttk.Label(
            parent_frame,
            text= rules[possible_rules[i]][1],
            font="Helvetica 12 bold"
          ).place(x=200, y=240)
          ttk.Label(
            parent_frame,
            text="CF score:",
            font="Helvetica 12"
          ).place(x=20, y=270)
          ttk.Label(
            parent_frame,
            text="{:.2f}".format(get_total_CF_score(global_CF_scores, rules[possible_rules[i]][2])),
            font="Helvetica 12 bold"
          ).place(x=95, y=270)

          print("WM:", working_memory)
          print("Global CF Scores:", global_CF_scores)
