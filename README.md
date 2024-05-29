# AES Encryption/Decryption & Steganography Application 

Launch the application by running the main.py file as 'python main.py' after installing required packages mentioned in requirements.txt file.
The main window titled "AES Encryption and Decryption" will appear.

**Encryption Process:**

Click on the "ENCRYPTION" button to start the encryption process.
You will be taken to the Encryption page.
Enter the message you want to encrypt in the "Enter message to encrypt" field.
Enter a 16-character key in the "Enter 16-character Key" field. If your key is shorter than 16 characters, it will be padded automatically. If it's longer, it will be truncated.
Click the "Encrypt Message" button to encrypt the entered message using the provided key.
The encrypted text will be displayed in the "Encrypted Output" area.
Then select a cover image by clicking the "Select Image" button next to the "Select Cover Image" field for hiding text in the image pixel as part of steganography process.
Click the "Process" button to hide the encrypted text in the selected cover image.

**Decryption Process:**

Click on the "DECRYPTION" button to switch to the Decryption page.
You will be taken to the Decryption page.
Select the encrypted cover image by clicking the "Select Image" button next to the "Select Encrypted Cover Image" field.
Enter the new 16-character key in the "Enter New 16-character Key" field.
Click the "Use Key" button to use the entered key  and click process decryption button to decrypt the text hidden in the selected image using the provided key.
The decrypted text will be displayed in the "Decrypted Output" area.
utton located at the top-left corner of each page.
