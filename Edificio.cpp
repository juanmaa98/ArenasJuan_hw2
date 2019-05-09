#include <iostream>
#include <cmath> 
#include <fstream>
using namespace std;

float y=0.0;
float k=2000;
float m=1000.0;
int N=30000;

int v1_prima(float w,float t,float u1,float v1,float u2,float& a1){
	float F=sin(w*t);
	a1= (-y*v1-2*k*u1+k*u2+F)/m;
	return 0;
	
}

int v2_prima(float w,float t,float u2,float v2,float u1,float u3,float& a2){
	a2= (-y*v2+k*u1-2*k*u2+k*u3)/m;
	return 0;
	
}

int v3_prima(float w,float t,float u3,float v3,float u2,float& a3){
	a3= (-y*v3+k*u2-k*u3)/m;
	return 0;
	
}
float mayor(float u[]){
	float umax=abs(u[0]);
	for(int i=1;i<N;i++){
		if(abs(u[i])>=abs(u[i-1])){
			umax=abs(u[i]);
		}
	}
	return umax;
}
int main () {
	float x0=0;
	float v0=0;
	float dt=0.001;

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

	float u1max=0;
	float u2max=0;
	float u3max=0;
	
	int Nw=100;
	float w[Nw]={0};

	for (int i=0;i<Nw;i++){
		w[i]=(((3-0.2)/(Nw-1))*i+0.2)*sqrt(k/m);
	}

	ofstream outfile;
	outfile.open("umax.dat");

	for(int k=0;k<Nw;k++){
		for(int i=1;i<N;i++){
			t[i]=t[i-1]+dt;
			
			v1_prima(w[k],t[i-1],u1[i-1],v1[i-1],u2[i-1],a1[i-1]);
			v2_prima(w[k],t[i-1],u2[i-1],v2[i-1],u1[i-1],u3[i-1],a2[i-1]);
			v3_prima(w[k],t[i-1],u3[i-1],v3[i-1],u2[i-1],a3[i-1]);

			float kv1_1=dt*a1[i-1];
			float ku1_1=dt*v1[i-1];

			float ku2_1=dt*v2[i-1];
			float kv2_1=dt*a2[i-1];

			float ku3_1=dt*v3[i-1];
			float kv3_1=dt*a3[i-1];

			float a1_2=0;
			float a2_2=0;
			float a3_2=0;

			v1_prima(w[k],t[i-1]+dt*0.5,u1[i-1]+0.5*ku1_1,v1[i-1]+0.5*kv1_1,u2[i-1]+0.5*ku2_1,a1_2);
			v2_prima(w[k],t[i-1]+dt*0.5,u2[i-1]+0.5*ku2_1,v2[i-1]+0.5*kv2_1,u1[i-1]+0.5*ku1_1,u3[i-1]+0.5*ku3_1,a2_2);
			v3_prima(w[k],t[i-1]+dt*0.5,u3[i-1]+0.5*ku3_1,v3[i-1]+0.5*kv3_1,u2[i-1]+0.5*ku2_1,a3_2);

			float kv1_2=dt*a1_2;
			float ku1_2=dt*(v1[i-1]+0.5*kv1_1);

			float kv2_2=dt*a2_2;
			float ku2_2=dt*(v2[i-1]+0.5*kv2_1);

			float kv3_2=dt*a3_2;
			float ku3_2=dt*(v3[i-1]+0.5*kv3_1);

			v1_prima(w[k],t[i-1]+dt*0.5,u1[i-1]+0.5*ku1_2,v1[i-1]+0.5*kv1_2,u2[i-1]+0.5*ku2_2,a1_2);
			v2_prima(w[k],t[i-1]+dt*0.5,u2[i-1]+0.5*ku2_2,v2[i-1]+0.5*kv2_2,u1[i-1]+0.5*ku1_2,u3[i-1]+0.5*ku3_2,a2_2);
			v3_prima(w[k],t[i-1]+dt*0.5,u3[i-1]+0.5*ku3_2,v3[i-1]+0.5*kv3_2,u2[i-1]+0.5*ku2_2,a3_2);

			float kv1_3=dt*a1_2;
			float ku1_3=dt*(v1[i-1]+0.5*kv1_2);

			float kv2_3=dt*a2_2;
			float ku2_3=dt*(v2[i-1]+0.5*kv2_2);

			float kv3_3=dt*a3_2;
			float ku3_3=dt*(v3[i-1]+0.5*kv3_2);

			v1_prima(w[k],t[i-1]+dt,u1[i-1]+ku1_3,v1[i-1]+kv1_3,u2[i-1]+ku2_3,a1_2);
			v2_prima(w[k],t[i-1]+dt,u2[i-1]+ku2_3,v2[i-1]+kv2_3,u1[i-1]+ku1_3,u3[i-1]+ku3_3,a2_2);
			v3_prima(w[k],t[i-1]+dt,u3[i-1]+ku3_3,v3[i-1]+kv3_3,u2[i-1]+ku2_3,a3_2);

			float kv1_4=dt*a1_2;
			float ku1_4=dt*(v1[i-1]+kv1_3);

			float kv2_4=dt*a2_2;
			float ku2_4=dt*(v2[i-1]+kv2_3);

			float kv3_4=dt*a3_2;
			float ku3_4=dt*(v3[i-1]+kv3_3);
			
			float ku1_prom=(1.0/6.0)*(ku1_1+2*ku1_2+2*ku1_3+ku1_4);
			float kv1_prom=(1.0/6.0)*(kv1_1+2*kv1_2+2*kv1_3+kv1_4);

			float ku2_prom=(1.0/6.0)*(ku2_1+2*ku2_2+2*ku2_3+ku2_4);
			float kv2_prom=(1.0/6.0)*(kv2_1+2*kv2_2+2*kv2_3+kv2_4);

			float ku3_prom=(1.0/6.0)*(ku3_1+2*ku3_2+2*ku3_3+ku3_4);
			float kv3_prom=(1.0/6.0)*(kv3_1+2*kv3_2+2*kv3_3+kv3_4);
			
			v1[i]=v1[i-1]+kv1_prom;
			u1[i]=u1[i-1]+ku1_prom;

			v2[i]=v2[i-1]+kv2_prom;
			u2[i]=u2[i-1]+ku2_prom;

			v3[i]=v3[i-1]+kv3_prom;
			u3[i]=u3[i-1]+ku3_prom;
		
		}
		
		u1max=mayor(u1);
		u2max=mayor(u2);
		u3max=mayor(u3);
		
		outfile <<w[k]<<" "<<u1max<<" "<<u2max<<" "<<u3max<<endl;
	}
	outfile.close();
	return 0;
}
