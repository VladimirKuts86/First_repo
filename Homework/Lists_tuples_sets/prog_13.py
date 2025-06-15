all_tasks = ['помыть посуду', 'погулять']
completed_tasks = ['помыть посуду']
set_all_tasks = set(all_tasks)
set_completed_tasks = set(completed_tasks)
uncomplited_tasks = set_all_tasks.difference(set_completed_tasks)
print(list(uncomplited_tasks))