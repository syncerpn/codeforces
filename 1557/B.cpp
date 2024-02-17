#include <stdio.h>

int main()
{
    int t, n, s, si, prev, curr;
    scanf("%d", &t);
    
    for (int ti = 0; ti < t; ++ti) {
    	scanf("%d %d", &n, &s);
        si = 0;
    	for(int i = 0; i < n; i++) {
    		scanf("%d", &curr);
            if (i > 0) {
                if (curr < prev) si += 1;
            }
            prev = curr;
    	}
        si += 1;
        if (si > s || n < s) printf("No\n");
        else printf("Yes\n");
    }
	return 0;
}