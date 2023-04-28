
def imageSplitter():

    import image_slicer
    image_slicer.slice('../chessboard_splits/transformedImage.jpg', 64)


def resizer(filepath):

    import cv2
    import os
    import numpy as np
    from operator import itemgetter
    from glob import glob
    import matplotlib.pyplot as plt

    image = cv2.imread(filepath)
    filename = 'transformedImage.jpg'
    imagePath = filepath
    print(1)
    directory = r'/Users/connorscally/Documents/GitHub/ChessVision/BoardDigitizer/chessboard_splits'
    img = cv2.imread(imagePath)
    os.chdir(directory)

    # Coordinates that you want to Perspective Transform
    pts1 = np.float32([[1017, 412], [2997, 423], [330, 2145], [
                      3850, 2128]])  # tl, tr, bl, br

    # Size of the Transformed Image
    pts2 = np.float32([[0, 0], [500, 0], [0, 400], [500, 400]])

    for val in pts1:
        cv2.circle(image, (int(val[0]), int(val[1])), 5, (0, 255, 0), -1)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image, M, (500, 400))
    cv2.imwrite(filename, dst)
    print(2)


def infrencing():

    # running model on each image created by image_slicer
    print(3)
    import os
    from PIL import Image
    from os import listdir
    from roboflow import Roboflow
    rf = Roboflow(api_key="0uya8edueMEE3249OloG")
    project = rf.workspace().project("piece-detection-rayven")
    model = project.version(4).model

    path = "/Users/connorscally/Documents/GitHub/ChessVision/BoardDigitizer/chessboard_splits/"

    text_file = open("../classes.txt", "w")

    for i, image in enumerate(os.listdir(path)):

        if image != 'chessboard.jpg' or not 'transformedImage.jpg':
            image = path + image

            prediction = (model.predict(
                image, confidence=40, overlap=30).json())
            print(prediction)
            if len(prediction["predictions"]) == 0:
                eval = '[]'
            else:
                eval = prediction["predictions"][0]["class"]
            # writes class names assigned during image evaluation to a text file as long as class names are a chess piece, if not, 0 is written instead

            if eval == 'background' or eval == 'Background' or eval == '[]':
                text_file.write('0')
                text_file.write('\n')

            else:
                text_file.write(eval)
                text_file.write('\n')

    text_file.close()

    toArray()


def toArray():
    print(4)
    import numpy as np

    # Text file data converted to string data type
    piece_array = np.loadtxt("../classes.txt", dtype=str)
    print(piece_array)
