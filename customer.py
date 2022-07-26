import types
import sqlite3
from sqlite3 import Error
from datetime import datetime


class customer:
    def __init__(self, email, name: object, gstin, type_of_work, deals, mob1, mob2, add, area, pincode, due, next_con_date):
        self.name = name
        self.email = email
        self.gstin = gstin
        self.Type_Of_Work = type_of_work
        self.deals = deals
        self.mob1 = mob1
        self.mob2 = mob2
        self.add = add
        self.area = area
        self.pincode = pincode
        self.due = due
        self.next_con_date = "NULL"
        if next_con_date != "NULL":
            self.next_con_date = datetime.strptime(str(next_con_date), '%Y-%m-%d').date()
        else:
            self.next_con_date = "NULL"

    def add_new_customer(self, cus_db, cus_cursor):
        command = "insert into customer(name,gstin,Type_Of_Work,deals_in,address,area,pin_code,due_money"
        if self.mob1 != "*":
            command = command + ",mobile_no_1"
        if self.mob2 != "NULL":
            command = command + ",mobile_no_2"
        if self.email != "NULL":
            command = command + ",email_id"
        if self.next_con_date != "NULL":
            command = command + ",when_to_contact"
        command = command + ") values(?,?,?,?,?,?,?,?"
        if self.mob1 != "*":
            command = command + "," + str(self.mob1)
        if self.mob2 != "NULL":
            command = command + "," + str(self.mob2)
        if self.email != "NULL":
            command = command + ",'" + str(self.email) + "'"
        if self.next_con_date != "NULL":
            command = command + ",'" + str(self.next_con_date) + "'"
        command = command + ");"
        cus_cursor.execute(command,
                           (self.name, self.gstin, self.Type_Of_Work, self.deals, self.add, self.area, self.pincode,
                            self.due))

    def delete(self, cus_db, cus_cursor):
        command = "DELETE FROM customer WHERE mobile_no_1 = ?"
        p = (self.mob1,)
        cus_cursor.execute(command, p)
        # cus_db.commit()
        self = None

    # W = dict with values with new values of corr. keys, keys(in str) = name,email,gstin,type_of_work,deals,mob1,mob2,add,area,pincode,due,next_con_date
    def update(self, cus_db, cus_cursor, **w):
        C = 0
        print("Inside Function.... w = ", w, "type = ", type(w))
        Len = len(w)
        print("length of w = ", Len)
        Counter = 0
        com_p_1 = "UPDATE customer SET "
        com_str_p_2 = "' WHERE mobile_no_1 = ?;"
        com_p_2 = " WHERE mobile_no_1 = ?;"
        command = com_p_1
        if "name" in w.keys():
            Counter += 1
            command = self.nameupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "email" in w.keys():
            Counter += 1
            command = self.emailupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "gstin" in w.keys():
            Counter += 1
            command = self.gstinupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "type_of_work" in w.keys():
            Counter += 1
            command = self.type_of_workupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "deals" in w.keys():
            Counter += 1
            command = self.dealsupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "mob2" in w.keys():
            Counter += 1
            command = self.mob2update(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "add" in w.keys():
            Counter += 1
            command = self.addupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "area" in w.keys():
            Counter += 1
            command = self.adreaupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "pincode" in w.keys():
            Counter += 1
            command = self.pincodeupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "due" in w.keys():
            Counter += 1
            command = self.dueupdate(command, com_str_p_2, com_p_2, Len, Counter, **w)
        if "next_con_date" in w.keys() and w["next_con_date"] != "NULL":
            Counter += 1
            command = self.next_con_date(command, com_str_p_2, com_p_2, Len, Counter, **w)
        try:
            p = (int(self.mob1),)
            cus_cursor.execute(command, p)
            # cus_db.commit()
            if "name" in w.keys():
                self.name = str(w["name"])
            if "email" in w.keys():
                self.email = str(w["email"])
            if "gstin" in w.keys():
                self.gstin = str(w["gstin"])
            if "type_of_work" in w.keys():
                self.type_of_work = str(w["type_of_work"])
            if "deals" in w.keys():
                self.deals = str(w["type_of_work"])
            if "mob2" in w.keys():
                self.mob2 = w["mob2"]
            if "add" in w.keys():
                self.add = w["add"]
            if "area" in w.keys():
                self.area = w["area"]
            if "pincode" in w.keys():
                self.pincode = w["pincode"]
            if "due" in w.keys():
                self.due = w["due"]
            if "next_con_date" in w.keys() and w["next_con_date"] != "NULL":
                self.next_con_date = datetime.strptime(str(next_con_date), '%Y-%m-%d').date()
            return True
        except:
            C += 1
            if C <= 2:
                self.update(self, cus_db, cus_cursor, **w)
            else:
                return False

    def nameupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_name = "name = '"
        if Counter == Len:
            command = command + com_p_name + str(w["name"]) + com_str_p_2
        else:
            command = command + com_p_name + str(w["name"]) + "', "
        return command

    def emailupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_gstin = "GSTIN = '"
        if Counter == Len:
            command = command + com_p_gstin + str(w["gstin"]) + com_str_p_2
        else:
            command = command + com_p_gstin + str(w["gstin"]) + "', "
        return command

    def gstinupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_gstin = "gstin = '"
        if Counter == Len:
            command = command + com_p_gstin + str(w["gstin"]) + com_str_p_2
        else:
            command = command + com_p_gstin + str(w["gstin"]) + "', "
        return command

    def type_of_workupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_type_of_work = "Type_Of_Work = '"
        if Counter == Len:
            command = command + com_p_type_of_work + str(w["type_of_work"]) + com_str_p_2
        else:
            command = command + com_p_type_of_work + str(w["type_of_work"]) + "', "
        return command

    def mob2update(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_mob2 = "mobile_no_2 = "
        if Counter == Len:
            command = command + com_p_mob2 + str(w["mob2"]) + com_p_2
        else:
            command = command + com_p_mob2 + str(w["mob2"]) + ", "
        return command

    def addupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_add = "Address = '"
        if Counter == Len:
            command = command + com_p_add + str(w["add"]) + com_str_p_2
        else:
            command = command + com_p_add + str(w["add"]) + "', "
        return command

    def areaupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_area = "Area = '"
        if Counter == Len:
            command = command + com_p_area + str(w["area"]) + com_str_p_2
        else:
            command = command + com_p_area + str(w["area"]) + "', "
        return command

    def pincodeupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_pincode = "Pin_Code = "
        if Counter == Len:
            command = command + com_p_pincode + str(w["pincode"]) + com_p_2
        else:
            command = command + com_p_pincode + str(w["pincode"]) + ", "
        return command

    def dueupdate(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_due = "Due_Money = "
        if Counter == Len:
            command = command + com_p_due + str(float(w["due"])) + com_p_2
        else:
            command = command + com_p_due + str(float(w["due"])) + ", "
        return command

    def next_con_date(self, command, com_str_p_2, com_p_2, Len, Counter, **w):
        com_p_next_con_date = "When_To_Contact = "
        if Counter == Len:
            command = command + com_p_next_con_date + str(
                datetime.strptime(str(w["next_con_date"]), '%Y-%m-%d').date()) + com_p_2
        else:
            command = command + com_p_next_con_date + str(
                datetime.strptime(str(w["next_con_date"]), '%Y-%m-%d').date()) + ", "
        return command


def str_to_class(s):
    if s in globals() and isinstance(globals()[s], types.ClassType):
        return globals()[s]
    return None


def make_customer_obj(cus_db, cus_cursor, cus_name, cus_email_id, cus_gstin, Type_Of_Work, cus_deals, cus_mob1,
                      cus_mob2, cus_add, cus_area, cus_pin_code, cus_due, cus_next_con_date):
    if cus_mob1 != "*":
        cus_mob1 = int(cus_mob1)
    if cus_mob2 != "NULL":
        cus_mob2 = int(cus_mob2)
    if cus_pin_code != "NULL":
        cus_pin_code = int(cus_pin_code)
    if cus_due != "NULL":
        cus_due = float(cus_due)
    if cus_next_con_date != "NULL":
        cus_next_con_date = datetime.strptime(cus_next_con_date, '%Y-%m-%d').date()
    cus = customer(cus_name, cus_email_id, cus_gstin, Type_Of_Work, cus_deals, cus_mob1, cus_mob2, cus_add, cus_area,
                   cus_pin_code, cus_due, cus_next_con_date)
    return cus


def MakeCusObjByMob1(cus_db, cus_cursor, cus_mob1):
    command = "SELECT " + "name" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_name = row[0]
        else:
            cus_name = "NULL"
    else:
        cus_name = "NULL"
    command = "SELECT " + "email_id" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_email_id = row[0]
        else:
            cus_email_id = "NULL"
    else:
        cus_email_id = "NULL"
    command = "SELECT " + "gstin" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_gstin = row[0]
        else:
            cus_gstin = "NULL"
    else:
        cus_gstin = "NULL"
    command = "SELECT " + "type_of_work" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            Type_Of_Work = row[0]
        else:
            Type_Of_Work = "NULL"
    else:
        Type_Of_Work = "NULL"
    command = "SELECT " + "deals_in" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_deals = row[0]
        else:
            cus_deals = "NULL"
    else:
        cus_deals = "NULL"
    command = "SELECT " + "mobile_no_2" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_mob2 = str(row[0])
        else:
            cus_mob2 = "NULL"
    else:
        cus_mob2 = "NULL"
    command = "SELECT " + "address" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_add = row[0]
        else:
            cus_add = "NULL"
    else:
        cus_add = "NULL"
    command = "SELECT " + "area" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_area = row[0]
        else:
            cus_area = "NULL"
    else:
        cus_area = "NULL"
    command = "SELECT " + "pin_code" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_pin_code = str(row[0])
        else:
            cus_pin_code = "NULL"
    else:
        cus_pin_code = "NULL"
    command = "SELECT " + "due_money" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_due = str(row[0])
        else:
            cus_due = "NULL"
    else:
        cus_due = "NULL"
    command = "SELECT " + "when_to_contact" + " FROM customer WHERE mobile_no_1 = ?"
    cus_cursor.execute(command, (cus_mob1,))
    row = cus_cursor.fetchone()
    if row != None:
        if row[0] != None:
            cus_next_con_date = str(row[0])
        else:
            cus_next_con_date = "NULL"
    else:
        cus_next_con_date = "NULL"
    try:
        if cus_mob2 != "NULL":
            print(cus_mob2)
            cus_mob2 = int(cus_mob2)
        if cus_pin_code != "NULL":
            print(cus_pin_code)
            cus_pin_code = int(cus_pin_code)
        if cus_due != "NULL":
            print(cus_due)
            cus_due = float(cus_due)
        if cus_next_con_date != "NULL":
            print(cus_next_con_date)
            cus_next_con_date = datetime.strptime(cus_next_con_date, '%Y-%m-%d').date()
        cus = customer(cus_name, cus_email_id, cus_gstin, Type_Of_Work, cus_deals, cus_mob1, cus_mob2, cus_add,
                       cus_area, cus_pin_code, cus_due, cus_next_con_date)
        return cus
    except UnboundLocalError as e:
        print("Error!")
        print(e)
        cus = None
        return cus
    except Error as e:
        print("Error!")
        print(e)
        cus = None
        return cus


def SearchByPartOfName(PartOfName, cus_db, cus_cursor):
    PartOfName = str(PartOfName)
    command = "SELECT mobile_no_1 FROM customer WHERE name LIKE '%" + PartOfName + "%';"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByDealsIn(DealsIn, cus_db, cus_cursor):
    DealsIn = str(DealsIn)
    command = "SELECT mobile_no_1 FROM customer WHERE Deals_In LIKE '%" + DealsIn + "%';"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByArea(Area, cus_db, cus_cursor):
    Area = str(Area)
    command = "SELECT mobile_no_1 FROM customer WHERE Area LIKE '%" + Area + "%';"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByPinCode(PinCode, cus_db, cus_cursor):
    PinCode = str(int(PinCode))
    command = "SELECT mobile_no_1 FROM customer WHERE Pin_Code = " + PinCode + ";"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByTypeOfWork(TypeOfWork, cus_db, cus_cursor):
    TypeOfWork = str(TypeOfWork)
    command = "SELECT mobile_no_1 FROM customer WHERE Type_Of_Work LIKE '%" + TypeOfWork + "%';"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByExactDueCus(due, cus_db, cus_cursor):
    due = str(float(due))
    command = "SELECT mobile_no_1 FROM customer WHERE due_money = " + due + ";"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByDueCus(cus_db, cus_cursor):
    command = "SELECT mobile_no_1 FROM customer WHERE due_money > 0.00;"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByWhenToContact(WhenToContact, cus_db, cus_cursor):
    WhenToContact = str(datetime.strptime(str(WhenToContact), '%Y-%m-%d').date())
    command = "SELECT mobile_no_1 FROM customer WHERE When_To_Contact = date('" + WhenToContact + "');"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def SearchByWhenToContactToday(cus_db, cus_cursor):
    command = "SELECT mobile_no_1 FROM customer WHERE When_To_Contact = date('now');"
    values = cus_cursor.execute(command)
    rows = values.fetchall()
    cus_list = list()
    if rows != None:
        for row in rows:
            if row != None:
                cus_list.append(MakeCusObjByMob1(cus_db, cus_cursor, row[0]))
    return cus_list


def db():
    cus_db = sqlite3.connect(database=r"D:\USB Drive\dad's_app\db\app.db", isolation_level=None)
    return cus_db


def cursor(cus_db):
    cus_cursor = cus_db.cursor()
    return cus_cursor


def closeconn(cus_db, cus_cursor):
    try:
        # cus_db.commit()
        cus_cursor.close()
        return True
    except:
        return False


def do_nothing():
    print("This Feature Is Still Under Development")
    return


def main(cus_db, cus_cursor):
    global a
    a = True
    print("What Do You Want To Do??")
    print("Options    :    Work")
    print("   1       :    Add a Customer")
    print("   2       :    Update/Delete a Customer")
    print("   3       :    Search By Part Of Name")
    print("   4       :    Search By Deals In")
    print("   5       :    Search by Area")
    print("   6       :    Search by PinCode")
    print("   7       :    Search by Type Of Work")
    print("   8       :    List (Search) Due Customers")
    print("   9       :    When To Contact(Search)")
    print("   0      :    To Exit")
    Option = int(input("Enter Choosen Option:"))
    if Option == 1:
        print(
            "In The Following Info Plz. Enter 'NULL' In Capitals WITHOUT COMMAS Where U Don't Want To Enter Any Value")
        cus_name = input("enter The name of new customer:")
        cus_email_id = input("enter the email id of new customer:")
        cus_gstin = input("enter the gstin of new customer:")
        Type_Of_Work = input("enter the Type_Of_Work of new customer:")
        cus_deals = input("enter the types of products of new customer:")
        cus_mob1 = input("enter first mobile no. of new customer:")
        cus_mob2 = input("enter second mobile no. of new customer:")
        cus_add = input("enter the address of new customer:")
        cus_area = input("enter the area of new customer:")
        cus_pin_code = input("enter the pin code of new customer:")
        cus_due = input("enter the due amount of new customer:")
        cus_next_con_date = input("enter the next contact date of new customer:")
        cus = customer(cus_name, cus_email_id, cus_gstin, Type_Of_Work, cus_deals, cus_mob1, cus_mob2, cus_add,
                       cus_area, cus_pin_code, cus_due, cus_next_con_date)
        cus.add_new_customer(cus_db, cus_cursor)
    elif Option == 2:
        while True:
            print("SELECT A WAY TO SEARCH THE CUSTOMER YOU WANT TO UPDATE/DELETE")
            print("   1       :    Search By Part Of Name")
            print("   2       :    Search By Deals In")
            print("   3       :    Search by Area")
            print("   4       :    Search by PinCode")
            print("   5       :    Search by Type Of Work")
            print("   0       :    To Go Back")
            Op = int(input("Enter Choosen Option:"))
            # cus is a customer object (from customer class)
            if Op == 1:
                PartOfName = input("Enter The Part Of The Name Of Customer:")
                cus_list = SearchByPartOfName(PartOfName, cus_db, cus_cursor)
                if len(cus_list) == 0:
                    print("no values found!! RESTARTING APP!!.......")
                    conn_closed = closeconn(cus_db, cus_cursor)
                    only_non_gui_play()
                for i in range(0, len(cus_list)):
                    if cus_list[i] is not None:
                        name = str(cus_list[i].name)
                        mob1 = str(cus_list[i].mob1)
                        print("Option " + str(i + 1) + "    :    Name = " + name + "    Mobile No. 1 = " + mob1)
                print("other integers to search again")
                o = int(input("Enter Choosen Option:"))
                if o not in range(0, len(cus_list) + 1):
                    continue
                else:
                    for i in range(0, len(cus_list)):
                        if o == i + 1:
                            cus = cus_list[i]
                break

            elif Op == 2:
                DealsIn = input("Enter What Customer Deals In:")
                cus_list = SearchByDealsIn(DealsIn, cus_db, cus_cursor)
                if len(cus_list) == 0:
                    print("no values found!! RESTARTING APP!!.......")
                    conn_closed = closeconn(cus_db, cus_cursor)
                    only_non_gui_play()
                for i in range(0, len(cus_list)):
                    if cus_list[i] is not None:
                        name = str(cus_list[i].name)
                        deals = str(cus_list[i].deals)
                        mob1 = str(cus_list[i].mob1)
                        print("Option " + str(
                            i + 1) + "    :    Name = " + name + "    Deals In = " + deals + "    Mobile No. 1 = " + mob1)
                print("other integers to search again")
                o = int(input("Enter Choosen Option:"))
                if o not in range(0, len(cus_list) + 1):
                    continue
                else:
                    for i in range(0, len(cus_list)):
                        if o == i + 1:
                            cus = cus_list[i]
                break
            elif Op == 3:
                Area = input("Enter The Area of deal Of Customer:")
                cus_list = SearchByArea(Area, cus_db, cus_cursor)
                if len(cus_list) == 0:
                    print("no values found!! RESTARTING APP!!.......")
                    conn_closed = closeconn(cus_db, cus_cursor)
                    only_non_gui_play()
                for i in range(0, len(cus_list)):
                    if cus_list[i] is not None:
                        name = str(cus_list[i].name)
                        area = str(cus_list[i].area)
                        mob1 = str(cus_list[i].mob1)
                        print("Option " + str(
                            i + 1) + "    :    Name = " + name + "    Area = " + area + "    Mobile No. 1 = " + mob1)
                print("other integers to search again")
                o = int(input("Enter Choosen Option:"))
                if o not in range(0, len(cus_list) + 1):
                    continue
                else:
                    for i in range(0, len(cus_list)):
                        if o == i + 1:
                            cus = cus_list[i]
                break
            elif Op == 4:
                PinCode = input("Enter The PinCode Of The Customer:")
                cus_list = SearchByPinCode(PinCode, cus_db, cus_cursor)
                if len(cus_list) == 0:
                    print("no values found!! RESTARTING APP!!.......")
                    conn_closed = closeconn(cus_db, cus_cursor)
                    only_non_gui_play()
                for i in range(0, len(cus_list)):
                    if cus_list[i] is not None:
                        name = str(cus_list[i].name)
                        pincode = str(cus_list[i].pincode)
                        mob1 = str(cus_list[i].mob1)
                        print("Option " + str(
                            i + 1) + "    :    Name = " + name + "    Pincode = " + pincode + "    Mobile No. 1 = " + mob1)
                print("other integers to search again")
                o = int(input("Enter Choosen Option:"))
                if o not in range(0, len(cus_list) + 1):
                    continue
                else:
                    for i in range(0, len(cus_list)):
                        if o == i + 1:
                            cus = cus_list[i]
                break
            elif Op == 5:
                Type_Of_Work = input("Enter The Type Of Work Of Customer:")
                cus_list = SearchByTypeOfWork(Type_Of_Work, cus_db, cus_cursor)
                if len(cus_list) == 0:
                    print("no values found!! RESTARTING APP!!.......")
                    conn_closed = closeconn(cus_db, cus_cursor)
                    only_non_gui_play()
                for i in range(0, len(cus_list)):
                    if cus_list[i] is not None:
                        name = str(cus_list[i].name)
                        type_of_work = str(cus_list[i].Type_Of_Work)
                        mob1 = str(cus_list[i].mob1)
                        print("Option " + str(
                            i + 1) + "    :    Name = " + name + "    Type Of Work = " + type_of_work + "Mobile No. 1 = " + mob1)
                print("other integers to search again")
                o = int(input("Enter Choosen Option:"))
                if o not in range(0, len(cus_list) + 1):
                    continue
                else:
                    for i in range(0, len(cus_list)):
                        if o == i + 1:
                            cus = cus_list[i]
                break
            elif Op == 0:
                conn_closed = closeconn(cus_db, cus_cursor)
                only_non_gui_play()
            else:
                print("out of options Plz Try Again")
        while True:
            print("What Do You Want To Do WITH THIS CUSTOMER DETAILS ??")
            print("   1       :    Update any detail")
            print("   2       :    Delete This Customer (NOT REVERSIBLE)")
            print("   0       :    To Go Main Menu")
            Op = int(input("Enter Choosen Option:"))
            if Op == 1:
                print("Enter A DICTIONARY")
                print(
                    "A DICTIONARY is a comma seperated list (Starting and ending with curly bracs'{}') of key:value pairs with ':' in between")
                print(
                    "Start and end with '{}' and use inverted-commas ("") for Keys and also for all string (non-number) Values")
                print("Possible KEYS ARE AS Follows:")
                print("name, email, gstin, type_of_work, deals, mob1, mob2, add, area, pincode, due, next_con_date")
                # add is for address
                print("VALUES should be corresponding to KEYS")
                w = eval(input("Enter DICTIONARY ONLY WITH SPECIFIED KEY:VALUE PAIRS:"))
                print("w = ", w, "type = ", type(w))
                WheterDone = cus.update(cus_db, cus_cursor, **w)
                if WheterDone:
                    break
                else:
                    print("Error in Updating Value Plz Restart The App")
            elif Op == 2:
                print("Are You Sure To Delete this customer with name:", cus.mob1)
                o = input("Reply With 'y' or 'n'")
                if o == "Y" or "y":
                    cus.delete(cus_db, cus_cursor)
                    break
                elif o == "N" or "n":
                    continue
                else:
                    print("out of options!! try again")
            elif Op == 0:
                conn_closed = closeconn(cus_db, cus_cursor)
                only_non_gui_play()
            else:
                print("out of options Plz Try Again")
    elif Option == 3:

        PartOfName = input("Enter The Part Of The Name Of Customer:")
        cus_list = SearchByPartOfName(PartOfName, cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(i + 1) + "    :    Name = " + name + "    Mobile No. 1 = " + mob1)
            print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)

    elif Option == 4:
        do_nothing()
        DealsIn = input("Enter What Customer Deals In:")
        cus_list = SearchByDealsIn(DealsIn, cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                deals = str(cus_list[i].deals)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Deals In = " + deals + "    Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 5:
        do_nothing()
        Area = input("Enter The Area of deal Of Customer:")
        cus_list = SearchByArea(Area, cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                area = str(cus_list[i].area)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Area = " + area + "    Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 6:
        do_nothing()
        PinCode = input("Enter The PinCode Of The Customer:")
        cus_list = SearchByPinCode(PinCode, cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                pincode = str(cus_list[i].pincode)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Pincode = " + pincode + "    Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 7:
        do_nothing()
        Type_Of_Work = input("Enter The Type Of Work Of Customer:")
        cus_list = SearchByTypeOfWork(Type_Of_Work, cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                type_of_work = str(cus_list[i].Type_Of_Work)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Type Of Work = " + type_of_work + "    Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 8:
        do_nothing()
        cus_list = SearchByDueCus(cus_db, cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                due = str(cus_list[i].due)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Due Amount = " + due + "Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 9:
        do_nothing()
        Next_Con_Date = input("Enter The Next Contact Date Of Customer:")
        cus_list = SearchByWhenToContact(Next_Con_Date, cus_db, cus_cursor)
        # cus_list = SearchByWhenToContactToday(cus_db,cus_cursor)
        if len(cus_list) == 0:
            print("no values found!! RESTARTING APP!!.......")
            conn_closed = closeconn(cus_db, cus_cursor)
            only_non_gui_play()
        for i in range(0, len(cus_list)):
            if cus_list[i] is not None:
                name = str(cus_list[i].name)
                next_con_date = str(cus_list[i].next_con_date)
                mob1 = str(cus_list[i].mob1)
                print("Option " + str(
                    i + 1) + "    :    Name = " + name + "    Next Contact Date = " + next_con_date + "    Mobile No. 1 = " + mob1)
        print("other integers to search again")
        while True:
            o = int(input("Enter Choosen Option:"))
            if o not in range(1, len(cus_list) + 1):
                print("Out Of Options Try Again")
                continue
            else:
                for i in range(0, len(cus_list)):
                    op = i + 1
                    if o == op:
                        cus = cus_list[i]
                        break
                    else:
                        continue
                    break
                break
            break
        name = cus.name
        email = cus.email
        gstin = cus.gstin
        type_of_work = cus.Type_Of_Work
        deals = cus.deals
        mob1 = cus.mob1
        mob2 = cus.mob2
        add = cus.add
        area = cus.area
        pincode = cus.pincode
        due = cus.due
        next_con_date = cus.next_con_date
        print("The Customers Details Are Saved As Follows")
        print("name                  =  ", name)
        print("email                 =  ", email)
        print("gstin                 =  ", gstin)
        print("type of work          =  ", type_of_work)
        print("deals in              =  ", deals)
        print("mobile no. 1          =  ", mob1)
        print("mobile no. 2          =  ", mob2)
        print("address               =  ", add)
        print("area                  =  ", area)
        print("pincode               =  ", pincode)
        print("Due Amount            =  ", due)
        print("Next Date To Contact  =  ", next_con_date)
    elif Option == 0:
        connclosed = closeconn(cus_db, cus_cursor)
        if connclosed:
            a = False
        else:
            print("Error in Saving Data . Do You Want To Exit Without Saving??, Reply With y or n")
            b = lower(input())
            if b == "y":
                a = False
            else:
                a = True
    else:
        print("#############################################################")
        do_nothing()
    return a


def only_non_gui_play():
    cus_db = db()
    print("Connected To Customer Database from backend")
    cus_cursor = cursor(cus_db)
    print("Connected To Customer Database from backend for trasactions")
    command = "create table if not exists customer(Name varchar(70) not null,Email_Id varchar(35) unique,GSTIN char(15),Type_Of_Work varchar(50),Deals_In varchar(50),Mobile_No_1 Number(10) primary key,Mobile_No_2 Number(10) unique,Address varchar(150),Area varchar(50)not null,Pin_Code Number(6),Due_Money decimal(4,2),When_To_Contact Date)"
    cus_cursor.execute(command)
    print("Now Table Exits")
    global a
    a = True
    while a:
        a = main(cus_db, cus_cursor)
    conn_closed = closeconn(cus_db, cus_cursor)
    if conn_closed:
        quit()
    else:
        closeanyway = input(
            "Connection To server failed!! All Work Done In This Session May Lose.Do You Want To Close AnyWay??")
        if closeanyway == 'y' or 'Y' or 'yes' or 'Yes' or 'YES':
            quit()
        else:
            only_non_gui_play()


if __name__ == '__main__':
    only_non_gui_play()
