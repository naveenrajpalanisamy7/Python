import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sound")
root.geometry("480x430")
root.resizable(False, False)

# ---------------- Notebook (Playback / Recording / Sounds / Communications) ----------
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

tab_playback      = ttk.Frame(notebook)
tab_recording     = ttk.Frame(notebook)
tab_sounds        = ttk.Frame(notebook)
tab_communications = ttk.Frame(notebook)

notebook.add(tab_playback, text="Playback")
notebook.add(tab_recording, text="Recording")
notebook.add(tab_sounds, text="Sounds")
notebook.add(tab_communications, text="Communications")

# (We’ll only design the “Sounds” tab UI; others can stay empty)

# ------------------------ LAYOUT CONFIG FOR SOUNDS TAB ------------------------------
tab_sounds.columnconfigure(0, weight=1)
tab_sounds.columnconfigure(1, weight=0)
tab_sounds.columnconfigure(2, weight=0)

# Top description text
desc = (
    "A sound theme is a set of sounds applied to events in Windows and programs. "
    "You can select an existing theme or save one you have modified."
)
ttk.Label(tab_sounds, text=desc, wraplength=440, justify="left").grid(
    row=0, column=0, columnspan=3, sticky="w", pady=(5, 10)
)

# ------------------------ Sound Scheme row ------------------------------------------
ttk.Label(tab_sounds, text="Sound Scheme:").grid(
    row=1, column=0, sticky="w", padx=(0, 5), pady=(0, 5)
)

scheme_combo = ttk.Combobox(tab_sounds, state="readonly",
                            values=["Windows Default", "No Sounds", "My Custom Scheme"])
scheme_combo.current(0)
scheme_combo.grid(row=1, column=0, sticky="e", padx=(110, 5), pady=(0, 5))

btn_save_as = ttk.Button(tab_sounds, text="Save As...")
btn_delete  = ttk.Button(tab_sounds, text="Delete")

btn_save_as.grid(row=1, column=1, padx=3, pady=(0, 5), sticky="w")
btn_delete.grid(row=1, column=2, padx=3, pady=(0, 5), sticky="w")

# Instruction text
ttk.Label(
    tab_sounds,
    text=("To change sounds, click a program event in the following list and then "
          "select a sound to apply. You can save the changes as a new sound theme.")
).grid(row=2, column=0, columnspan=3, sticky="w", pady=(10, 5))

# ------------------------ Program Events listbox + scrollbar ------------------------
ttk.Label(tab_sounds, text="Program Events:").grid(
    row=3, column=0, columnspan=3, sticky="w"
)

events_frame = ttk.Frame(tab_sounds)
events_frame.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=(2, 10))

events_frame.columnconfigure(0, weight=1)
events_frame.rowconfigure(0, weight=1)

events_list = tk.Listbox(events_frame, height=8)
scrollbar = ttk.Scrollbar(events_frame, orient="vertical", command=events_list.yview)
events_list.config(yscrollcommand=scrollbar.set)

events_list.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Dummy tree-like items
events = [
    r"[Windows]",
    "  Asterisk",
    "  Calendar Reminder",
    "  Close Program",
    "  Critical Battery Alarm",
    "  Critical Stop",
    "  Default Beep",
    "  Device Connect",
    "  Device Disconnect",
]
for e in events:
    events_list.insert("end", e)

# ------------------------ Play startup sound checkbox -------------------------------
play_startup_var = tk.BooleanVar(value=True)
chk_startup = ttk.Checkbutton(
    tab_sounds, text="Play Windows Start-up sound", variable=play_startup_var
)
chk_startup.grid(row=5, column=0, columnspan=3, sticky="w", pady=(0, 10))

# ------------------------ Sounds selection + buttons --------------------------------
ttk.Label(tab_sounds, text="Sounds:").grid(
    row=6, column=0, sticky="w", pady=(0, 3)
)

sounds_combo = ttk.Combobox(tab_sounds, state="readonly",
                            values=["(None)", "Windows Ding", "Notify", "Chord"])
sounds_combo.current(0)
sounds_combo.grid(row=7, column=0, sticky="w", pady=(0, 5))

btn_test   = ttk.Button(tab_sounds, text="Test")
btn_browse = ttk.Button(tab_sounds, text="Browse...")

btn_test.grid(row=7, column=1, sticky="w", padx=3)
btn_browse.grid(row=7, column=2, sticky="w", padx=3)

# ------------------------ Bottom buttons (OK / Cancel / Apply) ----------------------
bottom = ttk.Frame(root)
bottom.pack(fill="x", padx=10, pady=(0, 10))

ttk.Button(bottom, text="OK", width=10, command=root.destroy).pack(side="right", padx=5)
ttk.Button(bottom, text="Cancel", width=10, command=root.destroy).pack(side="right", padx=5)
ttk.Button(bottom, text="Apply", width=10).pack(side="right", padx=5)

root.mainloop()
