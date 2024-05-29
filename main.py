import tkinter as tk
from tkinter import filedialog
from AES_Encryption.aes_encrypt import encrypt
from AES_Encryption.aes_decrypt import decrypt
from Steganography.encoder import encode
from Steganography.decoder import decode

def show_encryption_page():
    main_frame.pack_forget()
    encryption_frame.pack(fill=tk.BOTH, expand=True)

def show_decryption_page():
    main_frame.pack_forget()
    decryption_frame.pack(fill=tk.BOTH, expand=True)

def go_back_to_main():
    encryption_frame.pack_forget()
    decryption_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)

def encrypt_message():
    global encrypted_text, PassPhrase
    message = message_entry.get()
    PassPhrase = passphrase_entry.get()

    if len(PassPhrase) < 16:
        PassPhrase = PassPhrase.ljust(16, '0')
        print(PassPhrase)
    elif len(PassPhrase) > 16:
        print("Your passphrase was larger than 16 characters. Truncating passphrase.")
        PassPhrase = PassPhrase[:16]

    print(PassPhrase)

    encrypted_text = encrypt(message, PassPhrase)
    encrypted_output.config(state=tk.NORMAL)
    encrypted_output.delete("1.0", tk.END)
    encrypted_output.insert(tk.END, encrypted_text)
    encrypted_output.config(state=tk.DISABLED)

def select_cover_image():
    global path_1
    path_1 = filedialog.askopenfilename()
    cover_image_entry.delete(0, tk.END)
    cover_image_entry.insert(0, path_1)

def process_cover_image():
    global encoded_image
    encoded_image = encode(path_1, encrypted_text)
    print("Image encoded")

def select_encrypted_image():
    global path_2
    path_2 = filedialog.askopenfilename()
    encrypted_image_entry.delete(0, tk.END)
    encrypted_image_entry.insert(0, path_2)

def input_new_passphrase():
    global new_passphrase

    new_passphrase = input_passphrase_entry.get()
    # if len(new_passphrase) < 16:
    #     new_passphrase = new_passphrase.ljust(16, '0')
    # elif len(new_passphrase) > 16:
    #     print("Your passphrase was larger than 16 characters. Truncating passphrase.")
    #     new_passphrase = new_passphrase[:16]

    return new_passphrase

def process_encrypted_image():
    NewPass = input_new_passphrase()
    extracted_encrypted_text = decode(path_2)
    decrypted_text = decrypt(extracted_encrypted_text, NewPass)
    decrypted_output.config(state=tk.NORMAL)
    decrypted_output.delete("1.0", tk.END)
    decrypted_output.insert(tk.END, decrypted_text)
    print(decrypted_text)
    decrypted_output.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("AES Encryption and Decryption")
root.geometry("600x400")

def create_poppins_font(size, weight='', style=''):
    return ('Poppins', size, weight, style)

poppins_font = create_poppins_font(12, weight='bold')


# Main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

encryption_button = tk.Button(main_frame, text="ENCRYPTION", command=show_encryption_page, bg="#656569", fg="white", borderwidth=2, width=13, height=2, font=(poppins_font, 11, "bold"))
encryption_button.pack(pady=10)
decryption_button = tk.Button(main_frame, text="DECRYPTION", command=show_decryption_page, bg="#656569", fg="white", borderwidth=2, width=13, height=2, font=(poppins_font, 11, "bold"))
decryption_button.pack(pady=10)

# Encryption frame
encryption_frame = tk.Frame(root)

back_button_encryption = tk.Button(encryption_frame, text="Back", command=go_back_to_main,  bg="#656569", fg="white", borderwidth=2, width=10, height=1, font=(poppins_font, 11))
back_button_encryption.pack(anchor='w', padx=10, pady=5)

message_label = tk.Label(encryption_frame, text="Enter message to encrypt")
message_label.pack()

message_entry = tk.Entry(encryption_frame, width=50, bd=3)
message_entry.pack()
tk.Label(encryption_frame, text="").pack()  # Space

passphrase_label = tk.Label(encryption_frame, text="Enter 16-character Key")
passphrase_label.pack()

passphrase_entry = tk.Entry(encryption_frame, width=50, bd=3,show='*')
passphrase_entry.pack()
tk.Label(encryption_frame, text="").pack()  # Space

encrypt_button = tk.Button(encryption_frame, text="Encrypt Message", command=encrypt_message, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
encrypt_button.pack(pady=8)

encrypted_output = tk.Text(encryption_frame, height=3, width=50, state=tk.DISABLED, bd=3)
encrypted_output.pack()
tk.Label(encryption_frame, text="").pack()  # Space

cover_image_label = tk.Label(encryption_frame, text="Select Cover Image to hide encrypted text in it's pixel")
cover_image_label.pack()

cover_image_entry = tk.Entry(encryption_frame, width=50, bd=3)
cover_image_entry.pack()

select_cover_image_button = tk.Button(encryption_frame, text="Select Image", command=select_cover_image, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
select_cover_image_button.pack(pady=8)

process_cover_image_button = tk.Button(encryption_frame, text="Process", command=process_cover_image, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
process_cover_image_button.pack()
tk.Label(encryption_frame, text="").pack()  # Space

# Decryption frame
decryption_frame = tk.Frame(root)

back_button_decryption = tk.Button(decryption_frame, text="Back", command=go_back_to_main, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
back_button_decryption.pack(anchor='w', padx=10, pady=5)

encrypted_image_label = tk.Label(decryption_frame, text="Select Encrypted Cover Image to extract encrypted text")
encrypted_image_label.pack()

encrypted_image_entry = tk.Entry(decryption_frame, width=50, bd=3)
encrypted_image_entry.pack(pady=8)

select_encrypted_image_button = tk.Button(decryption_frame, text="Select Image", command=select_encrypted_image, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
select_encrypted_image_button.pack()
tk.Label(decryption_frame, text="").pack()  # Space

input_passphrase_label = tk.Label(decryption_frame, text="Enter New 16-character Key")
input_passphrase_label.pack()

input_passphrase_entry = tk.Entry(decryption_frame, width=50, bd=3, show='*')
input_passphrase_entry.pack(pady=5)

input_passphrase_button = tk.Button(decryption_frame, text="Use Key", command=input_new_passphrase, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
input_passphrase_button.pack(pady=12)

process_encrypted_image_button = tk.Button(decryption_frame, text="Process Decryption", command=process_encrypted_image, bg="#656569", fg="white", borderwidth=2, height=1, font=(poppins_font, 10))
process_encrypted_image_button.pack(pady=10)

decrypted_output = tk.Text(decryption_frame, height=5, width=50, state=tk.DISABLED, bd=3)
decrypted_output.pack()

# Start the GUI main loop
root.mainloop()
