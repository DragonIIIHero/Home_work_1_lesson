with open("hobby.csv", "r", encoding="utf=8") as h, open("users.csv", "r", encoding="utf=8") as u, open("users_hobby.txt", "w", encoding="utf=8") as u_h:
    for hobby, users in zip(h, u):
        u_h.write(f'{users.strip()}: {hobby.strip()}\n')
    for users in u:
         u_h.write((f'{users.strip()}: {"None"}\n'))