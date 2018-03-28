#Simple program to value Options based on binomial trees
import math

#recursively calculate the option value
def calcValue(S, u, d, T, n, K, r, o, p):

	#If we have reached maturity, we have a call and we exercise the option
	if (n == 0) & (o == 1) & (S > K):
		return S-K
	#If we have reached maturity, we have a put and we exercise the option
	elif (n == 0) & (o == 0) & (S < K):
		return K-S
	#If we have reached maturity, don't exercise the option
	elif (n == 0):
		return 0
	#We haven't reached maturity yet, value depends on future value
	else:
		return math.exp(-1*r*T)*((p*calcValue((S*u), u, d, T, (n-1), K, r, o, p))+((1-p)*calcValue((S*d), u, d, T, (n-1), K, r, o, p)))

def main():
	#These values are inputted based on the situation:
	#The risk free rate
	r=.08
	#number of time periods until expiration
	n=2
	#size of a time period in years
	T=.5
	#percentage increase
	u=1.1
	#percentage decrease
	d=0.9
	#Stock price at time 0
	S0=100
	#Type of option: 1 is call, 0 is put
	o=0
	#Exercise price K
	K=100



	#calculate the probability of an increase in price
	p=(math.exp(r*T)-d)/(u-d)

	#calculate the value of the option
	result = calcValue(S0, u, d, T, n, K, r, o, p)
	print(result)

if __name__ == "__main__":
	main()