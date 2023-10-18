#include <iostream>
#include <cstdlib>
#include <time.h>
#include <cmath>
using namespace std;

int geo_p_q(double p) {
    int count = 1;
    while ((double)rand() / RAND_MAX > p) {
        count++;
    }
    return count;
}

int geo_r_i_t(double p) {
    double U = (double)rand() / RAND_MAX;
    int i = 1;
    int count = 1;
    double baseline = p * pow(1 - p, i - 1);
    while (U >= baseline) {
        count++;
        i++;
        baseline+=p * pow(1 - p, i - 1);
    }
    return count;
}

int geo_formula(double p) {
    double U = (double)rand() / RAND_MAX;
    int X = floor(log(U) / log(1 - p)) + 1;
    return X;
}

int main() {
	long double p = 0.01;
	int num_samples = 10000;
	double t1,t2,t3,t4;
	t1 = clock();
	for(int i = 0; i <num_samples; i++){
		geo_p_q(p);
	}
	t2 = clock();
	for(int i = 0; i <num_samples; i++){
		geo_r_i_t(p);
	}
	t3 = clock();
	for(int i = 0; i <num_samples; i++){
		geo_formula(p);
	}
	t4 = clock();
	
	cout << "函式1 (geo_p_q) 執行時間： " << (long double)(t2-t1) <<"ms"<<endl;
    cout << "函式2 (geo_r_i_t) 執行時間： " << (long double)(t3-t2) <<"ms"<<endl;
    cout << "函式3 (geo_formula) 執行時間： " << (long double)(t4-t3) <<"ms"<< endl;
}
