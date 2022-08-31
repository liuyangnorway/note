# -*- coding: utf-8 -*-
""""""
import numpy as np
import matplotlib.pyplot as plt


def interp(p1, p2, x):
    """
    Get interpolated value y between two points(p1,p2) for x.

    Parameters
    ----------
    p1 : (x1,y1)
    p2 : (x2,y2)
    x : given x value

    Returns
    -------
    y :  output y value
    """

    k = get_Slope(p1, p2)

    y = k * (x - p1[0]) + p1[1]

    return y


def get_Slope(p1, p2):
    """
    # get slope of line between two points(p1,p2)
    p1 : (x1,y1)
    p2 : (x2,y2)
    k  : slope
    """

    if p1[0] == p2[0]:
        k = np.nan
    else:
        k = (p1[1] - p2[1]) / (p1[0] - p2[0])
    return k


def find_intersection_linear(p11, p12, p21, p22):
    """
    Find the intersection point for two linear lines
    Parameters
    ----------
    p11 : (x1,y1)
    p12 : (x2,y2)
    p21 : (x3,y3)
    p22 : (x4,y4)

    Returns
    -------
    intersection : intersection point (x:list ,y:list)

    """

    intersection = [np.nan, np.nan]
    L1_min_x = min(p11[0], p12[0])
    L1_max_x = max(p11[0], p12[0])

    L2_min_x = min(p21[0], p22[0])
    L2_max_x = max(p21[0], p22[0])

    if L1_max_x < L2_min_x or L2_max_x < L1_min_x:
        return intersection
    else:
        X = [p11[0], p12[0], p21[0], p22[0]]
        X.sort()
        x1 = X[1]
        x2 = X[2]

        y11 = interp(p11, p12, x1)
        y12 = interp(p11, p12, x2)

        y21 = interp(p21, p22, x1)
        y22 = interp(p21, p22, x2)
        [y11, y12, y21, y22]

        if x1 == x2:
            if np.isnan(y11):

                if y21 >= min(p11[1], p12[1]) and y21 <= max(p11[1], p12[1]):
                    intersection = [x1, y21]
            elif np.isnan(y21):
                if y11 >= min(p21[1], p22[1]) and y11 <= max(p21[1], p22[1]):
                    intersection = [x1, y11]
            else:
                if y11 == y21:
                    intersection = [x1, y11]

        else:
            k1 = get_Slope(p11, p12)
            k2 = get_Slope(p21, p22)

            if (y11 - y21) * (y12 - y22) < 0:
                y = (k2 * y11 - k1 * y21) / (k2 - k1)
                x = np.nan
                if k1 != 0:
                    x = (y - p11[1]) / k1 + p11[0]
                elif k2 != 0:
                    x = (y - p21[1]) / k2 + p21[0]
                intersection = [x, y]

            elif (y11 - y21) * (y12 - y22) == 0:
                if k1 != k2:
                    if y11 - y21 == 0:
                        intersection = [x1, y11]
                    else:
                        intersection = [x2, y12]
                # else:
                # print('It is same two lines')
    return intersection


