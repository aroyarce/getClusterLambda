# Lambda Function getClusterLambda
Lambda function in AWS for an endpoint of an API Gateway

## Description:
This function calculate the Clusters contain in a grid of 10x10, by measure the distance between points.

## Method
The distance is calculated based in the magnitud of a vector in a Cartessian Plane. This is the absolute difference between each axes of each point, where each distance must be inside the given value.

## Algorithm
The algorithm consist in thre steps:
- Loop for each active location.
- Measure of the distance between this point and all the others.
- Add to an array, reference by the current point, all the other points which distance is minor or equal to the given distance.
- Order the result array for simplified the next step.
- With the array for each point, It will be remove all duplicated, because of the distance for A to B is the same that B to A.
- Return the resulting array.

## Input Variables
The funtion receives two paramters. The distance to use for reference, and the grid where to make the calculus.

## Guidelines
Some check errors was ommited to avoid extend the project and test. But in case of not included the grid, and just the distance, it will be use the example grid send in the test. In case of the distance nor the grid is delivered, it will return an 400 error. The max distance avalable is 9, because is the maximum length of the grid of both axes.
