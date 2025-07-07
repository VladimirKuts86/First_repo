# Привести имена к нормальной форме ["john", "DOE", "alice", "Bob"]
wrong_names = ["john", "DOE", "alice", "Bob"]
right_names = [names.capitalize() for names in wrong_names]
print(right_names)