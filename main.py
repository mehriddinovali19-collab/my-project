from sys import exit

from utils import print_menu, print_error_menu

from handler import (handle_add_products_h, handle_check_status_h,  handle_show_product_h,
                      handle_show_details_h, handle_show_numbers_h, handle_search_product_h,
                      handle_delete_product_h, handle_price_product_h,  handle_all_category_product_h)



def main() -> None :
    while True:
        print_menu()

        option = input("> ")
        if option == "1":
            handle_add_products_h()
        elif option == "2":
            handle_check_status_h()
        elif option == "3":
             handle_show_product_h()
        elif option == "4":
            handle_show_details_h()
        elif option == "5":
            handle_show_numbers_h()
        elif option == "6":
            handle_search_product_h()
        elif option == "7":
            handle_delete_product_h()
        elif option == "8":
            handle_price_product_h()
        elif option == "9":
             handle_all_category_product_h()
        elif option == "0":
            exit()
        else:
            print_error_menu


main()



            






