my_title = "第一个python生成页"
my_content = "亲手创建的页面"
with open("index.html" , "w", encoding="utf-8") as f:
    f.write("<html>\n")
    f.write(f"    <head><title>{my_title}</title></head>\n")
    f.write("    <body style>='background-color:lightblue';text-align: cencer;'>\n")
    f.write(f"    <h1>{my_title}</h1>\n")
    f.write(f".   <p>{my_content}</p>\n")
    f.write("</html>\n")
    print("奇迹发生了!找 index.html")