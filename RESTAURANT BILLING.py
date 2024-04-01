from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog
def total_bills():

        # ============ Drinks Items price ===============
        lassi_price = 25
        coffee_price = 20
        tea_price = 10
        juice_price = 30
        shakes_price = 50
        milk_price = 10
        sweatbeer_price = 35
        redbull_price = 150
        # ============== Foods Items Price ==================
        roti_price = 10
        chicken_biryani_price = 120
        mutton_panner_price = 150
        parotta_price = 40
        mix_veg_price = 70
        omelete_price = 20
        veg_biryani_price = 120
        rice_price = 50


        # ============Drinks Item quantity ===================
        lassi_q = lassi_qty.get()
        coffee_q = coffee_qty.get()
        tea_q = tea_qty.get()
        juice_q = juice_qty.get()
        shakes_q = shakes_qty.get()
        milk_q = milk_qty.get()
        sweatbeer_q = sweatbeer_qty.get()
        redbull_q = redbull_qty.get()

        # ============= Foods Item quantity ======================
        roti_q = roti_qty.get()
        chicken_biryani_q = chicken_biryani_qty.get()
        mutton_panner_q = mutton_panner_qty.get()
        parotta_q = parotta_qty.get()
        mix_veg_q = mix_veg_qty.get()
        omelete_q = omelete_qty.get()
        veg_biryani_q = veg_biryani_qty.get()
        rice_q = rice_qty.get()


        # ================ Drinks Items Validation ====================
        if lassi_var.get() == 0:
                lassi_q = 0
        elif lassi_var.get() == 1 and lassi_qty.get() == "":
                messagebox.showerror("error","please fill the lassi quantity")
                lassi_q = 0

        if coffee_var.get() == 0:
                coffee_q = 0
        elif coffee_var.get() == 1 and coffee_qty.get() == "":
                messagebox.showerror("error","please fill the coffee quantity")
                coffee_q = 0

        if tea_var.get() == 0:
                tea_q = 0
        elif tea_var.get() == 1 and tea_qty.get() == "":
                messagebox.showerror("error","please fill the tea quantity")
                tea_q = 0

        if juice_var.get() == 0:
                juice_q = 0
        elif juice_var.get() == 1 and juice_qty.get() == "":
                messagebox.showerror("error","please fill the juice quantity")
                juice_q = 0

        if shakes_var.get() == 0:
                shakes_q = 0
        elif shakes_var.get() == 1 and shakes_qty.get() == "":
                messagebox.showerror("error","please fill the shakes quantity")
                shakes_q = 0

        if milk_var.get() == 0:
                milk_q = 0
        elif milk_var.get() == 1 and milk_qty.get() == "":
                messagebox.showerror("error","please fill the milk quantity")
                milk_q = 0

        if sweatbeer_var.get() == 0:
                sweatbeer_q = 0
        elif sweatbeer_var.get() == 1 and sweatbeer_qty.get() == "":
                messagebox.showerror("error","please fill the sweatbeer quantity")
                sweatbeer_q = 0

        if redbull_var.get() == 0:
                redbull_q = 0
        elif redbull_var.get() == 1 and redbull_qty.get() == "":
                messagebox.showerror("error","please fill the redbull quantity")
                redbull_q = 0

        
        # ================ Foods Items Validation ====================
        if roti_var.get() == 0:
                roti_q = 0
        elif roti_var.get() == 1 and roti_qty.get() == "":
                messagebox.showerror("error","please fill the Roti quantity")
                roti_q = 0

        if chicken_biryani_var.get() == 0:
                chicken_biryani_q = 0
        elif chicken_biryani_var.get() == 1 and chicken_biryani_qty.get() == "":
                messagebox.showerror("error","please fill the chicken biryani quantity")
                chicken_biryani_q = 0

        if mutton_panner_var.get() == 0:
                mutton_panner_q = 0
        elif mutton_panner_var.get() == 1 and mutton_panner_qty.get() == "":
                messagebox.showerror("error","please fill the Mutter panner quantity")
                mutter_panner_q = 0

        if parotta_var.get() == 0:
                parotta_q = 0
        elif parotta_var.get() == 1 and parotta_qty.get() == "":
                messagebox.showerror("error","please fill the Parotta quantity")
                parotta_q = 0

        if mix_veg_var.get() == 0:
                mix_veg_q = 0
        elif mix_veg_var.get() == 1 and mix_veg_qty.get() == "":
                messagebox.showerror("error","please fill the Mix Veg quantity")
                mix_veg_q = 0

        if omelete_var.get() == 0:
               omelete_q = 0
        elif omelete_var.get() == 1 and omelete_qty.get() == "":
                messagebox.showerror("error","please fill the Omelete quantity")
                omelete_q = 0

        if veg_biryani_var.get() == 0:
                veg_biryani_q = 0
        elif veg_biryani_var.get() == 1 and veg_biryani_qty.get() == "":
                messagebox.showerror("error","please fill the Veg Biryani quantity")
                veg_biryani_q = 0

        if rice_var.get() == 0:
                rice_q = 0
        elif rice_var.get() == 1 and rice_qty.get() == "":
                messagebox.showerror("error","please fill the Rice quantity")
                rice_q = 0
        
        
        # ============ Total Drinks Items Price ===================
        total_lassi_price = lassi_price * int(lassi_q)
        total_coffee_price = coffee_price * int(coffee_q)
        total_tea_price = tea_price * int(tea_q)
        total_juice_price = juice_price * int(juice_q)
        total_shakes_price = shakes_price * int(shakes_q)
        total_milk_price = milk_price * int(milk_q)
        total_sweatbeer_price = sweatbeer_price * int(sweatbeer_q)
        total_redbull_price = redbull_price * int(redbull_q)

        # ============ Total Drinks cost ===================
        total_drinks_cost = total_lassi_price + total_coffee_price + total_tea_price + total_juice_price + total_shakes_price + total_milk_price + total_sweatbeer_price + total_redbull_price

        if drinks_cost.get() != "":
                drinks_cost.delete(0,"end")
                drinks_cost.insert("end",total_drinks_cost)
        else:
                drinks_cost.insert("end",total_drinks_cost)

        
        # ============ Total Foods Items Price ===================
        total_roti_price = roti_price * int(roti_q)
        total_chicken_biryani_price = chicken_biryani_price * int(chicken_biryani_q)
        total_mutton_panner_price = mutton_panner_price * int(mutton_panner_q)
        total_parotta_price = parotta_price * int(parotta_q)
        total_mix_veg_price = mix_veg_price * int(mix_veg_q)
        total_omelete_price = omelete_price * int(omelete_q)
        total_veg_biryani_price = veg_biryani_price * int(veg_biryani_q)
        total_rice_price = rice_price * int(rice_q)

         # ============ Total Foods cost ===================
        total_foods_cost = total_roti_price + total_chicken_biryani_price + total_mutton_panner_price + total_parotta_price + total_mix_veg_price + total_omelete_price + total_veg_biryani_price + total_rice_price

        if foods_cost.get() != "":
                foods_cost.delete(0,"end")
                foods_cost.insert("end",total_foods_cost)
        else:
                foods_cost.insert("end",total_foods_cost)

        
        if service_charge_cost.get() != "":
                service_charge_cost.delete(0,"end")
                service_charge_cost.insert(0,"10")
        else:
                service_charge_cost.insert(0,"10")
        
        fc =  int(foods_cost.get())
        dc = int(drinks_cost.get())

        total_paid_tax = fc+dc
        total_paid_tax = total_paid_tax * 8 / 100


        if paid_tax_cost != "":
                paid_tax_cost.delete(0,"end")
                paid_tax_cost.insert(0,total_paid_tax)
        else:
                paid_tax_cost.insert(0,total_paid_tax)

        
        total_sub_cost = fc+dc+int(service_charge_cost.get())

        if sub_total_cost.get() != "":
                sub_total_cost.delete(0,"end")
                sub_total_cost.insert(0,total_sub_cost)
        else:
                sub_total_cost.insert(0,total_sub_cost)


        if total_cost_cost.get() != "":
                total_cost_cost.delete(0,"end")
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))
        else:
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))

        

         # =====================  Total Bill Receipt ===========================
        date = datetime.now().date()
        if bill_details.get(1.0,"end") != "":
                bill_details.delete(1.0,"end")
                bill_details.insert(1.0,f" Billno-{random.randint(100,1000)}\t{date}  =====================  Items(q) \t \tAmount  ===================== \n {'Lassi ('+str(lassi_q) + ')' + '         ' + str(int(lassi_q) * lassi_price) + '   '  if lassi_var.get() == 1 else''}{'coffee ('+str(coffee_q) + ')' + '        ' + str(int(coffee_q) * coffee_price) + '  '  if coffee_var.get() == 1 else ''}{ ' tea ('+str(tea_q) + ')' + '           ' + str(int(tea_q) * tea_price) + '  '  if tea_var.get() == 1 else''}{' juice ('+str(juice_q) + ')' + '         ' + str(int(juice_q) * juice_price) + '   '  if juice_var.get() == 1 else''}{'shakes('+str(shakes_q) + ')' + '         ' + str(int(shakes_q) * shakes_price) + '   '  if shakes_var.get() == 1 else''}{'milk('+str(milk_q) + ')' + '           ' + str(int(milk_q) * milk_price) + '   '  if milk_var.get() == 1 else''}{'sweatbeer('+str(sweatbeer_q) + ')' + '     ' + str(int(sweatbeer_q) * sweatbeer_price) + '     '  if sweatbeer_var.get() == 1 else''}{'redbull('+str(redbull_q) + ')' + '     ' + str(int(redbull_q) * redbull_price) + '     '  if redbull_var.get() == 1 else''}{'roti('+str(roti_q) + ')' + '          ' + str(int(roti_q) * roti_price) + '     '  if roti_var.get() == 1 else''}{'chicken biryani('+str(chicken_biryani_q) + ')' + '     ' + str(int(chicken_biryani_q) * chicken_biryani_price) + '  '  if chicken_biryani_var.get() == 1 else''}{'mutton panner('+str(mutton_panner_q) + ')' + '  ' + str(int(mutton_panner_q) * mutton_panner_price) + '  '  if mutton_panner_var.get() == 1 else''}{'parotta('+str(parotta_q) + ')' + '        ' + str(int(parotta_q) * parotta_price) + '   '  if parotta_var.get() == 1 else''}{'mix veg('+str(mix_veg_q) + ')' + '        ' + str(int(mix_veg_q) * mix_veg_price) + '   '  if mix_veg_var.get() == 1 else''}{'omelete('+str(omelete_q) + ')' + '        ' + str(int(omelete_q) * omelete_price) + '   '  if omelete_var.get() == 1 else''}{'veg biryani('+str(veg_biryani_q) + ')' + '    ' + str(int(veg_biryani_q) * veg_biryani_price) + '  '  if veg_biryani_var.get() == 1 else''}{'rice('+str(rice_q) + ')' + '          ' + str(int(rice_q) * rice_price) + '    '  if rice_var.get() == 1 else''}service charge    {service_charge_cost.get()}\n tax paid        {paid_tax_cost.get()}\n ===================== \n total          {total_cost_cost.get()}\n =====================")
        
                
        

