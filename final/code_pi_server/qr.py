from imutils.video import VideoStream

from pyzbar import pyzbar

import datetime
import imutils
import time
import cv2

vs = VideoStream(usePiCamera = True).start()
time.sleep(2)

found = set()
arrived = {}
chrono_start = time.time()

billboard = open("billboard.txt", "w")    
billboard.close()

while True :
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    barcodes = pyzbar.decode(frame)

    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
        # if the barcode text is currently not in our 
        # the timestamp + barcode to disk and update the set
        if barcodeData not in found:
            found.add(barcodeData)
        if barcodeData not in arrived.keys():
            arrived[barcodeData] = time.time()-chrono_start
            print(barcodeData + " : " + str(arrived[barcodeData]))
            billboard = open("billboard.txt", "a")
            billboard.write(barcodeData + " : " + str(arrived[barcodeData])+"\n")
            billboard.close()
    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()


