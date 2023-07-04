from sympy import *
def trans(matrix):
    matrix[0:3, 1], matrix[3:6, 0] = matrix[3:6, 0], matrix[0:3, 1]
    matrix[0:3, 2], matrix[6:9, 0] = matrix[6:9, 0], matrix[0:3, 2]
    matrix[3:6, 2], matrix[6:9, 1] = matrix[6:9, 1], matrix[3:6, 2]
    return matrix

def trans_quad(matrix):
    matrix[0:3, 3:6], matrix[3:6, 0:3] = matrix[3:6, 0:3], matrix[0:3, 3:6]
    matrix[0:3, 6:9], matrix[6:9, 0:3] = matrix[6:9, 0:3], matrix[0:3, 6:9]
    matrix[3:6, 6:9], matrix[6:9, 3:6] = matrix[6:9, 3:6], matrix[3:6, 6:9]
    return matrix

def trans_quad_2Swap(matrix):
    # input is a 9 by 3 matrix, consider a 3 by 1 vector as an element
    matrix[0, 1], matrix[1, 0] = matrix[1, 0], matrix[0, 1]
    matrix[0, 2], matrix[2, 0] = matrix[2, 0], matrix[0, 2]
    matrix[2, 1], matrix[1, 2] = matrix[1, 2], matrix[2, 1]

    matrix[0, 4], matrix[1, 3] = matrix[1, 3], matrix[0, 4]
    matrix[0, 5], matrix[2, 3] = matrix[2, 3], matrix[0, 5]
    matrix[2, 4], matrix[1, 5] = matrix[1, 5], matrix[2, 4]

    matrix[0, 7], matrix[1, 6] = matrix[1, 6], matrix[0, 7]
    matrix[0, 8], matrix[2, 6] = matrix[2, 6], matrix[0, 8]
    matrix[2, 7], matrix[1, 8] = matrix[1, 8], matrix[2, 7]

    matrix[3, 1], matrix[4, 0] = matrix[4, 0], matrix[3, 1]
    matrix[3, 2], matrix[5, 0] = matrix[5, 0], matrix[3, 2]
    matrix[5, 1], matrix[4, 2] = matrix[4, 2], matrix[5, 1]

    matrix[3, 4], matrix[4, 3] = matrix[4, 3], matrix[3, 4]
    matrix[5, 3], matrix[3, 5] = matrix[3, 5], matrix[5, 3]
    matrix[4, 5], matrix[5, 4] = matrix[5, 4], matrix[4, 5]

    matrix[3, 7], matrix[4, 6] = matrix[4, 6], matrix[3, 7]
    matrix[5, 6], matrix[3, 8] = matrix[3, 8], matrix[5, 6]
    matrix[4, 8], matrix[5, 7] = matrix[5, 7], matrix[4, 8]

    matrix[6, 1], matrix[7, 0] = matrix[7, 0], matrix[6, 1]
    matrix[6, 2], matrix[8, 0] = matrix[8, 0], matrix[6, 2]
    matrix[8, 1], matrix[7, 2] = matrix[7, 2], matrix[8, 1]

    matrix[6, 4], matrix[7, 3] = matrix[7, 3], matrix[6, 4]
    matrix[6, 5], matrix[8, 3] = matrix[8, 3], matrix[6, 5]
    matrix[7, 5], matrix[8, 4] = matrix[8, 4], matrix[7, 5]

    matrix[6, 7], matrix[7, 6] = matrix[7, 6], matrix[6, 7]
    matrix[6, 8], matrix[8, 6] = matrix[8, 6], matrix[6, 8]
    matrix[8, 7], matrix[7, 8] = matrix[7, 8], matrix[8, 7]
    return matrix

    # define a function to do operation of 3*3 matrix times 9*3 matrix

