'''
- Hvorfor unntak?
- Når oppstår de? kan dere komme på noen ganger det har
  oppstått unntak mens dere har holdt på med øvinger?
- Hvordan unngår man krasj? try_except_liste.py, try_except_float.py
- Oppgave: oppgave_try_except_deling.py
- Det finnes ulike typer unntak: try_except.py. 
- Man kan se feilmeldingene: exception_vis_feilmelding.py
- Man kan kjøre en kodebit bare hvis koden ikke utløser unntak. try_else.py
- Man kan kjøre programkode uavhengig av om det oppståer feil eller ikke: try_finally.py
'''


try:
    print('Ja, jeg er her.')
    tall = int(input("skriv inn et tall: "))
    print('Ja, jeg er her også.')
    print(f'4/{tall} er {4/tall}.')
    print('Men ikke her.')
except Exception as e:
    print('Noe ble feil:',e)

    
