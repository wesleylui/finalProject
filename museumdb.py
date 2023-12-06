import mysql.connector
import sys

def print_art_objs():
    #description and exhibition fields are too long and make table too long to read so have chosen to omit information
    instr = "select Id_no, Artist_Name, Epoch, Country, Title, Year_Created from ART_OBJECTS"
    # instr = "select *"
    cur.execute(instr)
    col_names = cur.column_names
    search_result = cur.fetchall()
    print(f"Search found {len(search_result)} entries: ")
    header_size=len(col_names)
    for i in range(header_size):
        print("{:<40s}".format(col_names[i]), end="")
    print()
    print(40*header_size*"-")
    for row in search_result:
        for val in row:
            print("{:<40s}".format(str(val)),end="")
        print()
    print(40*header_size*"-")

def print_specific_objs():
    choice = 1
    while choice != 5:
        print("What category would you like to browse?\
              \n1-Statues\
              \n2-Sculptures\
              \n3-Paintings\
              \n4-Other\
              \n5-Quit" + "\n" + 50 * "-")
        
        choice = input("Enter choice: ")  
        
        if choice == "1":
            instr = "select * from STATUE"
            cur.execute(instr)
            col_names = cur.column_names
            search_result = cur.fetchall()
            print(f"Search found {len(search_result)} entries: ")
            header_size=len(col_names)
            for i in range(header_size):
                print("{:<15s}".format(col_names[i]), end="")
            print()
            print(15*header_size*"-")
            for row in search_result:
                for val in row:
                    print("{:<15s}".format(str(val)),end="")
                print()
            print(15*header_size*"-")
        elif choice == "2":
            instr = "select * from SCULPTURE"
            cur.execute(instr)
            col_names = cur.column_names
            search_result = cur.fetchall()
            print(f"Search found {len(search_result)} entries: ")
            header_size=len(col_names)
            for i in range(header_size):
                print("{:<15s}".format(col_names[i]), end="")
            print()
            print(15*header_size*"-")
            for row in search_result:
                for val in row:
                    print("{:<15s}".format(str(val)),end="")
                print()
            print(15*header_size*"-")
        elif choice == "3":
            instr = "select * from PAINTING"
            cur.execute(instr)
            col_names = cur.column_names
            search_result = cur.fetchall()
            print(f"Search found {len(search_result)} entries: ")
            header_size=len(col_names)
            for i in range(header_size):
                print("{:<15s}".format(col_names[i]), end="")
            print()
            print(15*header_size*"-")
            for row in search_result:
                for val in row:
                    print("{:<15s}".format(str(val)),end="")
                print()
            print(15*header_size*"-")
        elif choice == "4":
            instr = "select * from OTHERS"
            cur.execute(instr)
            col_names = cur.column_names
            search_result = cur.fetchall()
            print(f"Search found {len(search_result)} entries: ")
            header_size=len(col_names)
            for i in range(header_size):
                print("{:<15s}".format(col_names[i]), end="")
            print()
            print(15*header_size*"-")
            for row in search_result:
                for val in row:
                    print("{:<15s}".format(str(val)),end="")
                print()
            print(15*header_size*"-")
        elif choice == "5":
            print("Exiting")
            sys.exit(0)
        else:
            print("Invalid option")

def print_exhibition():
    instr = "select * from EXHIBITION"
    cur.execute(instr)
    col_names = cur.column_names
    search_result = cur.fetchall()
    print(f"Search found {len(search_result)} entries: ")
    header_size=len(col_names)
    for i in range(header_size):
        print("{:<53s}".format(col_names[i]), end="")
    print()
    print(53*header_size*"-")
    for row in search_result:
        for val in row:
            print("{:<53s}".format(str(val)),end="")
        print()
    print(53*header_size*"-")

def print_collections():
    instr = "select * from COLLECTIONS"
    cur.execute(instr)
    col_names = cur.column_names
    search_result = cur.fetchall()
    print(f"Search found {len(search_result)} entries: ")
    header_size=len(col_names)
    for i in range(header_size):
        print("{:<47s}".format(col_names[i]), end="")
    print()
    print(47*header_size*"-")
    for row in search_result:
        for val in row:
            print("{:<47s}".format(str(val)),end="")
        print()
    print(47*header_size*"-")

