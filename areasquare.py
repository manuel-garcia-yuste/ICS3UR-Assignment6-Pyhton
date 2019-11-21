#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program calculate area of a rhombus


def main():
    # input
    input("Press enter to start ")
    p = int(input("Enter the diagonal p: "))
    q = int(input("Enter the diagonal q: "))

    # process
    area = p*q/2

    # output
    print("Area of rhombus is ", area)


if __name__ == "__main__":
    main()
