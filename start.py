
from customtkinter import *
from vue import *



def mainApp():
    
    m_ctk = CTk()
    panel = Vue1(m_ctk)
    panel.vu_panel_1.mainloop()
    panel.destroy()




if __name__ == '__main__':
    
    mainApp()
