import string
import random
import math
from tkinter import *

#THESE ARE DECLARATIONS OF VARIABLE TO BE USED BY BOTH BOTH/EITHER THE ENIGMA OR REVERSE_ENIGMA FUNCTIONS! THESE ARE DECLARATIONS OF VARIABLE TO BE USED BY BOTH BOTH/EITHER THE ENIGMA OR REVERSE_ENIGMA FUNCTIONS! THESE ARE DECLARATIONS OF VARIABLE TO BE USED BY BOTH BOTH/EITHER THE ENIGMA OR REVERSE_ENIGMA FUNCTIONS! THESE ARE DECLARATIONS OF VARIABLE TO BE USED BY BOTH BOTH/EITHER THE ENIGMA OR REVERSE_ENIGMA FUNCTIONS! 

all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '|', ',', '<', '.', '>', '/', '?', '#', '~', '@', "'", ';', ':', '=', '+', '-', '_', ')', '(', '*', '&', '^', '%', '$', '£', '"', '!', '[', ']', '{', '}', ' ']
num_char_pairs = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'A', 28: 'B', 29: 'C', 30: 'D', 31: 'E', 32: 'F', 33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: 'N', 41: 'O', 42: 'P', 43: 'Q', 44: 'R', 45: 'S', 46: 'T', 47: 'U', 48: 'V', 49: 'W', 50: 'X', 51: 'Y', 52: 'Z', 53: '0', 54: '1', 55: '2', 56: '3', 57: '4', 58: '5', 59: '6', 60: '7', 61: '8', 62: '9', 63: '|', 64: ',', 65: '<', 66: '.', 67: '>', 68: '/', 69: '?', 70: '#', 71: '~', 72: '@', 73: "'", 74: ';', 75: ':', 76: '=', 77: '+', 78: '-', 79: '_', 80: ')', 81: '(', 82: '*', 83: '&', 84: '^', 85: '%', 86: '$', 87: '£', 88: '"', 89: '!', 90: '[', 91: ']', 92: '{', 93: '}', 94: ' '}
char_num_pairs = {'l': 12, 'c': 3, 'Q': 43, 'F': 32, 'b': 2, 'I': 35, '|': 63, 'P': 42, 'e': 5, '#': 70, 'u': 21, 'x': 24, '5': 58, 'Y': 51, 'D': 30, '%': 85, 'X': 50, '8': 61, '@': 72, 'f': 6, 'j': 10, 't': 20, '3': 56, 'G': 33, 'o': 15, 'T': 46, 'y': 25, 'J': 36, 'N': 40, '[': 90, '.': 66, '>': 67, '6': 59, '/': 68, 'R': 44, ' ': 94, 'L': 38, 'O': 41, '"': 88, 'r': 18, '-': 78, 'B': 28, '<': 65, '4': 57, "'": 73, 'Z': 52, '^': 84, '~': 71, '0': 53, 'a': 1, 'v': 22, 'q': 17, 'i': 9, '&': 83, 'h': 8, '$': 86, '=': 76, '1': 54, 'K': 37, 'H': 34, '2': 55, '+': 77, '_': 79, 'd': 4, '!': 89, 'S': 45, '9': 62, ')': 80, ',': 64, ':': 75, 'g': 7, '7': 60, ';': 74, 'U': 47, 'n': 14, 'A': 27, 'M': 39, 'p': 16, '(': 81, ']': 91, 'V': 48, 'W': 49, 'E': 31, 'm': 13, 'C': 29, '}': 93, 'z': 26, 'w': 23, '*': 82, '?': 69, '£': 87, 'k': 11, 's': 19, '{': 92}

list_of_letters_I = 'P+0=Ogm"K:3Dk&NrY2^oXC}9Ix|b1;RfpZu<l,6_Qv{hA-Ja)(BM>dc%He*zTF4.wyS5sjE/?it$8U£ #qL~W!7@n[]V\'G'
rev_num_convert_I = {1: 68, 2: 40, 3: 93, 4: 86, 5: 19, 6: 91, 7: 35, 8: 81, 9: 89, 10: 25, 11: 88, 12: 78, 13: 13, 14: 61, 15: 31, 16: 34, 17: 77, 18: 90, 19: 24, 20: 58, 21: 79, 22: 59, 23: 92, 24: 4, 25: 70, 26: 45, 27: 28, 28: 21, 29: 57, 30: 36, 31: 72, 32: 56, 33: 51, 34: 10, 35: 75, 36: 30, 37: 82, 38: 5, 39: 43, 40: 46, 41: 53, 42: 55, 43: 62, 44: 37, 45: 8, 46: 14, 47: 2, 48: 29, 49: 67, 50: 71, 51: 49, 52: 64, 53: 23, 54: 87, 55: 69, 56: 18, 57: 16, 58: 48, 59: 80, 60: 84, 61: 63, 62: 33, 63: 38, 64: 76, 65: 39, 66: 83, 67: 26, 68: 47, 69: 15, 70: 41, 71: 9, 72: 52, 73: 85, 74: 94, 75: 50, 76: 22, 77: 12, 78: 60, 79: 73, 80: 27, 81: 20, 82: 66, 83: 32, 84: 3, 85: 54, 86: 44, 87: 17, 88: 74, 89: 6, 90: 42, 91: 11, 92: 1, 93: 65, 94: 7}


