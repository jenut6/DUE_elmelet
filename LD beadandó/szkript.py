import result,logging

logging.basicConfig(level=logging.INFO, filename="szkript.log", filemode="a", 
                    format="%(asctime)s - %(levelname)s - %(message)s")


logging.info("Start code")
pontszam = input("Add meg az elvégzett feladatért járó pontszámot: ")
pont = input("Adja meg a feladat teljes pont számát:")
szazalek = 0

logging.info("Input the data ")

if(pontszam != '' and pont != ''):

    pontszam = int(pontszam)
    pont = int(pont)

    if(pontszam != 0 and pont !=0):
        szazalek = (pontszam / pont) * 100
    else:
        logging.critical("Pontszam or pont is 0")

    obj = result.grade()
    obj.printGrade(pontszam,pont,szazalek)
    logging.info("Print the result")

else:
    print("Kérem adjon meg az elért pontszámot és a feladat pontszámát között.")
    logging.error("Please add valid data")

logging.info("Stop code")