def insert_data():
    choice = 1
    while choice != 4:
        print("What would you like to add?\
              \n1-New Art Object\
              \n2-New Exhibition\
              \n3-New Collection\
              \n4-Quit" + "\n" + 50 * "-")

        choice = input("Enter choice: ")    

        if choice == "1":
            template = "insert into ART_OBJECTS values (%s,%s,%s,%s,%s,%s,%s,%s)"
            id = input("Enter ID_no: ") or None
            artist = input("Enter artist's name: ") or None
            epoch = input("Enter epoch: ") or None
            country = input("Enter country of origin: ") or None
            title = input("Enter title: ") or None
            date = input("Enter year created: ") or None
            desc = input("Enter description: ") or None
            exh_name = input("Enter exhibition name: ") or None

            template_data = (id, artist, epoch, country, title, date, desc, exh_name)
            try:
                cur.execute(template, template_data)
                cnx.commit()
                print("Successful insert")
                print(50*"-")
            except:
                print("Insert failed")
                print(50*"-")

        elif choice == "2":
            template = "insert into EXHIBITION values (%s,%s,%s)"
            name = input("Enter exhibit name: ") or None
            start_date = input("Enter start date: ") or None
            end_date = input("Enter end date: ") or None

            template_data = (name, end_date, start_date)
            try:
                cur.execute(template, template_data)
                cnx.commit()
                print("Successful insert")
                print(50*"-")
            except:
                print("Insert failed")
                print(50*"-")

        elif choice == "3":
            template = "insert into COLLECTIONS values (%s, %s, %s, %s, %s, %s)"
            c_name = input("Enter collection name: ") or None
            address = input("Enter address of collection: ") or None
            p_num = input("Enter phone number") or None
            typee = input("Enter type of collection: ") or None
            contact = input("Enter contact: ") or None
            desc = input("Enter desc: ") or None
            
            template_data = (c_name, address, p_num, typee, contact, desc)
            try:
                cur.execute(template, template_data)
                cnx.commit()
                print("Successful insert")
                print(50*"-")
            except:
                print("Insert failed") 
                print(50*"-")     

        elif choice == "4":
            print("Exiting")
            sys.exit(0)
        else:
            print("Invalid option")
            print(50*"-")     

def delete_data():
    choice = 1
    while choice != 4:
        print("What would you like to remove?\
              \n1-Remove Art Object\
              \n2-Remove Exhibition\
              \n3-Remove Collection\
              \n4-Quit" + "\n" + 50 * "-")


        choice = input("Enter choice: ")    
        if choice == "1":
            id = input("Enter id of object you would like to be removed: ")
            instr = "delete from ART_OBJECTS where Id_no='{s}'".format(s=id)
            try:
                cur.execute(instr)
                cnx.commit()
                print("Successful deletion")
                print(50*"-")
            except: 
                print("Deletion failed")
                print(50*"-")
        elif choice == "2":
            name = input("Enter name of exhibition to be removed: ")
            instr = "delete from EXHIBITION where Namee='{s}'".format(s=name)
            try:
                cur.execute(instr)
                cnx.commit()
                print("Successful deletion")
                print(50*"-")
            except: 
                print("Deletion failed")
                print(50*"-")
        elif choice == "3":
            name = input("Enter name of collection to be removed: ")
            instr = "delete from COLLECTIONS where C_Name='{s}'".format(s=name)
            try:
                cur.execute(instr)
                cnx.commit()
                print("Successful deletion")
                print(50*"-")
            except: 
                print("Deletion failed")
                print(50*"-")
        elif choice == "4":
            print("Exiting")
            sys.exit(0)
        else:
            print("Invalid option")
            print(50*"-")

def update_data():
    choice = 1
    while choice != 4:
        print("What would you like to update?\
              \n1-Update Art Object\
              \n2-Update Exhibition\
              \n3-Update Collection\
              \n4-Quit" + "\n" + 50 * "-")
        
        choice = input("Enter choice: ")

        if choice == "1":
            cur.execute("select * from ART_OBJECTS")
            col_names = cur.column_names
            header_size = len(col_names)
            print("Names of attributes:")
            for i in range(header_size):
                print("{:<20s}".format(col_names[i]))
            print(50*"-")

            attribute = input("Enter what attribute you would like to update on: ")
            att_value = input("Enter value of attribute to be updated on: ")
            att_updated = input("Enter what attribute you would like to change: ")
            new_value = input("Enter new value for attribute")
            template = "update ART_OBJECTS set {a}='{b}' where {c}='{d}'".format(a=att_updated, b=new_value, c=attribute, d=att_value)
            try:
                cur.execute(template)
                cnx.commit()
                print("Successful update")
                print(50*"-")
            except:
                print("Failed update")
                print(50*"-")
        elif choice == "2":
            cur.execute("select * from EXHIBITION")
            col_names = cur.column_names
            header_size = len(col_names)
            print("Names of attributes:")
            for i in range(header_size):
                print("{:<20s}".format(col_names[i]))
            print(50*"-")

            attribute = input("Enter what attribute you would like to update on: ")
            att_value = input("Enter value of attribute to be updated on: ")
            att_updated = input("Enter what attribute you would like to change: ")
            new_value = input("Enter new value for attribute")
            template = "update EXHIBITION set {a}='{b}' where {c}='{d}'".format(a=att_updated, b=new_value, c=attribute, d=att_value)
            try:
                cur.execute(template)
                cnx.commit()
                print("Successful update")
                print(50*"-")
            except:
                print("Failed update")
                print(50*"-")
        elif choice == "3":
            cur.execute("select * from COLLECTIONS")
            col_names = cur.column_names
            header_size = len(col_names)
            print("Names of attributes:")
            for i in range(header_size):
                print("{:<20s}".format(col_names[i]))
            print(50*"-")

            attribute = input("Enter what attribute you would like to update on: ")
            att_value = input("Enter value of attribute to be updated on: ")
            att_updated = input("Enter what attribute you would like to change: ")
            new_value = input("Enter new value for attribute")
            template = "update COLLECTIONS set {a}='{b}' where {c}='{d}'".format(a=att_updated, b=new_value, c=attribute, d=att_value)
            try:
                cur.execute(template)
                cnx.commit()
                print("Successful update")
                print(50*"-")
            except:
                print("Failed update")
                print(50*"-")
        elif choice == "4":
            print("Exiting")
            sys.exit(0) 
        else:
            print("Invalid option")
            print(50*"-")                  

