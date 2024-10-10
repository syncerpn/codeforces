#include <stdio.h>

int main()
{
    int t, n, x, m;
	double s;
    scanf("%d", &t);
    
    for (int ti = 0; ti < t; ++ti) {
    	scanf("%d", &n);
        s = 0;
    	for(int i = 0; i < n; i++) {
    		scanf("%d", &x);
    		s += x;
    		
    	    if (i == 0) m = x;
    		else if (x > m) m = x;
    	}
    	s = (s - m) / (n-1);
    	printf("%.9f\n", s + m);
    }
	return 0;
}
