#include <iostream>

using namespace std;

void epsilon_double(int,int);
void epsilon_float(int);

int main(){
<<<<<<< HEAD

	epsilon_double(0,1);
=======
	int a;
	epsilon_double(1);
	epsilon_float(1);
	cin >> a;
>>>>>>> aac170ce266f1c276535586276398ce3b9bdbb99

	return 0;
}

void epsilon_double(int metodo,int coso) {
	double b = 3242.43280807796868;
	double* a = &b;
	cout << *a << endl;
	
	double d = 0.0;
	
	if (metodo == 1) {

		

		while ((1 + d) != 1)
		{
			cout << d << endl;
			d = d / 2;
		}
	}
	else
	{
		while (d!=0)
		{
			cout << d << endl;
			d = d / 2;
		}
	}
}

void epsilon_float(int metodo) {

	float d = 0.5;
	float r = 0.5;
	double x = 0.5;
	if (metodo == 1) {

		while ((1 + d) != 1)
		{
			cout << d << endl;
			d = d / 2;
		}
	}
	else
	{
		while (x != 0)
		{
			if (d == 0) {
				if (x == 0.5) {
					x = (double)r;
				}	
				cout << x << endl;
				x = x / 2;
			}
			else {
				r = d;
				cout << d << endl;
				d = d / 2;
			}
		}
		
	}
}