list_of_letters_II = '£SiA$n8lq|7oKvC,6zLB)_-uRY<a#M0.e>Wg+\'5c(N/1!Zr?T~fD2[]@4mG{tU3wOVy"EFh:p;Xb*&P} H=9dj^IxQsJ%k'
rev_num_convert_II = {1: 94, 2: 93, 3: 82, 4: 44, 5: 79, 6: 52, 7: 47, 8: 56, 9: 19, 10: 74, 11: 58, 12: 21, 13: 2, 14: 45, 15: 17, 16: 48, 17: 62, 18: 66, 19: 18, 20: 75, 21: 14, 22: 80, 23: 1, 24: 10, 25: 38, 26: 26, 27: 22, 28: 70, 29: 40, 30: 86, 31: 76, 32: 34, 33: 41, 34: 59, 35: 88, 36: 50, 37: 72, 38: 49, 39: 78, 40: 13, 41: 8, 42: 89, 43: 67, 44: 9, 45: 65, 46: 31, 47: 57, 48: 12, 49: 6, 50: 16, 51: 4, 52: 51, 53: 61, 54: 71, 55: 54, 56: 37, 57: 55, 58: 25, 59: 27, 60: 87, 61: 91, 62: 33, 63: 92, 64: 60, 65: 64, 66: 53, 67: 85, 68: 42, 69: 90, 70: 29, 71: 5, 72: 68, 73: 77, 74: 28, 75: 73, 76: 83, 77: 39, 78: 11, 79: 23, 80: 43, 81: 69, 82: 32, 83: 84, 84: 46, 85: 30, 86: 24, 87: 3, 88: 36, 89: 63, 90: 7, 91: 81, 92: 15, 93: 35, 94: 20}


list_of_letters_III = '£SiA$n8lq|7oKvC,6zLB)_-uRY<a#M0.e>Wg+5c(N/1!Zr?"T~fD2[]@4mG{tU3wOVy\'EFh:p;Xb*&P} H=9dj^IxQsJ%k'
rev_num_convert_III = {1: 8, 2: 72, 3: 12, 4: 37, 5: 61, 6: 58, 7: 11, 8: 94, 9: 64, 10: 21, 11: 15, 12: 10, 13: 42, 14: 44, 15: 69, 16: 86, 17: 16, 18: 30, 19: 48, 20: 38, 21: 33, 22: 34, 23: 68, 24: 78, 25: 63, 26: 82, 27: 32, 28: 45, 29: 1, 30: 90, 31: 19, 32: 56, 33: 31, 34: 39, 35: 25, 36: 77, 37: 65, 38: 53, 39: 4, 40: 5, 41: 36, 42: 85, 43: 84, 44: 91, 45: 62, 46: 46, 47: 83, 48: 6, 49: 87, 50: 55, 51: 2, 52: 22, 53: 50, 54: 89, 55: 66, 56: 28, 57: 54, 58: 59, 59: 92, 60: 18, 61: 73, 62: 35, 63: 76, 64: 40, 65: 17, 66: 60, 67: 9, 68: 24, 69: 27, 70: 29, 71: 47, 72: 23, 73: 43, 74: 70, 75: 49, 76: 79, 77: 7, 78: 52, 79: 75, 80: 57, 81: 20, 82: 3, 83: 81, 84: 74, 85: 14, 86: 51, 87: 26, 88: 80, 89: 88, 90: 13, 91: 71, 92: 67, 93: 93, 94: 41}


list_of_letters_IV = '$I)C!0/E^Qvd9*]1{Pyuk3zZ[~(?f+=nY"BFwDV4Octr,p#_G;\'xK-Nh7T>&:S.MHeo<sba6 i5X£%UmJRg2qlA}8@jWL|'
rev_num_convert_IV = {1: 52, 2: 92, 3: 7, 4: 10, 5: 25, 6: 24, 7: 87, 8: 77, 9: 83, 10: 21, 11: 75, 12: 2, 13: 89, 14: 48, 15: 82, 16: 6, 17: 38, 18: 11, 19: 53, 20: 32, 21: 94, 22: 31, 23: 17, 24: 42, 25: 49, 26: 37, 27: 59, 28: 23, 29: 56, 30: 45, 31: 3, 32: 74, 33: 67, 34: 26, 35: 34, 36: 47, 37: 28, 38: 22, 39: 79, 40: 90, 41: 81, 42: 1, 43: 29, 44: 19, 45: 50, 46: 88, 47: 27, 48: 4, 49: 40, 50: 65, 51: 64, 52: 13, 53: 68, 54: 71, 55: 9, 56: 84, 57: 58, 58: 72, 59: 35, 60: 16, 61: 8, 62: 20, 63: 61, 64: 93, 65: 14, 66: 57, 67: 80, 68: 30, 69: 86, 70: 43, 71: 73, 72: 18, 73: 76, 74: 78, 75: 66, 76: 54, 77: 33, 78: 51, 79: 70, 80: 12, 81: 69, 82: 63, 83: 39, 84: 15, 85: 55, 86: 91, 87: 41, 88: 36, 89: 44, 90: 5, 91: 62, 92: 85, 93: 60, 94: 46}


