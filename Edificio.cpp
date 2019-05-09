#include <iostream>
#include <cmath> 
#include <fstream>
using namespace std;

float y=0.0;
float k=2000;
float m=1000.0;
float w=1.0*sqrt(k/m);
#define PI 3.14159265

int v1_prima(float t,float u1,float v1,float u2,float& a1){
	float F=sin(w*t)
	a1= (-y*v1-2*k*u1+k*u2+F)/m;
	return 0;
	
}

int v2_prima(float t,float u2,float v2,float u1,float u3,float& a2){
	a2= (-y*v2+k*u1-2*k*u2+k*u3)/m;
	return 0;
	
}

int v3_prima(float t,float u3,float v3,float u2,float& a3){
	a3= (-y*v3+k*u2-k*u3)/m;
	return 0;
	
}

int main () {
	float x0=0;
	float v0=0;
	float dt=0.001;
	int N=3000;

	float v1[N]={0};
	float u1[N]={0};

	float v2[N]={0};
	float u2[N]={0};

	float v3[N]={0};
	float u3[N]={0};

	float t[N]={0};

	float a1[N]={0};
	float a2[N]={0};
	float a3[N]={0};
	
	for(int i=1;i<N;i++){
		t[i]=t[i-1]+dt;
		
		v1_prima(t[i-1],u1[i-1],v1[i-1],u2[i-1],a1[i-1]);

		float kv1_1=dt*a1[i-1];
		float ku1_1=dt*v1[i-1];	
		float ku2_1=dt*v2[i-1];

		

		v1_prima(t[i-1]+dt*0.5,u1[i-1]+0.5*ku1_1,v1[i-1]+0.5*kv1_1,u2[i-1]+0.5*ku2_1,a2);

		float kv2_1=dt*Ax2;
		
		Vx[i]=Vx[i-1]+k2x;
		Vy[i]=Vy[i-1]+k2y;

		x[i]=x[i-1]+dt*Vx[i];
		y[i]=y[i-1]+dt*Vy[i];
	
	}
	ofstream outfile;
	outfile.open("datosrunge.dat");


	for(int i=0;i<N;i++){
		outfile << t[i] <<" "<< x[i] <<" "<< Vx[i] <<" "<< y[i] <<" "<<Vy[i] << " " << endl;
	}
	return 0;
}
