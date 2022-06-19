import os, sys, requests
from decimal import Decimal
from termcolor import colored
if not os.path.isfile("coins/BTC.price"):
    create = open("coins/BTC.price","w+")
    create.write("0")
    create.close()
    create = open("coins/ETH.price","w+")
    create.write("0")
    create.close()
    create = open("coins/LRC.price","w+")
    create.write("0")
    create.close()
    create = open("coins/IMX.price","w+")
    create.write("0")
    create.close()
    create = open("coins/DOGE.price","w+")
    create.write("0")
    create.close()
    create = open("coins/XRP.price","w+")
    create.write("0")
    create.close()
    create = open("coins/ADA.price","w+")
    create.write("0")
    create.close()
    create = open("coins/BNB.price","w+")
    create.write("0")
    create.close()
    create = open("coins/DAI.price","w+")
    create.write("0")
    create.close()
    create = open("coins/SOL.price","w+")
    create.write("0")
    create.close()
def loop_get():
    btc_key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    eth_key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    lrc_key = "https://api.binance.com/api/v3/ticker/price?symbol=LRCUSDT"
    imx_key = "https://api.binance.com/api/v3/ticker/price?symbol=IMXUSDT"
    doge_key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"
    xrp_key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    ada_key = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
    bnb_key = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    dai_key = "https://api.binance.com/api/v3/ticker/price?symbol=DAIUSDT"
    sol_key = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
    btc_data = requests.get(btc_key)  
    btc_data = btc_data.json()
    btc_data['price'] = Decimal(btc_data['price']).normalize()
    eth_data = requests.get(eth_key)  
    eth_data = eth_data.json()
    eth_data['price'] = Decimal(eth_data['price']).normalize()
    lrc_data = requests.get(lrc_key)  
    lrc_data = lrc_data.json()
    lrc_data['price'] = Decimal(lrc_data['price']).normalize()
    imx_data = requests.get(imx_key)  
    imx_data = imx_data.json()
    imx_data['price'] = Decimal(imx_data['price']).normalize()
    doge_data = requests.get(doge_key)  
    doge_data = doge_data.json()
    doge_data['price'] = Decimal(doge_data['price']).normalize()
    xrp_data = requests.get(xrp_key)  
    xrp_data = xrp_data.json()
    xrp_data['price'] = Decimal(xrp_data['price']).normalize()
    ada_data = requests.get(ada_key)  
    ada_data = ada_data.json()
    ada_data['price'] = Decimal(ada_data['price']).normalize()
    bnb_data = requests.get(bnb_key)  
    bnb_data = bnb_data.json()
    bnb_data['price'] = Decimal(bnb_data['price']).normalize()
    dai_data = requests.get(dai_key)  
    dai_data = dai_data.json()
    dai_data['price'] = Decimal(dai_data['price']).normalize()
    sol_data = requests.get(sol_key)  
    sol_data = sol_data.json()
    sol_data['price'] = Decimal(sol_data['price']).normalize()
    btc_data['price'] = str(btc_data['price'])
    eth_data['price'] = str(eth_data['price'])
    lrc_data['price'] = str(lrc_data['price'])
    imx_data['price'] = str(imx_data['price'])
    doge_data['price'] = str(doge_data['price'])
    xrp_data['price'] = str(xrp_data['price'])
    ada_data['price'] = str(ada_data['price'])
    bnb_data['price'] = str(bnb_data['price'])
    dai_data['price'] = str(dai_data['price'])
    sol_data['price'] = str(sol_data['price'])
    btc_read = open("coins/BTC.price","r")
    old_btc = btc_read.read()
    old_btc = float(old_btc)
    btc_read.close()
    eth_read = open("coins/ETH.price","r")
    old_eth = eth_read.read()
    old_eth = float(old_eth)
    eth_read.close()
    lrc_read = open("coins/LRC.price","r")
    old_lrc = lrc_read.read()
    old_lrc = float(old_lrc)
    lrc_read.close()
    imx_read = open("coins/IMX.price","r")
    old_imx = imx_read.read()
    old_imx = float(old_imx)
    imx_read.close()
    doge_read = open("coins/DOGE.price","r")
    old_doge = doge_read.read()
    old_doge = float(old_doge)
    doge_read.close()
    xrp_read = open("coins/XRP.price","r")
    old_xrp = xrp_read.read()
    old_xrp = float(old_xrp)
    xrp_read.close()
    ada_read = open("coins/ADA.price","r")
    old_ada = ada_read.read()
    old_ada = float(old_ada)
    ada_read.close()
    bnb_read = open("coins/BNB.price","r")
    old_bnb = bnb_read.read()
    old_bnb = float(old_bnb)
    bnb_read.close()
    dai_read = open("coins/DAI.price","r")
    old_dai = dai_read.read()
    old_dai = float(old_dai)
    dai_read.close()
    sol_read = open("coins/SOL.price","r")
    old_sol = sol_read.read()
    old_sol = float(old_sol)
    sol_read.close()
    btc_cryp_data = open("coins/BTC.price","w+")
    eth_cryp_data = open("coins/ETH.price","w+")
    lrc_cryp_data = open("coins/LRC.price","w+")
    imx_cryp_data = open("coins/IMX.price","w+")
    doge_cryp_data = open("coins/DOGE.price","w+")
    xrp_cryp_data = open("coins/XRP.price","w+")
    ada_cryp_data = open("coins/ADA.price","w+")
    bnb_cryp_data = open("coins/BNB.price","w+")
    dai_cryp_data = open("coins/DAI.price","w+")
    sol_cryp_data = open("coins/SOL.price","w+")
    btc_cryp_data.write(btc_data['price'])
    eth_cryp_data.write(eth_data['price'])
    lrc_cryp_data.write(lrc_data['price'])
    imx_cryp_data.write(imx_data['price'])
    doge_cryp_data.write(doge_data['price'])
    xrp_cryp_data.write(xrp_data['price'])
    ada_cryp_data.write(ada_data['price'])
    bnb_cryp_data.write(bnb_data['price'])
    dai_cryp_data.write(dai_data['price'])
    sol_cryp_data.write(sol_data['price'])
    btc_cryp_data.close()
    eth_cryp_data.close()
    lrc_cryp_data.close()
    imx_cryp_data.close()
    doge_cryp_data.close()
    xrp_cryp_data.close()
    ada_cryp_data.close()
    bnb_cryp_data.close()
    dai_cryp_data.close()
    sol_cryp_data.close()
    new_btc = float(btc_data['price'])
    new_eth = float(eth_data['price'])
    new_lrc = float(lrc_data['price'])
    new_imx = float(imx_data['price'])
    new_doge = float(doge_data['price'])
    new_xrp = float(xrp_data['price'])
    new_ada = float(ada_data['price'])
    new_bnb = float(bnb_data['price'])
    new_dai = float(dai_data['price'])
    new_sol = float(sol_data['price'])
    btc_red = True
    eth_red = True
    lrc_red = True
    imx_red = True
    doge_red = True
    xrp_red = True
    ada_red = True
    bnb_red = True
    dai_red = True
    sol_red = True
    cyan_mark = 0
    os.system('cls')
    if old_btc > new_btc:
        btc_red = True
        print(colored("[BTC]\t","blue") +colored(f"{new_btc}","green") +colored(f" - {round(old_btc-new_btc,2)}","red"))
    else:
        if old_btc < new_btc:
            btc_red = False
            print(colored("[BTC]\t","blue") +colored(f"{new_btc} ","red")+colored(f"+ {round(new_btc-old_btc,2)}","green"))
        else:
            if old_btc == new_btc:
                btc_red = True
                cyan_mark += 1
                print(colored("[BTC]\t","blue")+colored(f"{new_btc}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[BTC] Loading...","blue"))
    if old_eth > new_eth:
        eth_red = True
        print(colored("[ETH]\t","blue")+colored(f"{new_eth}","green")+colored(f" - {round(old_eth-new_eth,2)}","red"))
    else:
        if old_eth < new_eth:
            etj_red = False
            print(colored("[ETH]\t","blue")+colored(f"{new_eth}","red")+colored(f" + {round(new_eth-old_eth,2)}","green"))
        else:
            if old_eth == new_eth:
                eth_red = True
                cyan_mark += 1
                print(colored("[ETH]\t","blue")+colored(f"{new_eth}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[ETH] Loading...","blue"))
    if old_lrc > new_lrc:
        lrc_red = True
        print(colored("[LRC]\t","blue")+colored(f"{new_lrc}","green")+colored(f" - {round(old_lrc-new_lrc,3)}","red"))
    else:
        if old_lrc < new_lrc:
            lrc_red = False
            print(colored("[LRC]\t","blue")+colored(f"{new_lrc}","red")+colored(f" + {round(new_lrc-old_lrc,3)}","green"))
        else:
            if old_lrc == new_lrc:
                lrc_red = True
                cyan_mark += 1
                print(colored("[LRC]\t","blue")+colored(f"{new_lrc}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[LRC] Loading...","blue"))
    if old_imx > new_imx:
        imx_red = True
        print(colored("[IMX]\t","blue")+colored(f"{new_imx}","green")+colored(f" - {round(old_imx-new_imx,3)}","red"))
    else:
        if old_imx < new_imx:
            imx_red = False
            print(colored("[IMX]\t","blue")+colored(f"{new_imx}","red")+colored(f" + {round(new_imx-old_imx,3)}","green"))
        else:
            if old_imx == new_imx:
                imx_red = True
                cyan_mark += 1
                print(colored("[IMX]\t","blue")+colored(f"{new_imx}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[IMX] Loading...","blue"))
    if old_doge > new_doge:
        doge_red = True
        print(colored("[DOGE]\t","blue")+colored(f"{new_doge}","green")+colored(f" - {round(old_doge-new_doge,3)}","red"))
    else:
        if old_doge < new_doge:
            doge_red = False
            print(colored("[DOGE]\t","blue")+colored(f"{new_doge}","red")+colored(f" + {round(new_doge-old_doge,3)}","green"))
        else:
            if old_doge == new_doge:
                doge_red = True
                cyan_mark += 1
                print(colored("[DOGE]\t","blue")+colored(f"{new_doge}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[DOGE] Loading...","blue"))
    if old_xrp > new_xrp:
        xrp_red = True
        print(colored("[XRP]\t","blue")+colored(f"{new_xrp}","green")+colored(f" - {round(old_xrp-new_xrp,3)}","red"))
    else:
        if old_xrp < new_xrp:
            xrp_red = False
            print(colored("[XRP]\t","blue")+colored(f"{new_xrp}","red")+colored(f" + {round(new_xrp-old_xrp,3)}","green"))
        else:
            if old_xrp == new_xrp:
                xrp_red = True
                cyan_mark += 1
                print(colored("[XRP]\t","blue")+colored(f"{new_xrp}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[XRP] Loading...","blue"))
    if old_ada > new_ada:
        ada_red = True
        print(colored("[ADA]\t","blue")+colored(f"{new_ada}","green")+colored(f" - {round(old_ada-new_ada,3)}","red"))   
    else:
        if old_ada < new_ada:
            ada_red = False
            print(colored("[ADA]\t","blue")+colored(f"{new_ada}","red")+colored(f" + {round(new_ada-old_ada,3)}","green"))
        else:
            if old_ada == new_ada:
                ada_red = True
                cyan_mark += 1
                print(colored("[ADA]\t","blue")+colored(f"{new_ada}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[ADA] Loading...","blue"))
    if old_bnb > new_bnb:
        bnb_red = True
        print(colored("[BNB]\t","blue")+colored(f"{new_bnb}","green")+colored(f" - {round(old_bnb-new_bnb,3)}","red"))   
    else:
        if old_bnb < new_bnb:
            bnb_red = False
            print(colored("[BNB]\t","blue")+colored(f"{new_bnb}","red")+colored(f" + {round(new_bnb-old_bnb,3)}","green"))
        else:
            if old_bnb == new_bnb:
                bnb_red = True
                cyan_mark += 1
                print(colored("[BNB]\t","blue")+colored(f"{new_bnb}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[BNB] Loading...","blue"))
    if old_dai > new_dai:
        dai_red = True
        print(colored("[DAI]\t","blue")+colored(f"{new_dai}","green")+colored(f" - {round(old_dai-new_dai,3)}","red"))   
    else:
        if old_dai < new_dai:
            dai_red = False
            print(colored("[DAI]\t","blue")+colored(f"{new_dai}","red")+colored(f" + {round(new_dai-old_dai,3)}","green"))
        else:
            if old_dai == new_dai:
                dai_red = True
                cyan_mark += 1
                print(colored("[DAI]\t","blue")+colored(f"{new_dai}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[DAI] Loading...","blue"))
    if old_sol > new_sol:
        sol_red = True
        print(colored("[SOL]\t","blue")+colored(f"{new_sol}","green")+colored(f" - {round(old_sol-new_sol,3)}","red"))
    else:
        if old_sol < new_sol:
            sol_red = False
            print(colored("[SOL]\t","blue")+colored(f"{new_sol}","red")+colored(f" + {round(new_sol-old_sol,3)}","green"))
        else:
            if old_sol == new_sol:
                sol_red = True
                cyan_mark += 1
                print(colored("[SOL]\t","blue")+colored(f"{new_sol}","cyan")+"  "+colored("+","green")+colored("/","white")+colored("-","red")+colored("  0","cyan"))
            else:
                print(colored("[SOL] Loading...","blue"))
    red_cryp = sum([btc_red, eth_red, lrc_red, imx_red, doge_red, xrp_red, ada_red, bnb_red, dai_red, sol_red])
    red_cryp = red_cryp - cyan_mark
    green_cryp = 10-red_cryp-cyan_mark
    print(colored(f"\nRed\t-    {red_cryp}","red"))
    print(colored(f"Green\t-    {green_cryp}","green"))
    print(colored(f"Cyan\t-    {cyan_mark}","cyan"))
    loop_get()
sys.setrecursionlimit(999999999)
print("[BTC]\tLoading...")
print("[ETH]\tLoading...")
print("[LRC]\tLoading...")
print("[IMX]\tLoading...")
print("[DOGE]\tLoading...")
print("[XRP]\tLoading...")
print("[ADA]\tLoading...")
print("[BNB]\tLoading...")
print("[DAI]\tLoading...")
print("[SOL]\tLoading...")
print("\nRed\t-    Loading...")
print("Green\t-    Loading...")
print("Cyan\t-    Loading...")
loop_get()