if __name__ == "__main__":

    #connect to server
    print("Welcome to the Museum Database:\
          \nIn order to proceed, please select your role from the list below:\
          \n1-DB Admin (login required)\
          \n2-Data Entry (login required)\
          \n3-Guest/browser (no login required)\
          \n4-Quit" + "\n" + 50 * "-")

    role_selection = ""
    while role_selection not in ["1","2","3","4"]:
        role_selection = input("Please type 1, 2, or 3 to select your role, or type 4 to exit program: ")
        if role_selection not in ["1","2","3","4"]:
            print("Invalid choice, please try again")


    if role_selection in ["1","2"]:
        #admin logins: username = museum_admin, password = admin
        #data entry logins: username = data_entry, password = data
        username = input("Username: ")
        passcode = input("Password: " )
    elif role_selection == "4":
        print("Exiting program")
        sys.exit(0)
    else:
        print("Guest selected")
        username = "guest"
        passcode = None

    try:
        cnx = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = username,
            password = passcode
        )
    except:
        print("Invalid login, exiting...")
        sys.exit(0)

    #get a cursor
    cur = cnx.cursor(buffered=True)
    cur.execute("use MUSEUM")

    if role_selection == "1":
        #admin
        choice = 1
        while choice != 4:
            print("What are you looking to do?\
                  \n1-Manage users\
                  \n2-Data entry/deletion\
                  \n3-Browse database\
                  \n4-Quit" + "\n" + 50 * "-")

            choice = input("Enter choice: ")
            if choice == "1":
                #MANAGE USERS
                choice = 1
                while choice != 5:
                    print("What would you like to modify about users\
                          \n1-Block user\
                          \n2-Modify user\
                          \n3-Add user\
                          \n4-Remove user\
                          \n5-Quit" + "\n" + 50 * "-")
                    

                    choice = input("Enter choice: ")
                    if choice == "1":
                        #BLOCK USER
                        user = input("Enter user you would like to block: ")
                        template = "revoke all privileges on *.* from {a}@localhost".format(a=user)
                        cur.execute(template)
                        cur.execute("flush privileges")
                        cnx.commit()
                        print("Successful block")
                        print(50*"-")
                    elif choice == "2":
                        #MODIFY USER
                        user = input("Enter user you would like to modify")
                        print("What would you like to modify?\
                          \n1-Change password\
                          \n2-Change role" + "\n" + 50 * "-")

                        a = input("Select choice: ")
                        if a == "1":
                            #CHANGE PASSWORD
                            new_pass = input("Enter new password: ")
                            template = "alter user {a}@localhost identified with mysql_native_password by '{b}'".format(a=user, b=new_pass)
                            cur.execute(template)
                            cnx.commit()
                            print("Successful password update")
                            print(50*"-")
                        elif a == "2":
                            #CHANGE ROLE
                            print("Enter number corresponding to role below to grant role\
                                  \n1-Admin\
                                  \n2-Data Entry\
                                  \n3-Guest" + "\n" + 50 * "-")


                            role = input("Enter choice of role: ")
                            if role == "1":
                                #ADMIN
                                template2 = "grant db_admin@localhost to {a}@localhost".format(a=user)
                                cur.execute(template2)
                            elif role == "2":
                                #DATA ENTRY
                                template2 = "grant change_data@localhost to {a}@localhost".format(a=user)
                                cur.execute(template2)
                            elif role == "3":
                                #GUEST
                                template2 = "grant guest@localhost to {a}@localhost".format(a=user)
                                cur.execute(template2)
                            cnx.commit()
                            print("Successfully updated role")
                            print(50*"-")
                    elif choice == "3":
                        #ADD USER
                        print("Enter number corresponding to role below to grant role\
                          \n1-Admin\
                          \n2-Data entry\
                          \n3-Guest" + "\n" + 50 * "-")
                        role = input("Enter choice of role: ")
                        user = input("Enter username of user to add: ")
                        pcode = input("Enter pcode of user: ")
                        cur.execute("drop user if exists {a}@localhost".format(a=user))
                        template = "create user {a}@localhost identified with mysql_native_password by '{b}'".format(a=user, b=pcode)
                        cur.execute(template)
                        if role == "1":
                            template2 = "grant db_admin@localhost to {a}@localhost".format(a=user)
                            cur.execute(template2)
                        elif role == "2":
                            template2 = "grant change_data@localhost to {a}@localhost".format(a=user)
                            cur.execute(template2)
                        elif role == "3":
                            template2 = "grant guest@localhost to {a}@localhost".format(a=user)
                            cur.execute(template2)
                        cur.execute("set default role all to {a}@localhost".format(a=user))
                        cnx.commit()
                        print("Successfully added")
                        print(50*"-")
                    elif choice == "4":
                        #REMOVE USER
                        user = input("Enter user to remove:")
                        template = "drop user if exists {s}@localhost".format(s=user)
                        cur.execute(template)
                        cnx.commit()
                        print("Successful removal")
                        print(50*"-")
                    elif choice == "5":
                        print("Exiting")
                        sys.exit(0)
                    else:
                        print("Invalid choice")
            elif choice == "2":
                choice = 1
                while choice != 4:
                    print("What are you looking to do?\
                          \n1-Insert data\
                          \n2-Delete data\
                          \n3-Update data\
                          \n4-Quit" + "\n" + 50 * "-")

                    choice = input("Enter choice: ")    

                    if choice == "1":
                        insert_data()
                    elif choice == "2":
                        delete_data()
                    elif choice == "3":
                        update_data()
                    elif choice == "4":
                        print("Exiting")
                        sys.exit(0)
                    else:
                        print("Invalid option")
                        print(50*"-")                   
            elif choice == "3":
                #BROWSE DATABASE
                choice = 1
                while choice != 4:
                    print("What are you looking to browse?\
                          \n1-All art objects\
                          \n2-Specific art objects\
                          \n3-Exhibitions\
                          \n4-Collections\
                          \n5-Quit" + "\n" + 50 * "-")

                    choice = input("Enter choice: ")

                    if choice == "1":
                        print_art_objs()
                    elif choice == "2":
                        print_specific_objs()
                    elif choice == "3":
                        print_exhibition()
                    elif choice == "4":
                        print_collections()
                    elif choice == "5":
                        print("Exiting")
                        sys.exit(0)
                    else:
                        print("Invalid option")
                        print(50*"-")                
            elif choice == "4":
                print("Exiting")
                sys.exit(0)
            else:
                print("Invalid choice")
    elif role_selection == "2":
        #data entry/deletion
        choice = 1
        while choice != 4:
            print("What are you looking to do?\
                          \n1-Insert Data\
                          \n2-Delete Data\
                          \n3-Update Data\
                          \n4-Browse Database\
                          \n5-Quit" + "\n" + 50 * "-")

            choice = input("Enter choice: ")    

            if choice == "1":
                insert_data()
            elif choice == "2":
                delete_data()
            elif choice == "3":
                update_data()
            elif choice =="4":
                choice = 1
                while choice != 4:
                    print("What are you looking to browse?\
                          \n1-All art objects\
                          \n1-Specific art objects\
                          \n3-Exhibitions\
                          \n4-Collections\
                          \n5-Quit" + "\n" + 50 * "-")

                    choice = input("Enter choice: ")

                    if choice == "1":
                        print_art_objs()
                    elif choice == "2":
                        print_specific_objs()
                    elif choice == "3":
                        print_exhibition()
                    elif choice == "4":
                        print_collections()
                    elif choice == "5":
                        print("Exiting")
                        sys.exit(0)
                    else:
                        print("Invalid option")
                        print(50*"-")
            elif choice == "5":
                print("Exiting")
                sys.exit(0)
            else:
                print("Invalid option")
                print(50*"-")                
    else:
        #guest 
        choice = 1
        while choice != 4:
            print("What are you looking to browse?\
                          \n1-All art objects\
                          \n1-Specific art objects\
                          \n3-Exhibitions\
                          \n4-Collections\
                          \n5-Quit" + "\n" + 50 * "-")

            choice = input("Enter choice: ")

            if choice == "1":
                print_art_objs()
            elif choice == "2":
                print_specific_objs()
            elif choice == "3":
                print_exhibition()
            elif choice == "4":
                print_collections()
            elif choice == "5":
                print("Exiting")
                sys.exit(0)
            else:
                print("Invalid option")
                print(50*"-")