from sympy import *
import numpy as np
from decimal import *
from Core.function import TensorMath as tm


def rotation(phi_angle):
    cos_holder = np.cos(phi_angle)
    sin_holder = np.sin(phi_angle)
    cos_holder = round(Decimal(str(cos_holder)), 6)
    sin_holder = round(Decimal(str(sin_holder)), 6)
    rotx = Matrix([[1, 0, 0], [0, cos_holder, -sin_holder], [0, sin_holder, cos_holder]])
    roty = Matrix([[cos_holder, 0, sin_holder], [0, 1, 0], [-sin_holder, 0, cos_holder]])
    rotz = Matrix([[cos_holder, sin_holder, 0], [sin_holder, cos_holder, 0], [0, 0, 1]])
    return rotx, roty, rotz


def rotationXSwap(matrix_input, general_tensor):
    F_input_matrix = np.array(matrix_input)
    F_input_matrix = F_input_matrix.flatten()
    unique_elements = set(F_input_matrix)
    unique_lst = []
    for element in unique_elements:
        unique_lst.append(element)
    for j in range(0, len(unique_lst), 1):
        element = unique_lst[j]
        indices = [(i, j) for i in range(matrix_input.rows) for j in range(matrix_input.cols) if
                   matrix_input[i, j] == element]
        if element == 0:
            for i in range(0, len(indices), 1):
                sub = general_tensor[indices[i][0], indices[i][1]]
                general_tensor = general_tensor.subs([(sub, 0)])
        else:
            for i in range(0, len(indices), 1):
                matrix_input = matrix_input.subs(
                    [(matrix_input[indices[i][0], indices[i][1]], general_tensor[indices[0][0], indices[0][1]])])
    return matrix_input

def rotationCal(rank, option_var_3,input_matrix, rankMatrix):
    print(option_var_3)
    if option_var_3 == '(001)' or option_var_3 == '[010]' or option_var_3 == '[100]':
        input_matrix = input_matrix
    elif option_var_3 == '[001]' or option_var_3 == '(010)':
        phi_angle = np.pi / 2
        rotx, roty, rotz = rotation(phi_angle)
        first_rot = tm.Intensity_Cal(rank, input_matrix, rotx)
        input_matrix = tm.roundMatrix(first_rot)
        input_matrix = rotationXSwap(input_matrix, rankMatrix)
    elif option_var_3 == '(100)':
        phi_angle = np.pi / 2
        rotx, roty, rotz = rotation(phi_angle)
        first_rot = tm.Intensity_Cal(rank, input_matrix, roty)
        input_matrix = tm.roundMatrix(first_rot)
        input_matrix = rotationXSwap(input_matrix, rankMatrix)
    elif option_var_3 == '[010]':
        phi_angle = np.pi / 2
        rotx, roty, rotz = rotation(phi_angle)
        first_rot = tm.Intensity_Cal(rank, input_matrix, rotz)
        input_matrix = tm.roundMatrix(first_rot)
        input_matrix = rotationXSwap(input_matrix, rankMatrix)
    elif option_var_3 == '(011)':
        phi_angle = np.pi / 4
        rotx, roty, rotz = rotation(phi_angle)
        first_rot = tm.Intensity_Cal(rank, input_matrix, rotx)
        input_matrix = tm.roundMatrix(first_rot)
        input_matrix = rotationXSwap(input_matrix, rankMatrix)
    elif option_var_3 == '(111)':
        phi_angle = np.arccos(1 / np.sqrt(3))
        rotx, roty, rotz = rotation(phi_angle)
        first_rot = tm.Intensity_Cal(rank, input_matrix, rotx)
        first_rot = tm.roundMatrix(first_rot)
        second_rot = tm.Intensity_Cal(rank, first_rot, rotx)
        input_matrix = tm.roundMatrix(second_rot)
        input_matrix = rotationXSwap(input_matrix, rankMatrix)
    else:
        input_matrix = input_matrix
        print('Error Selection on the Axes Rotation')
    return input_matrix