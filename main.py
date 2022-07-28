import argparse
import os
from glob import glob
import cv2
import matplotlib.pyplot as plt

def crop_objects():
    label_path, img_path, save_path = opt.label, opt.image, opt.save

    for txt_file in sorted(glob(label_path + '*.txt')):
        base_name = os.path.basename(txt_file)
        name = base_name.split(".")[0]
        img = cv2.imread(img_path+name+'.JPG')
        image_height, image_width, _ = img.shape
        print('-----------------------------------------------------------------------------')
        print('start to process image: ', name)
        for line in open(txt_file):
            box_coords = tuple([float(x) for x in line.strip('\n').split(' ')[1:]])
            print('bbox coords: ', box_coords)
            center_x, center_y, width, height = box_coords
            x1 = int((center_x - width / 2) * image_width)
            x2 = int((center_x + width / 2) * image_width)
            y1 = int((center_y - height / 2) * image_height)
            y2 = int((center_y + height / 2) * image_height)
            if x1 < 0:
                x1 = 0
            if x2 > image_width - 1:
                x2 = image_width - 1
            if y1 < 0:
                y1 = 0
            if y2 > image_height - 1:
                y2 = image_height - 1
            # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cropped = img[y1:y2, x1:x2]
            cv2.imwrite(save_path+name+'.jpg', cropped)
            print('cropped image saved')

        # print('-----------------------------------------------------------------------------')
        # plt.imshow(img)
        # plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', type=str, default='')
    parser.add_argument('--image', type=str,
                        default='')
    parser.add_argument('--save', type=str,
                        default='')
    opt = parser.parse_args()
    print(opt)
    crop_objects()
