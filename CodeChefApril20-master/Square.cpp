#include<bits/stdc++.h>
using namespace std;
int main(){
    long T, N;
    cin >> T;
    while(T--){
        cin >> N;
        long my_array[N], mul_arr[N];
        long i = 0, j = 0;
        long cnt = 0;
        long my_iter = 0;
        while(i < N)
            cin >> my_array[i++];
		for (i = 0; i < N; i++){
			mul_arr[i] = abs(my_array[i]) % 4;
		}
		for (my_iter = 0; my_iter < N; my_iter++){
			for (i = my_iter; i < N; i++){
				if (mul_arr[i] == 0){
					cnt = cnt + N - i;
					break;
				}
				else if ((mul_arr[i] == 1) || (mul_arr[i] == 3)){
					cnt++;
				}
				else if (mul_arr[i] == 2){
					while (i < N - 1){
						i++;
						if ((mul_arr[i] == 2) || (mul_arr[i] == 0)){
							cnt = cnt + N - i;
							break;
						}
					}
					break;
				}	
			}	
		}
		cout << cnt << endl;
	}
    return 0;
}
