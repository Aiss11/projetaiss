import sqlite3
conn =sqlite3.connect('mydb.db')
cur =conn.cursor()
print("bienvenu dans notre application")
print("TAPPER 0 POUR VOUS INSCRIRE OU un chiffre quelquonquePOUR VOUS CONNECTER")
b = int(input())
if b==0:
  nn=input('Veuillez entrer votre nom: ')
  pn=input('Veuillez entrer prenom: ')
  mail=input('Veuillez entrer votre mail: ')
  pass1=input('Veuillez entrer votre motdepasse: ')
  pass2=input('confirmer le mot de passe: ')
  req2 ="INSERT INTO user(nom,mail,motdepasse ) values (?, ?, ?)"
  cur.execute(req2 , (nn, mail, pass2))
  req="SELECT * FROM user"
user1 = cur.execute(req)

for row in user1:
	print(row[0])
      




else:
	print("bienvenu dans le menu connextion")
	nnn=input('Veuillez entrer votre nom: ')
	pass22=input('confirmer le mot de passe: ')
	
	req3="SELECT  nom, motdepasse FROM user WHERE nom = ? AND motdepasse=?"
	cur.execute(req3 , (nnn,  pass22))

	if len( cur.fetchall() ) == 0:
		print("tres bien")
       	
   
      