list_of_letters_V = 'r=V%i3(Luz9C/}ObkoDQ+*ePx£RyEn8Fv{):&2wG]S6K$BT^,mp0!X\'>fU|qd<ZWN.l?g7[;@MJt5Ia"#A4h1 _jscYH-~'
rev_num_convert_V = {1: 77, 2: 59, 3: 94, 4: 79, 5: 73, 6: 86, 7: 67, 8: 61, 9: 85, 10: 65, 11: 2, 12: 90, 13: 47, 14: 9, 15: 88, 16: 51, 17: 93, 18: 83, 19: 22, 20: 80, 21: 31, 22: 42, 23: 58, 24: 38, 25: 36, 26: 68, 27: 21, 28: 33, 29: 23, 30: 91, 31: 11, 32: 78, 33: 17, 34: 82, 35: 7, 36: 56, 37: 57, 38: 66, 39: 70, 40: 19, 41: 75, 42: 89, 43: 92, 44: 5, 45: 60, 46: 64, 47: 12, 48: 15, 49: 84, 50: 29, 51: 14, 52: 49, 53: 54, 54: 26, 55: 63, 56: 24, 57: 81, 58: 27, 59: 8, 60: 72, 61: 44, 62: 37, 63: 18, 64: 30, 65: 55, 66: 52, 67: 69, 68: 4, 69: 40, 70: 62, 71: 76, 72: 10, 73: 28, 74: 6, 75: 39, 76: 53, 77: 48, 78: 74, 79: 1, 80: 34, 81: 20, 82: 41, 83: 71, 84: 3, 85: 45, 86: 32, 87: 35, 88: 43, 89: 16, 90: 87, 91: 46, 92: 13, 93: 25, 94: 50}


list_of_letters_VI = '%Ir/bw\'4WJEN?,0Kp1ST#;n7jqOsA:"*!{hi}FvRcCZ)8_B+3 L<xY5~[UkP]m6$f@y|=DG>VaHe-&o^tzd9(.Mg£luXQ2'
rev_num_convert_VI = {1: 73, 2: 16, 3: 67, 4: 77, 5: 87, 6: 76, 7: 2, 8: 57, 9: 3, 10: 52, 11: 62, 12: 48, 13: 10, 14: 23, 15: 39, 16: 72, 17: 46, 18: 38, 19: 63, 20: 94, 21: 19, 22: 45, 23: 29, 24: 85, 25: 37, 26: 83, 27: 32, 28: 5, 29: 81, 30: 69, 31: 51, 32: 9, 33: 56, 34: 79, 35: 71, 36: 33, 37: 1, 38: 26, 39: 92, 40: 88, 41: 18, 42: 70, 43: 24, 44: 22, 45: 84, 46: 80, 47: 43, 48: 14, 49: 55, 50: 49, 51: 13, 52: 91, 53: 93, 54: 25, 55: 60, 56: 89, 57: 7, 58: 86, 59: 30, 60: 36, 61: 78, 62: 50, 63: 54, 64: 21, 65: 74, 66: 47, 67: 44, 68: 68, 69: 66, 70: 34, 71: 40, 72: 20, 73: 28, 74: 64, 75: 53, 76: 90, 77: 4, 78: 65, 79: 6, 80: 58, 81: 61, 82: 11, 83: 42, 84: 41, 85: 27, 86: 59, 87: 8, 88: 31, 89: 17, 90: 15, 91: 82, 92: 35, 93: 75, 94: 12}


list_of_letters_VII = 'W?:O7CA<Dt5#rLFjwS&J=3MbkKB Zu"-eXc8zhU^~P0T@Il1pn(2/£gfdy4_9sN>\',;%[$Qo)6GE!]*HRvqYVam+|.}{xi'
rev_num_convert_VII = {1: 79, 2: 2, 3: 74, 4: 25, 5: 37, 6: 51, 7: 53, 8: 49, 9: 26, 10: 42, 11: 63, 12: 17, 13: 36, 14: 16, 15: 71, 16: 31, 17: 46, 18: 39, 19: 81, 20: 89, 21: 8, 22: 54, 23: 57, 24: 73, 25: 55, 26: 20, 27: 56, 28: 45, 29: 11, 30: 76, 31: 7, 32: 41, 33: 22, 34: 44, 35: 21, 36: 35, 37: 4, 38: 84, 39: 58, 40: 3, 41: 15, 42: 83, 43: 64, 44: 72, 45: 30, 46: 66, 47: 92, 48: 47, 49: 61, 50: 86, 51: 18, 52: 91, 53: 50, 54: 6, 55: 40, 56: 5, 57: 52, 58: 10, 59: 82, 60: 19, 61: 80, 62: 38, 63: 93, 64: 9, 65: 70, 66: 85, 67: 75, 68: 94, 69: 27, 70: 1, 71: 60, 72: 68, 73: 69, 74: 62, 75: 59, 76: 88, 77: 28, 78: 23, 79: 78, 80: 14, 81: 65, 82: 12, 83: 32, 84: 90, 85: 24, 86: 77, 87: 48, 88: 67, 89: 34, 90: 29, 91: 33, 92: 13, 93: 43, 94: 87}


