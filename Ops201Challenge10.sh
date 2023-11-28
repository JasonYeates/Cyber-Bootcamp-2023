#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

echo "Triangle Check"
echo "please type the first integer"
read x
echo "please type the second integer"
read y
echo "please type the third integer"
read z
if [ $x -eq $y -a $y -eq $z ]
then echo "Equilateral Triangle"
elif [ $x -ne $y -a $y -ne $z ]
then echo "Scalene Triangle"
elif [ $x -eq $y -a $x -ne $z -o $y -eq $z -a $y -ne $x ]
then echo "Isosceles Triangle"
fi