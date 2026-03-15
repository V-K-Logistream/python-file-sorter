# 0. THE TOOLBOXES (IMPORTS)
# 'os' stands for Operating System. It lets Python talk to the OS to read folder paths and see what files exist.
import os

# 'shutil' stands for Shell Utilities. This is the toolbox used for actual file operations, like moving or copying.
import shutil

# 'datetime' is the toolbox for checking the current date and time so we can stamp our log files.
import datetime

# 1. DEFINE THE LOCATIONS
# We set up variables for the folder paths. 
# IMPORTANT: Change 'base_dir' to the actual path on your machine before running.
base_dir = "/your/file/must/be/here/TEST"
input_dir = os.path.join(base_dir, "Input")
hr_dir = os.path.join(base_dir, "HR")
ops_dir = os.path.join(base_dir, "Ops")
review_dir = os.path.join(base_dir, "Needs_Review")

# 2. SET UP THE LOG FILE NAME
# We grab the exact date and time right now to create a unique name for your text file.
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"sorting_log_{current_time}.txt"
log_filepath = os.path.join(base_dir, log_filename)

# 3. SET UP LISTS
# These empty brackets [] create lists. They act like buckets where we drop file details as we move them.
hr_files = []
ops_files = []
review_files = []

# 4. SCAN THE INPUT FOLDER
# os.listdir looks inside your Input folder and lists everything it finds.
all_items = os.listdir(input_dir)
initial_files = []

# Safety check: We only want to process actual files, not accidentally try to move hidden folders.
for item in all_items:
    if os.path.isfile(os.path.join(input_dir, item)):
        initial_files.append(item)

# 5. THE SORTING LOOP
for filename in initial_files:
    source_path = os.path.join(input_dir, filename)
    
    # Extract the file type (extension). 
    name, ext = os.path.splitext(filename)
    file_info = f"{filename} (Type: {ext if ext else 'Unknown'})"
        
    # LOGIC RULE 1: If the filename contains "Q1" (HR Files)
    if "Q1" in filename:
        destination_path = os.path.join(hr_dir, filename) 
        shutil.move(source_path, destination_path)        
        hr_files.append(file_info)                        
        
    # LOGIC RULE 2: If the filename contains "Q2" (Ops Files)
    elif "Q2" in filename:
        destination_path = os.path.join(ops_dir, filename)
        shutil.move(source_path, destination_path)
        ops_files.append(file_info)                       
        
    # LOGIC RULE 3: If it's a rogue file (Doesn't contain Q1 or Q2)
    else:
        destination_path = os.path.join(review_dir, filename)
        shutil.move(source_path, destination_path)
        review_files.append(file_info)                    

# 6. BUILD THE REPORT TEXT
report_text = f"=== FILE SORTING REPORT ===\n"
report_text += f"Date & Time: {current_time}\n"
report_text += f"Total files scanned in Input folder: {len(initial_files)}\n\n"

report_text += f"--- Moved to HR ({len(hr_files)} files) ---\n"
if len(hr_files) == 0: report_text += "  (None)\n"
for f in hr_files: report_text += f"  - {f}\n"

report_text += f"\n--- Moved to Ops ({len(ops_files)} files) ---\n"
if len(ops_files) == 0: report_text += "  (None)\n"
for f in ops_files: report_text += f"  - {f}\n"

report_text += f"\n--- Sent to Needs_Review / Exceptions ({len(review_files)} files) ---\n"
if len(review_files) == 0: report_text += "  (None)\n"
for f in review_files: report_text += f"  - {f}\n"

report_text += "===========================\n"

# 7. OUTPUT THE RESULTS
print(report_text)

with open(log_filepath, "w") as log_file:
    log_file.write(report_text)

print(f"Log file successfully saved to: {log_filepath}")
