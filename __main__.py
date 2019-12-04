#Þetta er rotarskrain


# Arnar: látið þessa skrá bara heita __main__.py og hafið hana ekki
# í sér möppu heldur í möppunni sem ER raunverulega rótin á verkefninu
# (þeas í möppunni  VERKLEGT-1-verkefni)


from UI_folder.MainmenuUI import MainmenuUI

def main():
    ui = UIMGR()
    ui.run()
    #búum til eitt fall í mananger sem er þá run og þar verður self.

if __name__ == '__main__':
    main()