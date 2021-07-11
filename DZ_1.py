result = []
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        line_sp = line.split()
        result.append((line_sp[0], line_sp[5].replace('"',''), line_sp[6]))


print(result)