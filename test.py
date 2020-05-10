user_ip_input = "255.1111.1.1"
ip_input = user_ip_input.split(".")

ip = []
for i in ip_input:
    ip.append(int(i))
    i = int(i)
    if i > 255:
        print("error")
    print(type(i))