list_of_letters_VIII = 'aX<=:{)"O#J0\']7 b$Qjm9|q+hV^sCR%vg43z(-x_SIl5B1p/uAf,rK?L.oUcwi*dNZey~E6HG£!;t@&8>[FnYkT}PMD2W'
rev_num_convert_VIII = {1: 7, 2: 5, 3: 74, 4: 84, 5: 27, 6: 37, 7: 18, 8: 87, 9: 89, 10: 54, 11: 8, 12: 24, 13: 34, 14: 67, 15: 73, 16: 79, 17: 30, 18: 62, 19: 42, 20: 63, 21: 1, 22: 58, 23: 75, 24: 9, 25: 70, 26: 85, 27: 49, 28: 13, 29: 14, 30: 4, 31: 59, 32: 2, 33: 76, 34: 66, 35: 65, 36: 69, 37: 60, 38: 31, 39: 32, 40: 48, 41: 47, 42: 91, 43: 53, 44: 10, 45: 45, 46: 29, 47: 57, 48: 43, 49: 41, 50: 71, 51: 90, 52: 44, 53: 56, 54: 86, 55: 80, 56: 15, 57: 25, 58: 68, 59: 94, 60: 17, 61: 77, 62: 26, 63: 23, 64: 52, 65: 50, 66: 64, 67: 3, 68: 82, 69: 6, 70: 72, 71: 20, 72: 92, 73: 93, 74: 16, 75: 11, 76: 19, 77: 22, 78: 39, 79: 40, 80: 83, 81: 28, 82: 61, 83: 35, 84: 51, 85: 36, 86: 38, 87: 81, 88: 55, 89: 78, 90: 88, 91: 33, 92: 21, 93: 12, 94: 46}


list_of_letters_IX = '0,t*8£9uL Sai=\'<IU${e+O/xH~K}gf24Dv?sq71NYbV_M!WAhozEGw@JZp]^35&>.#j6-ndkm;[CyQ()Br:F"P|XTcR%1'
rev_num_convert_IX = {1: 69, 2: 67, 3: 30, 4: 11, 5: 82, 6: 55, 7: 43, 8: 25, 9: 83, 10: 94, 11: 78, 12: 85, 13: 89, 14: 71, 15: 79, 16: 61, 17: 20, 18: 59, 19: 72, 20: 54, 21: 3, 22: 74, 23: 44, 24: 26, 25: 5, 26: 63, 27: 64, 28: 73, 29: 28, 30: 10, 31: 81, 32: 4, 33: 93, 34: 36, 35: 41, 36: 45, 37: 80, 38: 38, 39: 92, 40: 27, 41: 86, 42: 65, 43: 50, 44: 33, 45: 31, 46: 16, 47: 23, 48: 14, 49: 90, 50: 24, 51: 9, 52: 62, 53: 53, 54: 84, 55: 21, 56: 88, 57: 12, 58: 48, 59: 76, 60: 68, 61: 51, 62: 8, 63: 39, 64: 2, 65: 29, 66: 35, 67: 18, 68: 52, 69: 37, 70: 75, 71: 42, 72: 60, 73: 17, 74: 15, 75: 57, 76: 46, 77: 56, 78: 7, 79: 77, 80: 91, 81: 87, 82: 70, 83: 1, 84: 22, 85: 6, 86: 32, 87: 49, 88: 47, 89: 40, 90: 19, 91: 66, 92: 13, 93: 34, 94: 58}


list_of_letters_X = 'd)|UL$N]g:0XP>KZC5q£h@#.lVow1fjrG Q78(Azk{_HsD<3IW}E,^mb\'~F!xc/nv*e4&%Yp+;S?a-uMTBi9J[yO6t2R"='
rev_num_convert_X = {1: 68, 2: 39, 3: 18, 4: 26, 5: 53, 6: 66, 7: 56, 8: 87, 9: 34, 10: 84, 11: 21, 12: 73, 13: 30, 14: 47, 15: 61, 16: 45, 17: 58, 18: 69, 19: 15, 20: 14, 21: 29, 22: 92, 23: 28, 24: 20, 25: 52, 26: 76, 27: 2, 28: 27, 29: 57, 30: 35, 31: 79, 32: 65, 33: 90, 34: 77, 35: 11, 36: 41, 37: 91, 38: 33, 39: 46, 40: 70, 41: 63, 42: 12, 43: 78, 44: 44, 45: 36, 46: 22, 47: 89, 48: 67, 49: 43, 50: 40, 51: 85, 52: 82, 53: 54, 54: 24, 55: 31, 56: 10, 57: 50, 58: 72, 59: 16, 60: 71, 61: 81, 62: 49, 63: 60, 64: 19, 65: 9, 66: 88, 67: 6, 68: 42, 69: 59, 70: 8, 71: 5, 72: 25, 73: 93, 74: 38, 75: 80, 76: 62, 77: 51, 78: 3, 79: 55, 80: 7, 81: 17, 82: 13, 83: 75, 84: 74, 85: 23, 86: 94, 87: 48, 88: 83, 89: 1, 90: 86, 91: 64, 92: 4, 93: 37, 94: 32}



#ALL VITAL VARIABLES HAVE NOW BEEN DECLARED! ALL VITAL VARIABLES HAVE NOW BEEN DECLARED! ALL VITAL VARIABLES HAVE NOW BEEN DECLARED! ALL VITAL VARIABLES HAVE NOW BEEN DECLARED! ALL VITAL VARIABLES HAVE NOW BEEN DECLARED!




