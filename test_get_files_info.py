from functions.get_files_info import get_files_info


call_1 = get_files_info("calculator", ".")
print("Result for '.' directory:")
print(call_1)

call_2 = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(call_2)


call_3 = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(call_3)


call_4 = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(call_4)

print(call_1)
print(call_2)
print(call_3)
print(call_4)
