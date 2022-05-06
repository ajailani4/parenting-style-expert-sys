import tkinter as tk
from tkinter import Frame, ttk
from typing import Text

''' Set Rules '''
from turtle import width


rules = {}
rules_size = 20

# Set 1
rules["R1"] = [["karakter bagus", "lingkungan positif"], "pola pendampingan"]
rules["R2"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "berfinansial"], "pola pendampingan"]
rules["R3"] = [["karakter bagus", "lingkungan negatif", "pendidikan ortu tinggi", "tidak berfinansial"], "pola holistik"]
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

def backward_chaining(parent_frame, premise):
  possible_rules = search_rules(premise)
  input_premise = tk.StringVar()
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
              text= f"{current_premise}?",
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

            parent_frame.wait_variable(input_premise)
            input_premises.append(input_premise.get())

            # If user input in parent rule, then put that input in WM immediately
            if int(possible_rules[i][1:]) in range(1, 7):
              working_memory.append(input_premise.get())
      
    if len(input_premises) == len(rules[possible_rules[i]][0]):
      if is_rule_firing(input_premises, rules[possible_rules[i]][0]):
        working_memory.append(rules[possible_rules[i]][1])
        break

    if int(possible_rules[i][1:]) in range(1, 8):
      if len(working_memory) == len(rules[possible_rules[i]][0]):
        if is_rule_firing(working_memory, rules[possible_rules[i]][0]):
          ttk.Label(
            parent_frame,
            text= "Rekomendasi pola asuh:",
            width=20,
            font="Helvetica 11"
          ).place(x=20, y=130)
          ttk.Label(
            parent_frame,
            text= rules[possible_rules[i]][1],
            width=20,
            font="Helvetica 11 bold"
          ).place(x=190, y=130)

          print(rules[possible_rules[i]][1])
          print(working_memory)