#THE FUNCTIONS BELOW THIS COMMENT ARE USED TO ENCODE ENIGMA! THE FUNCTIONS BELOW THIS COMMENT ARE USED TO ENCODE ENIGMA! THE FUNCTIONS BELOW THIS COMMENT ARE USED TO ENCODE ENIGMA! THE FUNCTIONS BELOW THIS COMMENT ARE USED TO ENCODE ENIGMA!
def pairs(group, message):
         dic = {}
         index = 0
         mess2 = ""
         group2 = []
         for number in group[9:103]:
                  dic[all_chars[index]] = number
                  index += 1
         for letter in message:
                  group2.append(dic[letter])
         for number in group2:
                  mess2 += num_char_pairs[number]
                  
                  
         return(mess2)

def generate_wiring(group):
         dic = {}
         counter = 1
         for number in group:
                  dic[counter] = number
                  counter += 1
         return(dic)

def wiring_I(numbers, group):
         output = []
         for number in numbers:
                  output.append(generate_wiring(group[103:197])[number])
         return(output)


def wiring_II(numbers, group):
         output = []
         for number in numbers:
                  output.append(generate_wiring(group[197:291])[number])
         return(output)


def wiring_III(numbers, group):
         output = []
         for number in numbers:
                  output.append(generate_wiring(group[291:385])[number])
         return(output)


def wheel(letter, value):
         chars = {}
         for char in all_chars:
                  if value % 94 == 0:
                           chars[char] = 94       
                  else:
                           chars[char] = value % 94
                  value += 1
         return(chars[letter])



def wheel_I_turn(message, value):
         group = []
         for character in message:
                  x = wheel(character, value)
                  group.append(x)
                  value += 1
         return(group)


def wheel_II_turn(message, value):
         group = []
         counter = 0
         for character in message:
                  x = wheel(character, value)
                  group.append(x)
                  counter += 1
                  if counter % 3 == 0:
                           value += 1
         return(group)

def wheel_III_turn(message, value):
         group = []
         counter = 0
         for character in message:
                  x = wheel(character, value)
                  group.append(x)
                  counter += 1
                  if counter % 9 == 0:
                           value += 1
         return(group)


         
def letter_output_I(number, value):
          order_of_letters = {}
          for letter in list_of_letters_I:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_II(number, value):
          order_of_letters = {}
          for letter in list_of_letters_II:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])


         
def letter_output_III(number, value):
          order_of_letters = {}
          for letter in list_of_letters_III:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])



def letter_output_IV(number, value):
          order_of_letters = {}
          for letter in list_of_letters_IV:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_V(number, value):
          order_of_letters = {}
          for letter in list_of_letters_V:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_VI(number, value):
          order_of_letters = {}
          for letter in list_of_letters_VI:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_VII(number, value):
          order_of_letters = {}
          for letter in list_of_letters_VII:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_VIII(number, value):
          order_of_letters = {}
          for letter in list_of_letters_VIII:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_IX(number, value):
          order_of_letters = {}
          for letter in list_of_letters_IX:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         


def letter_output_X(number, value):
          order_of_letters = {}
          for letter in list_of_letters_X:
                   if value % 94 == 0:
                            order_of_letters[94] = letter
                            
                   else:
                            order_of_letters[value % 94] = letter
                            
                   value += 1
          return(order_of_letters[number])
         



