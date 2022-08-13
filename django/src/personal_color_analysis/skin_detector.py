from typing_extensions import Self
import cv2 as cv

# !pip install pyimagesearch
# from pyimagesearch import imutils
import numpy as np
import argparse
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# 사용자의 피부 색 팔레트 추출
class SkinDetector:
    def __init__(self) -> None:
        self.file_name = "test1"
        self.img = cv.imread("../../src/img/"+self.file_name+".jpg")
        self.result = None
        self.skin_img = None
        self.temp = None

    def skin_detect_1(self):
        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")

        converted = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)
        skinMask = cv.inRange(converted, lower, upper)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11,11))
        skinMask = cv.erode(skinMask, kernel, iterations = 2)
        skinMask = cv.dilate(skinMask, kernel, iterations = 2)

        skinMask = cv.GaussianBlur(skinMask, (3,3), 0)
        skin = cv.bitwise_and(self.img, self.img, mask = skinMask)

        self.result = skin
        # view_img = np.hstack([img, skin])
        # plt.imshow(self.result)
        # plt.show()
        # cv2.imshow("test", view_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def skin_detect_2(self):
        # 피부 검출2
        # img = cv2.cvtColor(skin, cv2.COLOR_HSV2BGR)
        # plt.imshow(img)
        # plt.show()
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

        self.img = cv.cvtColor(self.result, cv.COLOR_BGR2HLS)
        self.skin_img = self.img
        temp_img = cv.cvtColor(self.img, cv.COLOR_HLS2RGB)

        h, w, c = self.img.shape

        for i in range(h) :
            for j in range(w) :
                H = self.img[i][j][0]
                L = self.img[i][j][1]
                S = self.img[i][j][2]
                
                R = temp_img[i][j][0]
                G = temp_img[i][j][1]
                B = temp_img[i][j][2]
                
                LS_ratio = L/S
                skin_pixel = bool((S>=50) and (LS_ratio > 0.5) and (LS_ratio < 3.0) and ((H <= 25) or (H >= 165)))
                temp_pixel = bool((R == G) and (G == B) and (R >= 220))
                        
                if skin_pixel :
                    if temp_pixel :
                        self.skin_img[i][j][0] = 0
                        self.skin_img[i][j][1] = 0
                        self.skin_img[i][j][2] = 0
                    else :
                        pass
                else :
                    self.skin_img[i][j][0] = 0
                    self.skin_img[i][j][1] = 0
                    self.skin_img[i][j][2] = 0
                
        self.skin_img = cv.cvtColor(self.skin_img, cv.COLOR_HLS2BGR)            
        for i in range(h) :
            for j in range(w) :
                B = self.skin_img[i][j][0]
                G = self.skin_img[i][j][1]
                R = self.skin_img[i][j][2]

                bg_pixel = bool(B==0 and G==0 and R==0)
                
                if bg_pixel :
                    self.skin_img[i][j][0] = 255
                    self.skin_img[i][j][1] = 255
                    self.skin_img[i][j][2] = 255
                else :
                    pass
                
                
        # plt.imshow(self.skin_img)
        # plt.show()

        # cv2.imshow("Original", img)
        # cv2.imshow("Original", skin_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def change_color(self):
        cvt_img = cv.cvtColor(self.skin_img, cv.COLOR_BGR2RGB)
        # plt.imshow(cvt_img)
        # plt.show()

        cvt_img = cvt_img.reshape((cvt_img.shape[0]*cvt_img.shape[1], 3))
        k = 20
        clt = KMeans(n_clusters=k)
        clt.fit(cvt_img)
        return clt

    @staticmethod
    def color_ratio(clt):
        numLabels = np.arange(0, len(np.unique(clt.labels_))+1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()
        return hist

    # k=5이므로 다섯개의 영역에 얼마만큼의 퍼센테이지가 차지되었는지 return된다.

    @staticmethod
    def plot_colors(hist, centroids):
        bar = np.zeros((50, 300, 3), dtype = "uint8")
        startX = 0

        for (percent, color) in zip(hist, centroids):
            print("색깔 ",color)
            print("비율 : ", percent)
            endX = startX + (percent * 300)
            cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
                color.astype("uint8").tolist(), -1)
            startX = endX
        return bar

    def adjust_ratio(self, clt):
        hist = self.color_ratio(clt)
        temp = np.array(clt.cluster_centers_)

        # hist에서 높은 값 제거, cluster_centers_에서도 제거)
        del_index = hist.argmax()
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        # hist에서 제일 낮은 값 제거, cluster_centers_ 에서도 제거 
        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0) 

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0) # 3

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0) # 4

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0) # 5

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        del_index = np.argmin(hist)
        hist = np.delete(hist, del_index)
        temp = np.delete(temp, del_index, 0)

        # 비율 재조정
        hist = hist / hist.sum()
        ####################################
        return hist, temp

    def draw_plt(self, hist, temp):
        bar = self.plot_colors(hist, temp)
        plt.figure()
        plt.axis("off")
        plt.imshow(bar)
        plt.show()
        return bar

    def save_plt(self, bar):
        # RGB 변환 후 저장
        bar = cv.cvtColor(bar, cv.COLOR_BGR2RGB)
        cv.imwrite("../../src/save/skin_detect_result/"+self.file_name+".jpg", bar)


if __name__ == '__main__':
    sd = SkinDetector()
    sd.skin_detect_1()
    sd.skin_detect_2()
    clt = sd.change_color()
    hist, temp = sd.adjust_ratio(clt)
    bar = sd.draw_plt(hist, temp)
    sd.save_plt(bar)
