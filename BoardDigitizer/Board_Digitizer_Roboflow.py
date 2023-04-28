def evaluation():
    from stockfish import Stockfish
    Stockfish = Stockfish(path="/usr/local/Cellar/stockfish/15.1/bin/stockfish")
    

    Stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
    print('\n')
    print("The best move is:")
    print(Stockfish.get_best_move())
    print('\n')
    print("The top three moves are:")
    print(Stockfish.get_top_moves(3))
    print('\n')
    print("Printing Evaluation...")
    print(Stockfish.get_evaluation())


def chess(FEN):
    import urllib.request
    from PIL import Image

    # FEN = "1R1K1B2/Pp1QP1PN/N1Pn4/4pPp1/2p5/5n2/pb2k1p1/4r3"

    # Retrieving the resource located at the URL
    # and storing it in the file name a.png
    url = "https://fen2image.chessvision.ai" + FEN
    # print("PLEASE WORK: ")
    # print(FEN)
    urllib.request.urlretrieve(url, "board.png")

    # Opening the image and displaying it (to confirm its presence)
    img = Image.open(r"board.png")
    img.show()


def fenConversion(input_arr):
    l1 = ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-pawn",
          "white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-pawn"]
    l2 = ["r", "n", "b", "q", "k", "p", "R", "N", "B", "Q", "K", "P"]
    zero_count = 0
    final_string = ""
    for i, piece in enumerate(input_arr):
        piece = piece.lower()
        if i % 8 == 0:
            if zero_count > 0:
                final_string += str(zero_count)
                zero_count = 0
            final_string += '/'

        if piece not in l1:
            zero_count += 1
        else:
            if zero_count > 0:
                final_string += str(zero_count)
                zero_count = 0
            if piece == "black-rook":
                final_string += "r"
                continue
            if piece == "black-knight":
                final_string += "n"
                continue
            if piece == "black-bishop":
                final_string += "b"
                continue
            if piece == "black-queen":
                final_string += "q"
                continue
            if piece == "black-king":
                final_string += "k"
                continue
            if piece == "black-pawn":
                final_string += "p"
                continue

            if piece == "white-rook":
                final_string += "R"
                continue
            if piece == "white-knight":
                final_string += "N"
                continue
            if piece == "white-bishop":
                final_string += "B"
                continue
            if piece == "white-queen":
                final_string += "Q"
                continue
            if piece == "white-king":
                final_string += "K"
                continue
            if piece == "white-pawn":
                final_string += "P"
                continue
    return final_string[0:len(final_string) - 1]



def imageSplitter():

    import image_slicer
    image_slicer.slice('../chessboard_splits/transformedImage.jpg', 64)
    print("Splitting...")


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
    print('\n')
    print("Resizing...")


def infrencing():

    # running model on each image created by image_slicer
    print("Running model...")
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
            # print(prediction)
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

    return toArray()


def toArray():
    import numpy as np

    # Text file data converted to string data type
    piece_array = np.loadtxt("../classes.txt", dtype=str)
    # print(piece_array)

    return piece_array