def sTB(sm, bm):
    # new matrix is 9 by 3
    a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
        2, 2]
    A1, A2, A3, D1, D2, D3, G1, G2, G3 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
        7, 0], bm[8, 0]
    B1, B2, B3, E1, E2, E3, H1, H2, H3 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
        7, 1], bm[8, 1]
    C1, C2, C3, F1, F2, F3, K1, K2, K3 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
        7, 2], bm[8, 2]
    nm = zeros(9, 3)
    nm[0, 0] = a * A1 + b * D1 + c * G1
    nm[1, 0] = a * A2 + b * D2 + c * G2
    nm[2, 0] = a * A3 + b * D3 + c * G3
    nm[3, 0] = d * A1 + e * D1 + f * G1
    nm[4, 0] = d * A2 + e * D2 + f * G2
    nm[5, 0] = d * A3 + e * D3 + f * G3
    nm[6, 0] = g * A1 + h * D1 + k * G1
    nm[7, 0] = g * A2 + h * D2 + k * G2
    nm[8, 0] = g * A3 + h * D3 + k * G3
    nm[0, 1] = a * B1 + b * E1 + c * H1
    nm[1, 1] = a * B2 + b * E2 + c * H2
    nm[2, 1] = a * B3 + b * E3 + c * H3
    nm[3, 1] = d * B1 + e * E1 + f * H1
    nm[4, 1] = d * B2 + e * E2 + f * H2
    nm[5, 1] = d * B3 + e * E3 + f * H3
    nm[6, 1] = g * B1 + h * E1 + k * H1
    nm[7, 1] = g * B2 + h * E2 + k * H2
    nm[8, 1] = g * B3 + h * E3 + k * H3
    nm[0, 2] = a * C1 + b * F1 + c * K1
    nm[1, 2] = a * C2 + b * F2 + c * K2
    nm[2, 2] = a * C3 + b * F3 + c * K3
    nm[3, 2] = d * C1 + e * F1 + f * K1
    nm[4, 2] = d * C2 + e * F2 + f * K2
    nm[5, 2] = d * C3 + e * F3 + f * K3
    nm[6, 2] = g * C1 + h * F1 + k * K1
    nm[7, 2] = g * C2 + h * F2 + k * K2
    nm[8, 2] = g * C3 + h * F3 + k * K3
    return nm

    # define a function to do operation of 3*3 matrix times 9*9 matrix

