import cv2
import random
import dropbox

def takeImage():
    k=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        name="Picture"+str(k)+".jpg"
        cv2.imwrite(name,frame)
        result = False
    return name
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def uploadImage(file):
    dropbox_access_token= "sl.A6dAo-ehuukTM_U0P0X4j82-q0zm9fuwOEzykc-B-0OttKkGQ5D1ed_xMoKWlZfDJXLKBFe7-icSLcYAbD1UEvJvmcvFawLI78IkvFQh12H8KgQpWDWD4iIP_dxKo8DrqN1tsr9bjpI"    #Enter your own access token
    dropbox_path= "/abc/"+file
    computer_path=file
    client = dropbox.Dropbox(dropbox_access_token)
    print("[SUCCESS] dropbox account linked")
    client.files_upload(open(computer_path, "rb").read(), dropbox_path)
    print("[UPLOADED] {}".format(computer_path))

while(True):
    image=takeImage()
    uploadImage(image)