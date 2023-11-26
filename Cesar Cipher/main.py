alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import asciiimage

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if not char in alphabet:
      end_text +=char
    else:
     position = alphabet.index(char)
     new_position = position + shift_amount
     end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")




def main():
  print(asciiimage.logo) 
  decision = "yes"
  while decision== "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
  # What if the user enters a shift that is greater than the number of letters in the alphabet?
    if shift > 26:
      shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    decision =input("Type 'yes' if you wanna go again. Otherwise type 'no'\n")

  print("Bye!")

if __name__ == "__main__":
    main()