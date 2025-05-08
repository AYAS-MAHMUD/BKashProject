print("bkash")
print("1.Send Money") #done
print("2.Send Money to Non-bkash User") #done
print("3.Mobile Recharge") #done
print("4.Payment") #done
print("5.Cash Out") #done
print("6.Pay Bill")
print("7.Microfinance")
print("8.Downlodoad bkash App")
print("9.My bkash")
print("10.Resets PIN")
pin=12345 #password
print("\n")
a=int(input("Enter the number :"))
print("\n")
if a==1:
    number=int(input("Enter Receiver bKash Account No:"))  #if the bkash number lenth up/down 11 ->Invalid number
    print("FREE Send Money to 5 Priyo Numbers. ")
    print("Dial *247# and select number 9 to find priyo Numbers.")
    taka=int(input("Enter Amount:"))
    print("FREE Send Money to 5 Priyo Numbers up to 25,000 TK. every month. ")
    r=int(input("Enter Reference:"))
    print("\n")
    print("Add up to 5 Priyo Numbers to Send Money for FREE.")
    print("Send Money.")
    print("To:",number)
    print("Amount: TK ",taka)
    print("Reference:",r)
    
    p=int(input("Enter Menu PIN to confirm: "))
    if p==pin:
        print("THANK YOU...You request has been Processed")
    else:
        print("Invalid PIN")
    #back=input("If you want to back Homepage click (y):")


elif a==2:
    number=int(input("Enter Receiver Number:"))
    amount=int(input("Enter Amount:"))
    ref=int(input("Enter Reference:"))
    print("\n")
    print("Send Money to Non-bKash User")
    print("To:",number)
    print("Amount: Tk ",amount)
    print("Reference:",ref)
    p=int(input("Enter Menu PIN to comfirm:"))
    if p==pin:
        print("THANK YOU...You request has been Processed")
    else:
        print("Invalid PIN")

