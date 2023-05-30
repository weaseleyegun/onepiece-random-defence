from tkinter import *
from tkinter import messagebox
import random
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = Tk()
#window 창 옵션 설정
window.title("ORD")
window.geometry("800x600")

##characterful
characterFul = {"루피초월","조로초월","나미초월","우솝초월","상디초월","쵸파초월",
                "로빈초월","프랑키초월","브룩초월","샹크스초월","검은수염초월",
                "시라호시초월","아오키지초월","아카이누초월",
                "로우초월","도플라밍고초월","사보초월","후지토라초월","타시기초월",
                "루치초월","바질 호킨스초월","징베초월","스네이크맨초월","키드초월",
                "야마토초월","로쿠큐초월","로져불멸","레일리불멸","가반 불멸","흰수염불멸",
                "거프불멸","센고쿠불멸","시키불멸","제트불멸","드래곤불멸","제트불멸","카이도불멸",
                "빅맘불멸","에이스 영원","핸콕영원","버기영원","레필제한","레베카제한","카타쿠리 제한", "킹 제한"}

# label
label1 = Label(window, text= "ORD", font=(30),fg="blue")
label1.grid(row=0, column=0, columnspan=2)

#이미지
photo = PhotoImage(file=resource_path("./ord/ORD_img.png"))
label2 = Label(window,image=photo,width=640,height=480)
label2.grid(row=1, column=0, columnspan=2)

#menu bar
menubar = Menu(window)
menu1 = Menu(menubar)
menu1.add_command(label="by 김도건")

#menubar 등록
window.config(menu=menu1)

# 버튼 클릭 이벤트 핸들러
def btn1Click():
    character_kim = random.choice(list(characterFul))
    messagebox.showinfo("김도건",character_kim)

def btn2Click():
    character_lee = random.choice(list(characterFul))
    messagebox.showinfo("이원준",character_lee)

 
# 버튼 클릭 이벤트와 핸들러 정의
btn1 = Button(window, text="김도건", command=btn1Click,width=10,height=5)
btn2 = Button(window, text="이원준", command=btn2Click,width=10,height=5)

btn1.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
btn2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# 위젯들이 중앙에 오게 배열
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# mainloop
window.mainloop()