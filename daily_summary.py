hours_slept = float(input("How many hours did you sleep today: "))
study_hours = float(input("How many hours did you study today: "))
is_focused_today = input("Were you focused today: Yes/No? ").strip().lower()

if is_focused_today == "yes":
    is_focused_today = "True"
elif is_focused_today not in ["yes", "no"]: # If is_focused_today variable input is not in the list of "yes" or "no", the variable is now considered "N/A"
    is_focused_today = "N/A"
else:
    is_focused_today = "False"

tasks_completed = int(input("How many tasks did you complete today: "))
reflection_note = str(input("How did you feel completing everything today: "))

print(f"Today you slept for {hours_slept} hours, studied {study_hours} hours.")
print(f"Focused: {is_focused_today} | Tasks done: {tasks_completed}")
print(f"Notes: {reflection_note}")