def numbers_to_letters_I(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_I(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_II(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_II(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_III(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_III(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_IV(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_IV(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_V(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_V(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_VI(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_VI(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_VII(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_VII(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_VIII(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_VIII(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_IX(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_IX(number, value))
                  value += 1
         return(output_letters)

def numbers_to_letters_X(num_mes, value):
         output_letters = []
         for number in num_mes:
                  output_letters.append(letter_output_X(number, value))
                  value += 1
         return(output_letters)


def rotor_I(message, value, wire, grp):
         final_output = ""
         nums = wheel_I_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_I(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_II(message, value, wire, grp):
         final_output = ""
         nums = wheel_II_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_II(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)

def rotor_III(message, value, wire, grp):
         final_output = ""
         nums = wheel_III_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_III(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)


def rotor_IV(message, value, wire, grp):
         final_output = ""
         nums = wheel_I_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_IV(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_V(message, value, wire, grp):
         final_output = ""
         nums = wheel_II_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_V(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_VI(message, value, wire, grp):
         final_output = ""
         nums = wheel_III_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_VI(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_VII(message, value, wire, grp):
         final_output = ""
         nums = wheel_I_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_VII(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_VIII(message, value, wire, grp):
         final_output = ""
         nums = wheel_II_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_VIII(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_IX(message, value, wire, grp):
         final_output = ""
         nums = wheel_III_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_IX(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)



def rotor_X(message, value, wire, grp):
         final_output = ""
         nums = wheel_I_turn(message, value)
         new_nums = wire(nums, grp)
         almost_final_output = numbers_to_letters_X(new_nums, value)
         for letter in almost_final_output:
                  final_output += letter
         return(final_output)

def generate_key_first_12():
         string = ""
         for i in range(12):
                  x = random.randint(0, 9)
                  string += str(x)
         return(string)

def generate_key_pairs():
         count = 0
         group = []
         while count < 94:
                  x = random.randint(1, 94)
                  if  x not in group:
                     group.append(x)
                     count += 1
         return(group)

def generate_key_wiring():
         count = 0
         group = []
         while count < 94:
                  x = random.randint(1, 94)
                  if  x not in group:
                     group.append(x)
                     count += 1
         return(group)



def generate_key():
         key_string = generate_key_first_12()
         group_of_key_values = generate_key_pairs()+generate_key_wiring()+generate_key_wiring()+generate_key_wiring()
         for number in group_of_key_values:
                  if number < 10:
                           key_string += "0"+str(number)
                  else:
                           key_string += str(number)
         return(key_string)
                                 
def interp_key(key):
         key_meaning = []
         for character in key[0:6]:
                  key_meaning.append(int(character))
         index = 6
         while index <= 762:
                  if key[index] != "0":
                           holder = key[index] + key[index + 1]
                  else:
                           holder = key[index + 1]
                  index += 2
                  key_meaning.append(int(holder))
                           
         return(key_meaning)
         

def enigma(original_message, K):
    message = pairs(K, original_message)
    dic = {0:rotor_I, 1:rotor_II, 2:rotor_III, 3:rotor_IV, 4:rotor_V, 5:rotor_VI, 6:rotor_VII, 7:rotor_VIII, 8:rotor_IX, 9:rotor_X}
    return(dic[K[2]](dic[K[1]](dic[K[0]](message, K[6], wiring_I, K), K[7], wiring_II, K), K[8], wiring_III, K))

#THE FUNCTIONS BENEATH THIS COMMENT ARE THE EXTRA LAYER OF ENCRYPTION! #THE FUNCTIONS BENEATH THIS COMMENT ARE THE EXTRA LAYER OF ENCRYPTION! #THE FUNCTIONS BENEATH THIS COMMENT ARE THE EXTRA LAYER OF ENCRYPTION! #THE FUNCTIONS BENEATH THIS COMMENT ARE THE EXTRA LAYER OF ENCRYPTION! #THE FUNCTIONS BENEATH THIS COMMENT ARE THE EXTRA LAYER OF ENCRYPTION! 
def factorial(x):
         counter = 1
         for num in range(1, x+1):
                  counter *= num
         return(counter)

def sigma(x):
         counter = 0
         for num in range(1, x+1):
                  counter += num
         return(counter)

def f1(x):
         return(sigma(x + 3))

def f2(x):
         value = (x ** 2) + 9
         return(value)

def f3(x):
         value = ((x + 1) ** 2) + 6
         return(value)

def f4(x):
         value = sigma(x + 36)
         return(value)

def f5(x):
         value = sigma(x + 5)
         return(value)

def f6(x):
         value = ((x + 2) ** 2) + 13
         return(value)

def f7(x):
         value = ((x + 6) ** 2)
         return(value)

def f8(x):
         value = ((x + 4) ** 2) - 5
         return(value)


def f9(x):
         value = ((x + 3) ** 2) - 3
         return(value)


def if1(x):
         counter_1 = 0
         counter_2 = 0
         while counter_1 < x:
                  counter_2 += 1
                  counter_1 += counter_2
         output = counter_2 - 3
         return(output)

def if2(x):
         output = math.sqrt(x - 9)
         return(output)

def if3(x):
         output = math.sqrt(x - 6) - 1
         return(output)

def if4(x):
         counter_1 = 0
         counter_2 = 0
         while counter_1 < x:
                  counter_2 += 1
                  counter_1 += counter_2
         output = counter_2 - 36
         return(output)

def if5(x):
         counter_1 = 0
         counter_2 = 0
         while counter_1 < x:
                  counter_2 += 1
                  counter_1 += counter_2
         output = counter_2 - 5
         return(output)

def if6(x):
         value = math.sqrt(x - 13) - 2
         return(value)

def if7(x):
         value = math.sqrt(x) - 6
         return(value)

def if8(x):
         value = math.sqrt(x + 5) - 4
         return(value)

def if9(x):
         value = math.sqrt(x + 3) - 3
         return(value)
         

def create_filler_bulk():
         filler = []
         first_rand = random.randint(1000, 1200)
         for number in range(first_rand):
                  second_rand = random.randint(10, 15000)
                  filler.append(second_rand)
         return(filler)


def create_filler_cognito():
         filler = []
         first_rand = random.randint(10, 20)
         for number in range(first_rand):
                  second_rand = random.randint(10, 200)
                  filler.append(second_rand)
         return(filler)


def filler_merge(big_junk, small_junk):
         for number in small_junk:
                  index = random.randint(0, len(big_junk))
                  big_junk.insert(index, number)
         return(big_junk)


def tagged_message(key, message):
         message.insert(0, key[4])
         message.append(key[5])
         return(message)


def insert_message(message, junk):
         start_index = random.randint(0, len(junk))
         sea = junk[0:start_index + 1] + message + junk[start_index + 1: len(junk) + 1]
         return(sea)


def sea(message_in_numbers, key):
         junk = filler_merge(create_filler_bulk(), create_filler_cognito())
         to_be_inserted = tagged_message(key, message_in_numbers)
         output = insert_message(to_be_inserted, junk)
         return(output)


def list_to_string(x):
         string = ""
         for i in x:
                  string += str(i)
                  string += "."
         return(string)



def message_to_numbers_dictionary(x, K):
         message = enigma(x, K)
         chars = {}
         value = 1
         empty_set = []
         for let in all_chars:
                  chars[let] = value
                  value += 1
         for letter in message:
                  empty_set.append(chars[letter])
         return(empty_set)


def encrypt_message(empty_set, func):
    this_dic = {1:f1, 2:f2, 3:f3, 4:f4, 5:f5, 6:f6, 7:f7, 8:f8, 9:f9, 0:f8}
    new_list = []
    for numero in empty_set:
        new_list.append(this_dic[func[3]](numero))
    return(sea(new_list, func))


def encryption(x, key):
         for letter in key:
                  if letter.isalpha() or len(key) < 200:
                           return("Your KEY needs to be 200 digits from 0 to 9, how did you fuck this basic shit up? There's a button right there.")
         else:
                  funt = interp_key(key)
         number_message = message_to_numbers_dictionary(x, funt)
         encrypted_message = encrypt_message(number_message, funt)
         return(list_to_string(encrypted_message))

         

#THE CODE UNDERNEATH IS COMMENT IS FOR DECRYPTING ENIGMA! THE CODE UNDERNEATH IS COMMENT IS FOR DECRYPTING ENIGMA!THE CODE UNDERNEATH IS COMMENT IS FOR DECRYPTING ENIGMA!

def rev_pairs(group, message):
         dic = {}
         index = 0
         mess2 = ""
         group2 = []
         for number in group[9:103]:
                  dic[number] = all_chars[index]
                  index += 1
         for letter in message:
                  group2.append(char_num_pairs[letter])
         for number in group2:
                  mess2 += dic[number]
         return(mess2)



def reverse_wheel_I_turn(numbers, value):
         dic = {}
         group = []
         for number in numbers:
                  for char in all_chars:
                           if value % 94 == 0:
                                    dic[94] = char
                           else:
                                    dic[value % 94] = char
                           value += 1
                  letter = dic[number]
                  group.append(letter)
                  value += 1
         return(group)


def reverse_wheel_II_turn(numbers, value):
         dic = {}
         counter = 0
         group = []
         for number in numbers:
                  for char in all_chars:
                           if value % 94 == 0:
                                    dic[94] = char
                           else:
                                    dic[value % 94] = char
                           value += 1
                  letter = dic[number]
                  group.append(letter)
                  counter += 1
                  if counter % 3 == 0:
                           value += 1
         return(group)


def reverse_wheel_III_turn(numbers, value):
         dic = {}
         group = []
         counter = 0
         for number in numbers:
                  for char in all_chars:
                           if value % 94 == 0:
                                    dic[94] = char
                           else:
                                    dic[value % 94] = char
                           value += 1
                  letter = dic[number]
                  group.append(letter)
                  counter += 1
                  if counter % 9 == 0:
                           value += 1
         return(group)

def generate_reverse_wiring(group):
         dic = {}
         counter = 1
         for number in group:
                  dic[number] = counter
                  counter += 1
         return(dic)
                  
def reverse_wiring_I(numbers, group):
         output = []
         dic = generate_reverse_wiring(group[103:197])
         for number in numbers:
                  output.append(dic[number])
         return(output)

def reverse_wiring_II(numbers, group):
         output = []
         dic = generate_reverse_wiring(group[197:291])
         for number in numbers:
                  output.append(dic[number])
         return(output)

def reverse_wiring_III(numbers, group):
         output = []
         dic = generate_reverse_wiring(group[291:385])
         for number in numbers:
                  output.append(dic[number])
         return(output)


def reverse_letter_output_I(letter, value):
         order_of_letters = {}
         for let in list_of_letters_I:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_II(letter, value):
         order_of_letters = {}
         for let in list_of_letters_II:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])


def reverse_letter_output_III(letter, value):
         order_of_letters = {}
         for let in list_of_letters_III:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_IV(letter, value):
         order_of_letters = {}
         for let in list_of_letters_IV:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_V(letter, value):
         order_of_letters = {}
         for let in list_of_letters_V:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_VI(letter, value):
         order_of_letters = {}
         for let in list_of_letters_VI:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_VII(letter, value):
         order_of_letters = {}
         for let in list_of_letters_VII:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_VIII(letter, value):
         order_of_letters = {}
         for let in list_of_letters_VIII:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_IX(letter, value):
         order_of_letters = {}
         for let in list_of_letters_IX:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])

def reverse_letter_output_X(letter, value):
         order_of_letters = {}
         for let in list_of_letters_X:
                  if value % 94 == 0:
                           order_of_letters[let] = 94
                  else:
                           order_of_letters[let] = value % 94
                  value += 1
         return(order_of_letters[letter])




def reverse_numbers_to_letters_I(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_I(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_II(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_II(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_III(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_III(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_IV(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_IV(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_V(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_V(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_VI(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_VI(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_VII(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_VII(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_VIII(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_VIII(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_IX(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_IX(letter, value))
                  value += 1
         return(output_numbers)

def reverse_numbers_to_letters_X(message, value):
         output_numbers = []
         for letter in message:
                  output_numbers.append(reverse_letter_output_X(letter, value))
                  value += 1
         return(output_numbers)

def reverse_rotor_I(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_I(message, value)
         y = wire(x, grp)
         z = reverse_wheel_I_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)

def reverse_rotor_II(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_II(message, value)
         y = wire(x, grp)
         z = reverse_wheel_II_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)

def reverse_rotor_III(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_III(message, value)
         y = wire(x, grp)
         z = reverse_wheel_III_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)

def reverse_rotor_IV(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_IV(message, value)
         y = wire(x, grp)
         z = reverse_wheel_I_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)

def reverse_rotor_V(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_V(message, value)
         y = wire(x, grp)
         z = reverse_wheel_II_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)


def reverse_rotor_VI(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_VI(message, value)
         y = wire(x, grp)
         z = reverse_wheel_III_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)


def reverse_rotor_VII(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_VII(message, value)
         y = wire(x, grp)
         z = reverse_wheel_I_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)

def reverse_rotor_VIII(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_VIII(message, value)
         y = wire(x, grp)
         z = reverse_wheel_II_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)


def reverse_rotor_IX(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_IX(message, value)
         y = wire(x, grp)
         z = reverse_wheel_III_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)


def reverse_rotor_X(message, value, wire, grp):
         final_output = ""
         holder = []
         x = reverse_numbers_to_letters_X(message, value)
         y = wire(x, grp)
         z = reverse_wheel_I_turn(y, value)
         for t in z:
                  final_output += t
         return(final_output)
         

def reverse_enigma(message, K):
    dic = {0:reverse_rotor_I, 1:reverse_rotor_II, 2:reverse_rotor_III, 3:reverse_rotor_IV, 4:reverse_rotor_V, 5:reverse_rotor_VI, 6:reverse_rotor_VII, 7:reverse_rotor_VIII, 8:reverse_rotor_IX, 9:reverse_rotor_X}
    return(rev_pairs(K, dic[K[0]](dic[K[1]](dic[K[2]](message, K[8], reverse_wiring_III, K), K[7], reverse_wiring_II, K), K[6], reverse_wiring_I, K)))



def string_to_list(x):
         list_val_beta = []
         list_val = []
         value = ''
         length = len(x)
         for dig in range(length):
                  index = x[dig]
                  if index != '.':
                           value += index
                  else:
                           if dig == length - 1:
                                    list_val_beta.append(value)
                                    value = ''
                                    break
                           else:
                                    list_val_beta.append(value)
                                    value = ''
                                    dig += 1
         for number in list_val_beta:
                  number = int(number)
                  list_val.append(number)
         return(list_val)


        
def reverse_character_dictionary(x):
         #empty_set will have the message assigned to it in number form, with one value per space in the list
         value = 1
         chars = {}
         empty_set = []
         message = ""
         encrypted_message = []
         encrypted_message_1 = []
         for char in all_chars:
                  chars[value] = char
                  value += 1
         for number in x:
                  message += (chars[number])
         return(message)

def find_message(x, stt, stp):
         number_message = []
         start = x.index(stt)
         x.remove(stt)
         end = x.index(stp)
         for i in range(start, end):
                  number_message.append(x[i])
         return(number_message)
                                    

def decrypt(x, function):
    message_num = []
    dictionary = {1:if1, 2:if2, 3:if3, 4:if4, 5:if5, 6:if6, 7:if7, 8:if8, 9:if9, 0:if8}
    for number in x:
        message_num.append(dictionary[function](number))
    return(message_num)


def decryption(x, key):
         if len(key) < 12:
                  return("Your KEY needs to be at least 12 digits")


         else:
                  lis = string_to_list(x)
                  unjumble = interp_key(key)
                  MIEN = find_message(lis, unjumble[4], unjumble[5])
                  MIN = decrypt(MIEN, unjumble[3])
                  M = reverse_character_dictionary(MIN)
                  Message = reverse_enigma(M, unjumble)
                  return(Message)

def dec_but():
         ipt = text.get('1.0', 'end-1c')
         ky = mes.get()
         opt = decryption(ipt, ky)
         text.delete('1.0', 'end-1c')
         text.insert(INSERT, opt)


def enc_but():
         ipt = text.get('1.0', 'end-1c')
         ky = mes.get()
         opt = encryption(ipt, ky)
         text.delete('1.0', 'end-1c')
         text.insert(INSERT, opt)


def clr_but():
         text.delete('1.0', 'end-1c')
         

def key_but():
         key = generate_key()
         keybox.insert(INSERT, key)
         

root = Tk()
root.title("Encryption and Decryption App")

mes = StringVar()

text = Text(root, height=10, width=50, wrap=WORD, bg='black', fg='white', highlightbackground='green', insertbackground='red', selectbackground='green', insertwidth=4)
text.place(x=2, y=5)
x = text.get(1.0, END)

encryption_button = Button(root, bg='grey', fg='red', command=enc_but, text='ENCRYPTION', activebackground='grey', padx=3, pady=5, bd=5)
encryption_button.place(x=50, y=215)

decryption_button = Button(root, bg='grey', fg='green', command=dec_but, text='DECRYPTION', activebackground='grey', padx=3, pady=5, bd=5)
decryption_button.place(x=170, y=215)

keybox = Entry(root, width=55, textvariable=mes, selectborderwidth=15, bg='white', bd=5)
keybox.place(x=50, y=180)


clear_button = Button(root, text="CLEAR", bg='white', command=clr_but, fg='black', activebackground='grey', padx=3, pady=5, bd=5)
clear_button.place(x=300, y=215)


key_btn = Button(root, text="KEY", bg="black", fg="white", command=key_but, padx=3, pady=3, bd=3)
key_btn.place(x=10, y=177)

root.geometry("409x258")
root.resizable(width=False, height=False)
root.mainloop()
