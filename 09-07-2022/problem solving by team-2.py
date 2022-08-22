##Univariate quadratic polynomials are the most common polynomials. 
##Polynomials with only one unknown number and the highest degree of 2 are called univariate quadratic polynomials.
## Its standard form is ax^2+bx+c
##Please complete the code in solution.py to realize the function of equation.
##The equation function receives three parameters a, b, and c as the quadratic term, the primary term, and the constant term of the standard form of a bivariate quadratic polynomial. 
##Please use the lambda function to pass in an unknown number x for the equation function and take this lambda function as the return value of the equation function. 
##Find the result of the univariate quadratic polynomial ax^2+bx+c
##
##Example
##The quizzer runs main.py by executing python main.py {input_path} , which outputs the updated string after running, and you can see how the code is running in main.py.
##
##Example 1
##
##Input:
##2 3 7
##3
##Output:
##
##34
##
##
##Explanation:
##After passing in the first row of parameters, the expression is 2x^2+3x+7
##
##When x=3 the result of the expression is 34
##
##Example 2
##
##Input:
##
##1 2 0
##5
##Output:
##
##35
##Explanation:
##After passing in the first row of parameters, the expression is x^2+2x+0
##When x=5 the result of the expression is 35
a,b,c=input("Enter the quadratic term(a) for quadratic equation").split()
a=int(a)
b=int(b)
c=int(c)
x=int(input("enter the x value for quadratic equation"))
z=lambda x:a*(x**2)+b*x+c
print(z(x))