elif a==3:
    print("bKash")
    print("1.Robi") #done
    print("2.Airtel") #done
    print("3.Banglalink") #done
    print("4.Grameenphone")
    print("5.Teletalk")
    print("6.Get instant cashback on bKash Recharge")
    print("0.Main Menu") #if write 0, go to homepage
    print("\n")
    e=int(input("Enter number: "))
    print("\n")
    if e==1:
        print("bKash")
        print("1.Prepaid")
        print("2.Postpaid")
        print("3.Auto-recharge")
        print("4.Best Offers")
        print("5.Internet packs")
        print("6.Voice packs")
        print("7.Bundle packs")
        print("0.Main Menu")
        print("\n")
        c=int(input("Enter number: "))
        print("\n")
        if c==1:
            mob=int(input("Enter Robi Mobile No:"))
            print("9Tk Cashback+198mins for 7Days on 119Tk Recharge")
            tk=int(input("Enter Recharge Amount:"))
            print("Mobile Recharge")
            print("To:",mob)
            print("Amount:Tk ",tk)
            p=int(input("Enter Menu PIN to confirm: "))
            if p==pin:
                 print("THANK YOU...You request has been Processed")
            else:
                print("Invalid PIN")
    elif e==2:
        print("bKash")
        print("1.Prepaid")
        print("2.Postpaid")
        print("3.Auto-recharge")
        print("4.Best Offers")
        print("5.Internet packs")
        print("6.Voice packs")
        print("7.Bundle packs")
        print("0.Main Menu")
        print("\n")
        c=int(input("Enter number: "))
        print("\n")
        if c==1:
            mob=int(input("Enter Airtel Mobile No:"))
            print("7TkCashback+215mins for 10Days on 129Tk Recharge")
            tk=int(input("Enter Recharge Amount:"))
            print("\n")
            print("Mobile Recharge")
            print("To:",mob)
            print("Amount: Tk ",tk)
            print("to know if the amount is for recharge offer, contact mobile operator")
            p=int(input("Enter Menu PIN to comfirm:"))
            if p==pin:
                print("THANK YOU...You request has been Processed")
            else:
                print("Invalid PIN")
    elif e==3:
        print("bKash")
        print("1.Prepaid")
        print("2.Postpaid")
        print("3.Auto-recharge")
        print("4.Best Offers(Prepaid)")
        print("5.Internet packs")
        print("6.Voice packs")
        print("7.Bundle packs")
        print("0.Main Menu")
        print("\n")
        c=int(input("Enter number: "))
        print("\n")
        if c==1:
            mob=int(input("Enter Banglalink Mobile No:"))
            print("20TkCashback on 275Tk Recharge")
            tk=int(input("Enter Recharge Amount:"))
            print("\n")
            print("Mobile Recharge")
            print("To:",mob)
            print("Amount: Tk ",tk)
            print("to know if the amount is for recharge offer, contact mobile operator")
            p=int(input("Enter Menu PIN to comfirm:"))
            if p==pin:
                print("THANK YOU...You request has been Processed")
            else:
                print("Invalid PIN")
    elif e==4:
        print("bKash")
        print("1.Prepaid")
        print("2.Postpaid")
        print("3.Auto-recharge")
        print("4.Best Offers(Prepaid)")
        print("5.Internet packs")
        print("6.Voice packs")
        print("7.Bundle packs")
        print("0.Main Menu")
        print("\n")
        c=int(input("Enter number: "))
        print("\n")
        if c==1:
            mob=int(input("Enter Grameenphone Mobile No:"))
            print("2TkCashback on 200 Min 7 Days-129Tk Recharge")
            tk=int(input("Enter Recharge Amount:"))
            print("\n")
            print("Mobile Recharge")
            print("To:",mob)
            print("Amount: Tk ",tk)
            print("to know if the amount is for recharge offer, contact mobile operator")
            p=int(input("Enter Menu PIN to comfirm:"))
            if p==pin:
                print("THANK YOU...You request has been Processed")
            else:
                print("Invalid PIN")
    elif e==5:
        print("bKash")
        print("1.Prepaid")
        print("2.Postpaid")
        print("0.Main Menu")
        print("\n")
        c=int(input("Enter number: "))
        print("\n")
        if c==1:
            mob=int(input("Enter Teletalk Mobile No:"))
            print("Cash Out at 1.49% from 2 Priyo Agent numbers up to 50,000 Tk every month.")
            tk=int(input("Enter Recharge Amount:"))
            print("\n")
            print("Mobile Recharge")
            print("To:",mob)
            print("Amount: Tk ",tk)
            print("to know if the amount is for recharge offer, contact mobile operator")
            p=int(input("Enter Menu PIN to comfirm:"))
            if p==pin:
                print("THANK YOU...You request has been Processed")
            else:
                print("Invalid PIN")
elif a==4:
    pay=int(input("Enter Merchant bKash Account No:"))
    tk=int(input("Enter Amount:"))
    ref=int(input("Enter Reference:"))
    print("\n")
    print("Payment.")
    print("To:",pay)
    print("Amount: Tk ",tk)
    print("Reference: ",ref)
    p=int(input("Enter Menu PIN to confirm:"))
    if p==pin:
        print("THANK YOU...You request has been Processed")
    else:
        print("Invalid PIN")
elif a==5:
    print("bKash")
    print("1.From Agent")
    print("2.From ATM")
    
    print("3.Priyo Agent Numbers")
    print("4.Set up to 2 Priyo Agent Numbers to Cash Out at 1.49%")
    print("5.Other Cash Out charge and Balance")
    print("0.Main Menu")
    print("\n")
    e=int(input("Enter number:"))
    print("\n")
    if e==1:
        print("Cash out at 1.49% by adding up to 2 Priyo Agent Numbers.")
        print("Dial *247# select option 9 then select option 4")
        no=int(input("Enter Agent bKash Account No:"))
        print("\n")
        print("Cash Out at 1.49% from 2 Priyo Agent Numbers up to 50.000 Tk every month.")
        print("Dial *247# select option 9 then select option 4")
        tk=int(input("Enter Amount:"))
        print("\n")
        print("Cash Out at at 1.49% by adding up to 2 Priyo Agent Numbers.")
        print("Cash Out")
        print("To:",no)
        print("Amount: Tk ",tk)
        p=int(input("Enter Menu PIN to confirm:"))
        if p==pin:
            print("THANK YOU...You request has been Processed")
        else:
            print("Invalid PIN")
    
        





        



