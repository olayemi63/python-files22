from tinydb import TinyDB, Query
db = TinyDB("db.json")


User = Query()
doc_id = Query

mystring = "test"
"""
def create():
    firstName = input("Enter the firstName of the User")
    lastName = input("Enter the lastName of the User")
    height = input("Enter the height of the User")
    age = input("Enter the age of the User")
    city = input("Enter the city of the User")
    
    db.insert ({"firstName": firstName, "lastName": lastName, "height": height, "age": age, "city": city})

"""

def read():
    results = db.all()
    print(results)

"""
def update(): 
   firstName = input("Enter the firstName of the User")
   lastName = input("Enter the lastName of the User")
   height = input("Enter the height of the User")
   age = input("Enter the age of the User")
   city = input("Enter the city of the User")

   db.update({"firstName": firstName, "lastName": lastName, "height": height, "age": age, "city": city})
"""

def remove():
   #doc_id = read()
   if  doc_id == 0:
    print({"There is no data to delete."})
   else:
    doc_id1 =int(input("Enter first doc_id to delete: "))
    doc_id2 = int(input("Enter second doc_id to delete: "))
    doc_id3 = int(input("Enter third doc_id to delete: "))
    db.remove(User.id == doc_id1)
    db.remove(User.id == doc_id2)
    db.remove(User.id == doc_id3)

# db.remove(doc_id== ["7"])




#item = db.remove(doc_ids=[1, 2, 3])
#print(item)



def menu():
    menuDB = """Welcome to personal information database v12.8

    Please enter an Option to select
    1. Read personal information in the database
    2. Create a new personal information in the database
    3. Update an existing personal information in the database
    4. Delete an existing personal information in the database
    5. Exit the database
"""

    print(menuDB)
  
    options = ["1", "2", "3", "4", "5"]
    choice = input("Select an Option from the Menu: ")

    while choice not in options:
        print(f"print f choice is not a valid choice.")
        choice = input("Enter a valid option ")
  
    return choice

#doc_ID = int(input("Enter your option"))



def insert():
    db.insert({"id" : 1 ,"firstName": "Rafael", "lastName": "Nadal", "age": 37, "height": "6.8ft", "city": "Mallorca"})
    db.insert({"id" : 2, "firstName": "Roger", "lastName": "Federer", "age": 40})
    db.insert({"id" : 3, "firstName": "Andy", "lastName": "Murray", "age": 35})
    db.insert({ "id" : 4,"firstName": "Stan", "lastName": "Wawrinka", "age": 35})
    db.insert({ "id" : 5,"firstName": "Yemi", "lastName": "Adio", "age": 99, "height": "6.5ft", "city": "Radlett Hertfordshire"})
    db.insert({ "id" : 6,"firstName": "Jamaal", "lastName": "Mohammed", "age": 39, "city": "Edgware London"})
    db.insert({ "id" : 7,"firstName": "Mike", "lastName": "Tyson", "age": 53, "city": "Catskill New York"})
    db.insert({ "id" : 8,"firstName": "Anthony", "lastName": "Joshua", "age" :33, "city": "Watford Hertfordshire"})
    db.insert({ "id" : 9,"firstName": "David", "lastName": "Ginola", "age": 40})
    db.insert({ "id" : 10,"firstName": "Evander", "lastName": "Holyfield", "age": 54})
    db.insert({ "id" : 11, "firstName": "Cristiano", "lastName": "Ronaldo", "age": 38, "height": "6ft * feet", "city": "Saudi Arabia"})
    db.insert({ "id" : 12,"firstName": "Ed", "lastName": "Sheeran", "age" :29})
    db.insert({ "id" : 13,"firstName": "Bob", "lastName": "Marley", "age": 60})
    db.insert({"id" : 14,"firstName": "Eddie", "lastName": "Murphy", "age": 55})
    db.insert({"id" :  15,"firstName": "Esther", "lastName": "Krakue", "age": 38, "height": "5.6ft", "city": "London"})
    db.insert({"id" :  16,"firstName": "Jennifer", "lastName": "Lopez", "age": 55})
    db.insert({"id" :  17,"firstName": "Diana", "lastName": "Ross", "age": 71})
    db.insert({"id" :  18,"firstName": "Beyonce", "lastName": "Knowles", "age": 41, "city": "Houston Texas"})
    db.insert({"id" :  19,"firstName": "Kiki", "lastName": "Layne", "age": 31})
    db.insert({"id" :  20,"firstName": "Nomzamo", "lastName": "Mbatha", "age": 32, "height": "5feet", "city": "Los Angeles"})
    db.insert({"id" : 21, "firstName": "Teyana", "lastName": "Taylor", "age": 32})
    db.insert({"id" : 22, "firstName": "Kelly", "lastName": "Rowland", "age": 42, "height":  "5.9ft", "city": "New York"})
#menu()
#insert()
#read()
#update()
#remove()
#db.remove(doc_ids= [1, 2, 3])
#print(db.all())


#if __name__ == "__main__":

menuLoop = True

while menuLoop == True:
     userChoice = menu()
     if userChoice == "1":
         read()
     elif userChoice == "2":
         create()
     elif userChoice == "3":
         update()
     elif userChoice == "4":
         remove()
     elif userChoice == "5":
      menuLoop = False  

print("End Program")    


