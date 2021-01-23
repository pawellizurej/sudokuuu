import cv2
import numpy as np
from keras.models import load_model


def sort_corners(corners):
    arr2D = np.array([corners[0], corners[1], corners[2], corners[3]])
    sortedArr = arr2D[arr2D[:, 0].argsort()]

    if sortedArr[0][1] > sortedArr[1][1]:
        up_left = sortedArr[1]
        down_left = sortedArr[0]
    else:
        up_left = sortedArr[0]
        down_left = sortedArr[1]

    if sortedArr[2][1] > sortedArr[3][1]:
        upRight = sortedArr[3]
        downRight = sortedArr[2]
    else:
        upRight = sortedArr[2]
        downRight = sortedArr[3]

    return up_left, down_left, upRight, downRight


def detect_corners_from_contour(canvas, contours_main):
    epsilon = 0.02 * cv2.arcLength(contours_main, True)
    approx_corners = cv2.approxPolyDP(contours_main, epsilon, True)
    cv2.drawContours(canvas, approx_corners, -1, (255, 255, 0), 10)
    approx_corners = sorted(np.concatenate(approx_corners).tolist())

    for index, c in enumerate(approx_corners):
        character = chr(65 + index)

        cv2.putText(canvas, character, tuple(c), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Rearranging the order of the corner points
    approx_corners = [approx_corners[i] for i in [0, 2, 1, 3]]
    return approx_corners


def img_warp(path):
    img = cv2.imread(path)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # change = cv2.bitwise_not(gray, gray)
    contours, h = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    contours_main = contours[0]

    img = cv2.drawContours(img, contours_main, -1, (0, 255, 0), 5)

    canvas = np.zeros(img.shape, np.uint8)

    corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 100)
    corners = np.int0(corners)
    corners = sorted(np.concatenate(corners).tolist())

    corners_p = detect_corners_from_contour(canvas, contours_main)
    up_left, down_left, up_right, down_right = sort_corners(corners_p)
    img1 = cv2.imread(path)
    pt1 = np.float32([up_left, down_left, up_right, down_right])
    height, width = 450, 450
    pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    output = cv2.warpPerspective(img1, matrix, (width, height))
    output = cv2.rotate(output, cv2.ROTATE_90_CLOCKWISE)
    output = cv2.flip(output, 1)

    return output


def edit_cells(img):
    img_ret = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    contours, h = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    is_there_value = 0
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if x > 5 and y > 5 and w < 40 and h > 20 and cv2.contourArea(contour) > 50:
            img = cv2.bilateralFilter(img, 9, 75, 75)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            # img = cv2.bitwise_not(img)
            img = cv2.GaussianBlur(img, (5, 5), 1)

            img_ret = img[y:y + h, x:x + w]
            img_ret = cv2.copyMakeBorder(img_ret, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
            img_ret = cv2.cvtColor(img_ret, cv2.COLOR_GRAY2RGB)
            is_there_value = 1

    return img_ret, is_there_value


def split_into_parts(output):
    cells = []
    value = []
    for partx in range(9):
        for party in range(9):
            x = partx * 50
            x1 = ((partx + 1) * 50 + 5)
            y = party * 50
            y1 = ((party + 1) * 50)
            cell = output[x:x1, y:y1]
            cell, value_ = edit_cells(cell)
            cells.append(cell)
            value.append(value_)
    return cells, value


def create_grid(output):
    model = load_model('trained_modelv20.h5')
    cells, value = split_into_parts(output)
    grid = []
    for i in range(0, 81):
        if value[i] == 0:
            grid.append(0)
        else:
            img = cells[i]
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.resize(img, (28, 28))
            img = img.reshape(28, 28).reshape(1, 28, 28).reshape(1, 28, 28, 1)
            img = img / 255
            # predicting the class
            res = model.predict([img])[0]
            grid.append(np.argmax(res))

    grid = np.array(grid).reshape(9, 9)
    return grid