def sTB_quad(sm, bm):
    # new matrix is 9 by 3
    a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
        2, 2]
    A1, A2, A3, A4, A5, A6, A7, A8, A9 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
        7, 0], bm[8, 0]
    B1, B2, B3, B4, B5, B6, B7, B8, B9 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
        7, 1], bm[8, 1]
    C1, C2, C3, C4, C5, C6, C7, C8, C9 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
        7, 2], bm[8, 2]
    D1, D2, D3, D4, D5, D6, D7, D8, D9 = bm[0, 3], bm[1, 3], bm[2, 3], bm[3, 3], bm[4, 3], bm[5, 3], bm[6, 3], bm[
        7, 3], bm[8, 3]
    E1, E2, E3, E4, E5, E6, E7, E8, E9 = bm[0, 4], bm[1, 4], bm[2, 4], bm[3, 4], bm[4, 4], bm[5, 4], bm[6, 4], bm[
        7, 4], bm[8, 4]
    F1, F2, F3, F4, F5, F6, F7, F8, F9 = bm[0, 5], bm[1, 5], bm[2, 5], bm[3, 5], bm[4, 5], bm[5, 5], bm[6, 5], bm[
        7, 5], bm[8, 5]
    G1, G2, G3, G4, G5, G6, G7, G8, G9 = bm[0, 6], bm[1, 6], bm[2, 6], bm[3, 6], bm[4, 6], bm[5, 6], bm[6, 6], bm[
        7, 6], bm[8, 6]
    H1, H2, H3, H4, H5, H6, H7, H8, H9 = bm[0, 7], bm[1, 7], bm[2, 7], bm[3, 7], bm[4, 7], bm[5, 7], bm[6, 7], bm[
        7, 7], bm[8, 7]
    I1, I2, I3, I4, I5, I6, I7, I8, I9 = bm[0, 8], bm[1, 8], bm[2, 8], bm[3, 8], bm[4, 8], bm[5, 8], bm[6, 8], bm[
        7, 8], bm[8, 8]
    nm = zeros(9, 9)
    # First 9x3
    nm[0, 0] = a * A1 + b * A4 + c * A7
    nm[1, 0] = a * A2 + b * A5 + c * A8
    nm[2, 0] = a * A3 + b * A6 + c * A9
    nm[3, 0] = d * A1 + e * A4 + f * A7
    nm[4, 0] = d * A2 + e * A5 + f * A8
    nm[5, 0] = d * A3 + e * A6 + f * A9
    nm[6, 0] = g * A1 + h * A4 + k * A7
    nm[7, 0] = g * A2 + h * A5 + k * A8
    nm[8, 0] = g * A3 + h * A6 + k * A9
    nm[0, 1] = a * B1 + b * B4 + c * B7
    nm[1, 1] = a * B2 + b * B5 + c * B8
    nm[2, 1] = a * B3 + b * B6 + c * B9
    nm[3, 1] = d * B1 + e * B4 + f * B7
    nm[4, 1] = d * B2 + e * B5 + f * B8
    nm[5, 1] = d * B3 + e * B6 + f * B9
    nm[6, 1] = g * B1 + h * B4 + k * B7
    nm[7, 1] = g * B2 + h * B5 + k * B8
    nm[8, 1] = g * B3 + h * B6 + k * B9
    nm[0, 2] = a * C1 + b * C4 + c * C7
    nm[1, 2] = a * C2 + b * C5 + c * C8
    nm[2, 2] = a * C3 + b * C6 + c * C9
    nm[3, 2] = d * C1 + e * C4 + f * C7
    nm[4, 2] = d * C2 + e * C5 + f * C8
    nm[5, 2] = d * C3 + e * C6 + f * C9
    nm[6, 2] = g * C1 + h * C4 + k * C7
    nm[7, 2] = g * C2 + h * C5 + k * C8
    nm[8, 2] = g * C3 + h * C6 + k * C9
    # Second 9x3
    nm[0, 3] = a * D1 + b * D4 + c * D7
    nm[1, 3] = a * D2 + b * D5 + c * D8
    nm[2, 3] = a * D3 + b * D6 + c * D9
    nm[3, 3] = d * D1 + e * D4 + f * D7
    nm[4, 3] = d * D2 + e * D5 + f * D8
    nm[5, 3] = d * D3 + e * D6 + f * D9
    nm[6, 3] = g * D1 + h * D4 + k * D7
    nm[7, 3] = g * D2 + h * D5 + k * D8
    nm[8, 3] = g * D3 + h * D6 + k * D9
    nm[0, 4] = a * E1 + b * E4 + c * E7
    nm[1, 4] = a * E2 + b * E5 + c * E8
    nm[2, 4] = a * E3 + b * E6 + c * E9
    nm[3, 4] = d * E1 + e * E4 + f * E7
    nm[4, 4] = d * E2 + e * E5 + f * E8
    nm[5, 4] = d * E3 + e * E6 + f * E9
    nm[6, 4] = g * E1 + h * E4 + k * E7
    nm[7, 4] = g * E2 + h * E5 + k * E8
    nm[8, 4] = g * E3 + h * E6 + k * E9
    nm[0, 5] = a * F1 + b * F4 + c * F7
    nm[1, 5] = a * F2 + b * F5 + c * F8
    nm[2, 5] = a * F3 + b * F6 + c * F9
    nm[3, 5] = d * F1 + e * F4 + f * F7
    nm[4, 5] = d * F2 + e * F5 + f * F8
    nm[5, 5] = d * F3 + e * F6 + f * F9
    nm[6, 5] = g * F1 + h * F4 + k * F7
    nm[7, 5] = g * F2 + h * F5 + k * F8
    nm[8, 5] = g * F3 + h * F6 + k * F9
    # Third 9x3
    nm[0, 6] = a * G1 + b * G4 + c * G7
    nm[1, 6] = a * G2 + b * G5 + c * G8
    nm[2, 6] = a * G3 + b * G6 + c * G9
    nm[3, 6] = d * G1 + e * G4 + f * G7
    nm[4, 6] = d * G2 + e * G5 + f * G8
    nm[5, 6] = d * G3 + e * G6 + f * G9
    nm[6, 6] = g * G1 + h * G4 + k * G7
    nm[7, 6] = g * G2 + h * G5 + k * G8
    nm[8, 6] = g * G3 + h * G6 + k * G9
    nm[0, 7] = a * H1 + b * H4 + c * H7
    nm[1, 7] = a * H2 + b * H5 + c * H8
    nm[2, 7] = a * H3 + b * H6 + c * H9
    nm[3, 7] = d * H1 + e * H4 + f * H7
    nm[4, 7] = d * H2 + e * H5 + f * H8
    nm[5, 7] = d * H3 + e * H6 + f * H9
    nm[6, 7] = g * H1 + h * H4 + k * H7
    nm[7, 7] = g * H2 + h * H5 + k * H8
    nm[8, 7] = g * H3 + h * H6 + k * H9
    nm[0, 8] = a * I1 + b * I4 + c * I7
    nm[1, 8] = a * I2 + b * I5 + c * I8
    nm[2, 8] = a * I3 + b * I6 + c * I9
    nm[3, 8] = d * I1 + e * I4 + f * I7
    nm[4, 8] = d * I2 + e * I5 + f * I8
    nm[5, 8] = d * I3 + e * I6 + f * I9
    nm[6, 8] = g * I1 + h * I4 + k * I7
    nm[7, 8] = g * I2 + h * I5 + k * I8
    nm[8, 8] = g * I3 + h * I6 + k * I9
    return nm

