#Þetta er rotarskrain


# Arnar: látið þessa skrá bara heita __main__.py og hafið hana ekki
# í sér möppu heldur í möppunni sem ER raunverulega rótin á verkefninu
# (þeas í möppunni  VERKLEGT-1-verkefni)


from UI_folder.UImanager import UImanager

def main():
    ui = UImanager()
    ui.MainmenuUI()
    #búum til eitt fall í mananger sem er þá run og þar verður self.

if __name__ == '__main__':
    main()