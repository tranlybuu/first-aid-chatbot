from tkinter import *
from chat import get_response, bot_name
import tkinter.font as tkfont

BG_GRAY = "#f1f1f1"
BG_COLOR = "#f5f5f5"
TEXT_COLOUR = "#0a0803"

# FONT = "Helvetica 14"
# FONT_BOLD = "Helvetica 13 bold"

FONT = "Arial 14"
FONT_BOLD = "Arial 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Trợ lý")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=750, bg=BG_COLOR)

        # Top
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOUR, text="Trợ Lý Sơ Cứu Xin Chào!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.005)

        # Bottom
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Cấu hình chữ
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOUR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Ô chat
        self.msg_entry = Entry(bottom_label, bg=BG_GRAY, fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # Nút gửi
        send_button = Button(bottom_label, text="Gửi", font=FONT_BOLD, width=20, bg=BG_GRAY, command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "Bạn")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()