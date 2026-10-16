from functions.get_files_info import get_files_info


call_1 = get_files_info("calculator", ".")
call_2 = get_files_info("calculator", "/bin")
call_3 = get_files_info("calculator", "../")
call_4 = get_files_info("calculator", "main.py")

print(call_1)
print(call_2)
print(call_3)
print(call_4)
