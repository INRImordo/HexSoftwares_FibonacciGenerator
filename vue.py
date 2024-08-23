
from typing import Any
from customtkinter import *
from tkinter import messagebox
from generateur_fibonacci import Generer_fibonacci_number


# notre vue
class Vue1(CTkFrame):
    
    
    # 
    # debut des fonctions d'action sur nos btn
    def generer(self):
        # recuperation des donnees saisi
        self.number = self.entry_number.get()
        
        # creation d'un objet fibonacci
        fibo = Generer_fibonacci_number()
        rest = fibo.fibonacci_recursive(self.number)
        
        if rest:
            # messagebox.showinfo(
            #     title="Auto genere fibonacci nomber",
            #     message="Felicitation vous avez pouvoir comprendre maintenant la suite de fibonacci"
            #     )
            
            
            self.resultat.configure(text=f"\tLe ({self.number}ième)  nombre de fibonacci est : {rest}\t")
            self.resultat.pack(side=LEFT, padx=10, pady=10)         
    # 
    # fin des fonctions d'actions
    


    # fonction d'initialisation
    def __init__(self, master :Any, **kwargs):
        super().__init__(master, **kwargs)
        
        self.vu_panel_1 = CTk()
        self.vu_panel_1.geometry("708x540")
        self.vu_panel_1.title("Serie de Fibonacci v-1.0")
        
        
        # label pour le grand titre
        self.label_titre_1 = CTkLabel(
            self.vu_panel_1,
            text="HEX SOFWARES INNOVATE | CONNECT | INSPIRE",
            text_color="#123456",
            font=('arial', 15)
        )
        self.label_titre_1.pack(padx=10, pady=10)
        
        
        # label du titre de projet
        self.label_titre_2 = CTkLabel(
            self.vu_panel_1,
            text="PROJET 1:  \t FIBONACCI GENERATOR",
            font=('arial', 12)
        )
        self.label_titre_2.pack(padx=10, pady=10)
        
        
        
        
        # label du titre de projet
        self.label_3 = CTkLabel(
            self.vu_panel_1,
            text="*******************************************************************************************************************************************************************************************",
            font=('arial', 12)
        )
        self.label_3.pack(padx=1)
        
        
        # label du titre de projet
        self.label_t = CTkLabel(
            self.vu_panel_1,
            text="\tMeme si elle parait simple la suite de fibonacci apparait dans de nombreux domaines tel que:",
            font=('arial', 12)
        )
        self.label_t.pack(padx=1)
        
        self.label_t = CTkLabel(
            self.vu_panel_1,
            compound="left",
            text="\n--> Ladisposition des feuilles sur une tige.",
            font=('arial', 12)
        )
        self.label_t.pack(padx=1)
        
        self.label_t = CTkLabel(
            self.vu_panel_1,
            compound="left",
            text="\n--> La liaison au nombre d'or.",
            font=('arial', 12)
        )
        self.label_t.pack(padx=1)
        
        
        self.label_t = CTkLabel(
            self.vu_panel_1,
            compound="left",
            text="\n--> Utiliser dans des algorithmes de recherche.",
            font=('arial', 12)
        )
        self.label_t.pack(padx=1)
        
        
        # label du titre de projet
        self.label_3 = CTkLabel(
            self.vu_panel_1,
            text="*******************************************************************************************************************************************************************************************",
            font=('arial', 12)
        )
        self.label_3.pack(padx=1)
        
        
        
        
        
        
        
        #frame qui va contenir les infos
        self.fram1 = CTkFrame(
            self.vu_panel_1,
            corner_radius=5,
            fg_color="#e03d3d" )
        self.fram1.pack(padx=10, pady=10)
        
        
        # label pour indiquer quoi faire
        self.fram1_label_titre = CTkLabel(
            self.fram1,
            text="Entrer un nombre :",
            text_color="#fff" )
        self.fram1_label_titre.pack(side=LEFT, padx=0)
        
        
        # input pour le nombre
        self.entry_number = CTkEntry(
            self.fram1,
            placeholder_text="exple: 32",
            width=280 )
        self.entry_number.pack(side=RIGHT, padx=5, pady=2)
        
     
        
        # panel de resultat
        self.fram2 = CTkFrame(
            self.vu_panel_1,
            
        )
        self.fram2.pack(padx=10, pady=10)
        
           
        # bouton 
        self.btn_generer_fibonacci = CTkButton(
            self.fram2,
            text="Generer",
            fg_color="#eabc12",
            command=self.generer)
        self.btn_generer_fibonacci.pack(side=RIGHT, padx=5, pady=10)
        
        
        # label pour afficher les resultat
        self.resultat = CTkLabel(
            self.fram2,
            text="",
            text_color="#e03d3d",
            fg_color="#fff")
        
  
