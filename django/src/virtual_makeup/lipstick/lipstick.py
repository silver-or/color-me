import sys
import os
import dlib
import glob
import cv2
from skimage import io
from skimage import color
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from pylab import *

from color import Red

class Lipstick():
    def __init__(self) -> None:
        self.r, self.g, self.b = Red.spring()
        self.up_left_end = 4
        self.up_right_end = 7
        self.in_left_end = 3
        self.in_right_end = 7

        self.lower_left_end = 5
        self.upper_left_end = 11
        self.lower_right_end = 16
        self.upper_right_end = 22

        self.inten = 0.8

        self.x = None
        self.y = None
        self.alpha = None
        self.val = None

        self.im = None
        self.im2 = None

        self.img = np.array(imread("../../img/test1.jpg"))

    @staticmethod
    def inter(lx, ly, k1='quadratic'):
        unew = np.arange(lx[0], lx[-1] + 1, 1)
        f2 = interp1d(lx, ly, kind=k1)
        return f2, unew

    @staticmethod
    def getpoint(img):
        predictor_path = "../../data/shape_predictor_68_face_landmarks.dat"
        points = []
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_path)
        x = []
        y = []
        dets = detector(img, 1)
        for k, d in enumerate(dets):
            shape = predictor(img, d)
            print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                    shape.part(1)))
            i = 0
            for pt in shape.parts():
                i = i + 1
                x.append(pt.x)
                y.append(pt.y)
            for i in range(0, len(x) - 1):
                if i >= 48 and i <= 59:
                    pos = (x[i], y[i])
                    points.append(pos)
            pos = (x[48], y[48])
            points.append(pos)
            for i in range(0, len(x) - 1):
                if i >= 60 and i <= 67:
                    pos = (x[i], y[i])
                    points.append(pos)
                    if i == 64:
                        pos = (x[54], y[54])
                        points.append(pos)
            pos = (x[67], y[67])
            points.append(pos)
        return points   


    def apply_getpoint(self):
        inter = self.inter
        up_right_end = self.up_right_end
        in_right_end = self.in_right_end

        img = self.img
        points = self.getpoint(img)
        points=np.array(points)
        point_out_x = np.array((points[:12][:, 0]))
        point_out_y = np.array(points[:12][:, 1])
        point_in_x = np.array(points[12:][:, 0])
        point_in_y = np.array(points[12:][:, 1])

        self.im = img.copy()
        self.im2 = img.copy()


        o_l = self.inter([point_out_x[0]] + point_out_x[up_right_end - 1:][::-1].tolist(),
                    [point_out_y[0]] + point_out_y[up_right_end - 1:][::-1].tolist(), 'quadratic')
        o_u = inter( point_out_x[:up_right_end][::-1].tolist(),
                    point_out_y[:up_right_end][::-1].tolist(), 'quadratic')

        i_u = inter( point_in_x[:in_right_end][::-1].tolist(),
                    point_in_y[:in_right_end][::-1].tolist(), 'quadratic')
        i_l = inter([point_in_x[0]] + point_in_x[in_right_end - 1:][::-1].tolist(),
                    [point_in_y[0]] + point_in_y[in_right_end - 1:][::-1].tolist(), 'quadratic')
        self.x = []  # will contain the x coordinates of points on lips
        self.y = []  # will contain the y coordinates of points on lips

        for i in range(int(point_in_x[0]),int(point_in_x[6])):
        #   k = k + 1
            for j in range(int(o_u[0](i)),int(i_u[0](i))):
                self.x.append(j)
                self.y.append(i)
            for j in range(int(i_l[0](i)), int(o_l[0](i))):
                self.x.append(j)
                self.y.append(i)

        for i in range(int(point_out_x[0]),int(point_in_x[0])):
            for j in range(int(o_u[0](i)),int(o_l[0](i))):
                self.x.append(j)
                self.y.append(i)

        for i in range(int(point_in_x[6]),int(point_out_x[6])):
            for j in range(int(o_u[0](i)),int(o_l[0](i))):
                self.x.append(j)
                self.y.append(i)

    def change_rgb(self):
        inten = self.inten
        # Change RGB color
        self.val = color.rgb2lab((self.im[self.x, self.y] / 255.).reshape(len(self.x), 1, 3)).reshape(len(self.x), 3)
        L, A, B = mean(self.val[:, 0]), mean(self.val[:, 1]), mean(self.val[:, 2])
        L1, A1, B1 = color.rgb2lab(np.array((self.r / 255., self.g / 255., self.b / 255.)).reshape(1, 1, 3)).reshape(3, )
        ll, aa, bb = L1 - L, A1 - A, B1 - B
        self.val[:, 0] +=ll*inten
        self.val[:, 1] +=aa*inten
        self.val[:, 2] += bb*inten

    def change_hsv(self):
        # Change HSV, making it more natural,optional
        self.im[self.x, self.y] = color.lab2rgb(self.val.reshape(len(self.x), 1, 3)).reshape(len(self.x), 3) * 255
        hsv_val = cv2.cvtColor(self.im,cv2.COLOR_BGR2HSV)
        hsv_val2=hsv_val[self.x,self.y]
        L3,A3,B3=mean(hsv_val2[:, 0]), mean(hsv_val2[:, 1]),mean(hsv_val2[:, 2])
        hsv_val2[:,0]-=0
        hsv_val2[:,1]-=0
        hsv_val2[:,2]+=0

        hsv_val[self.x, self.y]=hsv_val2
        self.im=cv2.cvtColor(hsv_val,cv2.COLOR_HSV2BGR)
        for i in range(0,len(self.x)-1):
            k=self.x[i]
            f=self.y[i]
            if(self.im[k,f][0]==225):
                self.im[k,f]=(220,220,220.)

    def guassian_blur(self):
        # guassian blur
        height,width = self.im.shape[:2]
        filter = np.zeros((height,width))
        cv2.fillConvexPoly(filter,np.array(c_[self.y, self.x],dtype = 'int32'),1)

        filter = cv2.GaussianBlur(filter,(31,31),0)

        # Erosion to reduce blur size
        kernel = np.ones((10,10),np.uint8)
        filter = cv2.erode(filter,kernel,iterations = 1)
        self.alpha=np.zeros([height,width,3],dtype='float64')
        self.alpha[:,:,0]=filter
        self.alpha[:,:,1]=filter
        self.alpha[:,:,2]=filter

    def save(self):
        imsave('../../save/virtual_makeup/lips/test1.jpg', (self.alpha*self.im+(1-self.alpha)*self.im2).astype('uint8'))


if __name__ == '__main__':
    lipstick = Lipstick()
    lipstick.apply_getpoint()
    lipstick.change_rgb()
    lipstick.change_hsv()
    lipstick.guassian_blur()
    lipstick.save()