def bTS(bm, sm):
    # new matrix is 9 by 3
    a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
        2, 2]
    A1, A2, A3, D1, D2, D3, G1, G2, G3 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
        7, 0], bm[8, 0]
    B1, B2, B3, E1, E2, E3, H1, H2, H3 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
        7, 1], bm[8, 1]
    C1, C2, C3, F1, F2, F3, K1, K2, K3 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
        7, 2], bm[8, 2]
    nm = zeros(9, 3)
    nm[0, 0] = a * A1 + d * A2 + g * A3
    nm[1, 0] = b * A1 + e * A2 + h * A3
    nm[2, 0] = c * A1 + f * A2 + k * A3
    nm[3, 0] = a * D1 + d * D2 + g * D3
    nm[4, 0] = b * D1 + e * D2 + h * D3
    nm[5, 0] = c * D1 + f * D2 + k * D3
    nm[6, 0] = a * G1 + d * G2 + g * G3
    nm[7, 0] = b * G1 + e * G2 + h * G3
    nm[8, 0] = c * G1 + f * G2 + k * G3
    nm[0, 1] = a * B1 + d * B2 + g * B3
    nm[1, 1] = b * B1 + e * B2 + h * B3
    nm[2, 1] = c * B1 + f * B2 + k * B3
    nm[3, 1] = a * E1 + d * E2 + g * E3
    nm[4, 1] = b * E1 + e * E2 + h * E3
    nm[5, 1] = c * E1 + f * E2 + k * E3
    nm[6, 1] = a * H1 + d * H2 + g * H3
    nm[7, 1] = b * H1 + e * H2 + h * H3
    nm[8, 1] = c * H1 + f * H2 + k * H3
    nm[0, 2] = a * C1 + d * C2 + g * C3
    nm[1, 2] = b * C1 + e * C2 + h * C3
    nm[2, 2] = c * C1 + f * C2 + k * C3
    nm[3, 2] = a * F1 + d * F2 + g * F3
    nm[4, 2] = b * F1 + e * F2 + h * F3
    nm[5, 2] = c * F1 + f * F2 + k * F3
    nm[6, 2] = a * K1 + d * K2 + g * K3
    nm[7, 2] = b * K1 + e * K2 + h * K3
    nm[8, 2] = c * K1 + f * K2 + k * K3
    return nm