def find_line_intersection1(x1, y1, x2, y2, isextrapolate=0, isplot=0):
    """
    Find intersection points for two lines or two curves.
    input:
    line 1; x1,y1
       x1 = (x11,x12,x13,...,x1n)
       y1 = (y11,y12,y13,...,y1n)
    line 2; x2,y2
       x2 = (x21,x22,x23,...,x2m)
       y2 = (y21,y22,y23,...,y2m)

    isextrapolate: extrapolate intersection for two lines.

    isplot=1, plot
    isplot=0, no plot

    output:
    intersection: x,y
    x = (xi1,xi2,xi3,...,xin)
    2 = (yi1,yi2,yi3,...,yim)
    """
    x1 = list(x1)
    y1 = list(y1)
    x2 = list(x2)
    y2 = list(y2)
    x3 = x1.copy()
    y3 = y1.copy()
    #    print(1.1,'x2=',x2)

    #    print(1.1,'x1=',x1)
    if isextrapolate:
        # print('extrapolate the line 1')
        if min(x1) > min(x2):
            i = 0
            xi = min(x2)
            p1 = [x1[i], y1[i]]
            p2 = [x1[i + 1], y1[i + 1]]
            yi = interp(p1, p2, xi)
            if np.isnan(yi):
                yi = max(y2)

            if (xi - x1[i]) * (x1[i + 1] - x1[i]) < 0:
                x1 = [xi] + x1
                y1 = [yi] + y1
            if (xi - x1[i]) * (x1[i + 1] - x1[i]) == 0 and (yi - y1[i]) * (
                y1[i + 1] - y1[i]
            ) < 0:
                x1 = [xi] + x1
                y1 = [yi] + y1

        if max(x1) < max(x2):
            i = len(x1) - 2
            xi = max(x2)
            p1 = [x1[i], y1[i]]
            p2 = [x1[i + 1], y1[i + 1]]
            yi = interp(p1, p2, xi)
            if np.isnan(yi):
                yi = max(y2)
            yi = interp(p1, p2, xi)

            if (xi - x1[i + 1]) * (x1[i] - x1[i + 1]) < 0:
                x1 = x1 + [xi]
                y1 = y1 + [yi]
            if (xi - x1[i + 1]) * (x1[i] - x1[i + 1]) == 0 and (yi - y1[i]) * (
                y1[i + 1] - y1[i]
            ) < 0:
                x1 = x1 + [xi]
                y1 = y1 + [yi]

    x = []
    y = []

    #    print(1.2,'x1=',x1)
    for i in range(len(x1) - 1):
        for j in range(len(x2) - 1):
            p11 = [x1[i], y1[i]]
            p12 = [x1[i + 1], y1[i + 1]]
            p22 = [x2[j], y2[j]]
            p21 = [x2[j + 1], y2[j + 1]]
            intersection = find_intersection_linear(p11, p12, p21, p22)
            if np.nan not in intersection:
                x.append(intersection[0])
                y.append(intersection[1])

    if len(x) > 1:
        xy = np.array([x, y])
        xy = np.unique(xy, axis=1)
        x = xy[0]
        y = xy[1]
    if isplot:
        fig = plt.figure(1)
        fig.clf()
        (line1,) = plt.plot(x1, y1, "-o", label="line 1")
        (line2,) = plt.plot(x2, y2, "-d", label="line 2")
        if len(x3) < len(x1):
            plt.plot(x3, y3, "-o", label="line 1")
            line1.set_label("line 1 extrapolate")

        plt.scatter(x, y, s=50, marker="*", zorder=3, c="r", label="intersection")

        plt.legend()
    return x, y


def find_line_intersection(x1, y1, x2, y2, isplot=0, isextrapolate=1):
    """
    Find intersection points for two lines or two curves.
    input:
    line 1; x1,y1
       x1 = (x11,x12,x13,...,x1n)
       y1 = (y11,y12,y13,...,y1n)
    line 2; x2,y2
       x2 = (x21,x22,x23,...,x2m)
       y2 = (y21,y22,y23,...,y2m)

    isextrapolate: extrapolate intersection for two lines.

    isplot=1, plot
    isplot=0, no plot

    output:
    intersection: x,y
    x = (xi1,xi2,xi3,...,xin)
    2 = (yi1,yi2,yi3,...,yim)
    """
    # Find intersection points for two lines or two curves.
    x, y = find_line_intersection1(x1, y1, x2, y2, isextrapolate=0)
    if len(x) == 0:
        x, y = find_line_intersection1(x1, y1, x2, y2, isextrapolate=isextrapolate)
    if len(x) == 0:
        x1 = x1[::-1]
        y1 = y1[::-1]

        x, y = find_line_intersection1(x1, y1, x2, y2, isextrapolate=isextrapolate)

    if isplot:
        fig = plt.figure(2)
        fig.clf()
        (line1,) = plt.plot(x1, y1, "-", label="line 1")
        (line2,) = plt.plot(x2, y2, "-", label="line 2")

        plt.scatter(x, y, s=50, marker="*", zorder=3, c="r", label="intersection")

        plt.legend()
    return x, y