# ========= Save button Code ================

def save():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetypes=[("pdf","*.pdf"),("text","*.txt")])
        if root.filename is None:
                return
        file_save =  str(bill_details.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()
        

# ============= Drinks checkbutton validation =================
def lassi_chk():
        if lassi_var.get() == 1:
                lassi_qty['state'] = "normal"
                lassi_qty['bg'] = '#248aa2'
                lassi_qty['fg'] = "white"
                
        else:
                lassi_qty['state'] = "disabled"


def coffee_chk():
        if coffee_var.get() == 1:
                coffee_qty['state'] = "normal"
                coffee_qty['bg'] = '#248aa2'
                coffee_qty['fg'] = "white"
        else:
                coffee_qty['state'] = "disabled"

def tea_chk():
        if tea_var.get() == 1:
                tea_qty['state'] = "normal"
                tea_qty['bg'] = '#248aa2'
                tea_qty['fg'] = "white"
        else:
                tea_qty['state'] = "disabled"

def juice_chk():
        if juice_var.get() == 1:
                juice_qty['state'] = "normal"
                juice_qty['bg'] = '#248aa2'
                juice_qty['fg'] = "white"
        else:
                juice_qty['state'] = "disabled"

def shakes_chk():
        if shakes_var.get() == 1:
                shakes_qty['state'] = "normal"
                shakes_qty['bg'] = '#248aa2'
                shakes_qty['fg'] = "white"
        else:
                shakes_qty['state'] = "disabled"

def milk_chk():
        if milk_var.get() == 1:
                milk_qty['state'] = "normal"
                milk_qty['bg'] = '#248aa2'
                milk_qty['fg'] = "white"
        else:
                milk_qty['state'] = "disabled"

def sweatbeer_chk():
        if sweatbeer_var.get() == 1:
                sweatbeer_qty['state'] = "normal"
                sweatbeer_qty['bg'] = '#248aa2'
                sweatbeer_qty['fg'] = "white"
        else:
                sweatbeer_qty['state'] = "disabled"

def redbull_chk():
        if redbull_var.get() == 1:
                redbull_qty['state'] = "normal"
                redbull_qty['bg'] = '#248aa2'
                redbull_qty['fg'] = "white"
        else:
                redbull_qty['state'] = "disabled"



# === Foods checkbutton validation ================

def roti_chk():
        if roti_var.get() == 1:
                roti_qty['state'] = "normal"
                roti_qty['bg'] = '#248aa2'
                roti_qty['fg'] = "white"
                
        else:
                roti_qty['state'] = "disabled"

def chicken_biryani_chk():
        if chicken_biryani_var.get() == 1:
                chicken_biryani_qty['state'] = "normal"
                chicken_biryani_qty['bg'] = '#248aa2'
                chicken_biryani_qty['fg'] = "white"
        else:
               chicken_biryani_qty['state'] = "disabled"

def mutton_panner_chk():
        if mutton_panner_var.get() == 1:
                mutton_panner_qty['state'] = "normal"
                mutton_panner_qty['bg'] = '#248aa2'
                mutton_panner_qty['fg'] = "white"
        else:
                mutton_panner_qty['state'] = "disabled"

def parotta_chk():
        if parotta_var.get() == 1:
                parotta_qty['state'] = "normal"
                parotta_qty['bg'] = '#248aa2'
                parotta_qty['fg'] = "white"
        else:
                parotta_qty['state'] = "disabled"

def mix_veg_chk():
        if mix_veg_var.get() == 1:
                mix_veg_qty['state'] = "normal"
                mix_veg_qty['bg'] = '#248aa2'
                mix_veg_qty['fg'] = "white"
        else:
                mix_veg_qty['state'] = "disabled"

def omelete_chk():
        if omelete_var.get() == 1:
                omelete_qty['state'] = "normal"
                omelete_qty['bg'] = '#248aa2'
                omelete_qty['fg'] = "white"
        else:
                omelete_qty['state'] = "disabled"

def veg_biryani_chk():
        if veg_biryani_var.get() == 1:
                veg_biryani_qty['state'] = "normal"
                veg_biryani_qty['bg'] = '#248aa2'
                veg_biryani_qty['fg'] = "white"
        else:
                veg_biryani_qty['state'] = "disabled"

def rice_chk():
        if rice_var.get() == 1:
                rice_qty['state'] = "normal"
                rice_qty['bg'] = '#248aa2'
                rice_qty['fg'] = "white"
        else:
                rice_qty['state'] = "disabled"


# ===== Calculator code ================

def nine():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","9")
        else:
                result.insert("end","9")
                
            

def eight():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","8")
        else:
                result.insert("end","8")

def seven():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","7")
        else:
                result.insert("end","7")

def six():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","6")
        else:
                result.insert("end","6")

def five():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","5")
        else:
                result.insert("end","5")

def four():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","4")
        else:
                result.insert("end","4")

def three():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","3")
        else:
                result.insert("end","3")

def two():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","2")
        else:
                result.insert("end","2")

def one():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","1")
        else:
                result.insert("end","1")

def zero():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","0")
        else:
                result.insert("end","0")

def plus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","+")
        else:
                result.insert("end","+")

def minus():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","-")
        else:
                result.insert("end","-")

def mul():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","*")
        else:
                result.insert("end","*")

def divide():
        if 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")
                result.insert("end","/")
        else:
                result.insert("end","/")

def equal():


        if result.get() == "":
                result.insert("end","error")
        elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get()[0] == "/":
                result.delete(0,"end")
                result.insert("end","error")
        elif 'error' in result.get() or '=' in result.get():
                result.delete(0,"end")


        else:
                res = result.get()
                res = eval(res)
                result.insert("end"," = ")
                result.insert("end",res)

def clear():
        result.delete(0,"end")

# ==== Exit button code =================
def exit():
        message = messagebox.askquestion('Notepad',"Do you want to exit the application")
        if message == "yes":
                root.destroy()
        else:
                "return"

# ==== clear button code ============
def cleared_bill():
        # ========== Drinks ===========
        lassi_qty.delete(0,'end')
        lassi.deselect()
        lassi_qty['state'] = "disabled"
        coffee_qty.delete(0,'end')
        coffee.deselect()
        coffee_qty['state'] = "disabled"
        tea_qty.delete(0,'end')
        tea.deselect()
        tea_qty['state'] = "disabled"
        juice_qty.delete(0,'end')
        juice.deselect()
        juice_qty['state'] = "disabled"
        shakes_qty.delete(0,'end')
        shakes.deselect()
        shakes_qty['state'] = "disabled"
        milk_qty.delete(0,'end')
        milk.deselect()
        milk_qty['state'] = "disabled"
        sweatbeer_qty.delete(0,'end')
        sweatbeer.deselect()
        sweatbeer_qty['state'] = "disabled"
        redbull_qty.delete(0,'end')
        redbull.deselect()
        redbull_qty['state'] = "disabled"
        # ========== Drinks ===========
        roti_qty.delete(0,'end')
        roti.deselect()
        roti_qty['state'] = "disabled"
        chicken_biryani_qty.delete(0,'end')
        chicken_biryani.deselect()
        chicken_biryani_qty['state'] = "disabled"
        mutton_panner_qty.delete(0,'end')
        mutton_panner.deselect()
        mutton_panner_qty['state'] = "disabled"
        parotta_qty.delete(0,'end')
        parotta.deselect()
        parotta_qty['state'] = "disabled"
        mix_veg_qty.delete(0,'end')
        mix_veg.deselect()
        mix_veg_qty['state'] = "disabled"
        omelete_qty.delete(0,'end')
        omelete.deselect()
        omelete_qty['state'] = "disabled"
        veg_biryani_qty.delete(0,'end')
        veg_biryani.deselect()
        veg_biryani_qty['state'] = "disabled"
        rice_qty.delete(0,'end')
        rice.deselect()
        rice_qty['state'] = "disabled"
        # ========== Total cost ===========
        drinks_cost.delete(0,'end')
        foods_cost.delete(0,'end')
        service_charge_cost.delete(0,'end')
        paid_tax_cost.delete(0,'end')
        sub_total_cost.delete(0,'end')
        total_cost_cost.delete(0,'end')
        # ========== Bill Details ============
        bill_details.delete(1.0,'end')
# ===== Main Window code =================
root = tk.Tk()
root.geometry('650x500')
root.maxsize(650,490)
root.minsize(650,490)
root.title("Restaurent Management System")

frame = Frame(root,width=650,height=70,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame.place(x=0,y=0)

l1 = Label(frame,text="Restaurent Management System",font=('roboto',30,'bold'),bg='#248aa2',fg="#ffffff")
l1.place(x=10,y=4)

frame1= Frame(root,width=450,height=230,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1,width=150,height=220,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe1.place(x=0,y=0)

drinks  = LabelFrame(innerframe1,text="Drinks",width=135,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
drinks.place(x=2,y=2)



lassi_var = IntVar()
lassi = Checkbutton(drinks,text="Lassi",variable=lassi_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=lassi_chk)
lassi.place(x=2,y=2)

lassi_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state='disabled')
lassi_qty.place(x=74,y=2)
lassi_qty.insert(0,"0")

coffee_var = IntVar()
coffee = Checkbutton(drinks,text="Coffee",variable=coffee_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=coffee_chk)
coffee.place(x=2,y=22)

coffee_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
coffee_qty.place(x=74,y=22)

tea_var = IntVar()
tea = Checkbutton(drinks,text="Tea",variable=tea_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=tea_chk)
tea.place(x=2,y=44)
tea_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
tea_qty.place(x=74,y=44)

juice_var = IntVar()
juice = Checkbutton(drinks,text="Juice",variable=juice_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=juice_chk)
juice.place(x=2,y=66)
juice_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
juice_qty.place(x=74,y=66)

shakes_var = IntVar()
shakes = Checkbutton(drinks,text="Shakes",variable=shakes_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
shakes_qty.place(x=74,y=88)

milk_var = IntVar()
milk = Checkbutton(drinks,text="Milk",variable=milk_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=milk_chk)
milk.place(x=2,y=110)
milk_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
milk_qty.place(x=74,y=110)

sweatbeer_var = IntVar()
sweatbeer = Checkbutton(drinks,text="Sweatbeer",variable=sweatbeer_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=sweatbeer_chk)
sweatbeer.place(x=2,y=132)
sweatbeer_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
sweatbeer_qty.place(x=74,y=132)

redbull_var = IntVar()
redbull = Checkbutton(drinks,text="Redbull",variable=redbull_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=redbull_chk)
redbull.place(x=2,y=154)
redbull_qty = Entry(drinks,width=7,borderwidth=4,relief=SUNKEN,state="disabled")
redbull_qty.place(x=74,y=154)


innerframe2 = Frame(frame1,width=290,height=220,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe2.place(x=151,y=0)


foods  = LabelFrame(innerframe2,text="Foods",width=275,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#248aa2',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
foods.place(x=2,y=2)

roti_var = IntVar()
roti = Checkbutton(foods,text="Roti",variable=roti_var,font=('verdana',8,'bold'),command=roti_chk)
roti.place(x=2,y=2)
roti_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
roti_qty.place(x=140,y=2)

chicken_biryani_var = IntVar()
chicken_biryani = Checkbutton(foods,text="chicken biryani",variable=chicken_biryani_var,font=('verdana',8,'bold'),command=chicken_biryani_chk)
chicken_biryani.place(x=2,y=22)
chicken_biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
chicken_biryani_qty.place(x=140,y=22)

mutton_panner_var = IntVar()
mutton_panner = Checkbutton(foods,text="Mutton Panner",variable=mutton_panner_var,font=('verdana',8,'bold'),command=mutton_panner_chk)
mutton_panner.place(x=2,y=44)
mutton_panner_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
mutton_panner_qty.place(x=140,y=44)

parotta_var = IntVar()
parotta = Checkbutton(foods,text="Parotta",variable=parotta_var,font=('verdana',8,'bold'),command=parotta_chk)
parotta.place(x=2,y=66)
parotta_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
parotta_qty.place(x=140,y=66)

mix_veg_var = IntVar()
mix_veg = Checkbutton(foods,text="Mix Veg",variable=mix_veg_var,font=('verdana',8,'bold'),command=mix_veg_chk)
mix_veg.place(x=2,y=88)
mix_veg_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
mix_veg_qty.place(x=140,y=88)

omelete_var = IntVar()
omelete = Checkbutton(foods,text="Omelete",variable=omelete_var,font=('verdana',8,'bold'),command=omelete_chk)
omelete.place(x=2,y=110)
omelete_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
omelete_qty.place(x=140,y=110)

veg_biryani_var = IntVar()
veg_biryani = Checkbutton(foods,text="Veg Biryani",variable=veg_biryani_var,font=('verdana',8,'bold'),command=veg_biryani_chk)
veg_biryani.place(x=2,y=132)
veg_biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
veg_biryani_qty.place(x=140,y=132)

rice_var = IntVar()
rice = Checkbutton(foods,text="Rice",variable=rice_var,font=('verdana',8,'bold'),command=rice_chk)
rice.place(x=2,y=154)
rice_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
rice_qty.place(x=140,y=154)





# =================================================================

frame2= Frame(root,width=450,height=90,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame2.place(x=0,y=300)

innerframe3 = Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe3.place(x=0,y=0)


cost_of_drinks = Label(innerframe3,text="Cost of Drinks",font=('verdana',8,'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods = Label(innerframe3,text="Cost of Foods",font=('verdana',8,'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
foods_cost.place(x=130,y=22)

service_charge = Label(innerframe3,text="Service Charge",font=('verdana',8,'bold'))
service_charge.place(x=2,y=46)
service_charge_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
service_charge_cost.place(x=130,y=44)


paid_tax = Label(innerframe3,text="Paid Tax",font=('verdana',8,'bold'))
paid_tax.place(x=250,y=2)
paid_tax_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
paid_tax_cost.place(x=330,y=0)

sub_total = Label(innerframe3,text="Sub Total",font=('verdana',8,'bold'))
sub_total.place(x=250,y=24)
sub_total_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total_cost.place(x=330,y=22)

total_cost = Label(innerframe3,text="Total Cost",font=('verdana',8,'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_cost_cost.place(x=330,y=44)


#============================================================================
frame3= Frame(root,width=200,height=320,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame3.place(x=450,y=70)

innerframe4 = Frame(frame3,width=190,height=310,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe4.place(x=0,y=0)


result = Entry(innerframe4,width=28,relief=SUNKEN,borderwidth=3)
result.place(x=2,y=0)

nine = Button(innerframe4,text="9",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=nine)
nine.place(x=0,y=24)
eight = Button(innerframe4,text="8",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=eight)
eight.place(x=48,y=24)
seven = Button(innerframe4,text="7",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=seven)
seven.place(x=96,y=24)
plus = Button(innerframe4,text="+",padx=6,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=plus)
plus.place(x=144,y=24)


six = Button(innerframe4,text="6",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=six)
six.place(x=0,y=50)
five = Button(innerframe4,text="5",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=five)
five.place(x=48,y=50)
four = Button(innerframe4,text="4",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=four)
four.place(x=96,y=50)
minus = Button(innerframe4,text="-",padx=8,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=minus)
minus.place(x=144,y=50)

three = Button(innerframe4,text="3",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=three)
three.place(x=0,y=76)
two = Button(innerframe4,text="2",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=two)
two.place(x=48,y=76)
one = Button(innerframe4,text="1",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=one)
one.place(x=96,y=76)
multiply = Button(innerframe4,text="*",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=mul)
multiply.place(x=144,y=76)

zero = Button(innerframe4,text="0",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=zero)
zero.place(x=0,y=102)
clear = Button(innerframe4,text="C",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=clear)
clear.place(x=48,y=102)
equal = Button(innerframe4,text="=",padx=15,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='#248aa2',fg="white",command=equal)
equal.place(x=96,y=102)
divide = Button(innerframe4,text="/",padx=7,relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='white',fg="black",command=divide)
divide.place(x=144,y=102)


bill_details = ScrolledText(innerframe4,width=23,height=9,relief=SUNKEN,borderwidth=3,font=('courier',9,''))
bill_details.place(x=0,y=130)


total = Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=total_bills)
total.place(x=0,y=275)

save = Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=save)
save.place(x=43,y=275)

exit = Button(innerframe4,text="Exit",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=exit)
exit.place(x=82,y=275)

clr = Button(innerframe4,text="ClearAll",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="white",command=cleared_bill)
clr.place(x=124,y=275)

root.mainloop()
