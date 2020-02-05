#include <iostream>

using namespace std;

void epsilon_double(int);
void epsilon_float(int);

int main(){

	epsilon_double(0);
	epsilon_float(0);

	return 0;
}

void epsilon_double(int metodo) {

	double d = 0.5;

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

	if (metodo == 1) {

		while ((1 + d) != 1)
		{
			cout << d << endl;
			d = d / 2;
		}
	}
	else
	{
		while (d != 0)
		{
			cout << d << endl;
			d = d / 2;
		}
	}
}

