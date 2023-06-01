"""
figure 모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈
line class를 이용하여 선의 길이를 설정/참조를 수행
area_squre, area_circle, area_regular_triangle 함수로
각각 정사각형, 원, 정삼각형의 넓이를 반환한다.
"""
import math
class line:
    """
    line class는 선의 길이에 대해 저장하고 있는 class
    변수 는 외부에서 접근 불가능한 __width, __height가 있고,
    해당 변수를 수정, 접근을 위한
    set_length, get_length 메소드가 제공된다.
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """ 생성자 초기 length값을 받는다.
        Args:
            width (int or float) : 초기 선의 가로 길이
            heigth (int or float) : 초기 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        선의 길이를 수정합니다.
        Args:
            width (int or float) : 초기 선의 가로 길이
            height (int or float) : 초기 선의 세로 길이
        ""
        """
        self.__width = width
        self.__height = height
    def get_length(self):
        """ 객체가 저장하고 있는 선의 길이를 return
        returns:
            int or float: 저장하고 있는 선의 길이 입니다.
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """
    길이를 입력받아 직사각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float) : 초기 선의 가로 길이
        height (int or float) : 초기 선의 세로 길이
    Returns:
        int or float: 직사각형의 넓이를 반환합니다.

    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height
def area_ellipse(width, height):
    """
        길이를 입력받아 타원의 넓이를 구하는 함수입니다.
        Args:
            width (int or float) : 짧은 반지름 길이
            height (int or float) : 긴 반지름  길이
        Returns:
            float: 타원의 넓이를 반환합니다.
        """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi
def area_right_triangle(width, height):
    """
   길이를 입력받아 직각삼각형의 넓이를 구하는 함수입니다.
   Args:
        width (int or float) : 밑변의 길이
        height (int or float) : 높이의 길이
   Returns:
        int or float: 직각삼각형의 넓이를 반환합니다.
   """

    if width <= 0 or height <= 0: raise ValueError
    return width * height /2