# -*- coding: ISO-8859-1 -*-
import tkinter

class Application(tkinter.Frame):
    def __init__(self, parent):
        self.parent = parent
        
        self.locationJeuX=0
        self.locationJeuY=0
        
        self.largeurFrame=1024
        self.hauteurFrame=768
        
        self.largeurJeu=1024
        self.hauteurJeu=768
        
        self.root=tkinter.Tk()
        self.root.config(width=self.largeurFrame,height=self.hauteurFrame)
        self.root.title("Area B51")
        
        self.posX=300
        self.posY=300
        
        self.mouvement = list()
        #0-haut,1-droite,2-bas,3-gauche
        for i in range(4):
            self.mouvement.append(False)
            
        self.menuPrincipal()
        
    def menuPrincipal(self):
        self.backgroundImage = tkinter.PhotoImage(file='Prometheus_1.gif',width=1024,height=768)
        self.fondEcran= tkinter.Canvas(self.root,width=1024,height=768)
        self.fondEcran.create_image(512,384, image= self.backgroundImage)
        self.fondEcran.place(x=0,y=0)
        
        
        
        
        
        self.nouvellePartieTexte= self.fondEcran.create_text(512,250,text='Nouvelle partie',fill='white',font=("Arial","30"),tags="nouvelle_partie",activefill='red')
        self.continuerPartieTexte= self.fondEcran.create_text(512,350,text='Continuer une partie',fill='white',font=("Arial","30"),tags="continuer_partie",activefill='red')
        self.quitterTexte= self.fondEcran.create_text(512,450,text='Quitter',fill='white',font=("Arial","30"),tags="quitter",activefill='red')
        
        
        self.fondEcran.tag_bind("nouvelle_partie","<Button-1>",self.menu2)
        self.fondEcran.tag_bind("continuer_partie","<Button-1>")
        self.fondEcran.tag_bind("quitter","<Button-1>",self.fermerFenetre)
        
        
    def modif(self,event):
        self.fondEcran.itemconfigure("option", text="Marco est un pedo")
    
        
        
    def clear(self):
        self.fondEcran.delete("nouvelle_partie")
        self.fondEcran.delete("continuer_partie")
        self.fondEcran.delete("option")
        self.fondEcran.delete("quitter")
        self.fondEcran.delete("screensize")
        self.fondEcran.delete("save")
        self.fondEcran.delete("sound")
        self.fondEcran.delete("backbouton")   
        self.menuPrincipal()    
    
    def effaceMenuPrinc(self):
        #effacer l'ecran principale
        self.fondEcran.tag_unbind("nouvelle_partie","<Button-1>")
        self.fondEcran.tag_unbind("continuer_partie","<Button-1>")
        self.fondEcran.tag_unbind("option","<Button-1>")
        self.fondEcran.tag_unbind("quitter","<Button-1>")
        self.fondEcran.delete("nouvelle_partie")
        self.fondEcran.delete("continuer_partie")
        self.fondEcran.delete("option")
        self.fondEcran.delete("quitter")
        
    def validEntre(self):
        value=self.nomJoueur.get()
        newvalue=self.validate(value)
        if newvalue is None:
            print("nom vide")
            
        else:
            self.connection()
    def validate(self, newvalue):
        if newvalue:
            return False     
        
    def attribuhumain(self):
        self.fondEcran.delete("attribut")
        self.attribue = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,300,text='force',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,350,text='poid',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,400,text='intelligence',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,450,text='blabla',fill='white',font=("Arial","20"),tags="attribut")
    def race2(self):
        self.fondEcran.delete("attribut")
        self.attribue = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,300,text='force2',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,350,text='poid',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,400,text='intelligence',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,450,text='blabla',fill='white',font=("Arial","20"),tags="attribut")
    def race3(self):
        self.fondEcran.delete("attribut")
        self.attribue = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,300,text='force3',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,350,text='poid',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,400,text='intelligence',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,450,text='blabla',fill='white',font=("Arial","20"),tags="attribut")
    def race4(self):
        self.fondEcran.delete("attribut")
        self.attribue = self.fondEcran.create_text(700,250,text='Attribut:',fill='white',font=("Arial","30"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,300,text='force4',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,350,text='poid',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,400,text='intelligence',fill='white',font=("Arial","20"),tags="attribut")
        self.attribue = self.fondEcran.create_text(700,450,text='blabla',fill='white',font=("Arial","20"),tags="attribut")
    def menu2(self,event):
        #ajoute les données au list box
        #on efface le menu pour afficher l'autre
        self.variable = tkinter.StringVar(self.root)
        self.variable.set("Veuillez choisir une race...") 
        self.effaceMenuPrinc()
        self.nomLabel = tkinter.Label(self.root, text="Nom de Joueur:", width=15)
        self.nomJoueur = tkinter.Entry(self.root,  width="18")
        self.raceLabel = tkinter.Label(self.root, text="Race: ",width=15)
        #afficher les bouton pour les race
        self.boutonHumain= tkinter.Radiobutton(self.root, text='Humain',command=self.attribuhumain)
        self.boutonRace2= tkinter.Radiobutton(self.root, text='Race2',command=self.race2)
        self.boutonRace3= tkinter.Radiobutton(self.root, text='Race3',command=self.race3)
        self.boutonRace4= tkinter.Radiobutton(self.root, text='Race4',command=self.race4)
        #affiche les bouton retour et continuer
        self.boutonContinuer= tkinter.Button(self.root, text='continuer', command=self.validEntre)
        self.boutonRetour= tkinter.Button(self.root, text='retour',command=self.clear)
        #affiche les images des 4 races
        self.humainpic = tkinter.PhotoImage(file='th.gif',width=160,height=160)
        self.fondEcran.create_image(160,250, image= self.humainpic)
        self.fondEcran.create_image(400,250, image= self.humainpic)
        self.fondEcran.create_image(160,500, image= self.humainpic)
        self.fondEcran.create_image(400,500, image= self.humainpic)
  
        #place les widget et les bouton
        self.nomLabel.place(x=50, y=50)
        self.nomJoueur.place(x=200, y=50)
        self.raceLabel.place(x=50, y=100)
        self.boutonHumain.place(x=120,y=350)
        self.boutonRace2.place(x=320,y=350)
        self.boutonRace3.place(x=120,y=600)
        self.boutonRace4.place(x=320,y=600)
        self.boutonContinuer.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
        
        

    def activer(self):
        
        ## debuter la partie si les information rentrer son correct 
        #si nom et information de connection so correct donc on continue
        self.commencePartie(self) 
        # sinon on redemande de rentrer les info de reseau encore
        print (self.connectionentry.get())
        print (self.portentry.get())
    def commencePartie(self,event):
        
        self.fondEcran.tag_unbind("nouvelle_partie","<Button-1>")
        self.fondEcran.tag_unbind("continuer_partie","<Button-1>")
        self.fondEcran.tag_unbind("option","<Button-1>")
        self.fondEcran.tag_unbind("quitter","<Button-1>")
        
        self.fondEcran.delete("nouvelle_partie")
        self.fondEcran.delete("continuer_partie")
        self.fondEcran.delete("option")
        self.fondEcran.delete("quitter")
        
        self.creationMap()
        
    def connection(self):
        print (self.nomJoueur.get())
        self.boutonContinuer.destroy()
        self.connectionlabel = tkinter.Label(self.root, text="connection: ", width=15)
        self.connectionentry = tkinter.Entry(self.root, width="18" )
        self.portlabel = tkinter.Label(self.root, text="Port: ", width=15)
        self.portentry = tkinter.Entry(self.root, width="18" )
        self.bouton= tkinter.Button(self.root, text='Debuter', command=self.activer)
        
        #place les widget
        self.connectionlabel.place(x=50, y=50)
        self.connectionentry.place(x=200, y=50)
        self.portlabel.place(x=200, y=100)
        self.portentry.place(x=200, y=100)
        self.bouton.place(x=550,y=650)
        self.boutonRetour.place(x=400,y=650)
          
    def fermerFenetre(self,event):
        self.root.quit()
    
    def creationMap(self):
        self.fondEcran.destroy()
        self.Vie = 3
        self.nbScrap = 50
        self.energy = 100
        self.epaisseurContour=20
        
        self.map=tkinter.Canvas(self.root,width=self.largeurJeu,height=self.hauteurJeu,bg="white")
        self.hudhaut= tkinter.Canvas(self.root,width=800,height=100,bg="red")
        self.bar =tkinter.Canvas(self.root,width=100,height=800,bg="blue")
        
        self.f=tkinter.PhotoImage(file='iaza13838747868800.gif')
        
        self.limage=list()
        for i in range(57):
            if i%2==0:
                for k in range(21):
                    self.map.create_image(0+k*40,20+i*10,image=self.f)
            else:
                for k in range(20):
                    self.map.create_image(20+k*40,20+i*10,image=self.f)
            
        
        self.map.create_rectangle(0,0,self.epaisseurContour,self.hauteurFrame,fill='black')
        self.map.create_rectangle(0,0,self.largeurFrame,self.epaisseurContour,fill='black')
        self.map.create_rectangle(self.largeurJeu-self.epaisseurContour,0,self.largeurJeu,self.hauteurJeu,fill='black')
        self.map.create_rectangle(0,self.hauteurJeu-self.epaisseurContour,self.largeurJeu,self.hauteurJeu,fill='black')
        # la barre des point, vie , energie en jeu
        
        self.energy = tkinter.PhotoImage(file='energy.gif',width=35,height=35)
        self.scrapmetal = tkinter.PhotoImage(file='scrapmetal.gif',width=35,height=35)
        self.vie = tkinter.PhotoImage(file='vie.gif',width=35,height=35)
        
        self.hudhaut.create_image(40,40, image= self.vie)
        self.nbVie= self.hudhaut.create_text(30,75,text='X',fill='white',font=("Arial","10"))
        self.nbVie= self.hudhaut.create_text(40,75,text='3',fill='white',font=("Arial","10"))
        #self.map= self.hudhaut.create_text(70,50,text=self.joueurnom,fill='white',font=("Arial","30"),tags="full",activefill='red')
        self.hudhaut.create_image(140,40, image= self.scrapmetal)
        self.nbScrap= self.hudhaut.create_text(180,40,text='X',fill='white',font=("Arial","10"))
        self.nbScrap=self.hudhaut.create_text(200,40,text=self.nbScrap,fill='white',font=("Arial","10"))
        
        self.hudhaut.create_image(240,40, image= self.energy)
        self.nbVie= self.hudhaut.create_text(270,40,text='X',fill='white',font=("Arial","10"))
        self.nbVie= self.hudhaut.create_text(280,40,text='3',fill='white',font=("Arial","10"))
        
        self.hudhaut.place(x=0,y=0)
        self.map.place(x=0,y=100)
        self.bar.place(x=800,y=0)
        self.root.bind("<KeyPress-h>",self.parent.debut)
        
        self.root.bind("<KeyPress-d>",self.peseDroit)
        self.root.bind("<KeyPress-w>",self.peseHaut)
        self.root.bind("<KeyPress-s>",self.peseBas)
        self.root.bind("<KeyPress-a>",self.peseGauche)
        
        self.root.bind("<KeyRelease-d>",self.relacheDroit)
        self.root.bind("<KeyRelease-w>",self.relacheHaut)
        self.root.bind("<KeyRelease-s>",self.relacheBas)
        self.root.bind("<KeyRelease-a>",self.relacheGauche)
        
    ''' self.root.bind("<KeyPress-Right>",self.peseDroit)
        self.root.bind("<KeyPress-Up>",self.peseHaut)
        self.root.bind("<KeyPress-Down>",self.peseBas)
        self.root.bind("<KeyPress-Left>",self.peseGauche)
        
        self.root.bind("<KeyRelease-Right>",self.relacheDroit)
        self.root.bind("<KeyRelease-Up>",self.relacheHaut)
        self.root.bind("<KeyRelease-Down>",self.relacheBas)
        self.root.bind("<KeyRelease-Left>",self.relacheGauche)'''
        
    def peseHaut(self,event):
        self.mouvement[0]=True
    def relacheHaut(self,event):
        self.mouvement[0]=False
         
    def peseDroit(self,event):
        self.mouvement[1]=True
    def relacheDroit(self,event):
        self.mouvement[1]=False
    
    def peseBas(self,event):
        self.mouvement[2]=True
    def relacheBas(self,event):
        self.mouvement[2]=False
        
    def peseGauche(self,event):
        self.mouvement[3]=True
    def relacheGauche(self,event):
        self.mouvement[3]=False
        
    def actualiser(self):
        if self.mouvement[0]:
             self.posY-=5
        if self.mouvement[1]:
            self.posX+=5
        if self.mouvement[2]:
            self.posY+=5
        if self.mouvement[3]:
            self.posX-=5
        
        
        self.map.delete("carre")
        self.map.create_rectangle(self.posX,self.posY,self.posX+20,self.posY+20,fill='red',tags="carre")
        
              
       
        