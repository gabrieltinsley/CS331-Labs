ACM = {}

# Predefined subjects and objects and rights for the ACM
subjects = ["Alice", "Bob", "Charlie", "Eve", "Mallory"]
objects = ["File1", "File2", "Printer", "Server1", "Database"]
rights = ["read", "write", "execute", "own"]

# Initialize ACM with empty rights
for subject in subjects:
    ACM[subject] = {obj: [] for obj in objects}
def create_subject(subject_name, ACM, objects):
    if subject_name not in ACM:
        ACM[subject_name] = {obj: [] for obj in objects}
        print(f"Subject '{subject_name}' added.")
    else:
        print(f"Subject '{subject_name}' already exists.")
def create_object(object_name, ACM):
    for subject in ACM:
        if object_name not in ACM[subject]:
            ACM[subject][object_name] = []
    print(f"Object '{object_name}' added.")
def add_right(subject_name, object_name, right, ACM):
    if right not in ACM[subject_name][object_name]:
        ACM[subject_name][object_name].append(right)
        print(f"Right '{right}' added to subject '{subject_name}' for object '{object_name}'.")
    else:
        print(f"Right '{right}' already exists for subject '{subject_name}' for object '{object_name}'.")
def check_right(subject_name, object_name, right, ACM):
    if right in ACM[subject_name][object_name]:
        print(f"Subject '{subject_name}' has right '{right}' for object '{object_name}'.")
    else:
        print(f"Subject '{subject_name}' does not have right '{right}' for object '{object_name}'.")
# Dynamic rights management
def grant_right_secure(subject_name, object_name, right, ACM):
    if subject_name in ACM and object_name in ACM[subject_name]:
        if right not in ACM[subject_name][object_name]:
            ACM[subject_name][object_name].append(right)
            print(f"Right '{right}' assigned to {subject_name} for {object_name}.")
        else:
                print(f"Right '{right}' already exists for {subject_name} on {object_name}.")
    else:
        print(f"Invalid subject or object.")
    
    
def revoke_right_secure(subject_name, object_name, right, ACM):
 if subject_name in ACM and object_name in ACM[subject]:
    if right in ACM[subject_name][object_name]:
        ACM[subject_name][object_name].remove(right)
        print(f"Right '{right}' revoked from {subject_name} for {object_name}.")
    else:
        print(f"Right '{right}' does not exist for {subject_name} on {object_name}.")
 else:
    print(f"Invalid subject or object.")


# Create subjects and objects
create_subject("Alice", ACM, objects)
create_subject("Bob", ACM, objects)
create_subject("Charlie", ACM, objects)
create_object("File1", ACM)
create_object("File2", ACM)
create_object("File3", ACM)

# Add rights
add_right("Alice", "File1", "own", ACM)
add_right("Alice", "File1", "execute", ACM)
add_right("Bob", "File2", "read", ACM)
add_right("Bob", "File2", "write", ACM)
add_right("Charlie", "File3", "execute", ACM)

# Check rights
check_right("Alice", "File1", "read", ACM)
check_right("Alice", "File1", "write", ACM)
check_right("Alice", "File1", "execute", ACM)
check_right("Bob", "File2", "read", ACM)
check_right("Bob", "File2", "write", ACM)
check_right("Bob", "File2", "execute", ACM)

print(ACM)