import logging, string

logging.basicConfig(level=logging.INFO, filename="szkript.log", filemode="a", 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class grade:
    def printGrade(seft,pontszam,pont, szazalek):
        
        if(pontszam >= 0 and pontszam <= pont):

            if(szazalek >= 80 and szazalek <= 100):
                Eredmeny = 5
        
            if(szazalek >= 70 and szazalek <= 79):
                Eredmeny = 4
            
            if(szazalek >= 60 and szazalek <= 69):
                Eredmeny = 3
            
            if(szazalek >= 50 and szazalek <= 59):
                Eredmeny = 2

            if(szazalek < 50):
                Eredmeny = 1
        else:
            Eredmeny = "Kérem adjon meg egy pontszámot 0 - feladati teljes pontszáma között"
            logging.error("Please add valid data")
  
        print(f"Érdem jegy: {Eredmeny}")
        print("Pontszám: {}/{}, Százalék {:.2f}%".format(pontszam,pont,szazalek))

       

   