def bTS_quad(bm, sm):
    # new matrix is 9 by 3
    a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
        2, 2]
    A1, A2, A3, A4, A5, A6, A7, A8, A9 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
        7, 0], bm[8, 0]
    B1, B2, B3, B4, B5, B6, B7, B8, B9 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
        7, 1], bm[8, 1]
    C1, C2, C3, C4, C5, C6, C7, C8, C9 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
        7, 2], bm[8, 2]
    D1, D2, D3, D4, D5, D6, D7, D8, D9 = bm[0, 3], bm[1, 3], bm[2, 3], bm[3, 3], bm[4, 3], bm[5, 3], bm[6, 3], bm[
        7, 3], bm[8, 3]
    E1, E2, E3, E4, E5, E6, E7, E8, E9 = bm[0, 4], bm[1, 4], bm[2, 4], bm[3, 4], bm[4, 4], bm[5, 4], bm[6, 4], bm[
        7, 4], bm[8, 4]
    F1, F2, F3, F4, F5, F6, F7, F8, F9 = bm[0, 5], bm[1, 5], bm[2, 5], bm[3, 5], bm[4, 5], bm[5, 5], bm[6, 5], bm[
        7, 5], bm[8, 5]
    G1, G2, G3, G4, G5, G6, G7, G8, G9 = bm[0, 6], bm[1, 6], bm[2, 6], bm[3, 6], bm[4, 6], bm[5, 6], bm[6, 6], bm[
        7, 6], bm[8, 6]
    H1, H2, H3, H4, H5, H6, H7, H8, H9 = bm[0, 7], bm[1, 7], bm[2, 7], bm[3, 7], bm[4, 7], bm[5, 7], bm[6, 7], bm[
        7, 7], bm[8, 7]
    I1, I2, I3, I4, I5, I6, I7, I8, I9 = bm[0, 8], bm[1, 8], bm[2, 8], bm[3, 8], bm[4, 8], bm[5, 8], bm[6, 8], bm[
        7, 8], bm[8, 8]
    nm = zeros(9, 9)
    nm[0, 0] = a * A1 + d * B1 + g * C1
    nm[1, 0] = a * A2 + d * B2 + g * C2
    nm[2, 0] = a * A3 + d * B3 + g * C3
    nm[3, 0] = a * A4 + d * B4 + g * C4
    nm[4, 0] = a * A5 + d * B5 + g * C5
    nm[5, 0] = a * A6 + d * B6 + g * C6
    nm[6, 0] = a * A7 + d * B7 + g * C7
    nm[7, 0] = a * A8 + d * B8 + g * C8
    nm[8, 0] = a * A9 + d * B9 + g * C9

    nm[0, 1] = b * A1 + e * B1 + h * C1
    nm[1, 1] = b * A2 + e * B2 + h * C2
    nm[2, 1] = b * A3 + e * B3 + h * C3
    nm[3, 1] = b * A4 + e * B4 + h * C4
    nm[4, 1] = b * A5 + e * B5 + h * C5
    nm[5, 1] = b * A6 + e * B6 + h * C6
    nm[6, 1] = b * A7 + e * B7 + h * C7
    nm[7, 1] = b * A8 + e * B8 + h * C8
    nm[8, 1] = b * A9 + e * B9 + h * C9

    nm[0, 2] = c * A1 + f * B1 + k * C1
    nm[1, 2] = c * A2 + f * B2 + k * C2
    nm[2, 2] = c * A3 + f * B3 + k * C3
    nm[3, 2] = c * A4 + f * B4 + k * C4
    nm[4, 2] = c * A5 + f * B5 + k * C5
    nm[5, 2] = c * A6 + f * B6 + k * C6
    nm[6, 2] = c * A7 + f * B7 + k * C7
    nm[7, 2] = c * A8 + f * B8 + k * C8
    nm[8, 2] = c * A9 + f * B9 + k * C9

    nm[0, 3] = a * D1 + d * E1 + g * F1
    nm[1, 3] = a * D2 + d * E2 + g * F2
    nm[2, 3] = a * D3 + d * E3 + g * F3
    nm[3, 3] = a * D4 + d * E4 + g * F4
    nm[4, 3] = a * D5 + d * E5 + g * F5
    nm[5, 3] = a * D6 + d * E6 + g * F6
    nm[6, 3] = a * D7 + d * E7 + g * F7
    nm[7, 3] = a * D8 + d * E8 + g * F8
    nm[8, 3] = a * D9 + d * E9 + g * F9

    nm[0, 4] = b * D1 + e * E1 + h * F1
    nm[1, 4] = b * D2 + e * E2 + h * F2
    nm[2, 4] = b * D3 + e * E3 + h * F3
    nm[3, 4] = b * D4 + e * E4 + h * F4
    nm[4, 4] = b * D5 + e * E5 + h * F5
    nm[5, 4] = b * D6 + e * E6 + h * F6
    nm[6, 4] = b * D7 + e * E7 + h * F7
    nm[7, 4] = b * D8 + e * E8 + h * F8
    nm[8, 4] = b * D9 + e * E9 + h * F9

    nm[0, 5] = c * D1 + f * E1 + k * F1
    nm[1, 5] = c * D2 + f * E2 + k * F2
    nm[2, 5] = c * D3 + f * E3 + k * F3
    nm[3, 5] = c * D4 + f * E4 + k * F4
    nm[4, 5] = c * D5 + f * E5 + k * F5
    nm[5, 5] = c * D6 + f * E6 + k * F6
    nm[6, 5] = c * D7 + f * E7 + k * F7
    nm[7, 5] = c * D8 + f * E8 + k * F8
    nm[8, 5] = c * D9 + f * E9 + k * F9

    nm[0, 6] = a * G1 + d * H1 + g * I1
    nm[1, 6] = a * G2 + d * H2 + g * I2
    nm[2, 6] = a * G3 + d * H3 + g * I3
    nm[3, 6] = a * G4 + d * H4 + g * I4
    nm[4, 6] = a * G5 + d * H5 + g * I5
    nm[5, 6] = a * G6 + d * H6 + g * I6
    nm[6, 6] = a * G7 + d * H7 + g * I7
    nm[7, 6] = a * G8 + d * H8 + g * I8
    nm[8, 6] = a * G9 + d * H9 + g * I9

    nm[0, 7] = b * G1 + e * H1 + h * I1
    nm[1, 7] = b * G2 + e * H2 + h * I2
    nm[2, 7] = b * G3 + e * H3 + h * I3
    nm[3, 7] = b * G4 + e * H4 + h * I4
    nm[4, 7] = b * G5 + e * H5 + h * I5
    nm[5, 7] = b * G6 + e * H6 + h * I6
    nm[6, 7] = b * G7 + e * H7 + h * I7
    nm[7, 7] = b * G8 + e * H8 + h * I8
    nm[8, 7] = b * G9 + e * H9 + h * I9

    nm[0, 8] = c * G1 + f * H1 + k * I1
    nm[1, 8] = c * G2 + f * H2 + k * I2
    nm[2, 8] = c * G3 + f * H3 + k * I3
    nm[3, 8] = c * G4 + f * H4 + k * I4
    nm[4, 8] = c * G5 + f * H5 + k * I5
    nm[5, 8] = c * G6 + f * H6 + k * I6
    nm[6, 8] = c * G7 + f * H7 + k * I7
    nm[7, 8] = c * G8 + f * H8 + k * I8
    nm[8, 8] = c * G9 + f * H9 + k * I9
    return nm