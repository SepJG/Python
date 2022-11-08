def addSite(notebook):
  nettsted = input("nettsted: ")
  notebook.values()
  if nettsted in notebook.keys():
    print("finnes")
    return notebook
  brukernavn = input("brukernavn: ")
  passord = input("passord: ")
  notebook[nettsted] = [brukernavn, [passord]]
  return notebook

notebook = {'reddit': ['foo', ['bar']]}
# notebook = addSite(notebook)
# print(notebook)


def showSites(notebook):
  print("Sted\t", "bruker\t", "pwd")
  # for nettsted, verdi in notebook.items():
    # print(nettsted, verdi[0], verdi[1][-1])


notebook = {'Facebook': ['Urgle', ['pwd1']],
  'reddit': ['urgle', ['asdf1234', 'pwd1']],
  'Aftenposten': ['ivrig', ['pwdold', 'pwdnew']]}

# showSites(notebook)


def formatList(liste):
  return ", ".join(liste)



# def editSite(notebook, site):
#   old = True
  
#   while old:
#     password = input(f"Add new site password for {site}: ")
#     if password in str(notebook[site][1]):
#       print("Already used: {formatList(notebook[site][1])}")
#     else:
#       old = False
#   notebook[site][1].append(password)
#   print(f"{site} has been updated with a new password")
#   return notebook

# notebook = editSite(notebook, 'reddit')
# print(notebook)


def secureSites(notebook):
  pwds = {}
  for site, passlist in notebook.items():
    currentpwd = passlist[1][-1]
    if currentpwd in pwds: 
      pwds[currentpwd].append(site)
    else:
      pwds[currentpwd] = [site]
  for currentpwd in pwds:
    if len(pwds[currentpwd]) > 1:
      duplicates = True
      print("You have used the password '{0}' at the following sites: {1}.".format(currentpwd, formatList(pwds[currentpwd])))
  if not duplicates:
    print("No sites had similar passwords. Good job!")
