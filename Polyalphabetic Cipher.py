import math
import time
import random

encrypt_letter_to_num = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"'":26,",":27,".":28,"?":29,"/":30," ":31}
encrypt_num_to_letter = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",26:"'",27:",",28:".",29:"?",30:"/",31:" "}

while True:
    en_de = ""
    en_de = input("Would you like to encrypt a message or decrypt a message?[e/d]: ").lower()
 
    if en_de == "e":
        displacement_word = input("Please enter your displacement word: ")
        main_body = (input("Please input your message, all cases will be changed to lower: ")).lower()

        new_word = ""

        displacement_list = []
        for x in displacement_word:
            displacement_list.append(encrypt_letter_to_num[x])

        displacement_list_position_count = 0
     
        for x in main_body:
            if displacement_list_position_count == len(displacement_list):
                displacement_list_position_count = 0
            old_value = encrypt_letter_to_num[x]
            new_value = old_value + displacement_list[displacement_list_position_count]
            while new_value > 31:
                new_value -= 32
            new_word += encrypt_num_to_letter[new_value]
            displacement_list_position_count += 1

        print(new_word)



    if en_de == "d":
        displacement_word = input("Please enter your displacement word: ")
        main_body = (input("Please input your message, all cases will be changed to lower: ")).lower()

        new_word = ""

        displacement_list = []
        for x in displacement_word:
            displacement_list.append(encrypt_letter_to_num[x])

        displacement_list_position_count = 0
     
        for x in main_body:
            if displacement_list_position_count == len(displacement_list):
                displacement_list_position_count = 0
            old_value = encrypt_letter_to_num[x]
            new_value = old_value - displacement_list[displacement_list_position_count]
            while new_value < 0:
                new_value += 32
            new_word += encrypt_num_to_letter[new_value]
            displacement_list_position_count += 1

        print(new_word)