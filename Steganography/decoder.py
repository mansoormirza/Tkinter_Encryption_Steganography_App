from PIL import Image

def decode(path_2):

    enc_img = Image.open(path_2)

    enc_pixelMap = enc_img.load()

    msg = ""
    msg_index = 0 

    for row in range(enc_img.size[0]):
        for col in range(enc_img.size[1]):

            list = enc_pixelMap[row,col]
            r = list[0]	

            if col==0 and row==0:	
                msg_len = r
                    
            elif msg_len>msg_index:	
                msg =msg+ chr(r)	
                msg_index = msg_index+1

    enc_img.close()

    print('Decoded: ',(msg))

    return msg
  