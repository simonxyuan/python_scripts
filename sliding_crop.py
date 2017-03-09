import sys, os
import Image
import cv2
import numpy as np
import glob

crop_width = 64
save_route = '/home/xingfang/Documents/Dataset/4K_frames_patch/'
filelist = sorted(glob.glob("/home/xingfang/Documents/Dataset/4K_frames/*.png"))
label_route = '/home/xingfang/Documents/Dataset/4K_frames_label/'

for imagePath in filelist:
    img = cv2.imread(imagePath)

    print img.shape
    (imgHeight, imgWidth, channels) = img.shape

    labelList = []

    patchCount = 1
    startCount = 1
    #totalPatch = (imgHeight/(crop_width/4)-3)*(imgWidth/(crop_width/4)-3)
    #for x in range(0, imgHeight - crop_width * 3 / 4, crop_width/4):
    #    for y in range(0, imgWidth - crop_width * 3 / 4, crop_width/4):
    totalPatch = (imgHeight/(crop_width/2-1))*(imgWidth/(crop_width/2)-1)
    for x in range(0, imgHeight - crop_width / 2, crop_width/2):
        for y in range(0, imgWidth - crop_width /2, crop_width/2):
            if patchCount < startCount:
                patchCount += 1
            else:
                print 'Patch No. ' + str(patchCount) + '/' + str(totalPatch)
                patch = img[x : x + crop_width, y : y + crop_width]
                tempImg = img.copy()
                cv2.rectangle(tempImg, (y, x), (y + crop_width, x + crop_width), (255, 0, 0), 5)
                #cv2.rectangle(tempImg, (100,100), (500,500), (255,0,0), 5)
                tempImg = cv2.resize(tempImg,  None, fx = 0.3, fy = 0.3)
                cv2.imshow('Image: ' + imagePath, tempImg)
                cv2.imshow('Patch', patch)

                #cv2.imshow('control',control)
                if patchCount % 100 == 1: 
                    print 'Classes List:\n Hair, Metal, GLass, TRee, GRass, FLower,\nSkiN, Letter, SkY, ClouD, CloudSky, SOil,\nAsphalt, Water, SAnd, TAtami, Rock, FAbric\nOr Delete' 
                
                label = 'unknown'
                keyList = (ord('h'), ord('m'), ord('l'), ord('g'), ord('t'), ord('f'), \
                        ord('s'), ord('c'), ord('a'), ord('w'), ord('r'), ord('d')) 
                key1 = None

                while key1 not in keyList:
                    key1 = cv2.waitKey(0) & 255
                    if key1 == ord('h'):
                        label = 'hair'
                    elif key1 == ord('m'):
                        label = 'metal'
                    elif key1 == ord('g'):
                        print 'L for glass, R for grass'
                        key2 = cv2.waitKey(0) & 255
                        if key2 == ord('l'):
                            label = 'glass'
                        elif key2 == ord('r'):
                            label = 'grass'
                    elif key1 == ord('t'):
                        print 'R for tree, A for tatami'
                        key2 = cv2.waitKey(0) & 255
                        if key2 == ord('r'):
                            label = 'tree'
                        elif key2 == ord('a'):
                            label = 'tatami'
                    elif key1 == ord('f'):
                        print 'L for flower, A for fabric'
                        key2 = cv2.waitKey(0) & 255
                        if key2 == ord('l'):
                            label = 'flower'
                        elif key2 == ord('a'):
                            label = 'fabric'
                    elif key1 == ord('s'):
                        print 'N for skin, Y for sky, O for Soil, A for sand'
                        key2 = cv2.waitKey(0) & 255
                        if key2 == ord('n'):
                            label = 'skin'
                        elif key2 == ord('y'):
                            label = 'sky'
                        elif key2 == ord('o'):
                            label = 'soil'
                        elif key2 == ord('a'):
                            label = 'sand'
                    elif key1 == ord('l'):
                        label = 'letter'
                    elif key1 == ord('c'):
                        print 'S for cloudsky, D for cloud'
                        key2 = cv2.waitKey(0) & 255
                        if key2 == ord('s'):
                            label = 'cloudsky'
                        elif key2 == ord('d'):
                            label = 'cloud'
                    elif key1 == ord('a'):
                        label = 'asphalt'
                    elif key1 == ord('w'):
                        label = 'water'
                    elif key1 == ord('r'):
                        label = 'rock'
                    elif key1 == ord('d'):
                        label = 'null'
                    else:
                        print 'Wrong Command? Try Again'
                boxPos = [x, y, x+crop_width, y+crop_width]
                fullLabel = [label, boxPos, patchCount]
                labelList.append(fullLabel)
                print 'Class:' + label + '\n\n'
                imageName = imagePath.rsplit('/',1)[-1].split('.')[0]
                save_path = save_route + label + '/' + imageName + '_' + str(patchCount) + '.png'
                #print save_path
                if not os.path.exists(os.path.dirname(save_path)):
                    try:
                        os.makedirs(os.path.dirname(save_path))
                    except OSError as exc:
                        if exc.errno != errno.EEXIST:
                            raise
                 
                cv2.imwrite(save_path, patch)
                patchCount += 1

    labelFile = open(label_route + imageName + '.txt', 'w')
    print labelList
    for item in labelList:
        print>>labelFile, item[2], item[0], item[1]
    labelFile.close()
                 
    cv2.destroyAllWindows()
    os.remove(imagePath)

