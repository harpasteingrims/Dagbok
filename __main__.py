#Þetta er rotarskrain


# Arnar: látið þessa skrá bara heita __main__.py og hafið hana ekki
# í sér möppu heldur í möppunni sem ER raunverulega rótin á verkefninu
# (þeas í möppunni  VERKLEGT-1-verkefni)


from UI_folder.MainmenuUI import MainmenuUI

def main():
    ui = MainmenuUI()
    ui.show_main_menu()

if __name__ == '__main__':
    main()