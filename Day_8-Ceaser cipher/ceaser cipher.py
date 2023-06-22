from art import logo

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

run=True
print(logo)
print("Welcome to Ceaser Cipher!!")

while  run:
    def cipher(org_string,to_perform):
        num=0
        cipher_text=""
        if to_perform=="encode":
            num=int(input("Enter number of shifts: "))
            # encoder(input_string)
            for position in range (0,len(org_string)):
                if org_string[position] in alphabet:
                    cipher_text += alphabet[(alphabet.index(org_string[position])+ num) % 26]
                else:
                    cipher_text+= org_string[position]

            print(cipher_text)
        else:
            num=int(input("Enter number of shifts: "))
            for position in range (0, len(org_string)):
                if org_string[position] in alphabet:
                    cipher_text += alphabet[(alphabet.index(org_string[position])- num) % 26]
                else:
                    cipher_text+= org_string[position]

            print(cipher_text)

    str=input("Do you want to encode or decode? ").lower()
    input_string=input(f"Enter string for {str}: ").lower()
    cipher(input_string,str)
    decision=input("Do you want to continue, type'Yes' or'No': ").lower()
    if decision!="yes":
        run=False