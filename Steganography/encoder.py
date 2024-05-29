from PIL import Image

def encode(path, msg):
    # Creating a image object
    # org_img = Image.open('Steganography/Image-Steganography-hiding-text-inside-image-using-python/original_image.png')
    org_img = Image.open(path)


    # Loading pixel values of original image, each entry is pixel value ie., RGB values as sublist
    org_pixelMap = org_img.load()

    # Creating new image object with image mode and dimensions as that of original image
    enc_img = Image.new( org_img.mode, org_img.size)
    enc_pixelsMap = enc_img.load()

    msg_index=0

    # Finding the lenght of message
    msg_len=len(msg)

    # Traversing through the pixel values
    for row in range(org_img.size[0]):
        for col in range(org_img.size[1]):

        # Fetching RGB value a pixel to sublist
            list=org_pixelMap[row,col] 
            r=list[0] 	# R value
            g=list[1]	# G value
            b=list[2]	# B value
        
            if row==0 and col==0:		# 1st pixel is used to store the lenght of message
                ascii=msg_len
                enc_pixelsMap[row,col] = (ascii,g,b)
            elif msg_index<=msg_len:	# Hiding our message inside the R values of the pixels
                c=msg[msg_index-1]
                ascii=ord(c)
                enc_pixelsMap[row,col] = (ascii,g,b)
            else:				# Assigning the pixel values of old image to new image
                enc_pixelsMap[row,col] = (r,g,b)
            msg_index+=1

    org_img.close()

    # Display the image
    enc_img.show()  

    enc_path = "Steganography/encrypted_image.png" 

    enc_img.save(enc_path) 
    enc_img.close()

    return enc_path
